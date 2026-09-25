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

This runs in ephemeral cloud containers: anything not on `main` is lost to the next
session, which starts from a fresh clone. So `main` is the single source of truth for
transcripts and state files. Every component that writes data saves it the same way —
its own branch, a PR, and a merge into `main` — so each run leaves a reviewable PR
behind. The repo owner has authorized the skills to create and merge these PRs
themselves, without asking, even when the session was assigned a different working
branch. (Changes to skills, scripts or this file are ordinary code changes on the
session's working branch.)

### Before reading any state

`scripts/state.sh pull` — switches to `main` and fast-forwards to `origin/main`, since
another session may have merged since this container was cloned. If it fails, stop:
stale state means double-fetching and double-counting.

### Publishing data

Run at the end of each writing skill, with only the files that skill owns (table above):

1. `scripts/state.sh publish <skill> "<title>" <paths…>` — commits those paths on a new
   branch `data/<skill>-<stamp>`, rebased on `origin/main`, and pushes it. It prints
   `BRANCH=<name>`, or `NOTHING` when nothing changed (then stop: no PR).
2. Open the PR with `mcp__github__create_pull_request`: owner `m3yuval`, repo
   `transcripts`, head `<branch>`, base `main`, title `<title>`, body = what changed in
   2–5 lines (files added, counts, claims touched), ending with
   `🤖 Generated with [Claude Code](https://claude.com/claude-code)`.
3. Merge it with `mcp__github__merge_pull_request`, `merge_method: "squash"`,
   `commit_title: "<title> (#<PR number>)"`.
4. If the merge is refused because `main` moved, run `scripts/state.sh refresh <branch>`
   and merge once more. Exit 2 from `refresh` means a real conflict (usually two syncs
   raced on `index.json`): stop, leave the PR open, and report its link — do not resolve
   it by hand. Everything the PR holds is re-fetched or re-analyzed by the next run.
5. `scripts/state.sh finish <branch>` — puts the checkout back on the updated `main` and
   deletes the branch. It refuses to delete a branch whose content is not on `main`.

The work counts as saved only after step 5. A failure at any step is a failed run:
report the step, the branch and the PR link if there is one; never claim the data is
saved. Load the GitHub tools with ToolSearch (`select:mcp__github__create_pull_request,mcp__github__merge_pull_request`)
if they are not already loaded.

Scratch files (raw tool results, extracted PDF text) go in the session scratchpad or
`/tmp`, never in the repo.

## Large tool results

`.claude/settings.json` sets `MAX_MCP_OUTPUT_TOKENS=4000`. Any Zoom or Drive result
larger than that is saved by the harness to a file, whose path is printed in the tool
result. Always work from that file with the `scripts/` helpers. Never retype a
transcript, JSON or base64 from a tool result into a file — retyping corrupts it.

- `scripts/format_zoom_transcript.py RAW OUT DATE TOPIC UUID SOURCE` — Zoom JSON → transcript file
- `scripts/drive_download.py RAW OUT [SIZE]` — Drive base64 → exact bytes (+ `OUT.txt` for PDFs)
