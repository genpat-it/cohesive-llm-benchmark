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
cp "$REPO/dataset/dataset_200.jsonl"                                                      "$DEST/dataset_200.jsonl"
cp "$REPO/dataset/dataset_modifications.jsonl"                                            "$DEST/dataset_modifications.jsonl"
cp "$REPO/dataset/dataset_modifications_full.jsonl"                                       "$DEST/dataset_modifications_full.jsonl"

# Full-corpus LLM verdicts (200 single + 330 turn multi)
cp -f "$REPO/results/llm_full_200/verdicts.jsonl"                                          "$DEST/llm_full_200_verdicts.jsonl"                  2>/dev/null || true
cp -f "$REPO/results/llm_full_200/metadata.json"                                           "$DEST/llm_full_200_metadata.json"                   2>/dev/null || true
cp -f "$REPO/results/llm_full_multi_turn/verdicts_modifications.jsonl"                     "$DEST/llm_full_multi_turn_verdicts.jsonl"           2>/dev/null || true
cp -f "$REPO/results/llm_full_multi_turn/metadata.json"                                    "$DEST/llm_full_multi_turn_metadata.json"            2>/dev/null || true
cp "$REPO/results/example_run_mistral/verdicts.jsonl"                                     "$DEST/example_run_verdicts.jsonl"
cp "$REPO/results/example_run_mistral_multi_turn/verdicts_modifications.jsonl"            "$DEST/example_run_verdicts_modifications.jsonl"

# metadata.json files capturing version pins of each reference run
cp -f "$REPO/results/example_run_mistral/metadata.json"             "$DEST/example_run_metadata.json"             2>/dev/null || true
cp -f "$REPO/results/example_run_mistral_multi_turn/metadata.json"  "$DEST/example_run_metadata_multi_turn.json"  2>/dev/null || true

# Run history (aggregated by scripts/build_history.py)
cp -f "$REPO/results/history.jsonl" "$DEST/history.jsonl" 2>/dev/null || true

echo "Synced data + metadata + history into $DEST"
ls -la "$DEST"
