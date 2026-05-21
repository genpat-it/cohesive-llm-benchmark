#!/usr/bin/env bash
# finalize_run.sh -- post-LLM-run housekeeping in one command.
#
# After an LLM run has landed verdicts and reports, run this script to:
#   1. augment verdicts with verdict_tags + llm_full_reply + llm_turn_logs
#   2. copy the augmented files into docs/data/ (the static site source)
#   3. rebuild the run history table (results/history.jsonl + docs/data/history.jsonl)
#   4. regenerate badges (docs/badges/*.json)
#   5. rebuild the unified manifest (docs/data/benchmark.json)
#   6. git add + commit + push  (only if --commit is passed)
#
# Usage:
#   scripts/finalize_run.sh                # dry: refresh artefacts, no git
#   scripts/finalize_run.sh --commit       # also git commit + push
#   scripts/finalize_run.sh --commit -m "custom commit msg"
#
# Run from the repo root (the script cds to it anyway).

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

DO_COMMIT=0
COMMIT_MSG="results: refresh after LLM run"
while [[ $# -gt 0 ]]; do
  case "$1" in
    --commit) DO_COMMIT=1; shift ;;
    -m) COMMIT_MSG="$2"; shift 2 ;;
    *) echo "unknown arg: $1" >&2; exit 2 ;;
  esac
done

echo "[1/5] Augmenting verdicts in every results/ subdir..."
python3.11 scripts/augment_verdicts.py

echo "[2/5] Copying augmented verdicts into docs/data/..."
shopt -s nullglob
for d in results/*/; do
  name="$(basename "$d")"
  if [[ -f "$d/verdicts_augmented.jsonl" ]]; then
    cp "$d/verdicts_augmented.jsonl" "docs/data/${name}_verdicts_augmented.jsonl"
  fi
  if [[ -f "$d/verdicts_modifications_augmented.jsonl" ]]; then
    cp "$d/verdicts_modifications_augmented.jsonl" "docs/data/${name}_verdicts_modifications_augmented.jsonl"
  fi
  if [[ -f "$d/metadata.json" ]]; then
    cp "$d/metadata.json" "docs/data/${name}_metadata.json"
  fi
done

echo "[3/5] Rebuilding run history..."
python3.11 scripts/build_history.py

echo "[4/5] Regenerating badges..."
python3.11 scripts/generate_badges.py

echo "[5/5] Rebuilding consolidated manifest..."
python3.11 scripts/build_manifest.py

if [[ "$DO_COMMIT" -eq 1 ]]; then
  echo
  echo "Staging changes..."
  git add docs/data/ docs/badges/ results/history.jsonl results/*/verdicts_augmented.jsonl results/*/verdicts_modifications_augmented.jsonl 2>/dev/null || true
  if git diff --cached --quiet; then
    echo "Nothing to commit -- working tree already in sync."
    exit 0
  fi
  git commit -m "$(cat <<EOF
$COMMIT_MSG

Auto-generated via scripts/finalize_run.sh: augmented verdicts +
refreshed badges + history + benchmark.json manifest.

Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>
EOF
)"
  echo "Pushing..."
  git push origin main
  echo "Done."
else
  echo
  echo "Dry mode -- artefacts refreshed but nothing committed."
  echo "Re-run with --commit to publish."
fi
