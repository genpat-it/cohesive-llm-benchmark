# LLM evaluation — detailed report

Total prompts: **50**  ·  generated code: **50**  ·  syntactically valid: **50**  ·  semantically valid: **43**

Step-set vs. ground truth:  exact match **37**  ·  extra steps **10**  ·  missing steps **7**  ·  hallucinated (non-existent) steps **0**

## Error category breakdown

| Category | Count | Meaning |
|----|----|----|
| `none` | 37 | no error — pipeline passes |
| `ngsmanager_naming` | 6 | input file name does not match parseMetadataFromFileName regex |
| `missing_param` | 5 | step requires a param() that was not supplied |
| `silent_no_op` | 2 | DAG empty — pipeline runs but produces no output |

## Per-prompt outcome

| # | id | code? | syntax | semantic | procs | error category | first 80 chars of detail |
|---|----|-------|--------|----------|-------|----------------|------|
| 1 | `A01_mlst_listeria` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 2 | `A02_mlst_ecoli` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 3 | `A03_mlst_salmonella` | ✅ | ✅ | ❌ | 0/1 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 4 | `A04_cgmlst_listeria` | ✅ | ✅ | ❌ | 0/3 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 5 | `A05_cgmlst_ecoli` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 6 | `A06_cgmlst_salmonella` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 7 | `A07_flaa_campylobacter` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 8 | `A08_staramr_campylobacter` | ✅ | ✅ | ❌ | 0/1 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 9 | `B01_spades_listeria` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 10 | `B02_shovill_ecoli` | ✅ | ✅ | ❌ | 0/3 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 11 | `B03_unicycler_salmonella` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 12 | `B04_plasmidspades` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 13 | `B05_metaspades` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 14 | `C01_kmerfinder` | ✅ | ✅ | ✅ | 7/1 | `none` |  |
| 15 | `C02_mash` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 16 | `C03_kraken2` | ✅ | ✅ | ✅ | 2/2 | `none` |  |
| 17 | `D01_fastp_spades_lis` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 18 | `D02_fastp_shovill_eco` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 19 | `D03_trimmomatic_spades` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 20 | `D04_fastp_unicycler_sal` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 21 | `D05_fastp_spades_cam` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 22 | `E01_mlst_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 23 | `E02_cgmlst_lis_fastp_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 24 | `E03_cgmlst_sal_fastp_spades` | ✅ | ✅ | ✅ | 11/9 | `none` |  |
| 25 | `E04_cgmlst_eco_fastp_shovill` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 26 | `E05_flaa_cam` | ✅ | ✅ | ❌ | 0/7 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 27 | `E06_staramr_cam` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 28 | `E07_abricate_eco` | ✅ | ✅ | ❌ | 0/7 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 29 | `E08_prokka_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 30 | `E09_mlst_eco_trimmomatic` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 31 | `E10_mlst_sal_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 32 | `E11_cgmlst_lis_shovill` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 33 | `E12_mlst_cam` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 34 | `E13_abricate_sal` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 35 | `E14_prokka_eco` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 36 | `E15_cgmlst_lis_trimmomatic` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 37 | `F01_abricate_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 38 | `F02_prokka_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 39 | `F03_mash_lis` | ✅ | ✅ | ✅ | 1/1 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.LIS.A.1.1_R1.fastq.gz |
| 40 | `F04_kraken2_unknown` | ✅ | ✅ | ✅ | 2/2 | `none` |  |
| 41 | `G01_chopper_flye_lis` | ✅ | ✅ | ✅ | 4/4 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.LIS.B.1.1_R1.fastq.gz |
| 42 | `G02_chopper_flye_eco` | ✅ | ✅ | ✅ | 5/4 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.ECO.B.1.1_R1.fastq.gz |
| 43 | `H01_mlst_plus_cgmlst_lis` | ✅ | ✅ | ✅ | 10/10 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.LIS.C.1.1_R1.fastq.gz |
| 44 | `H02_mlst_plus_flaa_cam` | ✅ | ✅ | ❌ | 0/8 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 45 | `H03_prokka_plus_abricate_eco` | ✅ | ✅ | ✅ | 8/8 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.ECO.C.1.1_R1.fastq.gz |
| 46 | `H04_mlst_plus_abricate_sal` | ✅ | ✅ | ✅ | 8/8 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.SAL.C.1.1_R1.fastq.gz |
| 47 | `I01_kmerfinder_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 48 | `I02_mash_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 49 | `J01_mobsuite_plasmid` | ✅ | ✅ | ✅ | 4/1 | `none` |  |
| 50 | `J02_bbnorm_downsampling` | ✅ | ✅ | ✅ | 1/1 | `none` |  |

## Step-set comparison vs ground truth

| # | id | LLM steps | GT steps | extra | missing | hallucinated |
|---|----|-----------|----------|-------|---------|--------------|
| 1 | `A01_mlst_listeria` | mlst | mlst | · | · | · |
| 2 | `A02_mlst_ecoli` | mlst | mlst | · | · | · |
| 3 | `A03_mlst_salmonella` | kmerfinder,bowtie,abricate,prokka,staramr,mlst,flaA,chewbbaca | mlst | bowtie,kmerfinder,abricate,staramr,prokka,chewbbaca,flaA | · | · |
| 4 | `A04_cgmlst_listeria` |  | chewbbaca | · | chewbbaca | · |
| 5 | `A05_cgmlst_ecoli` | chewbbaca | chewbbaca | · | · | · |
| 6 | `A06_cgmlst_salmonella` | chewbbaca | chewbbaca | · | · | · |
| 7 | `A07_flaa_campylobacter` | flaA | flaA | · | · | · |
| 8 | `A08_staramr_campylobacter` | kmerfinder,staramr | staramr | kmerfinder | · | · |
| 9 | `B01_spades_listeria` | fastp,spades | spades | fastp | · | · |
| 10 | `B02_shovill_ecoli` | shovill | shovill | · | · | · |
| 11 | `B03_unicycler_salmonella` | fastp,unicycler | unicycler | fastp | · | · |
| 12 | `B04_plasmidspades` | plasmidspades | plasmidspades | · | · | · |
| 13 | `B05_metaspades` | metaspades | metaspades | · | · | · |
| 14 | `C01_kmerfinder` | fastp,spades,kmerfinder | kmerfinder | fastp,spades | · | · |
| 15 | `C02_mash` | mash | mash | · | · | · |
| 16 | `C03_kraken2` | kraken2 | kraken2 | · | · | · |
| 17 | `D01_fastp_spades_lis` | fastp,spades | fastp,spades | · | · | · |
| 18 | `D02_fastp_shovill_eco` | fastp,shovill | fastp,shovill | · | · | · |
| 19 | `D03_trimmomatic_spades` | trimmomatic,spades | trimmomatic,spades | · | · | · |
| 20 | `D04_fastp_unicycler_sal` | fastp,unicycler | fastp,unicycler | · | · | · |
| 21 | `D05_fastp_spades_cam` | fastp,spades | fastp,spades | · | · | · |
| 22 | `E01_mlst_lis` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 23 | `E02_cgmlst_lis_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 24 | `E03_cgmlst_sal_fastp_spades` | abricate,prokka,staramr,mlst,flaA,chewbbaca,spades | fastp,spades,chewbbaca | abricate,staramr,prokka,mlst,flaA | fastp | · |
| 25 | `E04_cgmlst_eco_fastp_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 26 | `E05_flaa_cam` | kmerfinder,bowtie,flaA | fastp,spades,flaA | bowtie,kmerfinder | fastp,spades | · |
| 27 | `E06_staramr_cam` | fastp,spades,staramr | fastp,spades,staramr | · | · | · |
| 28 | `E07_abricate_eco` |  | fastp,spades,abricate | · | fastp,spades,abricate | · |
| 29 | `E08_prokka_lis` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 30 | `E09_mlst_eco_trimmomatic` | trimmomatic,spades,mlst | trimmomatic,spades,mlst | · | · | · |
| 31 | `E10_mlst_sal_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 32 | `E11_cgmlst_lis_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 33 | `E12_mlst_cam` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 34 | `E13_abricate_sal` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 35 | `E14_prokka_eco` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 36 | `E15_cgmlst_lis_trimmomatic` | trimmomatic,spades,chewbbaca | trimmomatic,spades,chewbbaca | · | · | · |
| 37 | `F01_abricate_assembly` | abricate | abricate | · | · | · |
| 38 | `F02_prokka_assembly` | prokka | prokka | · | · | · |
| 39 | `F03_mash_lis` | mash | mash | · | · | · |
| 40 | `F04_kraken2_unknown` | kraken2 | kraken2 | · | · | · |
| 41 | `G01_chopper_flye_lis` | chopper,flye | chopper,flye | · | · | · |
| 42 | `G02_chopper_flye_eco` | chopper,spades | chopper,flye | spades | flye | · |
| 43 | `H01_mlst_plus_cgmlst_lis` | abricate,prokka,staramr,mlst,chewbbaca,spades | fastp,spades,mlst,chewbbaca | abricate,staramr,prokka | fastp | · |
| 44 | `H02_mlst_plus_flaa_cam` |  | fastp,spades,mlst,flaA | · | fastp,spades,mlst,flaA | · |
| 45 | `H03_prokka_plus_abricate_eco` | fastp,spades,prokka,abricate | fastp,spades,abricate,prokka | · | · | · |
| 46 | `H04_mlst_plus_abricate_sal` | fastp,spades,mlst,abricate | fastp,spades,abricate,mlst | · | · | · |
| 47 | `I01_kmerfinder_fastp_spades` | kmerfinder,fastp,spades | fastp,spades,kmerfinder | · | · | · |
| 48 | `I02_mash_fastp_shovill` | fastp,mash,shovill | fastp,shovill,mash | · | · | · |
| 49 | `J01_mobsuite_plasmid` | spades,mobsuite | mobsuite | spades | · | · |
| 50 | `J02_bbnorm_downsampling` | bbnorm | bbnorm | · | · | · |

## Failure detail (one section per failing prompt)

### `A03_mlst_salmonella` — `missing_param`

**Prompt:** MLST tipico (PubMLST) su un'assembly di Salmonella enterica.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    step_4TY_MLST__mlst(getInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        if (!params.skip_bestref_mapping) {
          trimmed.cross(assigned_species) { extractKey(it) }.multiMap {
            trimmed: it[0]
            species: it[1][1]
            referencePath: it[1][2]
          }.set { trimAndAndSpecies }
          step_2AS_mapping__bowtie(trimAndAndSpecies.trimmed, trimAndAndSpecies.referencePath)
        }

        step_4AN_AMR__abricate(assembly)

        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

        assembly.cross(assigned_species) { extractKey(it) }.multiMap {
          assembly: it[0]
          species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, '')
    
    emit:
        
        genus_species = assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_typing_bacteria(getTrimmedReads(true), getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `A04_cgmlst_listeria` — `missing_param`

**Prompt:** Profilo allelico cgMLST per Listeria monocytogenes a partire dall'assembly già pronta.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    step_4TY_cgMLST__chewbbaca(getInput(), param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { module_typing_bacteria } from '../modules/module_typing_bacteria'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    module_typing_bacteria(getTrimmedReads(true), getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `A08_staramr_campylobacter` — `missing_param`

**Prompt:** AMR profiling with staramr on a Campylobacter assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_4AN_AMR__staramr`
**Steps (GT):**  `step_4AN_AMR__staramr`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
workflow {
    step_4AN_AMR__staramr(getSingleInput(), param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    kmerfinder_out = step_3TX_species__kmerfinder(getSingleInput())
    step_4AN_AMR__staramr(kmerfinder_out.assigned_species.map { [ it[0], it[1], it[2][1] ] }, kmerfinder_out.assigned_species.map { it[1] })
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `B02_shovill_ecoli` — `silent_no_op`

**Prompt:** Quick bacterial genome assembly with Shovill from Illumina reads (Escherichia coli).

**Steps (LLM):** `step_2AS_denovo__shovill`
**Steps (GT):**  `step_2AS_denovo__shovill`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
workflow {
    step_2AS_denovo__shovill(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy
// ⚠️ WARNING: Pipeline generation failed strict DSL2 validation.
// The code above is potentially broken or incomplete and was output as a best-effort draft.

nextflow.enable.dsl=2

// --- IMPORTS ---

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_wgs_bacteria {
    
    take:
        
        trimmedReads
        
    
    main:
        step_2AS_denovo__shovill(trimmedReads)
    
    emit:
        
        step_2AS_denovo__shovill.out
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_wgs_bacteria(getSingleInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `E05_flaa_cam` — `silent_no_op`

**Prompt:** Pipeline per la tipizzazione flaA di Campylobacter da FASTQ paired Illumina.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4TY_flaA__flaA`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_flaA__flaA(assembled, param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
// ⚠️ WARNING: Pipeline generation failed strict DSL2 validation.
// The code above is potentially broken or incomplete and was output as a best-effort draft.

nextflow.enable.dsl=2

// --- IMPORTS ---

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        if (!params.skip_bestref_mapping) {
          trimmed.cross(assigned_species) { extractKey(it) }.multiMap {
            trimmed: it[0]
            species: it[1][1]
            referencePath: it[1][2]
          }.set { trimAndAndSpecies }
          step_2AS_mapping__bowtie(trimAndAndSpecies.trimmed, trimAndAndSpecies.referencePath)
        }

        assembly.cross(assigned_species) { extractKey(it) }.multiMap {
          assembly: it[0]
          species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
    
    emit:
        
        genus_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_typing_bacteria(getTrimmedReads(true), getAssembly())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `E07_abricate_eco` — `missing_param`

**Prompt:** Resistance gene detection with ABRicate on Escherichia coli from Illumina paired FASTQ.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { module_typing_bacteria } from '../modules/module_typing_bacteria'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    module_typing_bacteria(getTrimmedReads(true), getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `H02_mlst_plus_flaa_cam` — `missing_param`

**Prompt:** Comprehensive Campylobacter typing from paired Illumina FASTQ: MLST + flaA.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4TY_flaA__flaA(assembled, param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { module_typing_bacteria } from '../modules/module_typing_bacteria'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    module_typing_bacteria(getTrimmedReads(true), getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```
