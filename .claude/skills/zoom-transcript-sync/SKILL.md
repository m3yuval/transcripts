---
name: "zoom-transcript-sync"
description: "Sync meeting transcripts from Zoom and from a shared Google Drive folder of PDFs and text files into the transcripts repository, incrementally, so only items not already saved get fetched, then publish them to main through a merged PR. Use whenever the user wants to download, sync or update meeting transcripts, or wants to analyze a body of past calls."
---

# Transcript sync (Zoom + Google Drive)

Pull meeting transcripts from two sources and land them as plain text files at the root of this repository, so they can be grepped, diffed, fed to other tools, or read by a human. Both sources share one `index.json`, one naming convention and one file format, so the folder reads as a single archive rather than two piles.

Runs are incremental: the index records what has been fetched and what was attempted and failed, so a second run costs almost nothing.

This runs in a cloud container on a git repository (see `CLAUDE.md`). The destination is always the repo root — never ask. Nothing counts as saved until it is merged into `main` through a PR (step 7); the container and everything not on `main` are gone when the session ends.

- **Source A — Zoom**: fetched through the Zoom MCP tools (steps 2–4).
- **Source B — Google Drive**: a shared folder holding PDF and plain-text transcripts (step 5).

## Why this needs a skill

Five things here mislead, and each produces a confidently wrong answer rather than an error:

1. **`recordings_list` only returns recordings the user owns.** Meetings they merely attended — often most of them, if a colleague schedules the calls — don't appear at all. Enumerate with the search API instead. In one real account, 17 of 39 recorded meetings were invisible to `recordings_list`.
2. **Transcripts are enormous.** A 30-minute call is roughly 10k tokens. Pulling dozens through a single context will exhaust it long before the job is done.
3. **Most failures are expected, not bugs.** A 403 on someone else's recording, and an empty result for a call Zoom never transcribed, are both normal. Retrying them burns time; hiding them loses information the user needs.
4. **Zoom closed captions are visible but unreachable.** `recordings_list` advertises CC/VTT files with download URLs, which makes them look like an easy fallback. They are not: `get_recording_resource` accepts only `transcript`, `summary`, `nextStep`, `playUrl` — there is no `cc` type — and the download URLs fail from both a sandboxed container and the user's machine, because Zoom's download host is outside the egress allowlist. Don't rediscover this.
5. **Tool results must reach disk without being retyped.** The Drive text relay (`read_file_content`) drifts at the character level — markdown escapes appear (`Wow\!` where the source has `Wow!`), combining characters vanish. And any JSON or base64 that comes back *inline* in a tool result can only reach a file by being retyped, which corrupts it. The repo's `.claude/settings.json` sets `MAX_MCP_OUTPUT_TOKENS=4000`, so every Zoom transcript and nearly every Drive download is saved by the harness to a file whose path is printed in the result (`Output has been saved to <path>`). Work from that file with the `scripts/` helpers. Steps 4 and 5 have the details.

## Step 1 — Pull the latest state and read the index

Run `scripts/state.sh pull` from the repo root first. Another session may have synced since this container was cloned; reading a stale index re-fetches files that already exist and can land the same call twice. If it fails, stop and report — do not sync against stale state.

Confirm the tools are available: the Zoom connector (`mcp__Zoom_for_Claude__*`), the Google Drive connector (`mcp__Google_Drive__*`) and `python3 -c "import pypdf"` (the SessionStart hook installs it; if it is missing, run `pip install -q pypdf cffi`). A connector that is missing or unauthenticated is a real failure: say which one and stop, rather than syncing only half the sources and recording the other half as empty.

Scratch files (raw results you copy, extracted PDF text) go in the session scratchpad or `/tmp`, never in the repo.

Read `index.json` at the repo root. It keys on the source's own identifier — a Zoom meeting UUID or a Drive file ID:

```json
{
  "updated": "2026-09-23T14:20:00Z",
  "meetings": {
    "93D2AC0C-EF26-4303-BDCA-B1327C32EF7C": {
      "date": "2026-09-16", "topic": "Security leadership discussion",
      "host": "Yuval Mermer",
      "file": "2026-09-16_security-leadership-discussion_thomas-sinnott.txt",
      "source": "transcript", "status": "ok"
    },
    "1mX0zI3du4aI5DcxEzeLncqGSYek1tnYg": {
      "date": "2026-09-10", "topic": "AI Threats and Defense Strategies",
      "file": "2026-09-10_ai-threats-and-defense-strategies.txt",
      "source": "google-drive-pdf", "status": "ok",
      "origin": "drive-folder:18uDV4DN-uJnTMnhfC2plrLbToJIk1Sx6"
    }
  }
}
```

`status` is `ok`, `no_permission`, `no_transcript`, `skipped_duplicate` or `audio_no_text`. Entries that produced no file carry `"file": null`. When a Drive file supplies the text for a meeting Zoom never transcribed, cross-link them: the Drive entry gets `zoom_meeting_uuid`, the Zoom entry gets `covered_by`, and the Zoom status stays `no_transcript` because that remains true of Zoom.

**First run against a folder that already has files:** rebuild the index before fetching, or everything gets redownloaded. Read the `Meeting UUID:` or `Drive File ID:` line out of each file's header — the step 6 format guarantees one is there, and it is the dedup key. Do not match on filenames: slugs are lossy and collide in exactly the cases that matter. Files written before this skill may lack a `Source:` line; record `"source": "unknown"` rather than guessing, and leave those files alone — rewriting someone's archive to match a format risks mangling it.

## Step 2 — Zoom: enumerate every meeting, not just owned ones

```
mcp__Zoom_for_Claude__search with
  datasource_filters: [{"datasource": "zoom_meeting",
                        "filters": {"eq": {"key": "has_recording", "value": true}}}]
  page_size: 100
```

Results carry `meeting_uuid`, `topic`, `meeting_start_time`, `host_name`, `attendee_list`, `meeting_roles`. The `meeting_uuid` is the dashed form (`93D2AC0C-EF26-...`) and is exactly what `get_recording_resource` wants — pass it straight through, no encoding step, despite what that tool's parameter description implies.

`recordings_list` supplements this when the user wants file-level detail, but it is capped to a one-month window and covers only owned meetings, so it never replaces the enumeration.

If the user asked for a date range, filter on `meeting_start_time`. Otherwise take everything and tell them how far back the search actually reached, since that is not necessarily the start of the account.

## Step 3 — Decide what to fetch

Subtract the index from the enumeration. Not in the index → fetch. `ok` → skip; this is what makes reruns cheap. `no_transcript` → retry, since Zoom sometimes finishes transcribing days later. `no_permission` → retry once per run and no more; a 403 last week will usually 403 again.

State the plan before spending time on it — "39 meetings found, 22 already saved, 17 to attempt" — so the user can stop you if the range is wrong.

## Step 4 — Zoom: fetch

Call `get_recording_resource` with `meetingId=<dashed UUID>` and `types="transcript"`.

- Timeline entries → write the file.
- Empty → retry once with `types="summary"`. Zoom's AI summary is much thinner but occasionally exists when the transcript doesn't; save it with `Source: summary` so nobody mistakes it for verbatim. Otherwise record `no_transcript`.
- 403 → record `no_permission`, move on.

The result is large, so the harness saves it to a file and prints the path (`Output has been saved to …/tool-results/mcp-Zoom_for_Claude-get_recording_resource-<n>.txt`, JSON `{transcripts: [{timeline: […]}]}`). Pass that path straight to the repo's formatter; never hand-format or retype the JSON. Workers left to their own devices all write their own formatter, and not identically — which is how one batch of files ends up with different timestamp precision than another. The committed one reproduces the existing archive byte for byte:

```
python3 scripts/format_zoom_transcript.py <saved-result-path> 2026-09-16_security-leadership-discussion_thomas-sinnott.txt \
    2026-09-16 "Security leadership discussion" 93D2AC0C-EF26-4303-BDCA-B1327C32EF7C transcript
```

Exit 2 means the response held no timeline entries. A 403 or empty result is small and comes back inline — that is fine, there is nothing to save. If a result that *does* hold a transcript comes back inline (the output-token limit was not applied), do not retype it: report that `MAX_MCP_OUTPUT_TOKENS` is not in effect and record the meeting as not attempted, so the next run picks it up.

## Step 5 — Google Drive: fetch the shared folder

**Find the folder by ID, not by name.** Folder names contain typos — a real one was shared as "Redordings", so `title = 'Recordings'` returned nothing and looked like an empty result. Take the ID from the folder URL (`drive.google.com/drive/folders/<ID>`) and store it in the index's top-level `sources` block so later runs need not ask again. If you only have a name and it doesn't match, list `sharedWithMe = true` and look for near-misses before reporting that nothing is there.

List contents with `search_files`, `query: "parentId = '<folder id>'"`, and keep each file's `fileSize` — it is used as a checksum below. Paginate: the listing returns a `nextPageToken` and a partial listing looks exactly like a complete one.

### Fetch by type

| Drive file | Method | Why |
|---|---|---|
| `.pdf` | `download_file_content` → `scripts/drive_download.py` | exact bytes; the text relay drifts on PDFs |
| `.txt`, `.vtt`, `.md` | `download_file_content` → `scripts/drive_download.py` | exact bytes; no markdown escaping to undo |
| `.m4a` and other audio | skip, record `audio_no_text` | no text to extract; say so rather than ignoring silently |

`download_file_content` returns `{content: <base64>, mimeType, title}`; it is large, so the harness saves it to a file and prints the path. Decode it with:

```
python3 scripts/drive_download.py <saved-result-path> <scratch>/<name> <fileSize from the listing>
```

It writes the exact bytes, exits 3 if the byte count does not equal `fileSize` (that check is free and conclusive — do not add double reads or hash comparisons), and for a PDF also writes `<name>.txt` with the extracted text, pages separated by form feeds. Parse that text into turns (below), then write the transcript file at the repo root.

A text file small enough (under ~10 KB) for the result to come back inline is the one exception: use `read_file_content` once, strip the relay's added markdown escapes (`\-`, `\*`, `\!`), check that the length equals `fileSize`, and note `Extraction: read_file_content (text relay)` in the header.

Also watch for **near-duplicates**: some titles repeat with a leading `?` (`?2026-09-10 Topic.pdf`) and an identical file size. Prefer the unprefixed one, record the other as `skipped_duplicate` with `duplicate_of`, and don't write a second file.

### Parsing the transcripts

**PDFs** hold turns like `Speaker Name (M:SS) text`, messier than they first look — all three of these occur in real files:

- A speaker marker can run **directly into the previous turn's text** with no break (`...complementary skills. SoShoval (11:17)`). Split on the marker wherever it occurs, not on line breaks.
- A block with **no marker** is the tail of a turn split across a PDF page boundary. Append it to the preceding turn.
- Timestamps are `M:SS` or `MM:SS` with **no hour component**. Normalise to `HH:MM:SS` (`2:17` → `00:02:17`).

**Text files** are simpler and vary more: usually `Speaker: text` or `**Speaker:** text` one per line, sometimes fenced with `---`, sometimes carrying export artifacts like a trailing `[cite: 1]`. Strip the fences, the `**`, and the citation markers; say in your report what you stripped. They often have no timestamps — then omit them rather than inventing any, and add `Timestamps: none in source` to the header.

Speaker labels vary within a file — `Shoval`, `Speaker 1`, `Speaker 2`, and a bare `Speaker` for short backchannel turns. These are distinct; preserve them rather than guessing a mapping to real names. Hebrew labels may be transliterated to match the folder, but body text is never translated or corrected.

Sanity-check by counting: every non-blank source line should end up in exactly one turn. Orphan lines before the first marker, or a turn count of 1, mean the split failed.

### Identifying which meeting a text file is

Text files are often named loosely (`asaf.txt`, `jason-2026-09-07.txt`). Before writing one, match it to a meeting, because the folder already knows about meetings Zoom failed to transcribe and a new file frequently fills one of those gaps.

Two people can share a first name on the same day. When a date has more than one candidate, compare the new file's speakers, language and opening line against the transcript already on disk before deciding — one real file was distinguishable only by being Hebrew, three-way, and opening as a follow-up, where its namesake was English and two-way.

## Step 6 — File format

One `.txt` per item, named `YYYY-MM-DD_topic-slug.txt`, with the external participant appended when there is one (`..._thomas-sinnott.txt`). Date first so the folder sorts chronologically; lowercase, hyphen-separated. For an internal or untitled meeting with no external participant — Zoom labels these "Yuval Mermer's Zoom Meeting" or "Google Calendar Meeting (not synced)" — use the attendees' first names (`2026-09-19_yuval-shoval.txt`). Stability across runs matters more than elegance, since the name is what a human scans.

```
Date: 2026-09-16
Topic: Security leadership discussion
Meeting UUID: 93D2AC0C-EF26-4303-BDCA-B1327C32EF7C
Source: transcript

[00:00:02] Thomas Sinnott: Yeah, so as far as how CDW does it...
```

Drive files use `Drive File ID:` in place of `Meeting UUID:`, and `Source: google-drive-pdf` or `google-drive-txt`.

**Exactly one blank line separates header from body**, and everything above it is `Key: value`. Tools split on that blank line; a file written without it reads as one giant header. The `Source:` line does double duty: it tells a reader whether they have verbatim text or a summary, and it is what a future run uses to rebuild the index.

## Sizing the work

Match the machinery to the job. Three small text files are a few minutes of inline work; wrapping them in subagents, repeat reads and hash reconciliation turns that into half an hour and still risks failing.

- **A handful of items, or any small text files** → do it inline. No workers.
- **Many PDFs, or a large Zoom backlog** → fan out, 5–10 items per worker, because PDF extraction and Zoom timelines are what actually consume context.

When you do fan out, every worker gets the same contract: do the work, write the files, report back **only a status table** (filename, status, source, turn count, body hash). Transcript text must never travel back through the orchestrating context. Two things that bite:

- **Give each worker its own scratch subdirectory.** Parallel workers default to the same paths and overwrite each other's `raw.json` mid-run, producing files with another meeting's content.
- **Hand out explicit filenames**, or workers name similar meetings inconsistently.

Workers write finished transcript files directly to the repo root. They never commit, push or open PRs; the orchestrator publishes once, in step 7, so a run produces one PR. Tool-result paths are per session, so a worker must make its own tool calls rather than be handed a path from the orchestrator's results.

If context gets tight, stop, write the index with everything done so far, publish it (step 7), and say the run was partial. A partial sync with an accurate index is a good outcome; a run that dies having recorded nothing is the bad one.

## Step 7 — Update the index, publish (PR → merge), report

Rewrite `index.json` with an entry for every item seen, **including failures**. Recording failures is what lets the next run tell "never tried" apart from "tried, nothing there" — without it, every rerun re-attempts every 403.

Then publish exactly what this skill owns — `index.json` and the transcript files it wrote this run, nothing else — following **Publishing data** in `CLAUDE.md` (branch → PR → squash-merge → finish):

```
scripts/state.sh publish sync "sync: +<N> transcripts, <date>" index.json <new files…>
```

Publish even when nothing new arrived: the index still records this run's attempts. The title says what changed (`sync: +2 transcripts (jane-doe, a16z), 2026-09-26` or `sync: no new transcripts, 17 retries unchanged, 2026-09-26`). If any publishing step fails, the run failed: say at which step, give the branch and PR link, and do not report the files as saved.

Report briefly: the PR that was merged, how many files are in the folder, how many were added, and what couldn't be fetched, grouped by reason rather than one line per item. The distinction the user can act on is "permission-blocked, and the host re-sharing would unblock them" versus "never transcribed, and a later rerun might pick them up."

Flag, but never silently fix, errors that are in the source: a mislabelled speaker, two turns merged under one name. Say which file and which turn, and let the user decide.

## Scope notes

Transcripts are meeting content involving other people. Write them to this repository and nowhere else, and don't quote call content back into the conversation beyond a header line to confirm a file looks right.