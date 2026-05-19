# Installation

Minimum environment to run the bench from scratch.

## 1. Prerequisites

- **Python ≥ 3.11** (the harness uses `subprocess.run(capture_output=...)`
  and modern type hints).
- **Nextflow ≥ 22** on `$PATH` (`-stub-run` is supported from 22.04).
- **Docker** is *optional*. Without Docker, processes without a
  `stub:` directive will fail when their containers are pulled —
  the bench tolerates this (we count scheduling, not completion).
- A checkout of
  [`cohesive-ngsmanager`](https://github.com/genpat-it/cohesive-ngsmanager)
  somewhere on disk.

## 2. Python deps

```bash
pip install -r requirements.txt
```

## 3. Point the harness at the framework

```bash
export NGSMANAGER_DIR=/path/to/cohesive-ngsmanager
```

Sanity check:

```bash
python harness/harness.py --only=A01_mlst_listeria
```

Expected output (~15 s):

```
[  1/1] A01_mlst_listeria               PASS  - 1 distinct processes in DAG
```

## 4. Pick (or build) an LLM endpoint

The eval script speaks to any HTTP server that exposes:

```
POST {LLM_API_URL}/chat
Content-Type: application/json

{ "session_id": "...", "message": "<user prompt>", "generate_diagrams": false }
```

and returns:

```json
{
  "status":         "APPROVED" | "CHATTING" | "failed",
  "reply":          "...",
  "nextflow_code":  "nextflow.enable.dsl=2\n..."
}
```

The included reference run used
[`izs-llm`](https://github.com/mgradyn/izs-llm) — a FastAPI + LangGraph
agent that delegates to Mistral via `langchain-mistralai`.

### How to bring up `izs-llm` locally

```bash
git clone https://github.com/mgradyn/izs-llm
cd izs-llm

# Provide YOUR OWN keys -- do NOT commit them.
cat > .env <<EOF
MISTRAL_API_KEY=<paste your Mistral key here>
NGSMANAGER_DIR=/path/to/cohesive-ngsmanager
EOF

pip install -r requirements.txt
set -a && source .env && set +a
uvicorn app.api:app --host 127.0.0.1 --port 8765
```

The first start will download Qwen embeddings (~600 MB) and a FAISS
index; subsequent starts take <30 s.

Sanity check:

```bash
curl http://127.0.0.1:8765/health
# {"status":"online","vector_store":"loaded"}
```

### Using a different LLM

Any HTTP service that matches the `/chat` contract works. If your LLM has
a different output format, edit `eval/run_llm.py:ask_llm()` accordingly —
it is a ~50-line function.

## 5. Run the eval

```bash
export LLM_API_URL=http://127.0.0.1:8765
export BENCH_RUNS_DIR=$(pwd)/results/my_run

python eval/run_llm.py            # ~10 min for 50 prompts
python eval/validate_llm.py       # ~20 min for 50 prompts
python eval/emit_report.py        # <5 s
```

Outputs land in `$BENCH_RUNS_DIR`:

```
$BENCH_RUNS_DIR/
├── runs.jsonl       ← raw LLM responses
├── verdicts.jsonl   ← per-prompt validation verdict (24 fields)
├── report.md        ← human-readable report
├── report.tsv       ← grep / awk-friendly
└── report.csv       ← Excel / LibreOffice
```

## Disk-space note

The harness writes a per-example work dir under `/tmp/dataset_scratch/`.
For 50 examples and most pipelines this stays under 200 MB. If your `/tmp`
is small (some shared servers cap it at 1–2 GB) and you re-run the bench
multiple times without cleaning, expect `ENOSPC`. Clean with:

```bash
rm -rf /tmp/dataset_scratch
```

## What if my Python is older than 3.11?

The harness requires Python ≥ 3.7 for `subprocess.run(capture_output=...)`
and ≥ 3.10 for `X | Y` union types in annotations. On RHEL 8 the system
`python3` is 3.6 — use `/usr/bin/python3.11` or a venv.

## What if the Mistral API key is invalid?

You will see `401 Unauthorized` in the LLM server logs. Generate a fresh
key at https://console.mistral.ai/api-keys/ and put it in the LLM
server's `.env`. **Never commit the key to a repo.**
