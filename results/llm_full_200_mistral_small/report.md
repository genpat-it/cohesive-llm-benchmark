# LLM evaluation — detailed report

Total prompts: **200**  ·  generated code: **200**  ·  syntactically valid: **192**  ·  semantically valid: **139**

Step-set vs. ground truth:  exact match **130**  ·  extra steps **62**  ·  missing steps **33**  ·  hallucinated (non-existent) steps **0**

## Error category breakdown

| Category | Count | Meaning |
|----|----|----|
| `none` | 124 | no error — pipeline passes |
| `file_not_found` | 37 | expected input file is not in the framework layout |
| `missing_param` | 19 | step requires a param() that was not supplied |
| `arity_error` | 13 | workflow called with wrong number of arguments |
| `silent_no_op` | 4 | DAG empty — pipeline runs but produces no output |
| `ngsmanager_naming` | 2 | input file name does not match parseMetadataFromFileName regex |
| `partial_dag` | 1 | only some of the expected processes appeared in the DAG |

## Per-prompt outcome

| # | id | code? | syntax | semantic | procs | error category | first 80 chars of detail |
|---|----|-------|--------|----------|-------|----------------|------|
| 1 | `A01_mlst_listeria` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 2 | `A02_mlst_ecoli` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 3 | `A03_mlst_salmonella` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 4 | `A04_cgmlst_listeria` | ✅ | ✅ | ✅ | 3/3 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 5 | `A05_cgmlst_ecoli` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 6 | `A06_cgmlst_salmonella` | ✅ | ✅ | ✅ | 3/3 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 7 | `A07_flaa_campylobacter` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 8 | `A08_staramr_campylobacter` | ✅ | ✅ | ❌ | 0/1 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 9 | `B01_spades_listeria` | ✅ | ✅ | ✅ | 5/3 | `none` |  |
| 10 | `B02_shovill_ecoli` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 11 | `B03_unicycler_salmonella` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 12 | `B04_plasmidspades` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 13 | `B05_metaspades` | ✅ | ✅ | ✅ | 4/3 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 14 | `C01_kmerfinder` | ✅ | ✅ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 15 | `C02_mash` | ✅ | ✅ | ❌ | 0/1 | `missing_param` | ERROR ~ missing required param: step_3TX_class__kraken2__db |
| 16 | `C03_kraken2` | ✅ | ✅ | ✅ | 3/2 | `arity_error` | ERROR ~ Workflow `step_3TX_class__kraken2` declares 1 input channels but 0 were  |
| 17 | `D01_fastp_spades_lis` | ✅ | ✅ | ✅ | 6/6 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 18 | `D02_fastp_shovill_eco` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 19 | `D03_trimmomatic_spades` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 20 | `D04_fastp_unicycler_sal` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 21 | `D05_fastp_spades_cam` | ✅ | ✅ | ✅ | 7/6 | `none` |  |
| 22 | `E01_mlst_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 23 | `E02_cgmlst_lis_fastp_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 24 | `E03_cgmlst_sal_fastp_spades` | ✅ | ✅ | ❌ | 0/9 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 25 | `E04_cgmlst_eco_fastp_shovill` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 26 | `E05_flaa_cam` | ✅ | ✅ | ❌ | 0/7 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 27 | `E06_staramr_cam` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 28 | `E07_abricate_eco` | ✅ | ✅ | ❌ | 0/7 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 29 | `E08_prokka_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 30 | `E09_mlst_eco_trimmomatic` | ✅ | ❌ | ❌ | 3/7 | `arity_error` | ERROR ~ Workflow `step_1PP_trimming__trimmomatic` declares 1 input channels but  |
| 31 | `E10_mlst_sal_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 32 | `E11_cgmlst_lis_shovill` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 33 | `E12_mlst_cam` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 34 | `E13_abricate_sal` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 35 | `E14_prokka_eco` | ✅ | ❌ | ❌ | 3/7 | `arity_error` | ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were |
| 36 | `E15_cgmlst_lis_trimmomatic` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 37 | `F01_abricate_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 38 | `F02_prokka_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 39 | `F03_mash_lis` | ✅ | ✅ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 40 | `F04_kraken2_unknown` | ✅ | ✅ | ✅ | 3/2 | `arity_error` | ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were |
| 41 | `G01_chopper_flye_lis` | ✅ | ✅ | ✅ | 4/4 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.LIS.B.1.1_R1.fastq.gz |
| 42 | `G02_chopper_flye_eco` | ✅ | ✅ | ✅ | 4/4 | `none` |  |
| 43 | `H01_mlst_plus_cgmlst_lis` | ✅ | ✅ | ❌ | 0/10 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 44 | `H02_mlst_plus_flaa_cam` | ✅ | ✅ | ❌ | 0/8 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 45 | `H03_prokka_plus_abricate_eco` | ✅ | ✅ | ✅ | 8/8 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.ECO.C.1.1_R1.fastq.gz |
| 46 | `H04_mlst_plus_abricate_sal` | ✅ | ✅ | ❌ | 0/8 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 47 | `I01_kmerfinder_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 48 | `I02_mash_fastp_shovill` | ✅ | ✅ | ❌ | 7/7 | `none` |  |
| 49 | `J01_mobsuite_plasmid` | ✅ | ✅ | ✅ | 4/1 | `none` |  |
| 50 | `J02_bbnorm_downsampling` | ✅ | ✅ | ✅ | 4/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 51 | `K01_mlst_lis_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 52 | `K02_mlst_eco_fastp_spades` | ✅ | ✅ | ❌ | 3/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 53 | `K03_mlst_sal_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 54 | `K04_mlst_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 55 | `K05_chewbbaca_lis_fastp_spades` | ✅ | ❌ | ❌ | 3/9 | `arity_error` | ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were |
| 56 | `K06_chewbbaca_eco_fastp_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 57 | `K07_chewbbaca_sal_fastp_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 58 | `K08_abricate_lis_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 59 | `K09_abricate_eco_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 60 | `K10_abricate_sal_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 61 | `K11_abricate_cam_fastp_spades` | ✅ | ✅ | ❌ | 6/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 62 | `K12_prokka_lis_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 63 | `K13_prokka_eco_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 64 | `K14_prokka_sal_fastp_spades` | ✅ | ❌ | ❌ | 3/7 | `arity_error` | ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were |
| 65 | `K15_prokka_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 66 | `K16_flaA_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 67 | `K17_staramr_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 68 | `K18_mlst_lis_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 69 | `K19_mlst_eco_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 70 | `K20_mlst_sal_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 71 | `K21_mlst_cam_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 72 | `K22_chewbbaca_lis_fastp_shovill` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 73 | `K23_chewbbaca_eco_fastp_shovill` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 74 | `K24_chewbbaca_sal_fastp_shovill` | ✅ | ❌ | ❌ | 0/9 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 75 | `K25_abricate_lis_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 76 | `K26_abricate_eco_fastp_shovill` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 77 | `K27_abricate_sal_fastp_shovill` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 78 | `K28_abricate_cam_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 79 | `K29_prokka_lis_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 80 | `K30_prokka_eco_fastp_shovill` | ✅ | ✅ | ❌ | 0/7 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 81 | `K31_prokka_sal_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 82 | `K32_prokka_cam_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 83 | `K33_flaA_cam_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 84 | `K34_staramr_cam_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 85 | `K35_mlst_lis_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 86 | `K36_mlst_eco_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 87 | `K37_mlst_sal_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 88 | `K38_mlst_cam_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 89 | `K39_chewbbaca_lis_fastp_unicycler` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 90 | `K40_chewbbaca_eco_fastp_unicycler` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 91 | `K41_chewbbaca_sal_fastp_unicycler` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 92 | `K42_abricate_lis_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 93 | `K43_abricate_eco_fastp_unicycler` | ✅ | ✅ | ❌ | 3/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 94 | `K44_abricate_sal_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 95 | `K45_abricate_cam_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 96 | `K46_prokka_lis_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 97 | `K47_prokka_eco_fastp_unicycler` | ✅ | ❌ | ❌ | 3/7 | `arity_error` | ERROR ~ Workflow `wf_prokka_e_coli_annotation:step_4AN_genes__prokka` declares 1 |
| 98 | `K48_prokka_sal_fastp_unicycler` | ✅ | ❌ | ❌ | 3/7 | `arity_error` | ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were |
| 99 | `K49_prokka_cam_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 100 | `K50_flaA_cam_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 101 | `K51_staramr_cam_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 102 | `K52_mlst_lis_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 103 | `K53_mlst_eco_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 104 | `K54_mlst_sal_trimmomatic_spades` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 105 | `K55_mlst_cam_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 106 | `K56_chewbbaca_lis_trimmomatic_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 107 | `K57_chewbbaca_eco_trimmomatic_spades` | ✅ | ✅ | ❌ | 3/9 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 108 | `K58_chewbbaca_sal_trimmomatic_spades` | ✅ | ✅ | ❌ | 0/9 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 109 | `K59_abricate_lis_trimmomatic_spades` | ✅ | ✅ | ❌ | 6/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 110 | `K60_abricate_eco_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 111 | `L01_mlst_chewbbaca_lis` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 112 | `L02_mlst_chewbbaca_eco` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 113 | `L03_mlst_chewbbaca_sal` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 114 | `L04_mlst_abricate_lis` | ✅ | ✅ | ❌ | 4/8 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 115 | `L05_mlst_abricate_eco` | ✅ | ✅ | ❌ | 3/8 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 116 | `L06_chewbbaca_abricate_lis` | ✅ | ✅ | ❌ | 6/10 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 117 | `L07_chewbbaca_prokka_lis` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 118 | `L08_chewbbaca_prokka_sal` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 119 | `L09_mlst_prokka_eco` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 120 | `L10_mlst_prokka_sal` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 121 | `L11_abricate_prokka_lis` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 122 | `L12_abricate_prokka_sal` | ✅ | ✅ | ❌ | 6/8 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 123 | `L13_mlst_flaA_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 124 | `L14_mlst_staramr_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 125 | `L15_flaA_staramr_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 126 | `L16_flaA_abricate_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 127 | `L17_staramr_abricate_cam` | ✅ | ✅ | ❌ | 6/8 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 128 | `L18_staramr_prokka_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 129 | `L19_flaA_prokka_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 130 | `L20_mlst_prokka_lis` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 131 | `M01_mlst+chewbbaca+abricate_lis` | ✅ | ✅ | ✅ | 12/11 | `none` |  |
| 132 | `M02_mlst+chewbbaca+prokka_sal` | ✅ | ✅ | ❌ | 7/11 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 133 | `M03_mlst+abricate+prokka_eco` | ✅ | ✅ | ❌ | 0/9 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 134 | `M04_mlst+abricate+prokka_lis` | ✅ | ✅ | ❌ | 6/9 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 135 | `M05_mlst+flaA+staramr_cam` | ✅ | ✅ | ✅ | 10/9 | `none` |  |
| 136 | `M06_mlst+flaA+abricate_cam` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 137 | `M07_flaA+staramr+prokka_cam` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 138 | `M08_mlst+staramr+prokka_cam` | ✅ | ✅ | ❌ | 6/9 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 139 | `M09_chewbbaca+abricate+prokka_lis` | ✅ | ✅ | ❌ | 0/11 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 140 | `M10_chewbbaca+abricate+prokka_eco` | ✅ | ✅ | ✅ | 11/11 | `none` |  |
| 141 | `N01_canonical_mlst_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 142 | `N02_canonical_mlst_eco` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 143 | `N03_canonical_mlst_sal` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 144 | `N04_canonical_mlst_cam` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 145 | `N05_canonical_cgmlst_lis` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 146 | `N06_canonical_cgmlst_eco` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 147 | `N07_canonical_cgmlst_sal` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 148 | `NA01_mlst_cam_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 149 | `NA02_mlst_sal_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 150 | `NA03_abricate_lis_assembly` | ✅ | ✅ | ❌ | 0/1 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 151 | `NA04_abricate_sal_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 152 | `NA05_abricate_cam_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 153 | `NA06_prokka_sal_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 154 | `NA07_prokka_cam_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 155 | `NA08_prokka_eco_assembly` | ✅ | ✅ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 156 | `O01_spades_lis` | ✅ | ✅ | ❌ | 0/3 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 157 | `O02_spades_sal` | ✅ | ✅ | ✅ | 5/3 | `none` |  |
| 158 | `O03_spades_cam` | ✅ | ✅ | ✅ | 3/3 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 159 | `O04_shovill_lis` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 160 | `O05_shovill_sal` | ✅ | ✅ | ✅ | 3/3 | `arity_error` | ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were |
| 161 | `O06_shovill_cam` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 162 | `O07_unicycler_lis` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 163 | `O08_unicycler_eco` | ✅ | ✅ | ✅ | 3/3 | `arity_error` | ERROR ~ Workflow `wf_preprocess_e_coli:step_1PP_hostdepl__bowtie` declares 1 inp |
| 164 | `O09_unicycler_cam` | ✅ | ✅ | ❌ | 0/3 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 165 | `O10_plasmidspades_eco` | ✅ | ✅ | ✅ | 5/3 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 166 | `P01_chopper_flye_mlst_lis` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 167 | `P02_chopper_flye_mlst_sal` | ✅ | ✅ | ❌ | 2/5 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 168 | `P03_chopper_flye_mlst_eco` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 169 | `P04_chopper_flye_mlst_cam` | ✅ | ❌ | ❌ | 3/5 | `arity_error` | ERROR ~ Workflow `step_1PP_trimming__chopper` declares 1 input channels but 0 we |
| 170 | `P05_chopper_flye_abricate_lis` | ✅ | ✅ | ✅ | 7/5 | `none` |  |
| 171 | `P06_chopper_flye_abricate_eco` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 172 | `P07_chopper_flye_abricate_sal` | ✅ | ✅ | ❌ | 0/5 | `missing_param` | ERROR ~ missing required param: host |
| 173 | `P08_chopper_flye_prokka_lis` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 174 | `P09_chopper_flye_chewbbaca_lis` | ✅ | ✅ | ❌ | 5/7 | `partial_dag` | Only 5/7 expected processes appeared in the DAG |
| 175 | `P10_chopper_flye_chewbbaca_sal` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 176 | `Q01_kmerfinder_fastp_spades_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 177 | `Q02_kmerfinder_fastp_spades_eco` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 178 | `Q03_kmerfinder_fastp_spades_sal` | ✅ | ✅ | ❌ | 4/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 179 | `Q04_kmerfinder_fastp_shovill_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 180 | `Q05_kmerfinder_fastp_shovill_eco` | ✅ | ✅ | ❌ | 0/7 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 181 | `Q06_kmerfinder_fastp_shovill_sal` | ✅ | ✅ | ❌ | 0/7 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 182 | `Q07_mash_fastp_spades_lis` | ✅ | ✅ | ❌ | 7/7 | `none` |  |
| 183 | `Q08_mash_fastp_spades_eco` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 184 | `Q09_mash_fastp_spades_sal` | ✅ | ✅ | ❌ | 7/7 | `none` |  |
| 185 | `Q10_mash_fastp_shovill_lis` | ✅ | ✅ | ❌ | 8/7 | `none` |  |
| 186 | `R01_kmerfinder_cam` | ✅ | ✅ | ✅ | 7/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 187 | `R02_kmerfinder_sal` | ✅ | ✅ | ✅ | 9/1 | `none` |  |
| 188 | `R03_mash_sal` | ✅ | ✅ | ❌ | 0/1 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 189 | `R04_mash_eco` | ✅ | ✅ | ✅ | 4/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 190 | `R05_kraken2_lis` | ✅ | ✅ | ❌ | 0/2 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 191 | `R06_kraken2_eco` | ✅ | ✅ | ✅ | 3/2 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 192 | `R07_kraken2_sal` | ✅ | ✅ | ❌ | 0/2 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 193 | `R08_kraken2_cam` | ✅ | ✅ | ❌ | 0/2 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 194 | `S01_fastp_lis` | ✅ | ✅ | ❌ | 0/3 | `missing_param` | ERROR ~ missing required param: step_3TX_class__kraken2__db |
| 195 | `S02_fastp_sal` | ✅ | ✅ | ✅ | 3/3 | `arity_error` | ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were |
| 196 | `S03_trimmomatic_eco` | ✅ | ✅ | ✅ | 3/3 | `arity_error` | ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were |
| 197 | `S04_trimmomatic_cam` | ✅ | ✅ | ❌ | 0/3 | `missing_param` | ERROR ~ missing required param: step_3TX_class__kraken2__db |
| 198 | `S05_chopper_lis` | ✅ | ✅ | ✅ | 2/2 | `none` |  |
| 199 | `S06_chopper_sal` | ✅ | ✅ | ❌ | 0/2 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_sma |
| 200 | `S07_chopper_cam` | ✅ | ✅ | ✅ | 2/2 | `none` |  |

## Step-set comparison vs ground truth

| # | id | LLM steps | GT steps | extra | missing | hallucinated |
|---|----|-----------|----------|-------|---------|--------------|
| 1 | `A01_mlst_listeria` | mlst | mlst | · | · | · |
| 2 | `A02_mlst_ecoli` | mlst | mlst | · | · | · |
| 3 | `A03_mlst_salmonella` | mlst | mlst | · | · | · |
| 4 | `A04_cgmlst_listeria` | chewbbaca | chewbbaca | · | · | · |
| 5 | `A05_cgmlst_ecoli` | chewbbaca | chewbbaca | · | · | · |
| 6 | `A06_cgmlst_salmonella` | chewbbaca | chewbbaca | · | · | · |
| 7 | `A07_flaa_campylobacter` | flaA | flaA | · | · | · |
| 8 | `A08_staramr_campylobacter` | kmerfinder | staramr | kmerfinder | staramr | · |
| 9 | `B01_spades_listeria` | bowtie,spades | spades | bowtie | · | · |
| 10 | `B02_shovill_ecoli` | shovill | shovill | · | · | · |
| 11 | `B03_unicycler_salmonella` | fastp,unicycler | unicycler | fastp | · | · |
| 12 | `B04_plasmidspades` | fastp,plasmidspades | plasmidspades | fastp | · | · |
| 13 | `B05_metaspades` | fastq,fastp,metaspades | metaspades | fastq,fastp | · | · |
| 14 | `C01_kmerfinder` |  | kmerfinder | · | kmerfinder | · |
| 15 | `C02_mash` | kraken2 | mash | kraken2 | mash | · |
| 16 | `C03_kraken2` | fastq,kraken2 | kraken2 | fastq | · | · |
| 17 | `D01_fastp_spades_lis` | fastp,spades | fastp,spades | · | · | · |
| 18 | `D02_fastp_shovill_eco` | fastp,shovill | fastp,shovill | · | · | · |
| 19 | `D03_trimmomatic_spades` | trimmomatic,spades | trimmomatic,spades | · | · | · |
| 20 | `D04_fastp_unicycler_sal` | fastp,unicycler | fastp,unicycler | · | · | · |
| 21 | `D05_fastp_spades_cam` | fastp,spades | fastp,spades | · | · | · |
| 22 | `E01_mlst_lis` | fastp,shovill,mlst | fastp,spades,mlst | shovill | spades | · |
| 23 | `E02_cgmlst_lis_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 24 | `E03_cgmlst_sal_fastp_spades` | fastq,fastp,shovill,kmerfinder,chewbbaca | fastp,spades,chewbbaca | fastq,shovill,kmerfinder | spades | · |
| 25 | `E04_cgmlst_eco_fastp_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 26 | `E05_flaa_cam` | fastp,kmerfinder,spades,flaA,shovill | fastp,spades,flaA | shovill,kmerfinder | · | · |
| 27 | `E06_staramr_cam` | fastp,spades,staramr | fastp,spades,staramr | · | · | · |
| 28 | `E07_abricate_eco` | kmerfinder,shovill,abricate,fastp | fastp,spades,abricate | shovill,kmerfinder | spades | · |
| 29 | `E08_prokka_lis` | fastp,shovill,prokka | fastp,spades,prokka | shovill | spades | · |
| 30 | `E09_mlst_eco_trimmomatic` | fastq,trimmomatic,spades,mlst | trimmomatic,spades,mlst | fastq | · | · |
| 31 | `E10_mlst_sal_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 32 | `E11_cgmlst_lis_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 33 | `E12_mlst_cam` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 34 | `E13_abricate_sal` | fastp,shovill,abricate | fastp,spades,abricate | shovill | spades | · |
| 35 | `E14_prokka_eco` | fastq,fastp,shovill,prokka | fastp,spades,prokka | fastq,shovill | spades | · |
| 36 | `E15_cgmlst_lis_trimmomatic` | trimmomatic,spades,chewbbaca | trimmomatic,spades,chewbbaca | · | · | · |
| 37 | `F01_abricate_assembly` | abricate | abricate | · | · | · |
| 38 | `F02_prokka_assembly` | prokka | prokka | · | · | · |
| 39 | `F03_mash_lis` |  | mash | · | mash | · |
| 40 | `F04_kraken2_unknown` | fastq,fastp,kraken2 | kraken2 | fastq,fastp | · | · |
| 41 | `G01_chopper_flye_lis` | chopper,flye | chopper,flye | · | · | · |
| 42 | `G02_chopper_flye_eco` | chopper,flye | chopper,flye | · | · | · |
| 43 | `H01_mlst_plus_cgmlst_lis` | fastp,shovill,kmerfinder,mlst,chewbbaca | fastp,spades,mlst,chewbbaca | shovill,kmerfinder | spades | · |
| 44 | `H02_mlst_plus_flaa_cam` | fastp,spades,kmerfinder,mlst,flaA | fastp,spades,mlst,flaA | kmerfinder | · | · |
| 45 | `H03_prokka_plus_abricate_eco` | fastp,spades,prokka,abricate | fastp,spades,abricate,prokka | · | · | · |
| 46 | `H04_mlst_plus_abricate_sal` | kmerfinder,bowtie,abricate,prokka,staramr,mlst,flaA,chewbbaca,fastp,shovill | fastp,spades,abricate,mlst | shovill,bowtie,kmerfinder,staramr,prokka,chewbbaca,flaA | spades | · |
| 47 | `I01_kmerfinder_fastp_spades` | kmerfinder,fastp,spades | fastp,spades,kmerfinder | · | · | · |
| 48 | `I02_mash_fastp_shovill` | fastp,mash,shovill | fastp,shovill,mash | · | · | · |
| 49 | `J01_mobsuite_plasmid` | fastp,mobsuite | mobsuite | fastp | · | · |
| 50 | `J02_bbnorm_downsampling` | fastp,bbnorm | bbnorm | fastp | · | · |
| 51 | `K01_mlst_lis_fastp_spades` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 52 | `K02_mlst_eco_fastp_spades` | spades,mlst,fastp | fastp,spades,mlst | · | · | · |
| 53 | `K03_mlst_sal_fastp_spades` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 54 | `K04_mlst_cam_fastp_spades` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 55 | `K05_chewbbaca_lis_fastp_spades` | fastq,fastp,spades,chewbbaca | fastp,spades,chewbbaca | fastq | · | · |
| 56 | `K06_chewbbaca_eco_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 57 | `K07_chewbbaca_sal_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 58 | `K08_abricate_lis_fastp_spades` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 59 | `K09_abricate_eco_fastp_spades` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 60 | `K10_abricate_sal_fastp_spades` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 61 | `K11_abricate_cam_fastp_spades` | spades,fastp | fastp,spades,abricate | · | abricate | · |
| 62 | `K12_prokka_lis_fastp_spades` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 63 | `K13_prokka_eco_fastp_spades` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 64 | `K14_prokka_sal_fastp_spades` | fastq,fastp,spades,prokka | fastp,spades,prokka | fastq | · | · |
| 65 | `K15_prokka_cam_fastp_spades` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 66 | `K16_flaA_cam_fastp_spades` | fastp,spades,flaA | fastp,spades,flaA | · | · | · |
| 67 | `K17_staramr_cam_fastp_spades` | fastp,spades,staramr | fastp,spades,staramr | · | · | · |
| 68 | `K18_mlst_lis_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 69 | `K19_mlst_eco_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 70 | `K20_mlst_sal_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 71 | `K21_mlst_cam_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 72 | `K22_chewbbaca_lis_fastp_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 73 | `K23_chewbbaca_eco_fastp_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 74 | `K24_chewbbaca_sal_fastp_shovill` | fastp,shovill,kmerfinder,chewbbaca | fastp,shovill,chewbbaca | kmerfinder | · | · |
| 75 | `K25_abricate_lis_fastp_shovill` | fastp,shovill,abricate | fastp,shovill,abricate | · | · | · |
| 76 | `K26_abricate_eco_fastp_shovill` | fastp,shovill,abricate | fastp,shovill,abricate | · | · | · |
| 77 | `K27_abricate_sal_fastp_shovill` | shovill,abricate,filtering,fastp | fastp,shovill,abricate | filtering | · | · |
| 78 | `K28_abricate_cam_fastp_shovill` | fastp,shovill,abricate | fastp,shovill,abricate | · | · | · |
| 79 | `K29_prokka_lis_fastp_shovill` | shovill,prokka,fastp | fastp,shovill,prokka | · | · | · |
| 80 | `K30_prokka_eco_fastp_shovill` | fastp,shovill,prokka | fastp,shovill,prokka | · | · | · |
| 81 | `K31_prokka_sal_fastp_shovill` | fastp,shovill,prokka | fastp,shovill,prokka | · | · | · |
| 82 | `K32_prokka_cam_fastp_shovill` | fastp,shovill,prokka | fastp,shovill,prokka | · | · | · |
| 83 | `K33_flaA_cam_fastp_shovill` | fastp,shovill,flaA | fastp,shovill,flaA | · | · | · |
| 84 | `K34_staramr_cam_fastp_shovill` | fastp,shovill,staramr | fastp,shovill,staramr | · | · | · |
| 85 | `K35_mlst_lis_fastp_unicycler` | fastp,unicycler,mlst | fastp,unicycler,mlst | · | · | · |
| 86 | `K36_mlst_eco_fastp_unicycler` | fastp,unicycler,mlst | fastp,unicycler,mlst | · | · | · |
| 87 | `K37_mlst_sal_fastp_unicycler` | fastp,unicycler,mlst | fastp,unicycler,mlst | · | · | · |
| 88 | `K38_mlst_cam_fastp_unicycler` | fastp,unicycler,mlst | fastp,unicycler,mlst | · | · | · |
| 89 | `K39_chewbbaca_lis_fastp_unicycler` | fastp,unicycler,chewbbaca | fastp,unicycler,chewbbaca | · | · | · |
| 90 | `K40_chewbbaca_eco_fastp_unicycler` | fastp,unicycler,chewbbaca | fastp,unicycler,chewbbaca | · | · | · |
| 91 | `K41_chewbbaca_sal_fastp_unicycler` | fastp,unicycler,chewbbaca | fastp,unicycler,chewbbaca | · | · | · |
| 92 | `K42_abricate_lis_fastp_unicycler` | fastp,unicycler,abricate | fastp,unicycler,abricate | · | · | · |
| 93 | `K43_abricate_eco_fastp_unicycler` | unicycler,abricate,fastp | fastp,unicycler,abricate | · | · | · |
| 94 | `K44_abricate_sal_fastp_unicycler` | fastp,unicycler,abricate | fastp,unicycler,abricate | · | · | · |
| 95 | `K45_abricate_cam_fastp_unicycler` | fastp,unicycler,abricate | fastp,unicycler,abricate | · | · | · |
| 96 | `K46_prokka_lis_fastp_unicycler` | fastp,unicycler,prokka | fastp,unicycler,prokka | · | · | · |
| 97 | `K47_prokka_eco_fastp_unicycler` | prokka,fastp | fastp,unicycler,prokka | · | unicycler | · |
| 98 | `K48_prokka_sal_fastp_unicycler` | fastq,fastp,unicycler,prokka | fastp,unicycler,prokka | fastq | · | · |
| 99 | `K49_prokka_cam_fastp_unicycler` | fastp,unicycler,prokka | fastp,unicycler,prokka | · | · | · |
| 100 | `K50_flaA_cam_fastp_unicycler` | fastp,unicycler,flaA | fastp,unicycler,flaA | · | · | · |
| 101 | `K51_staramr_cam_fastp_unicycler` | fastp,unicycler,staramr | fastp,unicycler,staramr | · | · | · |
| 102 | `K52_mlst_lis_trimmomatic_spades` | trimmomatic,spades,mlst | trimmomatic,spades,mlst | · | · | · |
| 103 | `K53_mlst_eco_trimmomatic_spades` | spades,mlst,trimmomatic | trimmomatic,spades,mlst | · | · | · |
| 104 | `K54_mlst_sal_trimmomatic_spades` |  | trimmomatic,spades,mlst | · | trimmomatic,spades,mlst | · |
| 105 | `K55_mlst_cam_trimmomatic_spades` | trimmomatic,spades,mlst | trimmomatic,spades,mlst | · | · | · |
| 106 | `K56_chewbbaca_lis_trimmomatic_spades` | trimmomatic,spades,chewbbaca | trimmomatic,spades,chewbbaca | · | · | · |
| 107 | `K57_chewbbaca_eco_trimmomatic_spades` | spades,chewbbaca,fastp | trimmomatic,spades,chewbbaca | fastp | trimmomatic | · |
| 108 | `K58_chewbbaca_sal_trimmomatic_spades` | fastp,spades,kmerfinder,chewbbaca | trimmomatic,spades,chewbbaca | fastp,kmerfinder | trimmomatic | · |
| 109 | `K59_abricate_lis_trimmomatic_spades` | fastp,spades,abricate | trimmomatic,spades,abricate | fastp | trimmomatic | · |
| 110 | `K60_abricate_eco_trimmomatic_spades` | trimmomatic,spades,abricate | trimmomatic,spades,abricate | · | · | · |
| 111 | `L01_mlst_chewbbaca_lis` | fastp,spades,mlst,chewbbaca | fastp,spades,mlst,chewbbaca | · | · | · |
| 112 | `L02_mlst_chewbbaca_eco` | fastp,spades,mlst,chewbbaca | fastp,spades,mlst,chewbbaca | · | · | · |
| 113 | `L03_mlst_chewbbaca_sal` | fastp,spades,mlst,chewbbaca | fastp,spades,mlst,chewbbaca | · | · | · |
| 114 | `L04_mlst_abricate_lis` | spades,mlst,abricate,fastp | fastp,spades,abricate,mlst | · | · | · |
| 115 | `L05_mlst_abricate_eco` | spades,mlst,abricate,fastp | fastp,spades,abricate,mlst | · | · | · |
| 116 | `L06_chewbbaca_abricate_lis` | fastp,spades,abricate | fastp,spades,abricate,chewbbaca | · | chewbbaca | · |
| 117 | `L07_chewbbaca_prokka_lis` | spades,chewbbaca,prokka,fastp | fastp,spades,prokka,chewbbaca | · | · | · |
| 118 | `L08_chewbbaca_prokka_sal` | fastp,spades,chewbbaca,prokka | fastp,spades,prokka,chewbbaca | · | · | · |
| 119 | `L09_mlst_prokka_eco` | fastp,spades,mlst,prokka | fastp,spades,prokka,mlst | · | · | · |
| 120 | `L10_mlst_prokka_sal` | spades,mlst,prokka,fastp | fastp,spades,prokka,mlst | · | · | · |
| 121 | `L11_abricate_prokka_lis` | spades,prokka,abricate,fastp | fastp,spades,abricate,prokka | · | · | · |
| 122 | `L12_abricate_prokka_sal` | spades,abricate,prokka,fastp | fastp,spades,abricate,prokka | · | · | · |
| 123 | `L13_mlst_flaA_cam` | fastp,spades,mlst,flaA | fastp,spades,mlst,flaA | · | · | · |
| 124 | `L14_mlst_staramr_cam` | fastp,spades,mlst,staramr | fastp,spades,staramr,mlst | · | · | · |
| 125 | `L15_flaA_staramr_cam` | fastp,spades,flaA,staramr | fastp,spades,staramr,flaA | · | · | · |
| 126 | `L16_flaA_abricate_cam` | fastp,spades,flaA,abricate | fastp,spades,abricate,flaA | · | · | · |
| 127 | `L17_staramr_abricate_cam` | spades,fastp | fastp,spades,abricate,staramr | · | abricate,staramr | · |
| 128 | `L18_staramr_prokka_cam` | spades,prokka,staramr,fastp | fastp,spades,staramr,prokka | · | · | · |
| 129 | `L19_flaA_prokka_cam` | fastp,spades,flaA,prokka | fastp,spades,prokka,flaA | · | · | · |
| 130 | `L20_mlst_prokka_lis` | spades,mlst,prokka,fastp | fastp,spades,prokka,mlst | · | · | · |
| 131 | `M01_mlst+chewbbaca+abricate_lis` | fastp,spades,mlst,chewbbaca,abricate,prokka | fastp,spades,abricate,mlst,chewbbaca | prokka | · | · |
| 132 | `M02_mlst+chewbbaca+prokka_sal` | fastp,shovill,mlst,chewbbaca,prokka | fastp,spades,prokka,mlst,chewbbaca | shovill | spades | · |
| 133 | `M03_mlst+abricate+prokka_eco` | kmerfinder,bowtie,abricate,prokka,staramr,mlst,flaA,chewbbaca | fastp,spades,abricate,prokka,mlst | bowtie,kmerfinder,staramr,chewbbaca,flaA | fastp,spades | · |
| 134 | `M04_mlst+abricate+prokka_lis` | spades,mlst,abricate,prokka,fastp | fastp,spades,abricate,prokka,mlst | · | · | · |
| 135 | `M05_mlst+flaA+staramr_cam` | fastp,spades,mlst,flaA,staramr,prokka | fastp,spades,staramr,mlst,flaA | prokka | · | · |
| 136 | `M06_mlst+flaA+abricate_cam` | fastp,shovill,mlst,flaA,abricate | fastp,spades,abricate,mlst,flaA | shovill | spades | · |
| 137 | `M07_flaA+staramr+prokka_cam` | spades,flaA,staramr,prokka,fastp | fastp,spades,staramr,prokka,flaA | · | · | · |
| 138 | `M08_mlst+staramr+prokka_cam` | spades,mlst,staramr,prokka,fastp | fastp,spades,staramr,prokka,mlst | · | · | · |
| 139 | `M09_chewbbaca+abricate+prokka_lis` | fastp,shovill,kmerfinder,chewbbaca,abricate,prokka | fastp,spades,abricate,prokka,chewbbaca | shovill,kmerfinder | spades | · |
| 140 | `M10_chewbbaca+abricate+prokka_eco` | fastp,spades,chewbbaca,abricate,prokka | fastp,spades,abricate,prokka,chewbbaca | · | · | · |
| 141 | `N01_canonical_mlst_lis` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 142 | `N02_canonical_mlst_eco` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 143 | `N03_canonical_mlst_sal` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 144 | `N04_canonical_mlst_cam` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 145 | `N05_canonical_cgmlst_lis` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 146 | `N06_canonical_cgmlst_eco` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 147 | `N07_canonical_cgmlst_sal` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 148 | `NA01_mlst_cam_assembly` | mlst | mlst | · | · | · |
| 149 | `NA02_mlst_sal_assembly` | mlst | mlst | · | · | · |
| 150 | `NA03_abricate_lis_assembly` | kmerfinder,bowtie,abricate,prokka,staramr,mlst,flaA,chewbbaca | abricate | bowtie,kmerfinder,staramr,prokka,mlst,chewbbaca,flaA | · | · |
| 151 | `NA04_abricate_sal_assembly` | abricate | abricate | · | · | · |
| 152 | `NA05_abricate_cam_assembly` | abricate | abricate | · | · | · |
| 153 | `NA06_prokka_sal_assembly` | prokka | prokka | · | · | · |
| 154 | `NA07_prokka_cam_assembly` | prokka | prokka | · | · | · |
| 155 | `NA08_prokka_eco_assembly` | prokka | prokka | · | · | · |
| 156 | `O01_spades_lis` | bowtie,spades | spades | bowtie | · | · |
| 157 | `O02_spades_sal` | bowtie,spades | spades | bowtie | · | · |
| 158 | `O03_spades_cam` | fastp,bowtie,spades | spades | bowtie,fastp | · | · |
| 159 | `O04_shovill_lis` | fastp,shovill | shovill | fastp | · | · |
| 160 | `O05_shovill_sal` | bowtie,shovill,fastq,fastp | shovill | fastq,bowtie,fastp | · | · |
| 161 | `O06_shovill_cam` | shovill | shovill | · | · | · |
| 162 | `O07_unicycler_lis` | fastp,unicycler | unicycler | fastp | · | · |
| 163 | `O08_unicycler_eco` | fastp,bowtie,unicycler | unicycler | bowtie,fastp | · | · |
| 164 | `O09_unicycler_cam` | fastp,unicycler | unicycler | fastp | · | · |
| 165 | `O10_plasmidspades_eco` | fastp,bowtie,spades | plasmidspades | bowtie,fastp,spades | plasmidspades | · |
| 166 | `P01_chopper_flye_mlst_lis` | chopper,flye,mlst | chopper,flye,mlst | · | · | · |
| 167 | `P02_chopper_flye_mlst_sal` | minimap2,chopper,flye,mlst | chopper,flye,mlst | minimap2 | · | · |
| 168 | `P03_chopper_flye_mlst_eco` | chopper,flye,mlst | chopper,flye,mlst | · | · | · |
| 169 | `P04_chopper_flye_mlst_cam` | fastq,chopper,flye,prokka | chopper,flye,mlst | fastq,prokka | mlst | · |
| 170 | `P05_chopper_flye_abricate_lis` | chopper,flye,abricate | chopper,flye,abricate | · | · | · |
| 171 | `P06_chopper_flye_abricate_eco` | chopper,flye,staramr | chopper,flye,abricate | staramr | abricate | · |
| 172 | `P07_chopper_flye_abricate_sal` | chopper,flye,abricate | chopper,flye,abricate | · | · | · |
| 173 | `P08_chopper_flye_prokka_lis` | chopper,flye,prokka | chopper,flye,prokka | · | · | · |
| 174 | `P09_chopper_flye_chewbbaca_lis` | chopper,flye,mlst | chopper,flye,chewbbaca | mlst | chewbbaca | · |
| 175 | `P10_chopper_flye_chewbbaca_sal` | chopper,flye,chewbbaca | chopper,flye,chewbbaca | · | · | · |
| 176 | `Q01_kmerfinder_fastp_spades_lis` | fastp,spades,kmerfinder | fastp,spades,kmerfinder | · | · | · |
| 177 | `Q02_kmerfinder_fastp_spades_eco` | kmerfinder,fastp,spades | fastp,spades,kmerfinder | · | · | · |
| 178 | `Q03_kmerfinder_fastp_spades_sal` | fastq,fastp,spades,kmerfinder | fastp,spades,kmerfinder | fastq | · | · |
| 179 | `Q04_kmerfinder_fastp_shovill_lis` | fastp,shovill,kmerfinder | fastp,shovill,kmerfinder | · | · | · |
| 180 | `Q05_kmerfinder_fastp_shovill_eco` | kmerfinder,fastp,shovill | fastp,shovill,kmerfinder | · | · | · |
| 181 | `Q06_kmerfinder_fastp_shovill_sal` | fastp,shovill,kmerfinder | fastp,shovill,kmerfinder | · | · | · |
| 182 | `Q07_mash_fastp_spades_lis` | fastp,mash,spades | fastp,spades,mash | · | · | · |
| 183 | `Q08_mash_fastp_spades_eco` | fastp,mash,spades | fastp,spades,mash | · | · | · |
| 184 | `Q09_mash_fastp_spades_sal` | mash,fastp,spades | fastp,spades,mash | · | · | · |
| 185 | `Q10_mash_fastp_shovill_lis` | shovill,mash,fastp | fastp,shovill,mash | · | · | · |
| 186 | `R01_kmerfinder_cam` | fastp,spades,kmerfinder | kmerfinder | fastp,spades | · | · |
| 187 | `R02_kmerfinder_sal` | fastp,spades,kmerfinder,prokka,abricate | kmerfinder | fastp,spades,abricate,prokka | · | · |
| 188 | `R03_mash_sal` | kmerfinder | mash | kmerfinder | mash | · |
| 189 | `R04_mash_eco` | fastp,mash,spades | mash | fastp,spades | · | · |
| 190 | `R05_kraken2_lis` | fastq,kraken2,kmerfinder | kraken2 | fastq,kmerfinder | · | · |
| 191 | `R06_kraken2_eco` | kraken2,bowtie,spades | kraken2 | bowtie,spades | · | · |
| 192 | `R07_kraken2_sal` | kmerfinder,bowtie,abricate,prokka,staramr,mlst,flaA,chewbbaca | kraken2 | bowtie,kmerfinder,abricate,staramr,prokka,mlst,chewbbaca,flaA | kraken2 | · |
| 193 | `R08_kraken2_cam` | fastq,fastp,kraken2 | kraken2 | fastq,fastp | · | · |
| 194 | `S01_fastp_lis` | fastp,kraken2,shovill,prokka,abricate,mlst | fastp | shovill,kraken2,abricate,prokka,mlst | · | · |
| 195 | `S02_fastp_sal` | fastq,fastp | fastp | fastq | · | · |
| 196 | `S03_trimmomatic_eco` | fastq,fastp | trimmomatic | fastq,fastp | trimmomatic | · |
| 197 | `S04_trimmomatic_cam` | fastp,kraken2 | trimmomatic | fastp,kraken2 | trimmomatic | · |
| 198 | `S05_chopper_lis` | chopper | chopper | · | · | · |
| 199 | `S06_chopper_sal` |  | chopper | · | chopper | · |
| 200 | `S07_chopper_cam` | chopper | chopper | · | · | · |

## Failure detail (one section per failing prompt)

### `A08_staramr_campylobacter` — `missing_param`

**Prompt:** AMR profiling with staramr on a Campylobacter assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def genusSpecies = 'campylobacter_jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_amr_campylobacter {
    
    take:
        
        assembly
        
    
    main:
        kmerfinder_out = step_3TX_species__kmerfinder(assembly)
        staramr(assembly, kmerfinder_out.assigned_species)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_amr_campylobacter(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `C01_kmerfinder` — `file_not_found`

**Prompt:** Identify the species of an unknown bacterial isolate from Illumina paired FASTQ using KmerFinder.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_3TX_species__kmerfinder`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'
workflow {
    step_3TX_species__kmerfinder(getInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def stepCode = '0SQ_rawreads'

def methodCode = 'fastq'

def stepSpeciesCode = '3TX_species'

def methodSpeciesCode = 'kmerfinder'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_species_identification {
    
    take:
        
        raw_reads
        
    
    main:
        raw_reads | step_0SQ_rawreads__fastq | step_3TX_species__kmerfinder
    
}

// --- ENTRYPOINT ---
workflow {
    // Instantiate input channel from raw Illumina paired FASTQ reads
    raw_reads = getSingleInput()

    // Execute species identification workflow
    wf_species_identification(raw_reads)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.UNK.1.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `C02_mash` — `missing_param`

**Prompt:** Run Mash sketch-based species identification on paired-end Illumina reads.

**Steps (LLM):** `step_3TX_class__kraken2`
**Steps (GT):**  `step_3TX_species__mash`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'
workflow {
    step_3TX_species__mash(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_3TX_class__kraken2 } from '../steps/step_3TX_class__kraken2'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def kraken2DbPath = "${params.assets_dir}/step_3TX_class__kraken2/kraken2_db"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    reads = getSingleInput()

    // Kraken2 taxonomic classification
    kraken2_out = step_3TX_class__kraken2(reads)

    // Emit the genus-level report for downstream use
    // Note: The genus_report is already emitted by the step_3TX_class__kraken2 workflow
    // No further action needed here as the report is published by the process
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_class__kraken2__db
```

### `E03_cgmlst_sal_fastp_spades` — `missing_param`

**Prompt:** Generate cgMLST profiles for Salmonella enterica starting from paired-end Illumina FASTQ.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def genusSpecies = 'Salmonella_enterica'

def cgMLSTSchema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    raw_reads = getInput()

    // 1. Quality Control (FastQC)
    step_0SQ_rawreads__fastq(raw_reads)

    // 2. Preprocessing (Trimming with fastp)
    trimmed_reads = step_1PP_trimming__fastp(raw_reads).trimmed

    // 3. Assembly (De novo assembly with Shovill)
    assembly = step_2AS_denovo__shovill(trimmed_reads).assembly

    // 4. Species Identification (KmerFinder)
    step_3TX_species__kmerfinder(assembly)

    // 5. cgMLST Profiling (chewBBACA)
    step_4TY_cgMLST__chewbbaca(assembly, genusSpecies, cgMLSTSchema)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `E05_flaa_cam` — `missing_param`

**Prompt:** flaA typing pipeline for Campylobacter from paired-end Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__kmerfinder, step_2AS_denovo__spades, step_4TY_flaA__flaA, step_2AS_denovo__shovill`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def flaASchema = 'flaA'

def flaAGenusAllowed = ['campylobacter']

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_flaA_typing {
    
    take:
        
        rawReads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawReads)

        // Species confirmation using kmerfinder
        kmerfinder_out = step_3TX_species__kmerfinder(trimmed)
        assigned_species = kmerfinder_out.assigned_species.map { [ it[0], it[1] ] }

        // De novo assembly (using SPAdes)
        assembly = step_2AS_denovo__spades(trimmed).assembled

        // flaA typing
        step_4TY_flaA__flaA(assembly, assigned_species)
    
}

workflow wf_flaA_typing_shovill {
    
    take:
        
        rawReads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawReads)

        // Species confirmation using kmerfinder
        kmerfinder_out = step_3TX_species__kmerfinder(trimmed)
        assigned_species = kmerfinder_out.assigned_species.map { [ it[0], it[1] ] }

        // De novo assembly (using Shovill)
        assembly = step_2AS_denovo__shovill(trimmed).assembly

        // flaA typing
        step_4TY_flaA__flaA(assembly, assigned_species)
    
}

// --- ENTRYPOINT ---
workflow {
    // Choose assembly method: SPAdes (default) or Shovill
    // wf_flaA_typing(getSingleInput())
    wf_flaA_typing_shovill(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `E07_abricate_eco` — `missing_param`

**Prompt:** Resistance gene detection with ABRicate on Escherichia coli from Illumina paired FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_denovo__shovill, step_4AN_AMR__abricate, step_1PP_trimming__fastp`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def escherichiaColiSpecies = 'Escherichia coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_escherichia_coli_resistance_detection {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
        }
        .set { trimmedMap }

        // Species confirmation with KmerFinder
        kmerfinder_out = step_3TX_species__kmerfinder(trimmedMap.trimmed)

        // Branch based on species confirmation
        kmerfinder_out.assigned_species.branch {
            ecoli: it[1] == escherichiaColiSpecies
            not_ecoli: true
        }
        .set { speciesBranched }

        // Assembly with Shovill (only for E. coli)
        shovill_out = step_2AS_denovo__shovill(speciesBranched.ecoli)

        // Resistance gene detection with ABRicate
        step_4AN_AMR__abricate(shovill_out.assembly)
    
}

workflow wf_preprocess_illumina_paired {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
    
    emit:
        
        trimmed
        
    
}

// --- ENTRYPOINT ---
workflow {
    // Preprocess Illumina paired FASTQ reads
    rawreads = getSingleInput()

    // Preprocessing: Trimming
    wf_preprocess_illumina_paired(rawreads)

    // Resistance detection pipeline for Escherichia coli
    wf_escherichia_coli_resistance_detection(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `E09_mlst_eco_trimmomatic` — `arity_error`

**Prompt:** MLST on E. coli paired Illumina reads: Trimmomatic + SPAdes + mlst.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__trimmomatic, step_2AS_denovo__spades, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__trimmomatic(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

def mlstExcludedSchemas = 'abaumannii,campylobacter,clostridium,haemophilus,helicobacter,legionella,listeria,mycobacterium,pseudomonas,salmonella,streptococcus'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    rawreads = step_0SQ_rawreads__fastq(getSingleInput())
    trimmed = step_1PP_trimming__trimmomatic(rawreads).trimmed
    assembly = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `step_1PP_trimming__trimmomatic` declares 1 input channels but 0 were given
```

### `E13_abricate_sal` — `file_not_found`

**Prompt:** Antimicrobial resistance gene screening with ABRicate for Salmonella enterica from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4AN_AMR__abricate`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def step_1PP_trimming__fastp = '../steps/step_1PP_trimming__fastp/main.nf'

def step_2AS_denovo__shovill = '../steps/step_2AS_denovo__shovill/main.nf'

def step_4AN_AMR__abricate = '../steps/step_4AN_AMR__abricate/main.nf'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    contigs = step_2AS_denovo__shovill(trimmed)
    step_4AN_AMR__abricate(contigs)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.SAL.7.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `E14_prokka_eco` — `arity_error`

**Prompt:** Annotate an E. coli assembly with Prokka, starting from paired Illumina reads.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4AN_genes__prokka`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def prokkaKingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // 1. Input Handling
    rawreads = step_0SQ_rawreads__fastq(getInput())

    // 2. Trimming
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    // 3. De Novo Assembly
    assembly = step_2AS_denovo__shovill(trimmed).assembly

    // 4. Annotation
    assembly.multiMap {
        assembly: it
        kingdom: prokkaKingdom
        riscd_ref: '-'
        refid: '-'
        refpath: getEmpty()
    }.set { prokkaIn }
    step_4AN_genes__prokka(prokkaIn)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were given
```

### `F03_mash_lis` — `file_not_found`

**Prompt:** Sketch-based species ID with Mash on a Listeria isolate (paired Illumina).

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_3TX_species__mash`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'
workflow {
    step_3TX_species__mash(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def stepIdMash = 'step_3TX_species__mash'

def stepIdKmerfinder = 'step_3TX_species__kmerfinder'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_species_id {
    
    take:
        
        reads
        
    
    main:
        reads.multiMap {
            reads: it
        }
        .set { readsMap }

        mash_out = ${stepIdMash}(readsMap.reads)
        kmerfinder_out = ${stepIdKmerfinder}(readsMap.reads)
    
    emit:
        
        assigned_species = kmerfinder_out.assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_species_id(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.LIS.A.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `H01_mlst_plus_cgmlst_lis` — `missing_param`

**Prompt:** Run both MLST and cgMLST typing on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__kmerfinder, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def genusSpecies = 'Listeria monocytogenes'

def cgMLSTSchema = "${params.assets_dir}/step_4TY_cgMLST__chewbbaca/schemas/Listeria_monocytogenes_Pasteur_cgMLST_2022-06-23T18_03_54.613576.zip"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // 1. Input Handling
    rawreads = getSingleInput()

    // 2. Trimming (Step 1PP)
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    // 3. Assembly (Step 2AS)
    assembly = step_2AS_denovo__shovill(trimmed).assembly

    // 4. Species Confirmation (Step 3TX)
    assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

    // 5. MLST Typing (Step 4TY)
    step_4TY_MLST__mlst(assembly)

    // 6. cgMLST Typing (Step 4TY)
    // Cross assembly with genus_species and schema
    assembly.multiMap {
        assembly: it
        genus_species: genusSpecies
        schema: cgMLSTSchema
    }.set { cgmlst_input }

    step_4TY_cgMLST__chewbbaca(cgmlst_input.assembly, cgmlst_input.genus_species, cgmlst_input.schema)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `H02_mlst_plus_flaa_cam` — `missing_param`

**Prompt:** Comprehensive Campylobacter typing from paired Illumina FASTQ: MLST + flaA.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4TY_MLST__mlst, step_4TY_flaA__flaA`
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def flaA_MLST_SCHEMA = 'flaA'

def campylobacterAllowedSpecies = 'campylobacter'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_typing {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        assembly = step_2AS_denovo__spades(trimmed).assembled

        kmerfinder_out = step_3TX_species__kmerfinder(assembly)

        step_4TY_MLST__mlst(assembly)

        step_4TY_flaA__flaA(assembly, kmerfinder_out.assigned_species)
    
}

workflow step_1PP_trimming__fastp {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = fastp(rawreads).trimmed

        fastqc(trimmed)

        readsCheckInput = rawreads.cross(trimmed) { extractKey(it) }.multiMap {
            rawreads: it[0]
            trimmed: it[1]
        }
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)
    
    emit:
        
        trimmed
        
    
}

workflow step_2AS_denovo__spades {
    
    take:
        
        data
        
    
    main:
        denovo_out = denovo(data)

        assembly_filter_out = assembly_filter(denovo_out.scaffolds).fasta

        quast(assembly_filter_out)

        assembled = assembly_filter_out
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_campylobacter_typing(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `H04_mlst_plus_abricate_sal` — `missing_param`

**Prompt:** Salmonella enterica: MLST typing and AMR screening with ABRicate from paired Illumina FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp, step_2AS_denovo__shovill`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def genusSpecies = 'Salmonella enterica'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_typing {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        trimmed.cross(assigned_species) { extractKey(it) }.multiMap { 
          trimmed: it[0]
          species: it[1][1]
          referencePath: it[1][2]
        }.set { trimAndSpecies }

        step_2AS_mapping__bowtie(trimAndSpecies.trimmed, trimAndSpecies.referencePath)
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
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__shovill(trimmed)
    wf_salmonella_typing(trimmed, assembly)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `I02_mash_fastp_shovill` — `none`

**Prompt:** Species sketch with Mash plus assembly via fastp + Shovill from paired Illumina reads.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__mash, step_2AS_denovo__shovill`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__mash`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
workflow {
    raw = getSingleInput()
    step_3TX_species__mash(raw)
    trimmed   = step_1PP_trimming__fastp(raw).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_species_sketching {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        step_3TX_species__mash(trimmed)

        assembly = step_2AS_denovo__shovill(trimmed).assembly
    
}

// --- ENTRYPOINT ---
workflow {
    wf_species_sketching(getSingleInput())
}
```
**Error excerpt:**
```
(no excerpt)
```

### `K02_mlst_eco_fastp_spades` — `file_not_found`

**Prompt:** MLST typing on Escherichia coli from paired-end Illumina FASTQ (fastp + spades + mlst).

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

def mlstExcludedSchemas = 'ecoli,abc,aba,aba2,aba3,aba4,aba5,aba6,aba7,aba8,aba9,aba10,aba11,aba12,aba13,aba14,aba15,aba16,aba17,aba18,aba19,aba20'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_mlst {
    
    take:
        
        trimmed
        
    
    main:
        spades_out = step_2AS_denovo__spades(trimmed)
        step_4TY_MLST__mlst(spades_out.assembly)
    
    emit:
        
        assembly = spades_out.assembled
        
    
}

workflow wf_trim_and_qc {
    
    take:
        
        rawreads
        
    
    main:
        fastp_out = step_1PP_trimming__fastp(rawreads)
    
    emit:
        
        trimmed = fastp_out.trimmed
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_trim_and_qc(getSingleInput())
    wf_ecoli_mlst(wf_trim_and_qc.trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.ECO.100.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K05_chewbbaca_lis_fastp_spades` — `arity_error`

**Prompt:** cgMLST allelic profiling on Listeria monocytogenes from paired-end Illumina FASTQ (fastp + spades + chewbbaca).

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

def genusSpecies = 'Listeria monocytogenes'

def cgMLSTSchema = "${params.assets_dir}/module_cgmlst_listeria_monocytogenes/l_mono_chewie_1748_220623.zip"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    reads = step_0SQ_rawreads__fastq(getSingleInput())

    trimmed = step_1PP_trimming__fastp(reads).trimmed

    assembly = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_cgMLST__chewbbaca(assembly, genusSpecies, cgMLSTSchema)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were given
```

### `K11_abricate_cam_fastp_spades` — `file_not_found`

**Prompt:** ABRicate AMR screening on Campylobacter jejuni from paired-end Illumina FASTQ (fastp + spades + abricate).

**Steps (LLM):** `step_2AS_denovo__spades, step_1PP_trimming__fastp`
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def amrDb = 'vfdb'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_abricate_amr_screening {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            assembly: [ it[0], "${it[0][0]}_spades_assembly", it[1] ]
        }.set { prep }

        spades_out = step_2AS_denovo__spades(prep.trimmed)
        assembly_filter_out = assembly_filter(spades_out.assembled).fasta

        abricate(assembly_filter_out).set { abricate_out }
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_abricate_amr_screening(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.CAM.101.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K14_prokka_sal_fastp_spades` — `arity_error`

**Prompt:** Prokka annotation on Salmonella enterica from paired-end Illumina FASTQ (fastp + spades + prokka).

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

def kingdom = 'Bacteria'

def prokkaRiscd = '220308-020220308005121273-4AN_import-external'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Step 1: Input FASTQ files
    rawreads = step_0SQ_rawreads__fastq(getInput())

    // Step 2: Trimming with fastp
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    // Step 3: Assembly with SPAdes
    assembled = step_2AS_denovo__spades(trimmed).assembled

    // Step 4: Annotation with Prokka
    prokka_input = assembled.map { [prokkaRiscd, it, kingdom, '-', '-', getEmpty()] }
    step_4AN_genes__prokka(prokka_input)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were given
```

### `K24_chewbbaca_sal_fastp_shovill` — `missing_param`

**Prompt:** cgMLST allelic profiling on Salmonella enterica from paired-end Illumina FASTQ (fastp + shovill + chewbbaca).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def speciesCode = 'Salmonella_enterica'

def cgMLSTSchema = "${params.assets_dir}/module_cgmlst_salmonella/schema"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_cgmlst_salmonella {
    
    take:
        
        reads
        
    
    main:
        reads.set { rawreads }

        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        assembly = step_2AS_denovo__shovill(trimmed).assembly

        species_confirmed = step_3TX_species__kmerfinder(assembly).assigned_species

        // Filter for Salmonella enterica only
        species_confirmed.filter { it[1].contains(speciesCode) }.set { confirmed_salmonella }

        // Prepare inputs for chewBBACA: [riscd, assembly, species, schema]
        confirmed_salmonella.multiMap {
            assembly: it[0,1]
            species: speciesCode
            schema: file(cgMLSTSchema)
        }.set { chewbbaca_in }
        step_4TY_cgMLST__chewbbaca(chewbbaca_in.assembly, chewbbaca_in.species, chewbbaca_in.schema)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_cgmlst_salmonella(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `K26_abricate_eco_fastp_shovill` — `file_not_found`

**Prompt:** ABRicate AMR screening on Escherichia coli from paired-end Illumina FASTQ (fastp + shovill + abricate).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4AN_AMR__abricate`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4AN_AMR__abricate`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def params = [:]

def STEP_1PP_TRIMMING_METHOD = 'fastp'

def STEP_2AS_DENOVO_METHOD = 'shovill'

def STEP_4AN_AMR_METHOD = 'abricate'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_abricate_amr_screening {
    
    take:
        
        raw_reads
        
    
    main:
        trimmed_reads = step_1PP_trimming__fastp(raw_reads)
        assemblies = step_2AS_denovo__shovill(trimmed_reads)
        step_4AN_AMR__abricate(assemblies)
    
}

workflow step_1PP_trimming__fastp {
    
    take:
        
        raw_reads
        
    
    main:
        fastp_out = fastp(raw_reads)
        fastqc(fastp_out.trimmed)
        readsCheckInput = raw_reads.cross(fastp_out.trimmed) { extractKey(it) }.multiMap {
            rawreads: it[0]
            trimmed: it[1]
        }
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)
    
    emit:
        
        trimmed = fastp_out.trimmed
        
    
}

workflow step_2AS_denovo__shovill {
    
    take:
        
        trimmed_reads
        
    
    main:
        shovill_out = shovill(trimmed_reads)
        quast(shovill_out.assembly)
        if (!params.skip_checkm) {
            checkm(shovill_out.assembly)
        }
    
    emit:
        
        assembly = shovill_out.assembly
        
    
}

workflow step_4AN_AMR__abricate {
    
    take:
        
        assemblies
        
    
    main:
        abricate(assemblies)
    
}

// --- ENTRYPOINT ---
workflow {
    // Instantiate input channel from FASTQ files
    raw_reads = getSingleInput()

    // Run the AMR screening workflow
    wf_abricate_amr_screening(raw_reads)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.ECO.106.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K27_abricate_sal_fastp_shovill` — `file_not_found`

**Prompt:** ABRicate AMR screening on Salmonella enterica from paired-end Illumina FASTQ (fastp + shovill + abricate).

**Steps (LLM):** `step_2AS_denovo__shovill, step_4AN_AMR__abricate, step_4AN_AMR__filtering, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4AN_AMR__abricate`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__filtering } from '../steps/step_4AN_AMR__filtering'

// --- GLOBALS ---

def amrDb = 'vfdb'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_abricate_amr_screening {
    
    take:
        
        trimmed_reads
        
    
    main:
        trimmed_reads.multiMap {
            trimmed: it
            assembly: [ it[0], file("${it[0]}_assembly.fasta") ]
        }.set { trimmedAndAssembly }

        shovill_out = step_2AS_denovo__shovill(trimmedAndAssembly.trimmed)
        trimmedAndAssembly.assembly.mix(shovill_out.assembly).set { assembly }
        step_4AN_AMR__abricate(assembly)
        step_4AN_AMR__filtering(abricate_out.abricate_results)
    
}

workflow step_1PP_trimming__fastp {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = fastp(rawreads).trimmed

        fastqc(trimmed)
        readsCheckInput = rawreads.cross(trimmed) { extractKey(it) }.multiMap { 
            rawreads: it[0]
            trimmed: it[1]
        }
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)
    
    emit:
        
        trimmed_reads = trimmed
        
    
}

workflow step_2AS_denovo__shovill {
    
    take:
        
        rawreads
        
    
    main:
        contigs_from_pe = shovill(rawreads).assembly
        contigs_from_se = shovill_se(rawreads).assembly
        contigs = contigs_from_pe.mix(contigs_from_se)
        quast(contigs)
        if (!params.skip_checkm) {
            checkm(contigs)
        }
    
    emit:
        
        assembly = contigs
        
    
}

workflow step_4AN_AMR__abricate {
    
    take:
        
        data
        
    
    main:
        abricate(data)
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    trimmed_reads = step_1PP_trimming__fastp(rawreads)
    wf_abricate_amr_screening(trimmed_reads)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.SAL.106.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K30_prokka_eco_fastp_shovill` — `silent_no_op`

**Prompt:** Prokka annotation on Escherichia coli from paired-end Illumina FASTQ (fastp + shovill + prokka).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4AN_genes__prokka`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def kingdomEcoli = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads)

        shovill_out = step_2AS_denovo__shovill(trimmed)

        quast(shovill_out.assembly)
    
    emit:
        
        assembly = shovill_out.assembly
        
    
}

workflow wf_annotate_prokka {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], kingdomEcoli, '-', '-', getEmpty() ] })
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = Channel.fromPath(params.reads)

    wf_trim_and_assemble(rawreads)

    wf_annotate_prokka(wf_trim_and_assemble.assembly)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `K43_abricate_eco_fastp_unicycler` — `file_not_found`

**Prompt:** ABRicate AMR screening on Escherichia coli from paired-end Illumina FASTQ (fastp + unicycler + abricate).

**Steps (LLM):** `step_2AS_denovo__unicycler, step_4AN_AMR__abricate, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__unicycler, step_4AN_AMR__abricate`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__unicycler(trimmed).assembled
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

// --- GLOBALS ---

def amrDb = 'vfdb'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_abricate_amr_screening {
    
    take:
        
        trimmed_reads
        
    
    main:
        trimmed_reads.multiMap {
            trimmed: it
        }.set { prep }

        unicycler_out = step_2AS_denovo__unicycler(prep.trimmed)
        assembly_filter_out = assembly_filter(unicycler_out.assembled)

        step_4AN_AMR__abricate(assembly_filter_out.fasta)
    
}

workflow wf_preprocess_trim {
    
    take:
        
        reads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(reads).trimmed

        fastqc(trimmed)
        readsCheckInput = reads.cross(trimmed) { extractKey(it) }.multiMap {
            rawreads: it[0]
            trimmed: it[1]
        }
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)

        trimmed_reads = trimmed
    
    emit:
        
        trimmed_reads
        
    
}

// --- ENTRYPOINT ---
workflow {
    reads = getSingleInput()

    wf_preprocess_trim(reads)
    wf_abricate_amr_screening(wf_preprocess_trim.out.trimmed_reads)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.ECO.110.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K47_prokka_eco_fastp_unicycler` — `arity_error`

**Prompt:** Prokka annotation on Escherichia coli from paired-end Illumina FASTQ (fastp + unicycler + prokka).

**Steps (LLM):** `step_4AN_genes__prokka, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__unicycler, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__unicycler(trimmed).assembled
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

// --- GLOBALS ---

def prokkaKingdom = 'Bacteria'

def prokkaGenus = 'Escherichia'

def prokkaSpecies = 'coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_prokka_e_coli_annotation {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            kingdom: prokkaKingdom
            genus: prokkaGenus
            species: prokkaSpecies
            riscd_ref: '-'
            refid: '-'
            refpath: getEmpty()
        }.set { prokkaIn }
        step_4AN_genes__prokka(prokkaIn)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_prokka_e_coli_annotation(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_prokka_e_coli_annotation:step_4AN_genes__prokka` declares 1 input channels but 7 were given
```

### `K48_prokka_sal_fastp_unicycler` — `arity_error`

**Prompt:** Prokka annotation on Salmonella enterica from paired-end Illumina FASTQ (fastp + unicycler + prokka).

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_2AS_denovo__unicycler, step_4AN_genes__prokka`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__unicycler, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__unicycler(trimmed).assembled
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

// --- GLOBALS ---

def prokkaKingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Step 1: Accept paired-end Illumina FASTQ files
    rawreads = step_0SQ_rawreads__fastq(getInput())

    // Step 2: Trim adapters and low-quality bases using fastp
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    // Step 3: Assemble trimmed reads into contigs using Unicycler
    assembled = step_2AS_denovo__unicycler(trimmed).assembled

    // Step 4: Annotate assembled contigs for Salmonella enterica using Prokka
    step_4AN_genes__prokka(assembled.map { [it[0], it[1], prokkaKingdom, '-', '-', getEmpty()] })
}
```
**Error excerpt:**
```
ERROR ~ Workflow `step_1PP_trimming__fastp` declares 1 input channels but 0 were given
```

### `K54_mlst_sal_trimmomatic_spades` — `file_not_found`

**Prompt:** MLST typing on Salmonella enterica from paired-end Illumina FASTQ (trimmomatic + spades + mlst).

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__trimmomatic(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def mlstStep = '4TY_MLST'

def mlstMethod = 'mlst'

def spadesStep = '2AS_denovo'

def spadesMethod = 'spades'

def trimmomaticStep = '1PP_trimming'

def trimmomaticMethod = 'trimmomatic'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_mlst {
    
    take:
        
        rawreads
        
    
    main:
        rawreads | step_1PP_trimming__trimmomatic | step_2AS_denovo__spades | step_4TY_MLST__mlst
    
}

// --- ENTRYPOINT ---
workflow {
    wf_salmonella_mlst(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.SAL.112.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K57_chewbbaca_eco_trimmomatic_spades` — `file_not_found`

**Prompt:** cgMLST allelic profiling on Escherichia coli from paired-end Illumina FASTQ (trimmomatic + spades + chewbbaca).

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    trimmed   = step_1PP_trimming__trimmomatic(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

def ecoliSchema = 'e_coli_chewie_2360_210531'

def ecoliGenusSpecies = 'escherichia_coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_cgmlst_ecoli {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            genus_species: ecoliGenusSpecies
            schema: ecoliSchema
        }.set { prep }

        step_2AS_denovo__spades(prep.trimmed)

        spades_out = step_2AS_denovo__spades.out.assembled

        spades_out.multiMap {
            assembly: it
            genus_species: prep.genus_species
            schema: prep.schema
        }.set { cgmlst_input }

        step_4TY_cgMLST__chewbbaca(cgmlst_input.assembly, cgmlst_input.genus_species, cgmlst_input.schema)
    
}

workflow wf_trim_and_qc {
    
    take:
        
        rawreads
        
    
    main:
        step_1PP_trimming__fastp(rawreads)

        trimmed = step_1PP_trimming__fastp.out.trimmed

        fastqc(trimmed)
    
    emit:
        
        trimmed
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_trim_and_qc(getSingleInput())

    wf_cgmlst_ecoli(wf_trim_and_qc.trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.ECO.113.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K58_chewbbaca_sal_trimmomatic_spades` — `missing_param`

**Prompt:** cgMLST allelic profiling on Salmonella enterica from paired-end Illumina FASTQ (trimmomatic + spades + chewbbaca).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    trimmed   = step_1PP_trimming__trimmomatic(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def genusSpecies = 'Salmonella_enterica'

def cgMLSTSchema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_cgmlst {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        assembly = step_2AS_denovo__spades(trimmed).assembled

        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        assemblyAndSpecies = assembly.cross(assigned_species) { extractKey(it) }.multiMap {
            assembly: it[0]
            species: it[1][1]
        }

        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, cgMLSTSchema)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_salmonella_cgmlst(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `K59_abricate_lis_trimmomatic_spades` — `file_not_found`

**Prompt:** ABRicate AMR screening on Listeria monocytogenes from paired-end Illumina FASTQ (trimmomatic + spades + abricate).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate`
**Steps (GT):**  `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades, step_4AN_AMR__abricate`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__trimmomatic(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def amrDb = 'vfdb'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        raw_reads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(raw_reads)
        assembled = step_2AS_denovo__spades(trimmed)
    
    emit:
        
        assembly = assembled
        
    
}

workflow wf_abricate_screen {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_AMR__abricate(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    raw_reads = getSingleInput()
    wf_trim_and_assemble(raw_reads)
    wf_abricate_screen(wf_trim_and_assemble.assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.LIS.114.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `L04_mlst_abricate_lis` — `file_not_found`

**Prompt:** From paired Illumina FASTQ of Listeria monocytogenes: trim with fastp, assemble with SPAdes, then run mlst and abricate in parallel.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4AN_AMR__abricate, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { module_qc_fastqc } from '../modules/module_qc_fastqc'

// --- GLOBALS ---

def listeriaMLSTSchema = 'listeria'

def abricateDB = 'vfdb'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_typing {
    
    take:
        
        trimmed_fasta
        
    
    main:
        trimmed_fasta.multiMap {
            trimmed: it
            assembly: [ it[0], it[1] ]
        }.set { prep }

        spades_out = step_2AS_denovo__spades(prep.trimmed)
        step_4TY_MLST__mlst(spades_out.assembled.map { [ it[0], it[1] ] })
        step_4AN_AMR__abricate(spades_out.assembled.map { [ it[0], it[1] ] })
    
}

workflow wf_listeria_qc {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads)
        module_qc_fastqc(trimmed)

        readsCheckInput = rawreads.cross(trimmed) { extractKey(it) }.multiMap {
            rawreads: it[0]
            trimmed: it[1]
        }
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_listeria_qc(getSingleInput())

    trimmed_fasta = step_1PP_trimming__fastp(getSingleInput())

    wf_listeria_typing(trimmed_fasta.trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.LIS.116.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `L05_mlst_abricate_eco` — `file_not_found`

**Prompt:** From paired Illumina FASTQ of Escherichia coli: trim with fastp, assemble with SPAdes, then run mlst and abricate in parallel.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4AN_AMR__abricate, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

def escherichiaColiSchema = 'escherichia coli'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_typing {
    
    take:
        
        trimmed
        
    
    main:
        assembled = step_2AS_denovo__spades(trimmed).assembled

        step_4TY_MLST__mlst(assembled)
        step_4AN_AMR__abricate(assembled)
    
}

workflow wf_ecoli_qc {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        fastqc(rawreads)
        readsCheckInput = rawreads.cross(trimmed) { extractKey(it) }.multiMap {
            rawreads: it[0]
            trimmed: it[1]
        }
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_ecoli_qc(getSingleInput())
    wf_ecoli_typing(wf_ecoli_qc.trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.ECO.116.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `L06_chewbbaca_abricate_lis` — `file_not_found`

**Prompt:** From paired Illumina FASTQ of Listeria monocytogenes: trim with fastp, assemble with SPAdes, then run chewbbaca and abricate in parallel.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def chewbbacaSchema = 'l_mono_chewie_1748_220623'

def chewbbacaSchemaPath = "/schemas/Listeria_monocytogenes_Pasteur_cgMLST_2022-06-23T18_03_54.613576.zip"

def genusSpecies = 'Listeria monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_monocytogenes {
    
    take:
        
        rawReads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawReads).trimmed

        assembly = step_2AS_denovo__spades(trimmed).assembled

        chewbbaca(assembly, genusSpecies, chewbbacaSchema)

        step_4AN_AMR__abricate(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_listeria_monocytogenes(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.LIS.117.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `L12_abricate_prokka_sal` — `file_not_found`

**Prompt:** From paired Illumina FASTQ of Salmonella enterica: trim with fastp, assemble with SPAdes, then run abricate and prokka in parallel.

**Steps (LLM):** `step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__abricate(assembled)
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def kingdomSalmonella = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_assembly {
    
    take:
        
        trimmed
        
    
    main:
        spades_out = step_2AS_denovo__spades(trimmed)
        quast(spades_out.assembled)
    
    emit:
        
        assembly = spades_out.assembled
        
    
}

workflow wf_salmonella_amr {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_AMR__abricate(assembly)
    
}

workflow wf_salmonella_annotation {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], kingdomSalmonella, '-', '-', getEmpty() ] })
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_salmonella_assembly(trimmed)
    wf_salmonella_amr(wf_salmonella_assembly.out.assembly)
    wf_salmonella_annotation(wf_salmonella_assembly.out.assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.SAL.117.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `L17_staramr_abricate_cam` — `file_not_found`

**Prompt:** From paired Illumina FASTQ of Campylobacter jejuni: trim with fastp, assemble with SPAdes, then run staramr and abricate in parallel.

**Steps (LLM):** `step_2AS_denovo__spades, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4AN_AMR__staramr`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__staramr(assembled, param('genus_species'))
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def campylobacterSpecies = 'campylobacter_jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campy_amr {
    
    take:
        
        trimmed_reads
        
    
    main:
        spades_out = step_2AS_denovo__spades(trimmed_reads)

        staramr( spades_out.assembled, campylobacterSpecies )
        abricate( spades_out.assembled )
    
}

// --- ENTRYPOINT ---
workflow {
    // 1. Trimming
    trimmed_reads = step_1PP_trimming__fastp(getSingleInput()).trimmed

    // 2. Assembly
    // (handled inside wf_campy_amr)

    // 3. AMR annotation (parallel)
    wf_campy_amr(trimmed_reads)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.CAM.120.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `M02_mlst+chewbbaca+prokka_sal` — `file_not_found`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Salmonella enterica from paired Illumina FASTQ: trim, assemble, then run mlst, chewbbaca, prokka in parallel on the assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca, step_4AN_genes__prokka`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

// --- GLOBALS ---

def genusSpecies = 'Salmonella_enterica'

def cgMLSTSchema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_typing_amr_annotation {
    
    take:
        
        rawReads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawReads).trimmed
        assembly = step_2AS_denovo__shovill(trimmed).assembly

        // Parallel typing and annotation
        step_4TY_MLST__mlst(assembly)

        assembly.cross(genusSpecies).cross(cgMLSTSchema) { extractKey(it) }.map {
            [ it[0][0], it[0][1], it[1] ]
        }.set { chewbbacaInput }
        step_4TY_cgMLST__chewbbaca(chewbbacaInput, genusSpecies, cgMLSTSchema)

        // Prokka requires [riscd, assembly, kingdom, riscd_ref, refid, refpath]
        // For bacteria, use '-' for refid and refpath
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
    
}

// --- ENTRYPOINT ---
workflow {
    wf_salmonella_typing_amr_annotation(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.SAL.118.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `M03_mlst+abricate+prokka_eco` — `missing_param`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Escherichia coli from paired Illumina FASTQ: trim, assemble, then run mlst, abricate, prokka in parallel on the assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4AN_AMR__abricate(assembled)
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def bacterialKingdom = 'Bacteria'

def skipBestrefMapping = params.skip_bestref_mapping ?: false

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_typing_amr_annotation {
    
    take:
        
        trimmed_reads
        
        assembly
        
    
    main:
        assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

        if (!skipBestrefMapping) {
            trimmed_reads.cross(assigned_species) { extractKey(it) }.multiMap { 
                trimmed: it[0]
                species: it[1][1]
                referencePath: it[1][2]
            }.set { trimAndSpecies }
            step_2AS_mapping__bowtie(trimAndSpecies.trimmed, trimAndSpecies.referencePath)
        }

        step_4AN_AMR__abricate(assembly)

        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], bacterialKingdom, '-', '-', getEmpty() ] })

        assembly.cross(assigned_species) { extractKey(it) }.multiMap { 
            assembly: it[0]
            species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4AN_AMR__staramr(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, '')
    
}

// --- ENTRYPOINT ---
workflow {
    wf_ecoli_typing_amr_annotation(getTrimmedReads(true), getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `M04_mlst+abricate+prokka_lis` — `file_not_found`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Listeria monocytogenes from paired Illumina FASTQ: trim, assemble, then run mlst, abricate, prokka in parallel on the assembly.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4AN_AMR__abricate(assembled)
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def listeriaKingdom = 'Bacteria'

def listeriaSchema = 'listeria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_assembly {
    
    take:
        
        trimmed
        
    
    main:
        spades_out = step_2AS_denovo__spades(trimmed)
    
    emit:
        
        assembly = spades_out.assembled
        
    
}

workflow wf_listeria_typing {
    
    take:
        
        assembly
        
    
    main:
        step_4TY_MLST__mlst(assembly)
    
}

workflow wf_listeria_amr {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_AMR__abricate(assembly)
    
}

workflow wf_listeria_annotation {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], listeriaKingdom, '-', '-', getEmpty() ] })
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())

    wf_listeria_assembly(trimmed)
    wf_listeria_typing(wf_listeria_assembly.assembly)
    wf_listeria_amr(wf_listeria_assembly.assembly)
    wf_listeria_annotation(wf_listeria_assembly.assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.LIS.122.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `M08_mlst+staramr+prokka_cam` — `file_not_found`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Campylobacter jejuni from paired Illumina FASTQ: trim, assemble, then run mlst, staramr, prokka in parallel on the assembly.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4AN_AMR__staramr, step_4AN_genes__prokka, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr, step_4AN_genes__prokka, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4AN_AMR__staramr(assembled, param('genus_species'))
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def genusSpecies = 'Campylobacter jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_assembly {
    
    take:
        
        trimmed
        
    
    main:
        spades_out = step_2AS_denovo__spades(trimmed)
    
    emit:
        
        assembly = spades_out.assembled
        
    
}

workflow wf_campylobacter_mlst {
    
    take:
        
        assembly
        
    
    main:
        step_4TY_MLST__mlst(assembly)
    
}

workflow wf_campylobacter_amr {
    
    take:
        
        assembly
        
        genusSpecies
        
    
    main:
        step_4AN_AMR__staramr(assembly, genusSpecies)
    
}

workflow wf_campylobacter_annotation {
    
    take:
        
        assembly
        
    
    main:
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
    
}

// --- ENTRYPOINT ---
workflow {
    // Input handling
    rawreads = getSingleInput()

    // Preprocessing: Trimming
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    // De novo Assembly
    wf_campylobacter_assembly(trimmed)

    // Parallel downstream analyses
    wf_campylobacter_mlst(spades_out.assembled)
    wf_campylobacter_amr(spades_out.assembled, genusSpecies)
    wf_campylobacter_annotation(spades_out.assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.CAM.126.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `M09_chewbbaca+abricate+prokka_lis` — `missing_param`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Listeria monocytogenes from paired Illumina FASTQ: trim, assemble, then run chewbbaca, abricate, prokka in parallel on the assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca, step_4AN_AMR__abricate, step_4AN_genes__prokka`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
    step_4AN_AMR__abricate(assembled)
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def genusSpecies = 'listeria_monocytogenes'

def cgMLSTSchema = 'l_mono_chewie_1748_220623'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_monocytogenes_typing {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembly = step_2AS_denovo__shovill(trimmed).assembly
        kmerfinder_out = step_3TX_species__kmerfinder(assembly)
        step_4TY_cgMLST__chewbbaca(assembly, genusSpecies, cgMLSTSchema)
        step_4AN_AMR__abricate(assembly)
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
    
}

// --- ENTRYPOINT ---
workflow {
    wf_listeria_monocytogenes_typing(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `NA03_abricate_lis_assembly` — `missing_param`

**Prompt:** Run abricate on a pre-existing Listeria monocytogenes assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_4AN_AMR__abricate`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    step_4AN_AMR__abricate(getInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def genusSpecies = 'Listeria monocytogenes'

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
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, schemaPath)
    
    emit:
        
        genus_species = assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    schemaPath = params.schema ? file(params.schema) : getEmpty()
    module_typing_bacteria(getTrimmedReads(true), getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `NA08_prokka_eco_assembly` — `file_not_found`

**Prompt:** Run prokka on a pre-existing Escherichia coli assembly.

**Steps (LLM):** `step_4AN_genes__prokka`
**Steps (GT):**  `step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    step_4AN_genes__prokka(getInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    getInput()
        .multiMap {
            assembly: it
            kingdom: kingdom
            reference: [ '-', '-', getEmpty() ]
        }
        .set { prokkaInput }

    step_4AN_genes__prokka(prokkaInput.assembly, prokkaInput.assembly, prokkaInput.kingdom, prokkaInput.reference[0], prokkaInput.reference[1], prokkaInput.reference[2])
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.ECO.122.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `O01_spades_lis` — `file_not_found`

**Prompt:** De novo assembly with spades from paired Illumina FASTQ of Listeria monocytogenes.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
**Steps (GT):**  `step_2AS_denovo__spades`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
workflow {
    step_2AS_denovo__spades(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

// --- GLOBALS ---

def hostRiscd = '220308-020220308005121273-1PP_hostdepl-bowtie'

def hostCode = 'GRCh38'

def hostPath = "${params.assets_dir}/module_denovo/GRCh38.fasta"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_denovo {
    
    take:
        
        trimmedReads
        
        host
        
    
    main:
        trimmedReads.cross(host) { extractKey(it) }
            .map { [ it[0][0], it[0][1], it[1][1] ] } //riscd, reads, host
            .branch {
                with_host: it[1][1]
                without_host: true
            }
        .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set{ denovoInput }

        assembled = step_2AS_denovo__spades(denovoInput)
    
    emit:
        
        assembled
        
        depleted
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_denovo(getSingleInput(), [hostRiscd, hostCode, file(hostPath)])
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.LIS.127.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `O09_unicycler_cam` — `silent_no_op`

**Prompt:** De novo assembly with unicycler from paired Illumina FASTQ of Campylobacter jejuni.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__unicycler`
**Steps (GT):**  `step_2AS_denovo__unicycler`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'
workflow {
    step_2AS_denovo__unicycler(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

// --- GLOBALS ---

def params = [:]

def params.outdir = '${workflow.launchDir}/results'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_assembly {
    
    take:
        
        raw_reads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(raw_reads).trimmed
        assembly = step_2AS_denovo__unicycler(trimmed).assembled
    
}

// --- ENTRYPOINT ---
workflow {
    raw_reads = getSingleInput()
    wf_campylobacter_assembly(raw_reads)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `P02_chopper_flye_mlst_sal` — `file_not_found`

**Prompt:** Nanopore pipeline for Salmonella enterica: chopper trimming + Flye assembly + mlst.

**Steps (LLM):** `step_1PP_hostdepl__minimap2, step_1PP_trimming__chopper, step_2AS_denovo__flye, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__chopper, step_2AS_denovo__flye, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'
include { step_2AS_denovo__flye } from '../steps/step_2AS_denovo__flye'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__chopper(getSingleInput()).trimmed
    assembled = step_2AS_denovo__flye(trimmed).assembly
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey } from '../functions/common.nf'

include { getHostReference; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'

include { step_1PP_hostdepl__minimap2 } from '../steps/step_1PP_hostdepl__minimap2'

include { step_2AS_denovo__flye } from '../steps/step_2AS_denovo__flye'

// --- GLOBALS ---

def hostDepletionMethod = 'minimap2'

def hostDepletionRisCd = '231219-020223121900512127-1PP_hostdepl-minimap2'

def trimmingMethod = 'chopper'

def trimmingRisCd = '231219-020223121900512127-1PP_trimming-chopper'

def assemblyMethod = 'flye'

def assemblyRisCd = '231219-020223121900512127-2AS_denovo-flye'

def mlstMethod = 'mlst'

def mlstRisCd = '231219-020223121900512127-4TY_MLST-mlst'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_nanopore {
    
    take:
        
        raw_reads
        
        host_reference
        
    
    main:
        raw_reads.cross(host_reference) { extractKey(it) }.multiMap {
            reads: it[0]
            host:  it[1]
        }.set { prep }

        step_1PP_hostdepl__minimap2_out = step_1PP_hostdepl__minimap2(prep.reads, prep.host)
        depleted_reads = step_1PP_hostdepl__minimap2_out.depleted

        step_1PP_trimming__chopper_out = step_1PP_trimming__chopper(depleted_reads)
        trimmed_reads = step_1PP_trimming__chopper_out.trimmed

        step_2AS_denovo__flye_out = step_2AS_denovo__flye(trimmed_reads)
        assembled_contigs = step_2AS_denovo__flye_out.assembly

        step_4TY_MLST__mlst(assembled_contigs)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_salmonella_nanopore(getSingleInput(), getHostReference())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.SAL.126.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `P04_chopper_flye_mlst_cam` — `arity_error`

**Prompt:** Nanopore pipeline for Campylobacter jejuni: chopper trimming + Flye assembly + mlst.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__chopper, step_2AS_denovo__flye, step_4AN_genes__prokka`
**Steps (GT):**  `step_1PP_trimming__chopper, step_2AS_denovo__flye, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'
include { step_2AS_denovo__flye } from '../steps/step_2AS_denovo__flye'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__chopper(getSingleInput()).trimmed
    assembled = step_2AS_denovo__flye(trimmed).assembly
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

include { step_2AS_denovo__flye } from '../steps/step_2AS_denovo__flye'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

def prokkaKingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Step 1: Input raw Nanopore reads
    raw_reads = step_0SQ_rawreads__fastq(getSingleInput())

    // Step 2: Trimming with Chopper
    trimmed_reads = step_1PP_trimming__chopper(raw_reads).trimmed

    // Step 3: Assembly with Flye
    assembly = step_2AS_denovo__flye(trimmed_reads).assembly

    // Step 4: Annotation with Prokka
    // Prokka requires: [riscd, assembly, kingdom, riscd_ref, refid, refpath]
    // For Campylobacter jejuni (Bacteria), no GenBank reference is needed
    prokka_input = assembly.map { [ it[0], it[1], prokkaKingdom, '-', '-', getEmpty() ] }
    step_4AN_genes__prokka(prokka_input)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `step_1PP_trimming__chopper` declares 1 input channels but 0 were given
```

### `P07_chopper_flye_abricate_sal` — `missing_param`

**Prompt:** Nanopore pipeline for Salmonella enterica: chopper trimming + Flye assembly + abricate.

**Steps (LLM):** `step_1PP_trimming__chopper, step_2AS_denovo__flye, step_4AN_AMR__abricate`
**Steps (GT):**  `step_1PP_trimming__chopper, step_2AS_denovo__flye, step_4AN_AMR__abricate`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'
include { step_2AS_denovo__flye } from '../steps/step_2AS_denovo__flye'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__chopper(getSingleInput()).trimmed
    assembled = step_2AS_denovo__flye(trimmed).assembly
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getHost; getReferenceOptional; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'

include { step_2AS_denovo__flye } from '../steps/step_2AS_denovo__flye'

// --- GLOBALS ---

def abricateDbName = 'viruses_TREF'

def abricateDbRiscd = '220308-020220308005121273-4AN_import-external'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_nanopore {
    
    take:
        
        raw_reads
        
        host_genome
        
        reference_fasta
        
        reference_gb
        
    
    main:
        raw_reads.multiMap {
            reads: it
            host: host_genome
            reference: reference_fasta
            referenceGB: reference_gb
        }.set { prep }

        trimmed = step_1PP_trimming__chopper(prep.reads)

        flye_out = step_2AS_denovo__flye(trimmed)
        step_4AN_AMR__abricate(flye_out.assembly, [abricateDbRiscd, abricateDbName])

        trimmed.set { trimmed_reads }
        flye_out.assembly.set { assembly }
        abricate_out.calls.set { amr_annotation }
    
    emit:
        
        trimmed_reads
        
        assembly
        
        amr_annotation
        
    
}

// --- ENTRYPOINT ---
workflow {
    raw_reads = getSingleInput()
    host_genome = getHost()
    reference_fasta = getReferenceOptional('fa')
    reference_gb = getReferenceOptional('gb')

    wf_salmonella_nanopore(raw_reads, host_genome, reference_fasta, reference_gb)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: host
```

### `P09_chopper_flye_chewbbaca_lis` — `partial_dag`

**Prompt:** Nanopore pipeline for Listeria monocytogenes: chopper trimming + Flye assembly + chewbbaca.

**Steps (LLM):** `step_1PP_trimming__chopper, step_2AS_denovo__flye, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__chopper, step_2AS_denovo__flye, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'
include { step_2AS_denovo__flye } from '../steps/step_2AS_denovo__flye'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    trimmed   = step_1PP_trimming__chopper(getSingleInput()).trimmed
    assembled = step_2AS_denovo__flye(trimmed).assembly
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_denovo__flye } from '../steps/step_2AS_denovo__flye'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def step1RisCd = '240515-020224051500512127-1PP_trimming-chopper'

def step2RisCd = '240515-020224051500512127-2AS_denovo-flye'

def step3RisCd = '240515-020224051500512127-4TY_MLST-mlst'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()

    trimmed = step_1PP_trimming__chopper([step1RisCd, rawreads]).trimmed

    assembly = step_2AS_denovo__flye([step2RisCd, trimmed]).assembly

    step_4TY_MLST__mlst([step3RisCd, assembly])
}
```
**Error excerpt:**
```
Only 5/7 expected processes appeared in the DAG
```

### `Q03_kmerfinder_fastp_spades_sal` — `file_not_found`

**Prompt:** In parallel, identify the species with kmerfinder and trim+assemble paired Illumina FASTQ of Salmonella enterica with fastp + spades.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
workflow {
    raw = getSingleInput()
    step_3TX_species__kmerfinder(raw)
    trimmed   = step_1PP_trimming__fastp(raw).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

def kmerfinderSpeciesDir = "${params.assets_dir}/step_3TX_species__kmerfinder"

def kmerfinderReferenceDir = "${kmerfinderSpeciesDir}/Bacteria/Fasta/"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Step 1: Accept paired Illumina FASTQ reads as input
    reads = step_0SQ_rawreads__fastq(getSingleInput()).reads

    // Step 2: Trim reads using fastp
    trimmed = step_1PP_trimming__fastp(reads).trimmed

    // Step 3: Assemble trimmed reads using SPAdes
    assembled = step_2AS_denovo__spades(trimmed).assembled

    // Step 4: Identify species using KmerFinder on assembled contigs
    step_3TX_species__kmerfinder(assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.SAL.129.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `Q05_kmerfinder_fastp_shovill_eco` — `silent_no_op`

**Prompt:** In parallel, identify the species with kmerfinder and trim+assemble paired Illumina FASTQ of Escherichia coli with fastp + shovill.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_1PP_trimming__fastp, step_2AS_denovo__shovill`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__kmerfinder`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
workflow {
    raw = getSingleInput()
    step_3TX_species__kmerfinder(raw)
    trimmed   = step_1PP_trimming__fastp(raw).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def params = [:]

def workflow = [:]

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_species_identification {
    
    take:
        
        raw_reads
        
    
    main:
        kmerfinder_out = step_3TX_species__kmerfinder(raw_reads)
    
    emit:
        
        assigned_species = kmerfinder_out.assigned_species
        
    
}

workflow wf_ecoli_trimming {
    
    take:
        
        raw_reads
        
    
    main:
        fastp_out = step_1PP_trimming__fastp(raw_reads)
    
    emit:
        
        trimmed = fastp_out.trimmed
        
    
}

workflow wf_ecoli_assembly {
    
    take:
        
        trimmed_reads
        
    
    main:
        shovill_out = step_2AS_denovo__shovill(trimmed_reads)
    
    emit:
        
        assembly = shovill_out.assembly
        
    
}

// --- ENTRYPOINT ---
workflow {
    // Parallel species identification and trimming
    raw_reads = getSingleInput()

    // Species identification (KmerFinder)
    wf_ecoli_species_identification(raw_reads)

    // Trimming (fastp)
    wf_ecoli_trimming(raw_reads)

    // Assembly (Shovill) - depends on trimmed reads
    trimmed_reads = wf_ecoli_trimming.out.trimmed
    wf_ecoli_assembly(trimmed_reads)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `Q06_kmerfinder_fastp_shovill_sal` — `silent_no_op`

**Prompt:** In parallel, identify the species with kmerfinder and trim+assemble paired Illumina FASTQ of Salmonella enterica with fastp + shovill.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__kmerfinder`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__kmerfinder`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
workflow {
    raw = getSingleInput()
    step_3TX_species__kmerfinder(raw)
    trimmed   = step_1PP_trimming__fastp(raw).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

// --- GLOBALS ---

def params = [:]

def workflow = [:]

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    // Step 1: Trim paired Illumina FASTQ reads using fastp
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    // Step 2: Assemble trimmed reads using shovill
    assembly = step_2AS_denovo__shovill(trimmed).assembly

    // Step 3: Identify species using KmerFinder
    step_3TX_species__kmerfinder(assembly)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `Q07_mash_fastp_spades_lis` — `none`

**Prompt:** In parallel, identify the species with mash and trim+assemble paired Illumina FASTQ of Listeria monocytogenes with fastp + spades.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__mash, step_2AS_denovo__spades`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__mash`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
workflow {
    raw = getSingleInput()
    step_3TX_species__mash(raw)
    trimmed   = step_1PP_trimming__fastp(raw).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def stepNameTrimming = '1PP_trimming'

def methodNameTrimming = 'fastp'

def stepNameSpecies = '3TX_species'

def methodNameSpecies = 'mash'

def stepNameAssembly = '2AS_denovo'

def methodNameAssembly = 'spades'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_identify {
    
    take:
        
        rawReads
        
    
    main:
        fastpOut = step_1PP_trimming__fastp(rawReads)
        step_3TX_species__mash(fastpOut.trimmed)
    
    emit:
        
        trimmed = fastpOut.trimmed
        
    
}

workflow wf_assemble_from_trimmed {
    
    take:
        
        trimmed
        
    
    main:
        spadesOut = step_2AS_denovo__spades(trimmed)
    
    emit:
        
        assembled = spadesOut.assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    rawReads = getSingleInput()

    wf_trim_and_identify(rawReads)
    wf_assemble_from_trimmed(wf_trim_and_identify.out.trimmed)
}
```
**Error excerpt:**
```
(no excerpt)
```

### `Q08_mash_fastp_spades_eco` — `file_not_found`

**Prompt:** In parallel, identify the species with mash and trim+assemble paired Illumina FASTQ of Escherichia coli with fastp + spades.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__mash, step_2AS_denovo__spades`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__mash`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
workflow {
    raw = getSingleInput()
    step_3TX_species__mash(raw)
    trimmed   = step_1PP_trimming__fastp(raw).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

def step_1PP_trimming__fastp = '../steps/1PP_trimming__fastp.nf'

def step_3TX_species__mash = '../steps/3TX_species__mash.nf'

def step_2AS_denovo__spades = '../steps/2AS_denovo__spades.nf'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())

    // Species identification (Mash) - runs in parallel on trimmed reads
    step_3TX_species__mash(trimmed)

    // Assembly (SPAdes) - runs in parallel on trimmed reads
    assembled = step_2AS_denovo__spades(trimmed)

    // Publish assembly results (optional downstream usage)
    publishDir mode: 'rellink', "${params.outdir}/assembly", pattern: '*.fasta'
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.ECO.129.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `Q09_mash_fastp_spades_sal` — `none`

**Prompt:** In parallel, identify the species with mash and trim+assemble paired Illumina FASTQ of Salmonella enterica with fastp + spades.

**Steps (LLM):** `step_3TX_species__mash, step_1PP_trimming__fastp, step_2AS_denovo__spades`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__mash`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
workflow {
    raw = getSingleInput()
    step_3TX_species__mash(raw)
    trimmed   = step_1PP_trimming__fastp(raw).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def seqType = 'illumina_paired'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()

    // Parallel species identification with Mash
    mash_out = step_3TX_species__mash(rawreads)

    // Parallel trimming with fastp
    trimmed = step_1PP_trimming__fastp(rawreads).trimmed

    // Assembly of trimmed reads with SPAdes
    spades_out = step_2AS_denovo__spades(trimmed)

    // Publish Mash species identification report
    mash_out.set { _ }

    // Publish trimmed reads
    trimmed.set { _ }

    // Publish assembled contigs
    spades_out.assembled.set { _ }
}
```
**Error excerpt:**
```
(no excerpt)
```

### `Q10_mash_fastp_shovill_lis` — `none`

**Prompt:** In parallel, identify the species with mash and trim+assemble paired Illumina FASTQ of Listeria monocytogenes with fastp + shovill.

**Steps (LLM):** `step_2AS_denovo__shovill, step_3TX_species__mash, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_3TX_species__mash`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
workflow {
    raw = getSingleInput()
    step_3TX_species__mash(raw)
    trimmed   = step_1PP_trimming__fastp(raw).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { module_qc_quast } from '../modules/module_qc_quast'

include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'

include { module_qc_fastqc } from '../modules/module_qc_fastqc'

// --- GLOBALS ---

def mashDbPath = "${params.assets_dir}/mash/refseq/refseq.genomes.k21s1000.msh"

def mashGramPath = "${params.assets_dir}/mash/BACTpipe/resources/gram_stain.txt"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        trimmed
        
    
    main:
        shovill_out = step_2AS_denovo__shovill(trimmed)
        module_qc_quast(shovill_out.assembly)
    
    emit:
        
        assembly = shovill_out.assembly
        
    
}

workflow wf_species_id {
    
    take:
        
        reads
        
    
    main:
        step_3TX_species__mash(reads)
    
}

// --- ENTRYPOINT ---
workflow {
    // Instantiate input channels
    reads_ch = getSingleInput()
    mash_db_ch = Channel.fromPath(mashDbPath)

    // Parallel execution: trimming+assembly and species identification
    trimmed = step_1PP_trimming__fastp(reads_ch)
    wf_trim_and_assemble(trimmed)
    wf_species_id(reads_ch)

    // Optional: QC on raw reads (if needed)
    // module_qc_fastqc(reads_ch)
}
```
**Error excerpt:**
```
(no excerpt)
```

### `R03_mash_sal` — `missing_param`

**Prompt:** mash on paired Illumina FASTQ of Salmonella enterica.

**Steps (LLM):** `step_3TX_species__kmerfinder`
**Steps (GT):**  `step_3TX_species__mash`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'
workflow {
    step_3TX_species__mash(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def kmerfinderSpeciesDir = "${params.assets_dir}/step_3TX_species__kmerfinder__db"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    def reads = getSingleInput()

    // Directly pass paired FASTQ files to KmerFinder for species identification
    step_3TX_species__kmerfinder(reads)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `R05_kraken2_lis` — `missing_param`

**Prompt:** kraken2 on paired Illumina FASTQ of Listeria monocytogenes.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_3TX_class__kraken2, step_3TX_species__kmerfinder`
**Steps (GT):**  `step_3TX_class__kraken2`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_class__kraken2 } from '../steps/step_3TX_class__kraken2'
workflow {
    step_3TX_class__kraken2(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_3TX_class__kraken2 } from '../steps/step_3TX_class__kraken2'

include { getSingleInput } from '../functions/parameters.nf'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def step_0SQ_rawreads__fastq = '../steps/step_0SQ_rawreads__fastq.nf'

def step_3TX_class__kraken2 = '../steps/step_3TX_class__kraken2.nf'

def step_3TX_species__kmerfinder = '../steps/step_3TX_species__kmerfinder.nf'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()

    // Step 1: Quality Control (QC) of Raw Reads
    step_0SQ_rawreads__fastq(rawreads)

    // Step 2: Taxonomic Classification with Kraken2
    kraken2_out = step_3TX_class__kraken2(rawreads)

    // Step 3: Species-Level Identification with KmerFinder
    kmerfinder_out = step_3TX_species__kmerfinder(rawreads)

    // Emit the genus_report and assigned_species channels for downstream use
    // Note: These are the named emits from the respective processes
    // Kraken2 emits 'genus_report' and KmerFinder emits 'assigned_species'
    // No further processing needed as the outputs are already in the required format
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `R07_kraken2_sal` — `missing_param`

**Prompt:** kraken2 on paired Illumina FASTQ of Salmonella enterica.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_3TX_class__kraken2`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_class__kraken2 } from '../steps/step_3TX_class__kraken2'
workflow {
    step_3TX_class__kraken2(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

// --- GLOBALS ---

def genusSpecies = 'Salmonella_enterica'

def schema = "${params.assets_dir}/module_typing_bacteria/salmonella_cgmlst_schema"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_typing {
    
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
        step_4TY_cgMLST__chewbbaca(assemblyAndSpecies.assembly, assemblyAndSpecies.species, schema)
    
    emit:
        
        genus_species = assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_salmonella_typing(getTrimmedReads(true), getAssembly())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `R08_kraken2_cam` — `file_not_found`

**Prompt:** kraken2 on paired Illumina FASTQ of Campylobacter jejuni.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__fastp, step_3TX_class__kraken2`
**Steps (GT):**  `step_3TX_class__kraken2`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_3TX_class__kraken2 } from '../steps/step_3TX_class__kraken2'
workflow {
    step_3TX_class__kraken2(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getInput; hasFastqData; isIlluminaPaired; isIonTorrent; isNanopore } from '../functions/parameters.nf'

include { step_3TX_class__kraken2 } from '../steps/step_3TX_class__kraken2'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

def step_0SQ_rawreads__fastq = '../steps/step_0SQ_rawreads__fastq'

def step_1PP_trimming__fastp = '../steps/step_1PP_trimming__fastp'

def step_3TX_class__kraken2 = '../steps/step_3TX_class__kraken2'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    rawReads = getInput()

    rawReads.branch {
        with_data: hasFastqData(it[1])
        no_reads: true
    }
    .set { rawreads_branched }

    step_0SQ_rawreads__fastq(rawreads_branched.with_data)

    rawreads_branched.with_data.branch {
        illumina: isIlluminaPaired(it[1])
        ion: isIonTorrent(it[1])
        nanopore: isNanopore(it[1])
        other: true // won't be processed
    }
    .set { trimming_by_seqtype }

    trimmed = step_1PP_trimming__fastp(
        trimming_by_seqtype.illumina.mix(trimming_by_seqtype.ion)
    ).trimmed

    step_3TX_class__kraken2(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.CAM.136.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `S01_fastp_lis` — `missing_param`

**Prompt:** fastp read trimming on illumina paired FASTQ of Listeria monocytogenes.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_class__kraken2, step_2AS_denovo__shovill, step_4AN_genes__prokka, step_4AN_AMR__abricate, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__fastp`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
workflow {
    step_1PP_trimming__fastp(getInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_class__kraken2 } from '../steps/step_3TX_class__kraken2'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def kraken2_db_path = "${params.kraken_db}"

def abricate_db_path = "${params.abricate_db}"

def mlst_schema_path = "${params.mlst_schema}"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_monocytogenes {
    
    take:
        
        raw_reads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(raw_reads).trimmed

        trimmed.multiMap {
            trimmed: it
            kraken_db: [ '-', '-', file(kraken2_db_path) ]
        }.set { trimmedAndKraken }

        kraken2_out = step_3TX_class__kraken2(trimmedAndKraken.trimmed)

        assembly = step_2AS_denovo__shovill(trimmed).assembly

        prokka_out = assembly.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] }
        step_4AN_genes__prokka(prokka_out)

        abricate_out = assembly.map { [ it[0], it[1] ] }
        step_4AN_AMR__abricate(abricate_out)

        mlst_out = assembly.map { [ it[0], it[1] ] }
        step_4TY_MLST__mlst(mlst_out)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_listeria_monocytogenes(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_class__kraken2__db
```

### `S04_trimmomatic_cam` — `missing_param`

**Prompt:** trimmomatic read trimming on illumina paired FASTQ of Campylobacter jejuni.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_class__kraken2`
**Steps (GT):**  `step_1PP_trimming__trimmomatic`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'
workflow {
    step_1PP_trimming__trimmomatic(getInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getInput; hasFastqData; isIlluminaPaired } from '../functions/parameters.nf'

include { step_3TX_class__kraken2 } from '../steps/step_3TX_class__kraken2'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def KRAKEN2_DB = "${params.assets_dir}/step_3TX_class__kraken2/kraken2_db"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_illumina_trimming_kraken {
    
    take:
        
        rawReads
        
    
    main:
        rawReads.branch {
            with_data: hasFastqData(it[1])
            no_reads: true
        }
        .set { rawreads_branched }

        rawreads_branched.with_data.branch {
            illumina: isIlluminaPaired(it[1])
            other: true // will not be processed further
        }
        .set { trimming_by_seqtype }

        trimmed = step_1PP_trimming__fastp(trimming_by_seqtype.illumina).trimmed

        trimmed_genus_report = step_3TX_class__kraken2(trimmed).genus_report
    
}

// --- ENTRYPOINT ---
workflow {
    wf_illumina_trimming_kraken(getInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_class__kraken2__db
```

### `S06_chopper_sal` — `file_not_found`

**Prompt:** chopper read trimming on nanopore FASTQ of Salmonella enterica.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__chopper`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'
workflow {
    step_1PP_trimming__chopper(getInput())
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

include { module_qc_nanoplot } from '../modules/module_qc_nanoplot'

// --- GLOBALS ---

def trimStepCode = '1PP_trimming'

def trimMethodCode = 'chopper'

def trimStepMethod = 'step_1PP_trimming__chopper'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = trimStepMethod(getSingleInput())
    module_qc_nanoplot(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_mistral_small/_shared_inputdir/2026/2026.SAL.136.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```
