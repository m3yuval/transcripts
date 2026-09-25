#!/usr/bin/env bash
# Bring the checkout up to date with the state branch BEFORE reading any state file.
# Every skill runs this first, because another session may have pushed since this
# container was cloned.
set -uo pipefail
cd "$(git -C "$(dirname "$0")" rev-parse --show-toplevel)" || exit 1
BRANCH="${TRANSCRIPTS_STATE_BRANCH:-main}"

retry() {  # network retries with backoff 2,4,8,16s
  local d=2
  for _ in 1 2 3 4 5; do "$@" && return 0; sleep "$d"; d=$((d * 2)); done
  return 1
}

retry git fetch -q origin "$BRANCH" || { echo "state_pull: cannot fetch origin/$BRANCH" >&2; exit 1; }

cur="$(git rev-parse --abbrev-ref HEAD)"
if [ "$cur" != "$BRANCH" ]; then
  if ! git diff --quiet || ! git diff --cached --quiet; then
    echo "state_pull: uncommitted changes on '$cur'; commit or stash them before switching to $BRANCH" >&2
    exit 1
  fi
  git checkout -q "$BRANCH" 2>/dev/null || git checkout -q -b "$BRANCH" "origin/$BRANCH" || exit 1
  echo "state_pull: switched from '$cur' to '$BRANCH'"
fi

git pull -q --rebase --autostash origin "$BRANCH" || { echo "state_pull: pull failed" >&2; exit 1; }
echo "state_pull: $BRANCH at $(git rev-parse --short HEAD)"
