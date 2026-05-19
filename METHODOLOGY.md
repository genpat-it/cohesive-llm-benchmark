# Methodology

This document describes what the bench actually measures, and — equally
important — what it does *not* measure.

## The three validation levels

For every generated `.nf` we run, in order:

| Level | Command | What it proves about the LLM | Failure modes it can detect |
|---|---|---|---|
| 1 — syntax       | `nextflow run … -preview`  | The text is valid DSL2 | parse errors, unknown identifiers |
| 2 — DAG build    | `nextflow run … -stub-run` (subset) | The workflow's channel graph is wire-correct | arity mismatch on `take:`, wrong `.emit` name, undeclared variable, missing `param('…')` |
| 3 — DAG schedule | `nextflow run … -stub-run` (full)   | The pipeline schedules at least one process per declared step | `when:` clauses filtered everything (silent no-op), step incompatible with the chosen species/seq_type |

Levels 1 and 2 are entirely about the LLM's output.
Level 3 partially depends on the **input fixture** (what params, what dummy
files, what species we chose). Treat its verdicts accordingly.

## Who is at fault when a check fails?

This bench's job is to surface **objective** evidence of incorrectness, not
to assign blame; the failure category we attach to each row is meant to
help you decide. The guide we use ourselves:

| Category | Almost always the LLM's fault | Almost always a fixture issue | Mixed |
|---|---|---|---|
| `arity_error`        | ✅ | | |
| `channel_emit`       | ✅ | | |
| `compile_error`      | ✅ | | |
| `unknown_step`       | ✅ | | |
| `ngsmanager_naming`  | ✅ | | |
| `silent_no_op`       | | | ✅ |
| `missing_param`      | | ✅ | |
| `file_not_found`     | | ✅ | |

- **`missing_param`** typically means the LLM added a step that requires a
  database/path the user did not configure. The LLM's choice may still be
  reasonable for the prompt — the bench cannot tell.
- **`silent_no_op`** means a `when:` clause filtered everything. If the LLM
  chose a species the step actually supports and our fixture is sane,
  this is an LLM bug. If we passed an incompatible `seq_type`, it is on us.

## What this bench is NOT

- **Not a biological correctness check.** The bench validates that the
  pipeline *can run end-to-end*, not that the resulting allelic profile
  or AMR call is biologically meaningful.
- **Not a benchmark of LLM quality on prose.** The conversational reply
  (`reply` field) is captured but not graded.
- **Not a unit test of `cohesive-ngsmanager`.** Failures rooted in the
  framework itself (e.g. a buggy step) will surface here, but they are
  out of scope.

## Why we use `-stub-run` and not `-preview` alone

`-preview` only parses the DSL2 and resolves includes. It does *not*
construct the workflow's channel graph, so it does **not** catch arity
mismatches on `take:` or wrong emit names — exactly the errors we have
observed real LLMs make most often.

`-stub-run` builds the full DAG and schedules processes, but does not
execute their `script:` blocks (when a `stub:` directive exists) or runs
them as best-effort (when it does not). This gives us a reliable signal
about the workflow's *structure* without needing real bioinformatics data
or container pulls for every step.

The trade-off: processes without `stub:` blocks may fail at runtime even
on syntactically perfect pipelines, leading to noisy logs. We count
**scheduled** processes (placeholder rows in the live progress display),
not **completed** ones, to ignore that noise.

## Dummy input materialisation

The harness materialises dummy inputs under a shared `inputdir/` tree
following `cohesive-ngsmanager`'s `getResult()` convention:

```
<inputdir>/<anno>/<cmp>/<acc>/<DS>-<DT>_<met>/result/<files>
```

Where `<anno>` is the first 4 chars of `cmp`. We support four layouts:

- `fastq_paired:<cmp>` → `<...>/0SQ_rawreads/.../result/<base>_R{1,2}.fastq.gz`
- `fastq_single:<cmp>` → `<...>/0SQ_rawreads/.../result/<base>_R1.fastq.gz`
- `assembly:<cmp>`     → `<...>/2AS_import/.../result/<base>_external.fasta`
- `trimmed:<cmp>`      → `<...>/1PP_trimming/.../result/<base>_fastp_R{1,2}.fastq.gz`

Files are 0-byte gzipped reads or ≤30-byte fastas — just enough for
`parseMetadataFromFileName` to accept them and for the DAG to wire up.

Filenames must match the strict regex
`^(DS\d+)\D(DT\d+)_(\d{4})(\.[^.]+\.\d+\.\d+\.\d+)(_[^_]+)?.*$`,
so the `cmp` field of an example must follow `YYYY.<TAG>.<n>.<n>.<n>` —
e.g. `2026.LIS.1.1.1`. Get this wrong and you'll see
`ngsmanager_naming` errors that have nothing to do with the LLM.

## The expected_processes count

Each blueprint declares an `expected_processes` count: the minimum number
of distinct step processes that must appear as placeholders in the live
display for the pipeline to count as a `pass`. The count is derived from
the step files themselves (one entry per `process` keyword), with two
manual adjustments:

- `step_2AS_denovo__shovill` declares 4 processes (`shovill`, `shovill_se`,
  `quast`, `checkm`) but `checkm` is gated behind `params.skip_checkm`
  which defaults to `true`, so we count 3.
- The framework's `step_2AS_mapping__*` steps include heavyweight
  branches that are skipped under stub-run; counts reflect the active
  ones.

If you add a new step to the blueprint, update `PROCS` in
`dataset/blueprints.py` accordingly.

## Two ways to interpret a failure rate

Given **N** failures out of 50:

1. **Strict.** Count every failure regardless of root cause. This is what
   the headline number in `report.md` reports.
2. **LLM-only.** Drop failures whose `error_category` is in
   `{missing_param, file_not_found}` (typical fixture issues). This is
   the number to put in the discussion section of a paper, *after*
   reviewing each one to confirm the LLM's choice was reasonable.

The TSV / CSV / JSONL outputs give you everything you need to compute
either.

## Limitations and known issues

- **Single-LLM evaluation only.** The eval points at one
  `LLM_API_URL` at a time. Compare runs by setting different
  `BENCH_RUNS_DIR` values.
- **No multi-sample workflows yet.** `multi_*` workflows that take
  allele profiles or VCFs as input are not represented in the
  current blueprint set.
- **Validation is structural.** A pipeline that compiles and schedules
  the right number of processes can still produce biologically wrong
  output. Validating that needs real reads and references.
- **The bench assumes the framework's API is stable** at the commit you
  pinned via `NGSMANAGER_DIR`. If the framework changes a `take:`
  signature, the blueprints' calls may need updates.
