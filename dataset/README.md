# dataset_50.jsonl

50 validated (prompt, nextflow_code) pairs for training an offline LLM that
generates Nextflow pipelines compatible with the `cohesive-ngsmanager`
framework.

Every example was end-to-end validated with `nextflow -stub-run` against the
real framework. For each: the DAG must build and the expected number of
distinct step processes must appear as placeholders.

## Schema (one JSON object per line)

```json
{
  "id":            "E02_cgmlst_lis_fastp_spades",
  "category":      "3step",
  "prompt":        "cgMLST allelic profile for Listeria monocytogenes ...",
  "nextflow_code": "nextflow.enable.dsl=2\n...",
  "params":        { "cmp": "2026.LIS.6.1.1",
                     "riscd": "260224-99999-0SQ_rawreads-import",
                     "seq_type": "illumina_paired",
                     "genus_species": "listeria_monocytogenes" },
  "notes":         "",
  "validation":    { "method": "nextflow -stub-run",
                     "expected_processes": 9 }
}
```

## Categories

| Prefix | Pattern | Count |
|----|----|---|
| `A` | mono-step typing/AMR/annotation starting from an assembly | 8 |
| `B` | mono-step de-novo assembly from FASTQ | 5 |
| `C` | mono-step species ID / taxonomic classification from FASTQ | 3 |
| `D` | 2-step: trim + assemble | 5 |
| `E` | 3-step: trim + assemble + typing/AMR/annotation | 15 |
| `F` | mono-step variants (alternate species/source) | 4 |
| `G` | long-read Nanopore (chopper + flye) | 2 |
| `H` | 4-step (two downstream steps in parallel) | 4 |
| `I` | parallel branches: species ID alongside trim + assembly | 2 |
| `J` | misc (plasmid analysis, read normalisation) | 2 |
| **Total** | | **50** |

## Conventions enforced in every example

1. **Workflow chaining via the right emit name**
   - `.trimmed` for fastp / chopper / trimmomatic
   - `.assembled` for spades / unicycler / plasmidspades / metaspades
   - `.assembly` for shovill and flye (their actual emit names)
2. **Per-step `take:` arity is respected** — multi-take workflows are
   called with separate arguments. Never fused via `.map`.
3. **The bottom `workflow { }` block of each step file is the ground truth**.
   Every example's invocation mirrors it.
4. **Species in params only where the step filters on species**:
   - chewbbaca: `listeria_monocytogenes`, `escherichia_coli`,
     `salmonella_enterica`
   - flaA / staramr: `campylobacter*`
5. **`cmp` follows the framework's naming convention** —
   `YYYY.<TAG>.<n>.<n>.<n>` matching the `parseMetadataFromFileName`
   regex `(\d{4})(\.[^.]+\.\d+\.\d+\.\d+)`.
6. **Required step-specific params are present** (e.g.\ kmerfinder's `__db`,
   kraken2's `__db`). They use placeholder paths suitable for stub-run.

## How the validation works

For each example the harness:

1. Writes the .nf into `cohesive-ngsmanager/pipelines/_dataset_<id>.nf`.
2. Materialises dummy FASTQ / assembly files under `inputdir/` following the
   genpat layout `inputdir/<anno>/<cmp>/<acc>/<DS>-<DT>_<met>/result/<file>`.
3. Writes a `params.json`.
4. Runs `nextflow -stub-run -params-file params.json -work-dir <tmp>`.
5. Greps the live progress display for distinct process placeholders.
6. PASS if `distinct_processes >= expected_processes`.
7. Cleans up the temporary .nf and inputs at the end.

## Reproducing the validation

```bash
cd /home/IZSNT/a.deruvo/cohesive-llm
python3.11 dataset_harness.py            # all 50 examples (~25 min)
python3.11 dataset_harness.py --only=E02_cgmlst_lis_fastp_spades   # one
python3.11 dataset_harness.py --first=10 # first ten
```

Output PASS/FAIL per example plus a final summary. Logs land in
`/tmp/dataset_scratch/<eid>/nextflow.log` (preserved across runs for
postmortem).

## Files in this directory

| File | Purpose |
|---|---|
| `dataset_50.jsonl`             | the dataset (one JSON object per line) |
| `dataset_50.README.md`         | this file |
| `dataset_blueprints.py`        | the 50 example specs and the .nf generator helpers |
| `dataset_harness.py`           | validation runner with input materialisation |
| `emit_jsonl.py`                | regenerates `dataset_50.jsonl` from the blueprints |
| `build_inventory.py`           | extracts step metadata from cohesive-ngsmanager |
| `_inventory.json`              | step-by-step inventory (regenerable) |

## Known limitations

- Validation is **structural** (DAG construction + process scheduling), not
  **functional** (no real reads, no real schemas). Examples are guaranteed
  to start a valid Nextflow execution; they make no claim about biological
  meaningfulness with real input.
- Examples currently cover bacterial WGS workflows (Illumina paired, Ion,
  Nanopore). SARS-CoV-2 / Westnile lineage and multi-sample clustering
  workflows are not included — those need additional inputs (reference
  genomes, VCF, allele profiles) that complicate the dummy-input setup.

## Adding more examples

Edit `dataset_blueprints.py`, append to `build_all()`, run
`python3.11 dataset_harness.py --only=<new_id>` to validate, then
`python3.11 emit_jsonl.py` to regenerate the JSONL.
