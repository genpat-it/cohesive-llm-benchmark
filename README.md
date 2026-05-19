# cohesive-llm-benchmark

A benchmark for natural-language → Nextflow pipeline generators targeting the
[cohesive-ngsmanager](https://github.com/genpat-it/cohesive-ngsmanager)
framework.

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
│   ├── dataset_50.jsonl           ← 50 validated (prompt, nextflow_code) pairs
│   ├── blueprints.py              ← programmatic definition of the 50 pairs
│   ├── emit_jsonl.py              ← regenerate dataset_50.jsonl from blueprints
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

## Headline result on the included example run

A single 50-prompt evaluation of the
[`izs-llm`](https://github.com/mgradyn/izs-llm) agent (Mistral-backed,
RAG over the framework catalog), recorded in
`results/example_run_mistral/`:

| Metric | Value |
|---|---|
| Prompts answered with code | 50 / 50 |
| Syntactically valid (`nextflow -preview`) | 50 / 50 |
| **Semantically valid (`nextflow -stub-run`)** | **43 / 50  (86 %)** |
| Exact step-set match vs ground truth | 37 / 50 |
| Hallucinated (non-existent) steps | 0 / 50 |
| Median per-prompt LLM latency | 11 s |
| Median per-prompt validation latency | 20 s |

The 7 failures cluster into 2 root causes (see
`results/example_run_mistral/report.md` for the full per-example detail):

- **5 / 7** — `missing_param: step_3TX_species__kmerfinder__db`.
  The LLM over-engineers simple mono-step prompts by injecting an
  upstream species-ID step that needs a database path the user did not
  provide.
- **2 / 7** — `silent_no_op`. The LLM picked a `genus_species` or
  `seq_type` filtered by a step's `when:` clause; the pipeline runs but
  schedules zero tasks.

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

# 3. (Optional) validate the ground truth itself (sanity check; ~20 min)
python harness/harness.py

# 4. Run your LLM against the 50 prompts
#    The LLM is expected to expose POST <URL>/chat with JSON
#    {session_id, message, generate_diagrams}
#    and return JSON {status, reply, nextflow_code, ...}.
export LLM_API_URL=http://localhost:8765
export BENCH_RUNS_DIR=./results/my_run
python eval/run_llm.py

# 5. Validate each generated .nf with nextflow -stub-run
python eval/validate_llm.py

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

---

## Citation

If you use this bench in a paper, please cite it as:

> *cohesive-llm-benchmark: an end-to-end Nextflow-aware benchmark for natural
> language → bioinformatics pipeline generation, version 1.0, 2026.*

A bib entry will be added once the paper is published.
