# cohesive-llm-benchmark

[![validate ground truth](https://github.com/genpat-it/cohesive-llm-benchmark/actions/workflows/validate.yml/badge.svg)](https://github.com/genpat-it/cohesive-llm-benchmark/actions/workflows/validate.yml)
[![single-turn](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/genpat-it/cohesive-llm-benchmark/main/docs/badges/dataset_single.json)](dataset/dataset_50.jsonl)
[![multi-turn](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/genpat-it/cohesive-llm-benchmark/main/docs/badges/dataset_multi.json)](dataset/dataset_modifications.jsonl)
[![izs-llm single-turn](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/genpat-it/cohesive-llm-benchmark/main/docs/badges/llm_single_turn.json)](results/example_run_mistral/report.md)
[![izs-llm multi-turn](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/genpat-it/cohesive-llm-benchmark/main/docs/badges/llm_multi_turn.json)](results/example_run_mistral_multi_turn/report_modifications.md)
[![LLM eval](https://github.com/genpat-it/cohesive-llm-benchmark/actions/workflows/llm-eval.yml/badge.svg)](https://github.com/genpat-it/cohesive-llm-benchmark/actions/workflows/llm-eval.yml)

**Live site & interactive explorer:** https://genpat-it.github.io/cohesive-llm-benchmark/

**Cross-repo trigger:** every push to [`mgradyn/izs-llm`](https://github.com/mgradyn/izs-llm) `main` can fire the full benchmark automatically — see [`docs/TRIGGER_FROM_IZS_LLM.md`](docs/TRIGGER_FROM_IZS_LLM.md).

**Corpus size (May 2026):** 200 single-turn examples + 159 multi-turn conversations (330 turns). Every entry passes `nextflow -stub-run` validation against the framework. See [dataset/dataset_200.jsonl](dataset/dataset_200.jsonl) and [dataset/dataset_modifications_full.jsonl](dataset/dataset_modifications_full.jsonl).

A benchmark for natural-language → Nextflow pipeline generators targeting the
[cohesive-ngsmanager](https://github.com/genpat-it/cohesive-ngsmanager)
framework.

## Prerequisites — three external pieces you need

This repo is the **benchmark**, not the LLM and not the framework. To run
the bench end-to-end you need all three:

| Component | Where | Why |
|---|---|---|
| 1. **This repo** (`cohesive-llm-benchmark`) | `git clone https://github.com/genpat-it/cohesive-llm-benchmark` | dataset, harness, eval scripts |
| 2. **The target framework** (`cohesive-ngsmanager`) | `git clone https://github.com/genpat-it/cohesive-ngsmanager` | Nextflow steps/functions the benchmark validates against |
| 3. **An LLM service speaking the `/chat` contract** | e.g.\ [`izs-llm`](https://github.com/mgradyn/izs-llm) — `git clone https://github.com/mgradyn/izs-llm` | the system under test |

Point the bench at (2) via the `NGSMANAGER_DIR` env var, and at (3) via
`LLM_API_URL`. See [`INSTALL.md`](INSTALL.md) for the step-by-step
setup of each, including a working `izs-llm` reference deployment with
its own `MISTRAL_API_KEY`.

> **Validating only the ground truth?** Then you only need (1) + (2);
> the LLM is not exercised. Just `python harness/harness.py`.

---

This repo contains everything needed to:

1. **Train** an LLM (or RAG agent) on a small ground-truth corpus of
   `(prompt, nextflow_code, params)` triples.
2. **Evaluate** an LLM you are building (or hosted) by pointing the eval at
   a `/chat` endpoint, then running each generated `.nf` through Nextflow
   stub-run for end-to-end DAG validation.
3. **Triage** the failures: each error is auto-categorised
   (`arity_error`, `missing_param`, `silent_no_op`, `channel_emit`,
   `unknown_step`, `hallucination`, ...) so you can see *why* the model is
   wrong, not just *that* it is.

Everything is reproducible from this repo plus a checkout of
`cohesive-ngsmanager` and a running LLM endpoint.

---

## Repository layout

```
cohesive-llm-benchmark/
├── README.md                      ← this file
├── METHODOLOGY.md                 ← how the bench works, what it measures
├── INSTALL.md                     ← step-by-step setup
├── requirements.txt               ← Python deps
│
├── dataset/                       ← the ground-truth corpus
│   ├── dataset_50.jsonl           ← 50 single-turn (prompt, nextflow_code) pairs
│   ├── dataset_modifications.jsonl ← 17 multi-turn modification conversations
│   ├── blueprints.py              ← programmatic definition of the 50 single-turn pairs
│   ├── modifications.py           ← programmatic definition of the 17 conversations
│   ├── emit_jsonl.py              ← regenerate dataset_50.jsonl from blueprints
│   ├── emit_modifications.py     ← regenerate dataset_modifications.jsonl
│   ├── validate_modifications.py ← per-turn nextflow stub-run validation
│   └── README.md                  ← schema and conventions
│
├── harness/                       ← Nextflow validation engine
│   └── harness.py                 ← stub-run runner with dummy input materialisation
│
├── eval/                          ← LLM evaluation pipeline
│   ├── run_llm.py                 ← POST each prompt to a /chat endpoint
│   ├── validate_llm.py            ← run nextflow stub-run on each LLM output
│   ├── emit_report.py             ← convert verdicts.jsonl to TSV/CSV
│   └── README.md                  ← how to run the evaluation
│
├── tools/                         ← framework introspection
│   ├── build_inventory.py         ← extract take:/emit:/SPECIES_SCHEMA from steps
│   └── inventory_snapshot.json    ← snapshot taken 2026-05-19
│
├── docs/
│   ├── error_taxonomy.md          ← every failure category, with examples
│   └── dataset_schema.md          ← detail of every JSONL field
│
└── results/                       ← gitignored, except example_run_mistral/
    └── example_run_mistral/       ← the run we did against izs-llm on 2026-05-19
        ├── runs.jsonl             ← raw LLM responses
        ├── verdicts.jsonl         ← per-example structured verdict
        ├── report.md              ← human report
        ├── report.tsv             ← TSV for grep / awk
        └── report.csv             ← Excel / LibreOffice
```

---

## Headline result — izs-llm against the full corpus

The [`izs-llm`](https://github.com/mgradyn/izs-llm) agent
(Mistral-backed, RAG over the framework catalog) evaluated against the
**full 200 single-turn** corpus
(`results/llm_full_200/`):

| Metric | Value |
|---|---|
| Prompts answered with code | 200 / 200 |
| Syntactically valid (`nextflow -preview`) | 200 / 200 |
| **Semantically valid (`nextflow -stub-run`)** | **185 / 200  (92.5 %)** |
| Hallucinated (non-existent) steps | 0 / 200 |
| LLM round-trip total | 62 min |
| Validation total | 88 min |

Failures concentrate on:

- **8 / 15** — `missing_param: step_3TX_species__kmerfinder__db`.
  The LLM over-engineers simple mono-step prompts by injecting an
  upstream species-ID step that needs a database path the user did not
  provide.
- **3 / 15** — `silent_no_op`. The LLM picked a `genus_species` or
  `seq_type` filtered by a step's `when:` clause; the pipeline runs but
  schedules zero tasks.
- **2 / 15** — `partial_dag`. Only a subset of expected processes fired.
- **2 / 15** — naming / file-not-found edge cases.

For the original 50-prompt curated subset run (`results/example_run_mistral/`),
the score was **43 / 50 (86 %)** — see that folder for the historical baseline.

---

## Multi-turn modifications

The single-turn corpus tests a model's ability to produce a correct
pipeline from scratch. Real users iterate: they ask for a pipeline, then
ask to add a step, swap a tool, drop a step, or re-target the same chain
at a different species. `dataset/dataset_modifications_full.jsonl`
captures **159 conversations (330 turns)** — 17 base + 142 combinatorial
— covering four transformations:

| Kind | Count | Example |
|---|---|---|
| `add`            | ~50 | "Now also run classic MLST in parallel on the same assembly." |
| `replace`        | ~50 | "Use Shovill instead of SPAdes for the assembly." |
| `drop`           | ~30 | "Drop the cgMLST step, only keep MLST." |
| `switch_species` | ~28 | "Same pipeline, but for *Salmonella enterica* instead of *Listeria*." |

Every turn of every conversation is validated independently via
`nextflow -stub-run` (330 / 330 turns pass in ~120 min).

Run them yourself with:

```bash
python dataset/validate_modifications.py --extended
```

### LLM evaluation on the full multi-turn corpus

The izs-llm run captured in `results/llm_full_multi_turn/` scores
**287 / 330 turns (87 %)** and **136 / 159 fully-passing conversations
(86 %)**. Pass rate per transformation:

| Kind | Turns | Pass | % |
|----|-----:|-----:|---:|
| `replace`        | 99  | 96 | 97 |
| `add`            | 104 | 95 | 91 |
| `switch_species` | 61  | 48 | 79 |
| `drop`           | 66  | 48 | 73 |

The historical curated-subset run (`results/example_run_mistral_multi_turn/`)
scored 29 / 34 turns (85 %) and 14 / 17 conversations (82 %).

Top failure categories on the full corpus:

- `MOD_M03_B01_add_trimming` (both turns) — the LLM adds an upstream
  species-ID step (kmerfinder) and a database param the user did not
  provide → `missing_param`.
- `MOD_M11_H01_drop_cgmlst` (both turns) — same `missing_param` on t1,
  `silent_no_op` on t2 (the requested drop leaves an unsupported species
  filtered by `when:`).
- `MOD_M14_E02_switch_species_to_salmonella` (turn 1 only) — the LLM
  emits step names that look up files outside the test fixture's
  layout → `file_not_found`. Turn 2 (the actual switch) passes.

See `results/example_run_mistral_multi_turn/report_modifications.md` for
per-turn detail.

See `docs/dataset_schema.md` for the JSONL shape and `dataset/README.md`
for how to add new conversations.

---

## Quickstart (TL;DR)

You need a checkout of `cohesive-ngsmanager` next to this repo and an LLM
endpoint that speaks the same `/chat` contract as `izs-llm`.
**The LLM API key is *not* committed — configure it yourself, see below.**

```bash
# 0. Install Python deps (Python ≥ 3.11)
pip install -r requirements.txt

# 1. Point the harness at your cohesive-ngsmanager checkout
export NGSMANAGER_DIR=/path/to/cohesive-ngsmanager

# 2. (Optional) regenerate the ground-truth dataset from blueprints
python dataset/emit_jsonl.py

# 3. (Optional) validate the ground truth itself
python harness/harness.py             # 50 examples,  ~25 min
python harness/harness.py --extended  # 200 examples, ~90 min

# 4. Run your LLM against the prompts
#    The LLM is expected to expose POST <URL>/chat with JSON
#    {session_id, message, generate_diagrams}
#    and return JSON {status, reply, nextflow_code, ...}.
export LLM_API_URL=http://localhost:8765
export BENCH_RUNS_DIR=./results/my_run
python eval/run_llm.py                # 50 prompts,  ~10 min LLM
# or for the full 200:
BENCH_DATASET=dataset/dataset_200.jsonl python eval/run_llm.py     # ~60 min

# 5. Validate each generated .nf with nextflow -stub-run
python eval/validate_llm.py           # ~20 min for 50, ~90 min for 200

# 6. Emit human-friendly TSV / CSV / Markdown reports
python eval/emit_report.py

# 7. Open results
$BROWSER ./results/my_run/report.md
```

---

## Configuration (read this before running)

The repo has **zero secrets committed**. You must provide:

| Variable | Required by | What it is |
|---|---|---|
| `NGSMANAGER_DIR`       | `harness/`, `eval/validate_llm.py` | path to your `cohesive-ngsmanager` checkout |
| `LLM_API_URL`          | `eval/run_llm.py`                  | base URL of your LLM, e.g. `http://localhost:8765` |
| `BENCH_RUNS_DIR`       | `eval/*`                           | where to write `runs.jsonl`/`verdicts.jsonl`/`report.*` |
| `MISTRAL_API_KEY` *etc.* | the LLM you point `LLM_API_URL` at | **your own key**, configured **inside the LLM server**, never in this repo |

If you don't already have an LLM server, the included example results were
produced against the `izs-llm` FastAPI app. To run it locally you would:

```bash
git clone https://github.com/mgradyn/izs-llm
cd izs-llm
echo 'MISTRAL_API_KEY=<your-own-key>'     > .env       # ← configure this
echo 'NGSMANAGER_DIR=/path/to/cohesive-ngsmanager' >> .env
pip install -r requirements.txt
set -a && source .env && set +a
uvicorn app.api:app --host 127.0.0.1 --port 8765
```

then point `LLM_API_URL` at it. **Do not commit your `.env`.**

---

## What the bench measures

Every generated `.nf` is judged at three levels:

1. **Syntax** — `nextflow -preview` parses the DSL2.
2. **DAG construction** — `nextflow -stub-run` builds the workflow graph
   with the same `params.json` shape the ground truth uses.
3. **DAG completeness** — the number of distinct process placeholders that
   appear in the live progress display must be `≥ expected_processes`
   declared in the ground truth.

A pipeline that compiles but schedules **zero** tasks (the worst failure
mode — exit code 0, no output) is flagged as `silent_no_op`. See
`docs/error_taxonomy.md`.

See [`METHODOLOGY.md`](METHODOLOGY.md) for the full reasoning behind each
check, the choice of dummy input layouts, and the limitations.

---

## Extending the dataset (e.g. from 50 → 200)

Open `dataset/blueprints.py`, append entries to `build_all()` using the
existing helpers:

- `mono_typing(...)` — single typing/AMR step on an existing assembly
- `mono_assembly(...)` — single de-novo assembly from FASTQ
- `mono_species_id(...)` — single species-ID step from FASTQ
- `trim_assembly(...)` — fastp/trimmomatic/chopper + spades/shovill/flye/...
- `trim_assembly_typing(...)` — 3-step chain
- `four_step(...)` — 2 downstream steps in parallel after assembly
- `species_then_assembly(...)` — species ID in parallel with assembly

Each helper takes care of the canonical `take:` arity, the right emit name
(`.trimmed` / `.assembled` / `.assembly`), the right input getter
(`getInput` / `getSingleInput` / `getAssembly`), and the right
`expected_processes` count.

Then validate:

```bash
python harness/harness.py --only=<your_new_id>
# or, full set:
python harness/harness.py
```

Re-emit the JSONL:

```bash
python dataset/emit_jsonl.py
```
