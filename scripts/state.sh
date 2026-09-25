#!/usr/bin/env bash
# Git side of how every data-writing skill saves its work: branch → push → (PR + merge
# via the GitHub tools) → sync local main. See CLAUDE.md "Publishing data".
#
#   scripts/state.sh pull
#       Before reading any state: switch to main and fast-forward to origin/main.
#   scripts/state.sh publish <skill> "<title>" <path> [<path> ...]
#       Commit exactly those paths on a new branch data/<skill>-<utc stamp>-<rand>, rebased on
#       origin/main, and push it. Prints BRANCH=<name>, or NOTHING if no changes.
#   scripts/state.sh refresh <branch>
#       The merge was refused because main moved: rebase the branch onto origin/main
#       and force-push it (it is this run's own data branch). Exit 2 on a real conflict.
#   scripts/state.sh finish <branch>
#       After the PR is merged: fast-forward local main, delete the branch here and on origin.
set -uo pipefail
cd "$(git -C "$(dirname "$0")" rev-parse --show-toplevel)" || exit 1
BASE="${TRANSCRIPTS_STATE_BRANCH:-main}"

retry() {  # network retries, backoff 2,4,8,16s
  local d=2
  for _ in 1 2 3 4 5; do "$@" && return 0; sleep "$d"; d=$((d * 2)); done
  return 1
}
die() { echo "state: $*" >&2; exit 1; }

sync_base() {
  retry git fetch -q origin "$BASE" || die "cannot fetch origin/$BASE"
  local cur; cur="$(git rev-parse --abbrev-ref HEAD)"
  if [ "$cur" != "$BASE" ]; then
    git checkout -q "$BASE" 2>/dev/null || git checkout -q -b "$BASE" "origin/$BASE" \
      || die "cannot switch from '$cur' to $BASE (uncommitted changes to tracked files?)"
    echo "state: switched from '$cur' to $BASE"
  fi
  git merge -q --ff-only "origin/$BASE" \
    || die "local $BASE has diverged from origin/$BASE; resolve by hand before running skills"
}

cmd="${1:-}"; shift || true
case "$cmd" in
  pull)
    sync_base
    echo "state: $BASE at $(git rev-parse --short HEAD)"
    ;;

  publish)
    [ "$#" -ge 3 ] || die "usage: publish <skill> \"<title>\" <path>..."
    skill="$1"; title="$2"; shift 2
    git add -A -- "$@" || die "git add failed"
    if git diff --cached --quiet; then echo "NOTHING"; exit 0; fi
    # timestamp + random suffix: two sessions can publish in the same second
    branch="data/${skill}-$(date -u +%Y%m%d-%H%M%S)-$(od -An -N3 -tx1 /dev/urandom | tr -d ' \n')"
    git checkout -q -b "$branch" || die "cannot create $branch"
    git commit -q -m "$title" || die "commit failed"
    retry git fetch -q origin "$BASE" || die "cannot fetch origin/$BASE"
    if ! git rebase -q "origin/$BASE"; then
      git rebase --abort
      die "branch $branch conflicts with origin/$BASE; commit kept locally, not pushed"
    fi
    retry git push -q -u origin "$branch" || die "push of $branch failed; commit is local only"
    echo "BRANCH=$branch"
    ;;

  refresh)
    branch="${1:?usage: refresh <branch>}"
    case "$branch" in data/*) ;; *) die "refresh only rewrites data/* branches";; esac
    retry git fetch -q origin "$BASE" || die "cannot fetch origin/$BASE"
    git checkout -q "$branch" || die "no local branch $branch"
    if ! git rebase -q "origin/$BASE"; then
      git rebase --abort
      echo "state: $branch conflicts with $BASE; needs a human" >&2
      exit 2
    fi
    retry git push -q --force-with-lease origin "$branch" || die "force-push of $branch failed"
    echo "state: $branch rebased onto $BASE and pushed"
    ;;

  finish)
    branch="${1:?usage: finish <branch>}"
    sync_base
    # Delete only if main already holds the branch's content (squash merges leave no
    # ancestry, so compare the files the branch changed).
    if git rev-parse -q --verify "$branch" >/dev/null; then
      files="$(git diff --name-only "$(git merge-base "$branch" "origin/$BASE")" "$branch")"
      if [ -n "$files" ] && ! git diff --quiet "origin/$BASE" "$branch" -- $files; then
        echo "state: $BASE does not contain $branch yet (not merged?); branch kept" >&2
        exit 1
      fi
    fi
    git branch -q -D "$branch" 2>/dev/null
    # Cloud sessions cannot delete remote branches (the git proxy returns 403). The repo's
    # "Automatically delete head branches" setting removes merged data branches instead.
    git push -q origin --delete "$branch" >/dev/null 2>&1 \
      || echo "state: origin/$branch left for GitHub's auto-delete (harmless)"
    echo "state: $BASE at $(git rev-parse --short HEAD); $branch cleaned up"
    ;;

  *) die "usage: state.sh pull | publish <skill> <title> <paths...> | refresh <branch> | finish <branch>" ;;
esac
