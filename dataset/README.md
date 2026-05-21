# dataset/

Ground-truth corpora for training and evaluating an offline LLM that
generates Nextflow pipelines compatible with the `cohesive-ngsmanager`
framework.

| File | Size | What it is |
|---|---:|---|
| `dataset_50.jsonl`                  | 50   | curated single-turn subset, kept for stable historical reference |
| `dataset_200.jsonl`                 | 200  | full single-turn corpus (50 curated + 150 combinatorial extension) |
| `dataset_205.jsonl`                 | 205  | 200 + 5 multi-sample workflow blueprints (X*: panaroo, vcf2mst, grapetree, reportree-alleles, reportree-vcf) |
| `dataset_modifications.jsonl`       | 17 conversations (34 turns) | curated multi-turn subset |
| `dataset_modifications_full.jsonl`  | 159 conversations (330 turns) | full multi-turn corpus (17 curated + 142 combinatorial extension) |

Every example in every corpus was end-to-end validated with
`nextflow -stub-run` against the real framework. For each: the DAG must
build and the expected number of distinct step processes must appear
as placeholders.

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

### Curated 50 (single-turn)

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

### Extended 150 (single-turn additional)

| Prefix | Pattern | Count |
|----|----|---|
| `K` | combinatorial 3-step chains (trim × asm × typing × species) | 60 |
| `L` | 4-step parallel downstream (two typing/AMR) | 20 |
| `M` | 5-step parallel downstream (three typing/AMR/annotation) | 10 |
| `N` / `NA` | cross-species canonical chains | 23 |
| `O` | mono-step assembly variants | 10 |
| `P` | long-read (chopper + flye + typing) | 10 |
| `Q` | parallel branches with species ID | 10 |
| `R` | mono species-id + db params | 8 |
| `S` | mono trimming (Illumina / Ion / Nanopore) | 7 |
| **Total** | | **150** |  ⇒ 50 + 150 = **200** in `dataset_200.jsonl` |

### Multi-sample workflows (5 blueprints, category `X*`)

These exercise the `multi/*` workflows of cohesive-ngsmanager, which take
arrays of per-sample inputs (GFFs, VCFs, allele profiles).

| ID | Multi-workflow | What it tests |
|----|----|---|
| `X01_multi_pangenome_panaroo_listeria` | `multi_pangenome__panaroo` | pangenome across 3 prokka-annotated Listeria assemblies |
| `X02_multi_clustering_vcf2mst` | `multi_clustering__vcf2mst` | minimum spanning tree from 3 snippy VCFs |
| `X03_multi_clustering_grapetree_listeria` | `multi_clustering__grapetree` | cgMLST clustering of 3 Listeria allele profiles |
| `X04_multi_clustering_reportree_alleles_listeria` | `multi_clustering__reportree` (alleles variant) | ReporTree clustering across 3 Listeria allele profiles |
| `X05_multi_clustering_reportree_vcf` | `multi_clustering__reportree` (vcf variant) | ReporTree clustering across 3 VCFs |

These are only in `dataset_205.jsonl` (not in `dataset_50.jsonl` or
`dataset_200.jsonl`).

### Multi-turn modifications (159 conversations, 330 turns)

| Kind | 17 curated | 142 extended | Total |
|---|---:|---:|---:|
| `add`             | 5 | ~38 | ~43 |
| `replace`         | 5 | ~40 | ~45 |
| `drop`            | 3 | ~30 | ~33 |
| `switch_species`  | 4 | ~28 | ~32 |
| 3-turn conversations | — | 6 | 6 |
| **Total**         | **17** | **142** | **159** |

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
# Assumes you have cloned this repo and exported NGSMANAGER_DIR.
# See ../INSTALL.md for the full setup.
cd <path-to>/cohesive-llm-benchmark
export NGSMANAGER_DIR=/path/to/cohesive-ngsmanager
python harness/harness.py                                  # all 50 examples (~25 min)
python harness/harness.py --only=E02_cgmlst_lis_fastp_spades  # one
python harness/harness.py --first=10                       # first ten
```

Output PASS/FAIL per example plus a final summary. Logs land in
`<scratch>/<eid>/nextflow.log` where `<scratch>` defaults to
`<system-tempdir>/cohesive_llm_bench/` (override with
`BENCH_SCRATCH_DIR`). They are preserved across runs for postmortem.

## Files in this directory

| File | Purpose |
|---|---|
| `dataset_50.jsonl`              | single-turn dataset (one JSON object per line) |
| `dataset_modifications.jsonl`   | multi-turn modification conversations (17, two turns each) |
| `README.md`                     | this file |
| `blueprints.py`                 | the 50 single-turn example specs and the `.nf` generator helpers |
| `modifications.py`              | the 17 multi-turn modification conversations |
| `emit_jsonl.py`                 | regenerates `dataset_50.jsonl` from the blueprints |
| `emit_modifications.py`         | regenerates `dataset_modifications.jsonl` from the conversations |
| `validate_modifications.py`     | runs `nextflow -stub-run` on every turn |
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
