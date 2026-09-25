#!/usr/bin/env bash
# SessionStart hook. Makes a fresh cloud container ready to run the transcript skills.
ROOT="${CLAUDE_PROJECT_DIR:-$(cd "$(dirname "$0")/.." && pwd)}"

# The repo root IS the transcripts folder. Account-level skills (update-thesis, and older
# copies of the sync/debrief skills) still say ~/transcripts, so point that at the repo.
if [ ! -e "$HOME/transcripts" ]; then
  ln -s "$ROOT" "$HOME/transcripts"
fi

# PDF extraction for Drive transcripts. The system cryptography package needs cffi
# before pypdf will import.
if [ "${CLAUDE_CODE_REMOTE:-}" = "true" ]; then
  python3 -c "import pypdf" 2>/dev/null \
    || pip install -q pypdf cffi >/dev/null 2>&1 \
    || echo "session_start: pypdf install failed; Drive PDFs cannot be synced this session"
fi
exit 0
