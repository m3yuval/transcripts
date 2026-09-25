---
name: "zoom-transcript-sync"
description: "Sync meeting transcripts from Zoom and from a shared Google Drive folder of PDFs and text files into one local folder, incrementally, so only items not already saved get fetched. Use whenever the user wants to download, sync or update meeting transcripts, or wants to analyze a body of past calls."
---

# Transcript sync (Zoom + Google Drive)

Pull meeting transcripts from two sources and land them as plain text files in a single folder, so they can be grepped, diffed, fed to other tools, or read by a human. Both sources share one `index.json`, one naming convention and one file format, so the folder reads as a single archive rather than two piles.

Runs are incremental: the index records what has been fetched and what was attempted and failed, so a second run costs almost nothing.

- **Source A — Zoom**: fetched through the Zoom MCP tools (steps 2–4).
- **Source B — Google Drive**: a shared folder holding PDF and plain-text transcripts (step 5).

## Why this needs a skill

Five things here mislead, and each produces a confidently wrong answer rather than an error:

1. **`recordings_list` only returns recordings the user owns.** Meetings they merely attended — often most of them, if a colleague schedules the calls — don't appear at all. Enumerate with the search API instead. In one real account, 17 of 39 recorded meetings were invisible to `recordings_list`.
2. **Transcripts are enormous.** A 30-minute call is roughly 10k tokens. Pulling dozens through a single context will exhaust it long before the job is done.
3. **Most failures are expected, not bugs.** A 403 on someone else's recording, and an empty result for a call Zoom never transcribed, are both normal. Retrying them burns time; hiding them loses information the user needs.
4. **Zoom closed captions are visible but unreachable.** `recordings_list` advertises CC/VTT files with download URLs, which makes them look like an easy fallback. They are not: `get_recording_resource` accepts only `transcript`, `summary`, `nextStep`, `playUrl` — there is no `cc` type — and the download URLs fail from both a sandboxed container and the user's machine, because Zoom's download host is outside the egress allowlist. Don't rediscover this.
5. **Drive files need opposite handling by type, and getting it backwards is what wastes the most time.** For a **PDF**, the text relay drifts at the character level — markdown escapes appear (`Wow\!` where the source has `Wow!`), combining characters vanish — so a PDF must come across as bytes. For a **plain-text file** the reverse holds: `download_file_content` returns base64 *inline in the tool result* for anything under the result-size limit, and inline base64 can't reach a file without being retyped, which corrupts it. Step 5 has the rule; follow it rather than picking one method for everything.

## Step 1 — Establish the destination and read the index

Ask the user where transcripts should go if they haven't said. If this session is linked to their computer, a folder on their machine is usually what they want; check `mcp__remote-devices__get_device_info` for connected folders and request access with `device_request_folder_access` if needed.

Read `index.json` at the root of that folder. It keys on the source's own identifier — a Zoom meeting UUID or a Drive file ID:

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

Save the raw response to a file and run it through this formatter rather than hand-formatting. Workers left to their own devices all write this same function, and not identically — which is how one batch of files ends up with different timestamp precision than another. Write it once to `format_transcript.py` and have every worker call it:

```python
import json, sys
raw, out, date, topic, uuid, source = sys.argv[1:7]
p = json.load(open(raw, encoding="utf-8"))
entries = []
for key in ("transcripts", "summaries", "recordings"):
    for rec in p.get(key) or []:
        entries += rec.get("timeline") or []
if not entries:
    sys.exit(2)                      # fall back to summary, or record no_transcript
lines = [f"Date: {date}", f"Topic: {topic}", f"Meeting UUID: {uuid}",
         f"Source: {source}", ""]
for e in entries:
    body = (e.get("text") or "").strip()
    if body:                          # Zoom emits blank entries for pauses
        ts = str(e.get("ts") or "00:00:00").split(".")[0]   # whole seconds
        lines.append(f"[{ts}] {e.get('display_name') or 'Unknown'}: {body}")
open(out, "w", encoding="utf-8").write("\n".join(lines) + "\n")
print(f"{out}: {len(lines) - 5} entries")
```

Call it as `python3 format_transcript.py raw.json out.txt 2026-09-16 "Security leadership discussion" 93D2AC0C-... transcript`. Exit 2 means the response held nothing.

## Step 5 — Google Drive: fetch the shared folder

**Find the folder by ID, not by name.** Folder names contain typos — a real one was shared as "Redordings", so `title = 'Recordings'` returned nothing and looked like an empty result. Take the ID from the folder URL (`drive.google.com/drive/folders/<ID>`) and store it in the index's top-level `sources` block so later runs need not ask again. If you only have a name and it doesn't match, list `sharedWithMe = true` and look for near-misses before reporting that nothing is there.

List contents with `search_files`, `query: "parentId = '<folder id>'"`, and keep each file's `fileSize` — it is used as a checksum below. Paginate: the listing returns a `nextPageToken` and a partial listing looks exactly like a complete one.

### Fetch by type

| Drive file | Method | Why |
|---|---|---|
| `.pdf` | `download_file_content` → decode base64 → `pypdf` | the text relay drifts on PDFs |
| `.txt`, `.vtt`, `.md` | `read_file_content`, **one call** | small files come back as inline base64 from `download_file_content`, which cannot be written to a file |
| `.m4a` and other audio | skip, record `audio_no_text` | no text to extract; say so rather than ignoring silently |

For a text file one read is enough — resist adding double reads and hash comparisons, which multiply the time for no gain. To confirm nothing was lost, compare against the `fileSize` from the listing: the relay adds markdown escaping (`\-`, `\*`, `\!`), so the read's length minus the added backslashes should equal `fileSize` exactly. That check is free and conclusive.

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

Write files to their destination with `device_commit_files`, staging under `/mnt/user-data/outputs/`. Avoid `device_bash` heredocs: the device shell can't read container files, and heredocs break unpredictably once a transcript gets large. A commit can take up to a minute to become visible — re-read before concluding it failed.

If context gets tight, stop, write the index with everything done so far, and say the run was partial. A partial sync with an accurate index is a good outcome; a run that dies having recorded nothing is the bad one.

## Step 7 — Update the index and report

Rewrite `index.json` with an entry for every item seen, **including failures**. Recording failures is what lets the next run tell "never tried" apart from "tried, nothing there" — without it, every rerun re-attempts every 403.

Report briefly: how many files are in the folder, how many were added, and what couldn't be fetched, grouped by reason rather than one line per item. The distinction the user can act on is "permission-blocked, and the host re-sharing would unblock them" versus "never transcribed, and a later rerun might pick them up."

Flag, but never silently fix, errors that are in the source: a mislabelled speaker, two turns merged under one name. Say which file and which turn, and let the user decide.

## Scope notes

Transcripts are meeting content involving other people. Write them where the user asked and nowhere else, and don't quote call content back into the conversation beyond a header line to confirm a file looks right.