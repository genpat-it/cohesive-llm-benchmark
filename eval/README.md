# eval/

The LLM evaluation pipeline. Supports both single-turn
(`dataset_50.jsonl`) and multi-turn (`dataset_modifications.jsonl`)
corpora.

## Single-turn pipeline

| Script | Reads | Writes | What it does |
|---|---|---|---|
| `run_llm.py`      | `dataset/dataset_50.jsonl` | `$BENCH_RUNS_DIR/runs.jsonl`     | Sends every prompt to `LLM_API_URL/chat`, captures the returned `nextflow_code` |
| `validate_llm.py` | `runs.jsonl` (+ framework via `NGSMANAGER_DIR`) | `$BENCH_RUNS_DIR/verdicts.jsonl` + `report.md` | Runs each generated `.nf` through `nextflow -stub-run`, judges, categorises errors |
| `emit_report.py`  | `verdicts.jsonl` (and/or `verdicts_modifications.jsonl`) | `report.tsv`/`.csv` (and/or `report_modifications.tsv`/`.csv`) | Converts verdicts to spreadsheet-friendly formats |

## Multi-turn pipeline

| Script | Reads | Writes | What it does |
|---|---|---|---|
| `run_llm_multi_turn.py`      | `dataset/dataset_modifications.jsonl` | `$BENCH_RUNS_DIR/runs_modifications.jsonl` | Walks each conversation reusing the same `session_id` across turns; captures one `nextflow_code` per turn |
| `validate_llm_multi_turn.py` | `runs_modifications.jsonl` | `verdicts_modifications.jsonl` + `report_modifications.md` | Validates each turn independently with `nextflow -stub-run`; tags turns with their `conv_id`, `turn_index`, `modification_kind`, `base_id` |
| `emit_report.py`             | `verdicts_modifications.jsonl` | `report_modifications.tsv` + `.csv` | Same emitter, handles both shapes |

## Environment variables

```bash
export LLM_API_URL=http://127.0.0.1:8765        # your LLM server (no trailing slash needed)
export NGSMANAGER_DIR=/path/to/cohesive-ngsmanager
export BENCH_RUNS_DIR=$(pwd)/results/my_run     # any directory; will be created
```

## End-to-end one-liner

```bash
python eval/run_llm.py && python eval/validate_llm.py && python eval/emit_report.py
```

Roughly 30 minutes for the curated 50 prompts on a typical machine, ~3 hours
for the full 200 single-turn + 159 multi-turn corpus.

## Command-line flags

`run_llm.py` and `validate_llm.py` both support:

- `--first=N`         — run only the first N prompts (smoke test)
- `--only=id1,id2,…`  — run only specific prompt IDs (cherry-pick)

Example: re-run just the failing ones from a previous run

```bash
python eval/validate_llm.py --only=A03_mlst_salmonella,B02_shovill_ecoli
```

## The chat handshake

`izs-llm`-style agents use a two-turn handshake:

1. Send the prompt → status `CHATTING` + a plan
2. Send `"Yes, approve it..."` → status `APPROVED` + the `.nf`

`run_llm.py` automates this for up to 4 turns. If your LLM exposes the
code on turn 1 directly, that's fine too — the loop returns on the first
turn that yields `nextflow_code`.

## Output verdict schema

Each line of `verdicts.jsonl` has these 24 fields (see also
`docs/dataset_schema.md`):

```
id, prompt, ground_truth_code, params, expected_processes,
llm_reply_excerpt, nextflow_code,
syntax_valid, semantic_valid, n_processes,
error_category, error_detail,
elapsed_s, turns,
code_chars, code_lines,
included_steps, called_steps, hallucinated_steps, n_workflow_calls,
ground_truth_steps, matches_gt_steps, extra_steps, missing_steps
```

`error_category` is one of:

`none, no_code, arity_error, missing_param, missing_input, channel_emit,
compile_error, unknown_step, species_filter, ngsmanager_naming,
file_not_found, silent_no_op, partial_dag, other`

See `docs/error_taxonomy.md` for what each one means and how to triage it.

## Notes about LLM API keys

**This repo never stores credentials.** Whatever LLM you point
`LLM_API_URL` at, you configure its keys inside that server (e.g.
the `MISTRAL_API_KEY` in the `izs-llm` `.env`). Make sure to add the
LLM server's `.env` to its `.gitignore`.
