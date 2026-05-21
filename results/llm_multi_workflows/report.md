# LLM evaluation — detailed report

Total prompts: **5**  ·  generated code: **5**  ·  syntactically valid: **5**  ·  semantically valid: **2**

Step-set vs. ground truth:  exact match **3**  ·  extra steps **2**  ·  missing steps **0**  ·  hallucinated (non-existent) steps **0**

## Error category breakdown

| Category | Count | Meaning |
|----|----|----|
| `silent_no_op` | 2 | DAG empty — pipeline runs but produces no output |
| `file_not_found` | 2 | expected input file is not in the framework layout |
| `none` | 1 | no error — pipeline passes |

## Per-prompt outcome

| # | id | code? | syntax | semantic | procs | error category | first 80 chars of detail |
|---|----|-------|--------|----------|-------|----------------|------|
| 1 | `X01_multi_pangenome_panaroo_listeria` | ✅ | ✅ | ❌ | 0/1 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 2 | `X02_multi_clustering_vcf2mst` | ✅ | ✅ | ✅ | 2/2 | `none` |  |
| 3 | `X03_multi_clustering_grapetree_listeria` | ✅ | ✅ | ❌ | 0/2 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/202 |
| 4 | `X04_multi_clustering_reportree_alleles_listeria` | ✅ | ✅ | ❌ | 0/1 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 5 | `X05_multi_clustering_reportree_vcf` | ✅ | ✅ | ✅ | 1/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/202 |

## Step-set comparison vs ground truth

| # | id | LLM steps | GT steps | extra | missing | hallucinated |
|---|----|-----------|----------|-------|---------|--------------|
| 1 | `X01_multi_pangenome_panaroo_listeria` | prokka |  | prokka | · | · |
| 2 | `X02_multi_clustering_vcf2mst` |  |  | · | · | · |
| 3 | `X03_multi_clustering_grapetree_listeria` |  |  | · | · | · |
| 4 | `X04_multi_clustering_reportree_alleles_listeria` |  |  | · | · | · |
| 5 | `X05_multi_clustering_reportree_vcf` | mlst |  | mlst | · | · |

## Failure detail (one section per failing prompt)

### `X01_multi_pangenome_panaroo_listeria` — `silent_no_op`

**Prompt:** Pangenome analysis with panaroo across multiple Listeria monocytogenes assemblies, each previously annotated with Prokka.

**Steps (LLM):** `step_4AN_genes__prokka`
**Steps (GT):**  `(none)`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; getVCFs; param; optionalOrDefault; getReferenceUnkeyed } from '../functions/parameters.nf'
include { multi_pangenome__panaroo } from '../multi/multi_pangenome__panaroo'
workflow {
    multi_pangenome__panaroo(getInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getAssembly } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_prokka_and_panaroo {
    
    take:
        
        assemblies
        
    
    main:
        step_4AN_genes__prokka(assemblies.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

        prokka_out.map { it[1] }.collect().set { gffs }
        panaroo(gffs)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_prokka_and_panaroo(getAssembly())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `X03_multi_clustering_grapetree_listeria` — `file_not_found`

**Prompt:** cgMLST-based clustering of multiple Listeria monocytogenes samples with grapetree, after their allelic profiles were generated.

**Steps (LLM):** `(none)`
**Steps (GT):**  `(none)`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; getVCFs; param; optionalOrDefault; getReferenceUnkeyed } from '../functions/parameters.nf'
include { multi_clustering__grapetree } from '../multi/multi_clustering__grapetree'
workflow {
    multi_clustering__grapetree(getInput(), param('metadata'), param('geodata'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getInput; param } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_grapetree {
    
    take:
        
        input
        
        metadata
        
        geodata
        
    
    main:
        cgMLST = extract_cgMLST(input.collect()).cgMLST
        dists(cgMLST)
        nwk_nj = grapetree(cgMLST).nwk_nj
        augur(nwk_nj, metadata, geodata)
    
}

// --- ENTRYPOINT ---
workflow {
    GEO_RESOLUTION_COLUMNS = param('multi_clustering__reportree__summary_geo_column')
    SUMMARY_DATE_ALIASES = param('multi_clustering__reportree__summary_date_aliases')
    SAMPLE_COLUMN = param('multi_clustering__reportree__summary_sample_column')
    module_grapetree(getInput(), param('metadata'), param('geodata'))
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.MULTI.GRAPE.2.1/4TY_cgMLST/DS99999-DT260224_chewbbaca/result/*_results_crc32.?sv'
```

### `X04_multi_clustering_reportree_alleles_listeria` — `silent_no_op`

**Prompt:** ReporTree clustering on the allelic profiles of several Listeria samples.

**Steps (LLM):** `(none)`
**Steps (GT):**  `(none)`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; getVCFs; param; optionalOrDefault; getReferenceUnkeyed } from '../functions/parameters.nf'
include { multi_clustering__reportree } from '../multi/multi_clustering__reportree_alleles'
workflow {
    multi_clustering__reportree(getInput(),
                                param('metadata'),
                                param('geodata'),
                                optionalOrDefault('multi_clustering__reportree__nomenclature', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getInput; param } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

process extract_cgMLST {
    container 'ghcr.io/genpat-it/chewbbaca-w-chewie-schemas:2.8.5--16b816c96d'
    
    input:
    
    path(alleles)
    
    
    output:
    
    path '**'
    
    path 'cgMLST.tsv', emit: cgMLST
    
    path '*.sh', hidden: true
    
    
    script:
    """
for file in ${alleles} ; do awk 'FNR==1{print ""}1' \${file} | sed 's/,/\t/g' | sed -E "s/^[^SF][^ai]\\S+/\${file}/" | sed -E 's/DS[[:digit:]]+-DT[[:digit:]]+_([^_]+)_[[:graph:]]+/\\1/'; done | sort -ru  > results_alleles_all.tsv
chewie ExtractCgMLST -i results_alleles_all.tsv -o . > extract_cgMLST.log
    """
}

process dists {
    container 'quay.io/biocontainers/cgmlst-dists:0.4.0--hec16e2b_2'
    
    input:
    
    path(cgMLST)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
cgmlst-dists -c ${cgMLST} > cgMLST_dists_matrix.csv
    """
}

process grapetree {
    container 'quay.io/biocontainers/grapetree:2.1--pyh3252c3a_0'
    
    input:
    
    path(cgMLST)
    
    
    output:
    
    path '*'
    
    path '*.sh', hidden: true
    
    path("cgMLST_NJ.nwk"), emit: nwk_nj
    
    
    script:
    """
grapetree -p ${cgMLST} > cgMLST.nwk
grapetree --method RapidNJ -p ${cgMLST} > cgMLST_NJ.nwk
    """
}

process augur {
    container 'quay.io/biocontainers/augur:22.0.0--pyhdfd78af_0'
    
    input:
    
    path(nwk)
    
    path(metadata)
    
    path(geodata)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
cat ${metadata} | sed 's/${SAMPLE_COLUMN}/name/i' \
   | sed 's/${SUMMARY_DATE_ALIASES}/date/i' > augur_metadata.tsv
METADATA_LIST=$(head -n 1 augur_metadata.tsv | tr $'\t' ' ')
augur refine --tree ${nwk} --output-tree tree_tt.nwk --output-node-data refine.node.json --metadata augur_metadata.tsv
augur export v2 --tree tree_tt.nwk --node-data refine.node.json --output auspice.json \
  --color-by-metadata ${METADATA_LIST} \
  --geo-resolutions ${GEO_RESOLUTION_COLUMNS} \
  --metadata augur_metadata.tsv \
  --lat-longs ${geodata}
    """
}

// --- SUB WORKFLOWS ---

workflow multi_clustering__grapetree {
    
    take:
        
        input
        
        metadata
        
        geodata
        
    
    main:
        cgMLST = extract_cgMLST(input.collect()).cgMLST
        dists(cgMLST)
        nwk_nj = grapetree(cgMLST).nwk_nj
        augur(nwk_nj, metadata, geodata)
    
}

// --- ENTRYPOINT ---
workflow {
    GEO_RESOLUTION_COLUMNS = param('multi_clustering__reportree__summary_geo_column')
    SUMMARY_DATE_ALIASES = param('multi_clustering__reportree__summary_date_aliases')
    SAMPLE_COLUMN = param('multi_clustering__reportree__summary_sample_column')
    multi_clustering__grapetree(getInput(), param('metadata'), param('geodata'))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```
