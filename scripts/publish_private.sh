#!/usr/bin/env bash
set -euo pipefail

OWNER="${GITHUB_OWNER:-EasonZhangyichen}"
REPO="${GITHUB_REPO:-blackboard-design-skill}"
DESCRIPTION="Portable Agent Skill for generating age-appropriate Chinese school blackboard designs"

command -v git >/dev/null || { echo "Missing git"; exit 1; }
command -v gh >/dev/null || { echo "Missing GitHub CLI: install with 'brew install gh'"; exit 1; }

gh auth status
python3 scripts/validate_package.py
python3 scripts/build_release.py

if [[ ! -d .git ]]; then
  git init -b main
fi

if [[ -z "$(git config user.name || true)" || -z "$(git config user.email || true)" ]]; then
  echo "Please configure git user.name and user.email before publishing."
  exit 1
fi

git add .
if ! git diff --cached --quiet; then
  git commit -m "feat: release blackboard design skill v0.7.1"
fi

if gh repo view "$OWNER/$REPO" >/dev/null 2>&1; then
  VISIBILITY="$(gh repo view "$OWNER/$REPO" --json visibility --jq .visibility)"
  if [[ "$VISIBILITY" != "PRIVATE" ]]; then
    echo "Repository exists but is not private. Aborting."
    exit 1
  fi
  if ! git remote get-url origin >/dev/null 2>&1; then
    git remote add origin "https://github.com/$OWNER/$REPO.git"
  fi
  git push -u origin main
else
  gh repo create "$OWNER/$REPO" \
    --private \
    --description "$DESCRIPTION" \
    --source . \
    --remote origin \
    --push
fi

echo "Published privately: https://github.com/$OWNER/$REPO"
