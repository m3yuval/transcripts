#!/usr/bin/env bash
# Commit exactly the given paths and push them to the state branch.
# usage: scripts/state_push.sh "<commit message>" <path> [<path> ...]
# Exit 0 = pushed (or nothing to commit), 1 = commit or push failed.
set -uo pipefail
cd "$(git -C "$(dirname "$0")" rev-parse --show-toplevel)" || exit 1
BRANCH="${TRANSCRIPTS_STATE_BRANCH:-main}"
msg="$1"; shift
[ "$#" -gt 0 ] || { echo "state_push: no paths given" >&2; exit 1; }

git add -A -- "$@" || exit 1
if git diff --cached --quiet; then
  echo "state_push: nothing to commit"
  exit 0
fi
git commit -q -m "$msg" || exit 1

d=2
for _ in 1 2 3 4 5; do
  # Rebase onto whatever other sessions pushed meanwhile, then push.
  if git pull -q --rebase origin "$BRANCH" && git push -q origin "HEAD:$BRANCH"; then
    echo "state_push: pushed $(git rev-parse --short HEAD) to $BRANCH"
    exit 0
  fi
  git rebase --abort 2>/dev/null
  sleep "$d"; d=$((d * 2))
done
echo "state_push: push to $BRANCH failed after retries; commit $(git rev-parse --short HEAD) is local only" >&2
exit 1
