---
name: "transcript-pipeline"
description: "Run the full transcript pipeline end to end: sync new transcripts from Zoom and Google Drive, and if any arrived, run the discovery debrief and the transcript brief on them, then push a phone notification with the brief. If nothing new arrived, push a notification saying so. Use only when the user types /transcript-pipeline or asks to run the transcript pipeline."
---

# Transcript Pipeline

One trigger that chains three skills and ends with a phone notification:

```
pull main → snapshot index → zoom-transcript-sync (push) → diff index
   ├─ nothing new → notify "No new transcripts" → stop
   └─ new files   → discovery-debrief (push) → transcript-brief (push) → notify brief
```

It runs in a cloud container on this git repository (see `CLAUDE.md`). Each skill
commits and pushes its own files to `main` as it finishes, so a failure in a later step
never loses an earlier step's work, and the next run — in a fresh container — starts
from what was pushed.

This skill is only the conductor. Each step's real work is done by its own skill,
following that skill's instructions in full. Do not re-implement or shortcut them.

## Hard rules

- **Never write to `index.json`.** Not to fix it, not to annotate a run,
  not to record pipeline state. It belongs to `zoom-transcript-sync`, which is the only
  thing that may change it. This pipeline only reads it.
- Never modify transcript files.
- Never commit on behalf of a step. Each skill commits exactly the files it owns;
  the pipeline itself commits nothing.
- Every run ends with exactly one notification: success, no-news, or failure.

## Step 0 — Pull the latest state

Run `scripts/state_pull.sh` from the repo root. It puts the checkout on `main` at the
latest `origin/main`. The snapshot in step 1 must be taken after this, or files another
session already synced would be counted as new. If it fails, go to step 7 with step
`pull`.

## Step 1 — Snapshot the index (read only)

Read `index.json` at the repo root and keep in memory the set of entries that have a
file:

```
before = { key: entry.file  for key, entry in meetings  if entry.status == "ok" and entry.file }
```

Also note `sources.zoom.meetings_enumerated` and `sources.google_drive.files_listed`
for the no-news message. If `index.json` is missing or unreadable, fail at `snapshot`
(step 7).

## Step 2 — Sync

Invoke the `zoom-transcript-sync` skill and follow it fully. The destination is the
repo root; do not ask. It ends by committing and pushing `index.json` and the new files.

Permission-blocked (403) and never-transcribed meetings are normal outcomes, not
failures. A real failure is: a connector that cannot be reached or is not
authenticated, a Drive listing that errors, the sync stopping before it rewrote the
index, or its push failing. On a real failure go to step 7 with step `sync`.

## Step 3 — Diff (read only)

Re-read `index.json` and build `after` the same way. New transcripts are:

```
new_files = [ after[k] for k in after if k not in before ]
```

Check each file in `new_files` actually exists at the repo root. Keep the list in
the sync's date order.

**If `new_files` is empty:** notify (step 6) with
`No new transcripts. Checked <Z> Zoom meetings, <D> Drive files.` using the
post-sync counts, and stop. Do not run the debrief or the brief. Meetings that are
still blocked or untranscribed are not mentioned in the notification — they stay in
the session output from the sync.

## Step 4 — Debrief

Invoke the `discovery-debrief` skill and follow it fully. Tell it the new files are
exactly `new_files`. It writes, commits and pushes `ledger.md` and prints its full A/B/C analysis into
this session — that output is the detailed record the notification leads back to.

From its section B, note every claim it reports as **weakened** or **contradicted**.
If the debrief fails, or its push fails, go to step 7 with step `debrief`.

## Step 5 — Brief

Invoke the `transcript-brief` skill and follow it fully. Hand it `new_files` as the
explicit list, plus the weakened/contradicted claims from step 4 so it can add its
`Thesis:` line. Print the full brief in the session. It commits and pushes
`.brief-state.json`.

If the brief fails, or its push fails, go to step 7 with step `brief`.

## Step 6 — Notify

Send one `PushNotification`. Tapping it opens this session, where the sync report,
the full debrief and the full brief are all visible — so the notification is a
pointer, not the report.

The tool limit is **200 characters, one line, no markdown**. Build the message as:

- **One new call:** `1 new call: <Name>, <role> @ <company>. Fit: <verdict>. Tap for debrief.`
- **Several:** `<N> new calls: <name>, <name>, … Fit: <x> strong, <y> partial, <z> against. Tap for debrief.`
- If the debrief weakened a claim, replace the last words with `Thesis #<n> weakened.`
  — that outranks everything else.

If the message is still over 200 characters, drop names first, then the role/company,
never the fit tally or a weakened-claim warning.

The tool may report "not sent" when the user is at the computer and the session is
already in front of them. That is fine — say so in one line and do not retry.

Where it lands depends on where the session runs. In a cloud session, it goes to the
Claude app on the user's phone when notifications are enabled there. In a local
session, phone delivery needs Remote Control connected. If the tool reports that it had
nowhere to go, say so once at the end of the run; do not retry.

## Step 7 — Failure

Stop at the first real failure and notify:

```
Transcript pipeline failed at <step>: <short reason>.
```

If the sync already landed new files before a later step failed, add
`<N> new files saved.` (only if the sync's push succeeded) so the user knows the sync part worked and the next run's
debrief/brief can pick them up (the debrief finds unprocessed files through the ledger,
and the brief through `.brief-state.json`). Keep the whole message under 200 characters.

## Final session summary

End the run in the session with four lines: what was synced, what the debrief
changed in the ledger, the commits pushed to `main` (short hashes, one per skill that
committed), and the notification text that was sent (or why it was not).
