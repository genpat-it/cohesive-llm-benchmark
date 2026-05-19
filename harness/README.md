# harness/

The Nextflow validation engine that powers both the ground-truth
generation and the LLM evaluation.

`harness.py` exports:

- `class Example` — dataclass that wraps a `(prompt, nextflow_code, params, inputs, expected_processes)` tuple.
- `class Harness` — knows how to materialise dummy inputs and call
  `nextflow -stub-run`.
- `run_examples(examples)` — runs a list of `Example`s and returns a list
  of `Verdict`s.

## CLI

```bash
# Validate every example in the dataset
python harness/harness.py

# Just a few
python harness/harness.py --only=A01_mlst_listeria,E02_cgmlst_lis_fastp_spades

# First N
python harness/harness.py --first=10
```

`NGSMANAGER_DIR` must point at your cohesive-ngsmanager checkout.

## How an `Example` becomes a Nextflow run

1. The `.nf` is written to `<framework>/pipelines/_dataset_<id>.nf` so
   that its `include {...} from '../functions/parameters.nf'` resolves.
2. Dummy inputs are materialised under
   `/tmp/dataset_scratch/_shared_inputdir/<anno>/<cmp>/<acc>/<DS>-<DT>_<met>/result/`
   based on `Example.inputs` — entries are spec strings like
   `fastq_paired:2026.LIS.1.1.1`, `assembly:2026.CAMP.1.1.1`,
   `trimmed:2026.LIS.1.1.1`.
3. A `params.json` is written with `cmp`/`riscd` from the example plus
   our `inputdir`, `outdir`, `assets_dir` overrides.
4. `nextflow run pipelines/_dataset_<id>.nf -stub-run -params-file …
   -work-dir /tmp/.../work` is invoked with a 120 s timeout.
5. The stdout/stderr is captured, the placeholder rows are counted, and
   a `Verdict(passed, reason, log_tail)` is returned.
6. The temporary `.nf`, the work dir and the framework's own `work/`
   are deleted to keep disk usage bounded across runs.

## Supported input layout kinds

| Spec prefix      | Materialised |
|---|---|
| `fastq_paired:<cmp>` | `.../<base>_R1.fastq.gz` + `_R2.fastq.gz` (0 byte gzip) |
| `fastq_single:<cmp>` | `.../<base>_R1.fastq.gz` |
| `assembly:<cmp>`     | `.../<base>_external.fasta` (≤30 byte) |
| `trimmed:<cmp>`      | `.../<base>_fastp_R{1,2}.fastq.gz` |

## Adding a new layout kind

Edit `_materialise` in `harness.py`, add a `<kind>_layout` helper that
writes the dummy files, and use the new spec prefix in your blueprints.

## What it does **not** do

- It does not pull Docker images. Processes without a `stub:` directive
  will fail at the script step; the bench tolerates that because we
  only need the DAG to *schedule*, not to *complete*.
- It does not check biological correctness — see `METHODOLOGY.md`.
