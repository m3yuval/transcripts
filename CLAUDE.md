# Transcripts repo

Evidence base for Skylayer customer discovery. The **repository root is the transcripts
folder**: wherever a skill or note says `~/transcripts`, it means this repo's root
(`git rev-parse --show-toplevel`; `/home/user/transcripts` in a cloud session). A
SessionStart hook also symlinks `~/transcripts` to the root so older wording still works.

## Layout

| Path | What it is | Written only by |
|---|---|---|
| `YYYY-MM-DD_*.txt` (root) | transcripts, the evidence record; never edited after landing | `zoom-transcript-sync` |
| `index.json` | what was fetched / attempted from Zoom and Drive | `zoom-transcript-sync` |
| `ledger.md` | claim-by-claim evidence, processed-file list | `discovery-debrief` |
| `.brief-state.json` | which transcripts have been briefed | `transcript-brief` |
| `thesis.md` | the thesis on trial | the founder (by hand) |
| `_to_delete/` | holding folder; skills ignore it | the founder |
| `scripts/` | helpers the skills call | — |
| `.claude/skills/` | `zoom-transcript-sync`, `discovery-debrief`, `transcript-brief`, `transcript-pipeline` | — |

## State lives on `main`

This runs in ephemeral cloud containers: anything not pushed is lost when the session
ends, and every new session starts from a fresh clone. So the **`main` branch is the
single source of truth** for transcripts and state files, and each skill pushes its own
results straight to `main` when it finishes. The repo owner has authorized this for the
skills' data commits, even when the session was assigned a different working branch.
(Changes to skills, scripts or this file are ordinary code changes: those go through
the session's working branch and a PR as usual.)

Every skill that reads or writes state follows the same two steps:

1. **Before reading any state file:** `scripts/state_pull.sh`. It fetches, switches to
   `main` if needed and rebases onto the latest `origin/main`. If it fails, stop — reading
   stale state leads to double-fetching and double-counting.
2. **After writing:** `scripts/state_push.sh "<message>" <paths…>`, passing only the
   files that skill owns (see the table). It commits those paths, rebases onto
   concurrent pushes and pushes with retries. A failed push is a failed run: report it
   and do not claim the work is saved.

Scratch files (raw tool results, extracted PDF text) go in the session scratchpad or
`/tmp`, never in the repo.

## Large tool results

`.claude/settings.json` sets `MAX_MCP_OUTPUT_TOKENS=4000`. Any Zoom or Drive result
larger than that is saved by the harness to a file, whose path is printed in the tool
result. Always work from that file with the `scripts/` helpers. Never retype a
transcript, JSON or base64 from a tool result into a file — retyping corrupts it.

- `scripts/format_zoom_transcript.py RAW OUT DATE TOPIC UUID SOURCE` — Zoom JSON → transcript file
- `scripts/drive_download.py RAW OUT [SIZE]` — Drive base64 → exact bytes (+ `OUT.txt` for PDFs)
