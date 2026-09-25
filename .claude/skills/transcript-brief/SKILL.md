---
name: "transcript-brief"
description: "Write a short, notification-sized summary of the transcripts that were newly added to the transcripts repository: who the call was with, what it was about, and the one or two things worth remembering. Use when the user asks what came in, what the new calls were about, for a brief or recap of new transcripts, or as the final step of the transcript pipeline (sync → debrief → brief → notify)."
---

# Transcript Brief

Tell the founder, in a few lines he can read on a phone lock screen, what new calls
arrived and what each one was about. This is a heads-up, not an analysis. The
skeptical evidence work belongs to `discovery-debrief`; do not repeat it here.

## Setup

Transcripts live at the root of this repository (see `CLAUDE.md`; older notes call it
`~/transcripts`). Never fetch, sync or download anything, and never modify a transcript
file. The only file this skill writes is `.brief-state.json`, which it publishes to
`main` through a merged PR (step 5).

Before step 1, run `scripts/state.sh pull` so `.brief-state.json` reflects every earlier
run — a stale copy re-briefs calls that already reached a notification. If it fails,
stop.

## 1. Decide which transcripts are new

"New" means: not yet briefed. The source of truth is `.brief-state.json` at the repo root:

```json
{ "updated": "2026-09-25T10:30:00Z", "briefed": ["2026-09-24_vulnerability-remediation-process-discussion.txt"] }
```

- If the caller passed an explicit list of files (for example the pipeline handing over
  what the sync just added), brief those — minus any already in `briefed`, so the same
  call never reaches a notification twice. Say which were skipped as already briefed.
- Otherwise list every regular file at the repo root — no extension filter — and
  subtract: names in `briefed`, `thesis.md`, `ledger.md`, `index.json`, `CLAUDE.md`,
  `README*`, any dotfile, and subfolders such as `_to_delete/`, `scripts/`, `.claude/`.
- **First run, state file missing:** do not brief the whole archive. Write the state
  file with every current transcript marked as briefed, say "Brief baseline set: N
  existing transcripts marked as seen", and stop.

Skip any candidate with no speaker turns (not a transcript) and do not mark it briefed.
If two files are the same call (same date, same people, same opening turns), brief it
once and mention the duplicate in one line.

If nothing is new, output exactly `No new transcripts.` and stop.

## 2. Read the thesis

Read `thesis.md` in full. Use the numbered beliefs under "What we
believe" (#1, #2, …) as the claims to check, plus the wedge options (A, B, …) if the
thesis lists them. Refer to them by those labels so the notification matches the file.
Also note anything under "Not claiming" — a call that argues for one of those is not
support.

## 3. Read each new transcript

Read each one in full. With more than three, use one subagent per transcript in
parallel, each returning only the fields below — transcript text never comes back
into the main context.

Per call, collect:

- **Who:** name, role, company, as the transcript itself gives them. If the transcript
  never names the person, say "unnamed" — do not take a name from the filename.
- **Type:** customer discovery (practitioner) / advisor / investor / internal.
- **About:** one sentence on the main topic.
- **Takeaway:** the single most useful thing said — a concrete problem, a number from
  their own environment, a strong objection, or a next step. One short verbatim quote
  (under 20 words) if there is a good one; otherwise no quote.
- **Next step:** anything agreed (intro, follow-up, pilot, send material). "None" if none.
- **Thesis fit:** compare what *this person needs* against each thesis belief. For
  each belief that came up, mark it:
  - `+` supports — and whether it was **unprompted** (they raised it before the
    founder named it) or **led** (only after the founder described it). When unsure,
    call it led.
  - `−` cuts against — including agreeing with the symptom but naming a different
    cause than the thesis does (e.g. "we can't patch fast enough because nobody owns
    it" is `−` for #2, not `+`).
  - skip beliefs that never came up.
  Then give an overall verdict — **Strong** (a core belief supported unprompted by a
  sitting practitioner), **Partial** (support is led, or only from an advisor/investor,
  or covers minor beliefs), **None** (their needs are elsewhere), or **Against**
  (anything `−` on #1 or #2). Against wins over any other verdict — put it first.
  Agreement that was led never makes a call Strong.

## 4. Output

Plain text, short enough for a notification. Put a headline first, then one line or
two per call.

```
3 new calls (Sep 24–25)
• Jane Doe, CISO @ Acme — discovery. Vuln backlog owned by nobody; "we close maybe a third". Next: intro to her SecOps lead.
  Fit: AGAINST — #2− (says cause is ownership, not impact risk) · #1+ unprompted
• John Roe — investor (a16z). Wants 5 paying design partners before a seed. Next: none.
  Fit: Partial — #3+ led (investor view)
• Yuval/Shoval — internal. Pricing and ICP discussion.
```

Internal calls get no Fit line. When several calls came in, end with one tally line:
`Fit: 1 strong, 1 partial, 1 against.`

Rules:
- Aim for 700 characters or less in total. Past ~5 calls, list the rest as one line
  ("+4 more: names…").
- Direct, plain English. No "great call", no rating of how interested someone sounded.
- Never invent a name, company, number or quote.
- If `discovery-debrief` ran in the same pipeline and reported that a claim got
  weaker, add one final line: `Thesis: <claim label> weakened — see debrief.`

## 5. Update state

After the brief is produced, add every briefed filename (exactly as on disk) to
`briefed` in `.brief-state.json` and set `updated`. Do this last, so a run that fails
halfway does not hide calls from the next run. Then publish it — only it — following
**Publishing data** in `CLAUDE.md` (branch → PR → squash-merge → finish):

```
scripts/state.sh publish brief "brief: <N> calls briefed" .brief-state.json
```

The first-run baseline in step 1 is published the same way (`"brief: baseline, N marked
seen"`). If any publishing step fails, say so after the brief with the PR link: the next
run will brief these calls again.
