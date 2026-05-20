#!/usr/bin/env bash
# Sync the JSONL artifacts into docs/data/ so the GitHub Pages site reflects
# the current state of the repo. Run after regenerating any dataset or
# results/example_run*/ verdicts.

set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO="$(cd "$HERE/.." && pwd)"
DEST="$HERE/data"

mkdir -p "$DEST"

cp "$REPO/dataset/dataset_50.jsonl"                                                       "$DEST/dataset_50.jsonl"
cp "$REPO/dataset/dataset_modifications.jsonl"                                            "$DEST/dataset_modifications.jsonl"
cp "$REPO/results/example_run_mistral/verdicts.jsonl"                                     "$DEST/example_run_verdicts.jsonl"
cp "$REPO/results/example_run_mistral_multi_turn/verdicts_modifications.jsonl"            "$DEST/example_run_verdicts_modifications.jsonl"

echo "Synced 4 jsonl files into $DEST"
ls -la "$DEST"
