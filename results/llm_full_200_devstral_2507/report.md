# LLM evaluation — detailed report

Total prompts: **200**  ·  generated code: **185**  ·  syntactically valid: **182**  ·  semantically valid: **116**

Step-set vs. ground truth:  exact match **134**  ·  extra steps **43**  ·  missing steps **49**  ·  hallucinated (non-existent) steps **0**

## Error category breakdown

| Category | Count | Meaning |
|----|----|----|
| `none` | 114 | no error — pipeline passes |
| `file_not_found` | 48 | expected input file is not in the framework layout |
| `no_code` | 15 | LLM did not return any .nf code |
| `silent_no_op` | 12 | DAG empty — pipeline runs but produces no output |
| `partial_dag` | 4 | only some of the expected processes appeared in the DAG |
| `missing_param` | 3 | step requires a param() that was not supplied |
| `arity_error` | 2 | workflow called with wrong number of arguments |
| `ngsmanager_naming` | 2 | input file name does not match parseMetadataFromFileName regex |

## Per-prompt outcome

| # | id | code? | syntax | semantic | procs | error category | first 80 chars of detail |
|---|----|-------|--------|----------|-------|----------------|------|
| 1 | `A01_mlst_listeria` | ✅ | ❌ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 2 | `A02_mlst_ecoli` | ✅ | ✅ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 3 | `A03_mlst_salmonella` | ✅ | ✅ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 4 | `A04_cgmlst_listeria` | ✅ | ✅ | ❌ | 0/3 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 5 | `A05_cgmlst_ecoli` | ✅ | ✅ | ❌ | 0/3 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 6 | `A06_cgmlst_salmonella` | ⚪ | ❌ | ❌ | 0/3 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 7 | `A07_flaa_campylobacter` | ✅ | ✅ | ❌ | 0/1 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 8 | `A08_staramr_campylobacter` | ✅ | ✅ | ✅ | 3/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 9 | `B01_spades_listeria` | ✅ | ✅ | ✅ | 5/3 | `none` |  |
| 10 | `B02_shovill_ecoli` | ✅ | ✅ | ❌ | 0/3 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 11 | `B03_unicycler_salmonella` | ⚪ | ❌ | ❌ | 0/3 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 12 | `B04_plasmidspades` | ⚪ | ❌ | ❌ | 0/3 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 13 | `B05_metaspades` | ⚪ | ❌ | ❌ | 0/3 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 14 | `C01_kmerfinder` | ✅ | ✅ | ✅ | 3/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 15 | `C02_mash` | ✅ | ✅ | ❌ | 4/1 | `none` |  |
| 16 | `C03_kraken2` | ✅ | ✅ | ✅ | 7/2 | `none` |  |
| 17 | `D01_fastp_spades_lis` | ✅ | ✅ | ❌ | 5/6 | `partial_dag` | Only 5/6 expected processes appeared in the DAG |
| 18 | `D02_fastp_shovill_eco` | ⚪ | ❌ | ❌ | 0/6 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 19 | `D03_trimmomatic_spades` | ✅ | ✅ | ❌ | 0/6 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 20 | `D04_fastp_unicycler_sal` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 21 | `D05_fastp_spades_cam` | ⚪ | ❌ | ❌ | 0/6 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 22 | `E01_mlst_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 23 | `E02_cgmlst_lis_fastp_spades` | ✅ | ✅ | ❌ | 0/9 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 24 | `E03_cgmlst_sal_fastp_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 25 | `E04_cgmlst_eco_fastp_shovill` | ✅ | ✅ | ❌ | 0/9 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 26 | `E05_flaa_cam` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 27 | `E06_staramr_cam` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 28 | `E07_abricate_eco` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 29 | `E08_prokka_lis` | ✅ | ✅ | ❌ | 3/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 30 | `E09_mlst_eco_trimmomatic` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 31 | `E10_mlst_sal_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 32 | `E11_cgmlst_lis_shovill` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 33 | `E12_mlst_cam` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 34 | `E13_abricate_sal` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 35 | `E14_prokka_eco` | ✅ | ❌ | ❌ | 6/7 | `arity_error` | ERROR ~ Workflow `wf_ecoli_annotation:step_4AN_genes__prokka` declares 1 input c |
| 36 | `E15_cgmlst_lis_trimmomatic` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 37 | `F01_abricate_assembly` | ✅ | ✅ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 38 | `F02_prokka_assembly` | ✅ | ✅ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 39 | `F03_mash_lis` | ✅ | ✅ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 40 | `F04_kraken2_unknown` | ⚪ | ❌ | ❌ | 0/2 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 41 | `G01_chopper_flye_lis` | ✅ | ✅ | ✅ | 4/4 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.LIS.B.1.1_R1.fastq.gz |
| 42 | `G02_chopper_flye_eco` | ✅ | ✅ | ❌ | 0/4 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 43 | `H01_mlst_plus_cgmlst_lis` | ✅ | ✅ | ✅ | 10/10 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.LIS.C.1.1_R1.fastq.gz |
| 44 | `H02_mlst_plus_flaa_cam` | ✅ | ✅ | ❌ | 0/8 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 45 | `H03_prokka_plus_abricate_eco` | ✅ | ✅ | ❌ | 0/8 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 46 | `H04_mlst_plus_abricate_sal` | ✅ | ✅ | ❌ | 0/8 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 47 | `I01_kmerfinder_fastp_spades` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 48 | `I02_mash_fastp_shovill` | ✅ | ✅ | ❌ | 7/7 | `none` |  |
| 49 | `J01_mobsuite_plasmid` | ⚪ | ❌ | ❌ | 0/1 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 50 | `J02_bbnorm_downsampling` | ✅ | ✅ | ❌ | 0/1 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 51 | `K01_mlst_lis_fastp_spades` | ✅ | ✅ | ❌ | 4/7 | `partial_dag` | Only 4/7 expected processes appeared in the DAG |
| 52 | `K02_mlst_eco_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 53 | `K03_mlst_sal_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 54 | `K04_mlst_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 55 | `K05_chewbbaca_lis_fastp_spades` | ✅ | ✅ | ❌ | 0/9 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 56 | `K06_chewbbaca_eco_fastp_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 57 | `K07_chewbbaca_sal_fastp_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 58 | `K08_abricate_lis_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 59 | `K09_abricate_eco_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 60 | `K10_abricate_sal_fastp_spades` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 61 | `K11_abricate_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 62 | `K12_prokka_lis_fastp_spades` | ✅ | ✅ | ✅ | 11/7 | `none` |  |
| 63 | `K13_prokka_eco_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 64 | `K14_prokka_sal_fastp_spades` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 65 | `K15_prokka_cam_fastp_spades` | ✅ | ✅ | ❌ | 4/7 | `partial_dag` | Only 4/7 expected processes appeared in the DAG |
| 66 | `K16_flaA_cam_fastp_spades` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 67 | `K17_staramr_cam_fastp_spades` | ✅ | ✅ | ❌ | 6/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 68 | `K18_mlst_lis_fastp_shovill` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 69 | `K19_mlst_eco_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 70 | `K20_mlst_sal_fastp_shovill` | ✅ | ✅ | ❌ | 6/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 71 | `K21_mlst_cam_fastp_shovill` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 72 | `K22_chewbbaca_lis_fastp_shovill` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 73 | `K23_chewbbaca_eco_fastp_shovill` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 74 | `K24_chewbbaca_sal_fastp_shovill` | ✅ | ✅ | ❌ | 6/9 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 75 | `K25_abricate_lis_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 76 | `K26_abricate_eco_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 77 | `K27_abricate_sal_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 78 | `K28_abricate_cam_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 79 | `K29_prokka_lis_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 80 | `K30_prokka_eco_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 81 | `K31_prokka_sal_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 82 | `K32_prokka_cam_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 83 | `K33_flaA_cam_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 84 | `K34_staramr_cam_fastp_shovill` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 85 | `K35_mlst_lis_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 86 | `K36_mlst_eco_fastp_unicycler` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 87 | `K37_mlst_sal_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 88 | `K38_mlst_cam_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 89 | `K39_chewbbaca_lis_fastp_unicycler` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 90 | `K40_chewbbaca_eco_fastp_unicycler` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 91 | `K41_chewbbaca_sal_fastp_unicycler` | ✅ | ✅ | ❌ | 6/9 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 92 | `K42_abricate_lis_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 93 | `K43_abricate_eco_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 94 | `K44_abricate_sal_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 95 | `K45_abricate_cam_fastp_unicycler` | ✅ | ✅ | ❌ | 6/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 96 | `K46_prokka_lis_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 97 | `K47_prokka_eco_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 98 | `K48_prokka_sal_fastp_unicycler` | ✅ | ✅ | ✅ | 11/7 | `none` |  |
| 99 | `K49_prokka_cam_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 100 | `K50_flaA_cam_fastp_unicycler` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 101 | `K51_staramr_cam_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 102 | `K52_mlst_lis_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 103 | `K53_mlst_eco_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 104 | `K54_mlst_sal_trimmomatic_spades` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 105 | `K55_mlst_cam_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 106 | `K56_chewbbaca_lis_trimmomatic_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 107 | `K57_chewbbaca_eco_trimmomatic_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 108 | `K58_chewbbaca_sal_trimmomatic_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 109 | `K59_abricate_lis_trimmomatic_spades` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 110 | `K60_abricate_eco_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 111 | `L01_mlst_chewbbaca_lis` | ✅ | ✅ | ❌ | 0/10 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 112 | `L02_mlst_chewbbaca_eco` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 113 | `L03_mlst_chewbbaca_sal` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 114 | `L04_mlst_abricate_lis` | ⚪ | ❌ | ❌ | 0/8 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 115 | `L05_mlst_abricate_eco` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 116 | `L06_chewbbaca_abricate_lis` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 117 | `L07_chewbbaca_prokka_lis` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 118 | `L08_chewbbaca_prokka_sal` | ✅ | ✅ | ❌ | 6/10 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 119 | `L09_mlst_prokka_eco` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 120 | `L10_mlst_prokka_sal` | ✅ | ✅ | ✅ | 11/8 | `none` |  |
| 121 | `L11_abricate_prokka_lis` | ✅ | ✅ | ✅ | 11/8 | `none` |  |
| 122 | `L12_abricate_prokka_sal` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 123 | `L13_mlst_flaA_cam` | ✅ | ✅ | ❌ | 6/8 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 124 | `L14_mlst_staramr_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 125 | `L15_flaA_staramr_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 126 | `L16_flaA_abricate_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 127 | `L17_staramr_abricate_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 128 | `L18_staramr_prokka_cam` | ✅ | ❌ | ❌ | 6/8 | `arity_error` | ERROR ~ Workflow `wf_annotation_amr:step_4AN_genes__prokka` declares 1 input cha |
| 129 | `L19_flaA_prokka_cam` | ✅ | ✅ | ❌ | 5/8 | `partial_dag` | Only 5/8 expected processes appeared in the DAG |
| 130 | `L20_mlst_prokka_lis` | ✅ | ✅ | ✅ | 11/8 | `none` |  |
| 131 | `M01_mlst+chewbbaca+abricate_lis` | ✅ | ✅ | ✅ | 11/11 | `none` |  |
| 132 | `M02_mlst+chewbbaca+prokka_sal` | ✅ | ✅ | ❌ | 0/11 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 133 | `M03_mlst+abricate+prokka_eco` | ✅ | ✅ | ✅ | 11/9 | `none` |  |
| 134 | `M04_mlst+abricate+prokka_lis` | ⚪ | ❌ | ❌ | 0/9 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 135 | `M05_mlst+flaA+staramr_cam` | ⚪ | ❌ | ❌ | 0/9 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 136 | `M06_mlst+flaA+abricate_cam` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 137 | `M07_flaA+staramr+prokka_cam` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 138 | `M08_mlst+staramr+prokka_cam` | ✅ | ✅ | ✅ | 11/9 | `none` |  |
| 139 | `M09_chewbbaca+abricate+prokka_lis` | ✅ | ✅ | ✅ | 11/11 | `none` |  |
| 140 | `M10_chewbbaca+abricate+prokka_eco` | ✅ | ✅ | ✅ | 11/11 | `none` |  |
| 141 | `N01_canonical_mlst_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 142 | `N02_canonical_mlst_eco` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 143 | `N03_canonical_mlst_sal` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 144 | `N04_canonical_mlst_cam` | ✅ | ✅ | ❌ | 3/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 145 | `N05_canonical_cgmlst_lis` | ✅ | ✅ | ❌ | 0/9 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 146 | `N06_canonical_cgmlst_eco` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 147 | `N07_canonical_cgmlst_sal` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 148 | `NA01_mlst_cam_assembly` | ✅ | ✅ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 149 | `NA02_mlst_sal_assembly` | ✅ | ✅ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 150 | `NA03_abricate_lis_assembly` | ✅ | ✅ | ❌ | 0/1 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 151 | `NA04_abricate_sal_assembly` | ✅ | ✅ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 152 | `NA05_abricate_cam_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 153 | `NA06_prokka_sal_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 154 | `NA07_prokka_cam_assembly` | ✅ | ✅ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 155 | `NA08_prokka_eco_assembly` | ✅ | ✅ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 156 | `O01_spades_lis` | ✅ | ✅ | ✅ | 5/3 | `none` |  |
| 157 | `O02_spades_sal` | ✅ | ✅ | ✅ | 5/3 | `none` |  |
| 158 | `O03_spades_cam` | ✅ | ✅ | ✅ | 5/3 | `none` |  |
| 159 | `O04_shovill_lis` | ⚪ | ❌ | ❌ | 0/3 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 160 | `O05_shovill_sal` | ✅ | ✅ | ✅ | 5/3 | `none` |  |
| 161 | `O06_shovill_cam` | ✅ | ✅ | ❌ | 0/3 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 162 | `O07_unicycler_lis` | ✅ | ✅ | ✅ | 11/3 | `none` |  |
| 163 | `O08_unicycler_eco` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 164 | `O09_unicycler_cam` | ✅ | ✅ | ✅ | 5/3 | `none` |  |
| 165 | `O10_plasmidspades_eco` | ⚪ | ❌ | ❌ | 0/3 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 166 | `P01_chopper_flye_mlst_lis` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 167 | `P02_chopper_flye_mlst_sal` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 168 | `P03_chopper_flye_mlst_eco` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 169 | `P04_chopper_flye_mlst_cam` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 170 | `P05_chopper_flye_abricate_lis` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 171 | `P06_chopper_flye_abricate_eco` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 172 | `P07_chopper_flye_abricate_sal` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 173 | `P08_chopper_flye_prokka_lis` | ✅ | ✅ | ✅ | 11/5 | `none` |  |
| 174 | `P09_chopper_flye_chewbbaca_lis` | ✅ | ✅ | ❌ | 4/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 175 | `P10_chopper_flye_chewbbaca_sal` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 176 | `Q01_kmerfinder_fastp_spades_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 177 | `Q02_kmerfinder_fastp_spades_eco` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 178 | `Q03_kmerfinder_fastp_spades_sal` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 179 | `Q04_kmerfinder_fastp_shovill_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 180 | `Q05_kmerfinder_fastp_shovill_eco` | ✅ | ✅ | ✅ | 11/7 | `none` |  |
| 181 | `Q06_kmerfinder_fastp_shovill_sal` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 182 | `Q07_mash_fastp_spades_lis` | ✅ | ✅ | ❌ | 7/7 | `none` |  |
| 183 | `Q08_mash_fastp_spades_eco` | ✅ | ✅ | ❌ | 7/7 | `none` |  |
| 184 | `Q09_mash_fastp_spades_sal` | ✅ | ✅ | ❌ | 0/7 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 185 | `Q10_mash_fastp_shovill_lis` | ✅ | ✅ | ❌ | 0/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 186 | `R01_kmerfinder_cam` | ✅ | ✅ | ✅ | 4/1 | `none` |  |
| 187 | `R02_kmerfinder_sal` | ✅ | ✅ | ❌ | 0/1 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 188 | `R03_mash_sal` | ✅ | ✅ | ❌ | 0/1 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 189 | `R04_mash_eco` | ✅ | ✅ | ✅ | 11/1 | `none` |  |
| 190 | `R05_kraken2_lis` | ⚪ | ❌ | ❌ | 0/2 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 191 | `R06_kraken2_eco` | ✅ | ✅ | ✅ | 5/2 | `none` |  |
| 192 | `R07_kraken2_sal` | ✅ | ✅ | ❌ | 0/2 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 193 | `R08_kraken2_cam` | ✅ | ✅ | ✅ | 5/2 | `none` |  |
| 194 | `S01_fastp_lis` | ✅ | ✅ | ✅ | 3/3 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 195 | `S02_fastp_sal` | ✅ | ✅ | ✅ | 5/3 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_25 |
| 196 | `S03_trimmomatic_eco` | ✅ | ✅ | ❌ | 0/3 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 197 | `S04_trimmomatic_cam` | ✅ | ✅ | ❌ | 0/3 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 198 | `S05_chopper_lis` | ⚪ | ❌ | ❌ | 0/2 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 199 | `S06_chopper_sal` | ✅ | ✅ | ❌ | 0/2 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 200 | `S07_chopper_cam` | ✅ | ✅ | ✅ | 2/2 | `none` |  |

## Step-set comparison vs ground truth

| # | id | LLM steps | GT steps | extra | missing | hallucinated |
|---|----|-----------|----------|-------|---------|--------------|
| 1 | `A01_mlst_listeria` | mlst | mlst | · | · | · |
| 2 | `A02_mlst_ecoli` | mlst | mlst | · | · | · |
| 3 | `A03_mlst_salmonella` | mlst | mlst | · | · | · |
| 4 | `A04_cgmlst_listeria` | chewbbaca | chewbbaca | · | · | · |
| 5 | `A05_cgmlst_ecoli` | chewbbaca | chewbbaca | · | · | · |
| 7 | `A07_flaa_campylobacter` | flaA | flaA | · | · | · |
| 8 | `A08_staramr_campylobacter` | spades | staramr | spades | staramr | · |
| 9 | `B01_spades_listeria` | bowtie,spades | spades | bowtie | · | · |
| 10 | `B02_shovill_ecoli` | shovill | shovill | · | · | · |
| 14 | `C01_kmerfinder` | unicycler,kmerfinder | kmerfinder | unicycler | · | · |
| 15 | `C02_mash` | mash,fastp | mash | fastp | · | · |
| 16 | `C03_kraken2` | kraken2,fastq,fastp | kraken2 | fastq,fastp | · | · |
| 17 | `D01_fastp_spades_lis` | bowtie,spades | fastp,spades | bowtie | fastp | · |
| 19 | `D03_trimmomatic_spades` | bowtie,spades | trimmomatic,spades | bowtie | trimmomatic | · |
| 20 | `D04_fastp_unicycler_sal` | fastp,unicycler | fastp,unicycler | · | · | · |
| 22 | `E01_mlst_lis` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 23 | `E02_cgmlst_lis_fastp_spades` | spades,chewbbaca,fastp | fastp,spades,chewbbaca | · | · | · |
| 24 | `E03_cgmlst_sal_fastp_spades` | chewbbaca,fastp,spades | fastp,spades,chewbbaca | · | · | · |
| 25 | `E04_cgmlst_eco_fastp_shovill` | shovill,chewbbaca,fastp | fastp,shovill,chewbbaca | · | · | · |
| 26 | `E05_flaa_cam` | spades,flaA,fastp | fastp,spades,flaA | · | · | · |
| 27 | `E06_staramr_cam` | staramr,fastp,unicycler | fastp,spades,staramr | unicycler | spades | · |
| 28 | `E07_abricate_eco` | spades,abricate,fastp | fastp,spades,abricate | · | · | · |
| 29 | `E08_prokka_lis` | fastp | fastp,spades,prokka | · | spades,prokka | · |
| 30 | `E09_mlst_eco_trimmomatic` | trimmomatic,spades,mlst | trimmomatic,spades,mlst | · | · | · |
| 31 | `E10_mlst_sal_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 32 | `E11_cgmlst_lis_shovill` | shovill,chewbbaca,fastp | fastp,shovill,chewbbaca | · | · | · |
| 33 | `E12_mlst_cam` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 34 | `E13_abricate_sal` | unicycler,abricate,fastp | fastp,spades,abricate | unicycler | spades | · |
| 35 | `E14_prokka_eco` | spades,prokka,fastp | fastp,spades,prokka | · | · | · |
| 36 | `E15_cgmlst_lis_trimmomatic` | trimmomatic,spades,chewbbaca | trimmomatic,spades,chewbbaca | · | · | · |
| 37 | `F01_abricate_assembly` | abricate | abricate | · | · | · |
| 38 | `F02_prokka_assembly` | prokka | prokka | · | · | · |
| 39 | `F03_mash_lis` | fastp,mash | mash | fastp | · | · |
| 41 | `G01_chopper_flye_lis` | chopper,flye | chopper,flye | · | · | · |
| 42 | `G02_chopper_flye_eco` | chopper,flye | chopper,flye | · | · | · |
| 43 | `H01_mlst_plus_cgmlst_lis` | spades,mlst,chewbbaca,fastp | fastp,spades,mlst,chewbbaca | · | · | · |
| 44 | `H02_mlst_plus_flaa_cam` | spades,kmerfinder,mlst,flaA,fastp | fastp,spades,mlst,flaA | kmerfinder | · | · |
| 45 | `H03_prokka_plus_abricate_eco` | fastp,spades,prokka,abricate | fastp,spades,abricate,prokka | · | · | · |
| 46 | `H04_mlst_plus_abricate_sal` | kmerfinder,bowtie,abricate,prokka,staramr,mlst,flaA,chewbbaca | fastp,spades,abricate,mlst | bowtie,kmerfinder,staramr,prokka,chewbbaca,flaA | fastp,spades | · |
| 47 | `I01_kmerfinder_fastp_spades` |  | fastp,spades,kmerfinder | · | fastp,spades,kmerfinder | · |
| 48 | `I02_mash_fastp_shovill` | fastp,mash,shovill | fastp,shovill,mash | · | · | · |
| 50 | `J02_bbnorm_downsampling` | bbnorm | bbnorm | · | · | · |
| 51 | `K01_mlst_lis_fastp_spades` | spades,mlst | fastp,spades,mlst | · | fastp | · |
| 52 | `K02_mlst_eco_fastp_spades` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 53 | `K03_mlst_sal_fastp_spades` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 54 | `K04_mlst_cam_fastp_spades` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 55 | `K05_chewbbaca_lis_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 56 | `K06_chewbbaca_eco_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 57 | `K07_chewbbaca_sal_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 58 | `K08_abricate_lis_fastp_spades` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 59 | `K09_abricate_eco_fastp_spades` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 60 | `K10_abricate_sal_fastp_spades` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 61 | `K11_abricate_cam_fastp_spades` | spades,staramr,fastp | fastp,spades,abricate | staramr | abricate | · |
| 62 | `K12_prokka_lis_fastp_spades` | ivar,pangolin | fastp,spades,prokka | ivar,pangolin | fastp,spades,prokka | · |
| 63 | `K13_prokka_eco_fastp_spades` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 64 | `K14_prokka_sal_fastp_spades` | spades,prokka,fastp | fastp,spades,prokka | · | · | · |
| 65 | `K15_prokka_cam_fastp_spades` | spades,prokka | fastp,spades,prokka | · | fastp | · |
| 66 | `K16_flaA_cam_fastp_spades` |  | fastp,spades,flaA | · | fastp,spades,flaA | · |
| 67 | `K17_staramr_cam_fastp_spades` | spades,fastp,staramr | fastp,spades,staramr | · | · | · |
| 68 | `K18_mlst_lis_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 69 | `K19_mlst_eco_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 70 | `K20_mlst_sal_fastp_shovill` | shovill,fastp,mlst | fastp,shovill,mlst | · | · | · |
| 71 | `K21_mlst_cam_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 72 | `K22_chewbbaca_lis_fastp_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 73 | `K23_chewbbaca_eco_fastp_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 74 | `K24_chewbbaca_sal_fastp_shovill` | shovill,chewbbaca,fastp | fastp,shovill,chewbbaca | · | · | · |
| 75 | `K25_abricate_lis_fastp_shovill` | fastp,spades,abricate | fastp,shovill,abricate | spades | shovill | · |
| 76 | `K26_abricate_eco_fastp_shovill` | fastp,shovill,abricate | fastp,shovill,abricate | · | · | · |
| 77 | `K27_abricate_sal_fastp_shovill` | shovill,abricate,fastp | fastp,shovill,abricate | · | · | · |
| 78 | `K28_abricate_cam_fastp_shovill` | fastp,shovill,abricate | fastp,shovill,abricate | · | · | · |
| 79 | `K29_prokka_lis_fastp_shovill` | spades,prokka,fastp | fastp,shovill,prokka | spades | shovill | · |
| 80 | `K30_prokka_eco_fastp_shovill` | fastp,shovill,prokka | fastp,shovill,prokka | · | · | · |
| 81 | `K31_prokka_sal_fastp_shovill` | fastp,shovill,prokka | fastp,shovill,prokka | · | · | · |
| 82 | `K32_prokka_cam_fastp_shovill` | fastp,shovill,prokka | fastp,shovill,prokka | · | · | · |
| 83 | `K33_flaA_cam_fastp_shovill` | fastp,shovill,flaA | fastp,shovill,flaA | · | · | · |
| 84 | `K34_staramr_cam_fastp_shovill` | shovill,staramr,fastp | fastp,shovill,staramr | · | · | · |
| 85 | `K35_mlst_lis_fastp_unicycler` | fastp,unicycler,mlst | fastp,unicycler,mlst | · | · | · |
| 86 | `K36_mlst_eco_fastp_unicycler` | fastp,unicycler,mlst | fastp,unicycler,mlst | · | · | · |
| 87 | `K37_mlst_sal_fastp_unicycler` | fastp,unicycler,mlst | fastp,unicycler,mlst | · | · | · |
| 88 | `K38_mlst_cam_fastp_unicycler` | unicycler,mlst,fastp | fastp,unicycler,mlst | · | · | · |
| 89 | `K39_chewbbaca_lis_fastp_unicycler` | unicycler,chewbbaca,fastp | fastp,unicycler,chewbbaca | · | · | · |
| 90 | `K40_chewbbaca_eco_fastp_unicycler` | unicycler,chewbbaca,fastp | fastp,unicycler,chewbbaca | · | · | · |
| 91 | `K41_chewbbaca_sal_fastp_unicycler` | fastp,unicycler,chewbbaca | fastp,unicycler,chewbbaca | · | · | · |
| 92 | `K42_abricate_lis_fastp_unicycler` | fastp,unicycler,abricate | fastp,unicycler,abricate | · | · | · |
| 93 | `K43_abricate_eco_fastp_unicycler` | fastp,unicycler,abricate | fastp,unicycler,abricate | · | · | · |
| 94 | `K44_abricate_sal_fastp_unicycler` | unicycler,abricate,fastp | fastp,unicycler,abricate | · | · | · |
| 95 | `K45_abricate_cam_fastp_unicycler` | fastp,unicycler,abricate | fastp,unicycler,abricate | · | · | · |
| 96 | `K46_prokka_lis_fastp_unicycler` | unicycler,prokka,fastp | fastp,unicycler,prokka | · | · | · |
| 97 | `K47_prokka_eco_fastp_unicycler` | fastp,unicycler,prokka | fastp,unicycler,prokka | · | · | · |
| 98 | `K48_prokka_sal_fastp_unicycler` | ivar,pangolin | fastp,unicycler,prokka | ivar,pangolin | fastp,unicycler,prokka | · |
| 99 | `K49_prokka_cam_fastp_unicycler` | fastp,unicycler,prokka | fastp,unicycler,prokka | · | · | · |
| 100 | `K50_flaA_cam_fastp_unicycler` | fastp,unicycler,flaA | fastp,unicycler,flaA | · | · | · |
| 101 | `K51_staramr_cam_fastp_unicycler` | unicycler,staramr,fastp | fastp,unicycler,staramr | · | · | · |
| 102 | `K52_mlst_lis_trimmomatic_spades` | spades,mlst,trimmomatic | trimmomatic,spades,mlst | · | · | · |
| 103 | `K53_mlst_eco_trimmomatic_spades` | trimmomatic,spades,mlst | trimmomatic,spades,mlst | · | · | · |
| 104 | `K54_mlst_sal_trimmomatic_spades` | spades,mlst,trimmomatic | trimmomatic,spades,mlst | · | · | · |
| 105 | `K55_mlst_cam_trimmomatic_spades` | trimmomatic,spades,mlst | trimmomatic,spades,mlst | · | · | · |
| 106 | `K56_chewbbaca_lis_trimmomatic_spades` | trimmomatic,spades,chewbbaca | trimmomatic,spades,chewbbaca | · | · | · |
| 107 | `K57_chewbbaca_eco_trimmomatic_spades` | trimmomatic,spades,chewbbaca | trimmomatic,spades,chewbbaca | · | · | · |
| 108 | `K58_chewbbaca_sal_trimmomatic_spades` | trimmomatic,spades,chewbbaca | trimmomatic,spades,chewbbaca | · | · | · |
| 109 | `K59_abricate_lis_trimmomatic_spades` | trimmomatic,spades,abricate | trimmomatic,spades,abricate | · | · | · |
| 110 | `K60_abricate_eco_trimmomatic_spades` | abricate,trimmomatic,spades | trimmomatic,spades,abricate | · | · | · |
| 111 | `L01_mlst_chewbbaca_lis` | spades,mlst,chewbbaca,fastp | fastp,spades,mlst,chewbbaca | · | · | · |
| 112 | `L02_mlst_chewbbaca_eco` | spades,mlst,chewbbaca,fastp | fastp,spades,mlst,chewbbaca | · | · | · |
| 113 | `L03_mlst_chewbbaca_sal` | spades,mlst,chewbbaca,fastp | fastp,spades,mlst,chewbbaca | · | · | · |
| 115 | `L05_mlst_abricate_eco` | fastp,spades,mlst,abricate | fastp,spades,abricate,mlst | · | · | · |
| 116 | `L06_chewbbaca_abricate_lis` | fastp,spades,chewbbaca,abricate | fastp,spades,abricate,chewbbaca | · | · | · |
| 117 | `L07_chewbbaca_prokka_lis` | spades,chewbbaca,prokka,fastp | fastp,spades,prokka,chewbbaca | · | · | · |
| 118 | `L08_chewbbaca_prokka_sal` | spades,chewbbaca,prokka,fastp | fastp,spades,prokka,chewbbaca | · | · | · |
| 119 | `L09_mlst_prokka_eco` | spades,prokka,mlst,fastp | fastp,spades,prokka,mlst | · | · | · |
| 120 | `L10_mlst_prokka_sal` | ivar,pangolin | fastp,spades,prokka,mlst | ivar,pangolin | fastp,spades,prokka,mlst | · |
| 121 | `L11_abricate_prokka_lis` | ivar,pangolin | fastp,spades,abricate,prokka | ivar,pangolin | fastp,spades,abricate,prokka | · |
| 122 | `L12_abricate_prokka_sal` | spades,abricate,prokka,fastp | fastp,spades,abricate,prokka | · | · | · |
| 123 | `L13_mlst_flaA_cam` | mlst,flaA,fastp,spades | fastp,spades,mlst,flaA | · | · | · |
| 124 | `L14_mlst_staramr_cam` | fastp,spades,mlst,staramr | fastp,spades,staramr,mlst | · | · | · |
| 125 | `L15_flaA_staramr_cam` | flaA,staramr,fastp,spades | fastp,spades,staramr,flaA | · | · | · |
| 126 | `L16_flaA_abricate_cam` | spades,flaA,abricate,fastp | fastp,spades,abricate,flaA | · | · | · |
| 127 | `L17_staramr_abricate_cam` | spades,staramr,abricate,fastp | fastp,spades,abricate,staramr | · | · | · |
| 128 | `L18_staramr_prokka_cam` | prokka,staramr,fastp,spades | fastp,spades,staramr,prokka | · | · | · |
| 129 | `L19_flaA_prokka_cam` | spades,prokka,flaA | fastp,spades,prokka,flaA | · | fastp | · |
| 130 | `L20_mlst_prokka_lis` | ivar,pangolin | fastp,spades,prokka,mlst | ivar,pangolin | fastp,spades,prokka,mlst | · |
| 131 | `M01_mlst+chewbbaca+abricate_lis` | mlst,chewbbaca,abricate,fastp,spades | fastp,spades,abricate,mlst,chewbbaca | · | · | · |
| 132 | `M02_mlst+chewbbaca+prokka_sal` | unicycler,mlst,chewbbaca,prokka,abricate,fastp | fastp,spades,prokka,mlst,chewbbaca | unicycler,abricate | spades | · |
| 133 | `M03_mlst+abricate+prokka_eco` | ivar,pangolin | fastp,spades,abricate,prokka,mlst | ivar,pangolin | fastp,spades,abricate,prokka,mlst | · |
| 136 | `M06_mlst+flaA+abricate_cam` | mlst,flaA,abricate,fastp,spades | fastp,spades,abricate,mlst,flaA | · | · | · |
| 137 | `M07_flaA+staramr+prokka_cam` | flaA,staramr,prokka,fastp,spades | fastp,spades,staramr,prokka,flaA | · | · | · |
| 138 | `M08_mlst+staramr+prokka_cam` | ivar,pangolin | fastp,spades,staramr,prokka,mlst | ivar,pangolin | fastp,spades,staramr,prokka,mlst | · |
| 139 | `M09_chewbbaca+abricate+prokka_lis` | chewbbaca,abricate,prokka,fastp,unicycler | fastp,spades,abricate,prokka,chewbbaca | unicycler | spades | · |
| 140 | `M10_chewbbaca+abricate+prokka_eco` | spades,chewbbaca,abricate,prokka,fastp | fastp,spades,abricate,prokka,chewbbaca | · | · | · |
| 141 | `N01_canonical_mlst_lis` | spades,mlst,fastp | fastp,spades,mlst | · | · | · |
| 142 | `N02_canonical_mlst_eco` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 143 | `N03_canonical_mlst_sal` | spades,mlst,fastp | fastp,spades,mlst | · | · | · |
| 144 | `N04_canonical_mlst_cam` | fastp,mlst | fastp,spades,mlst | · | spades | · |
| 145 | `N05_canonical_cgmlst_lis` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 146 | `N06_canonical_cgmlst_eco` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 147 | `N07_canonical_cgmlst_sal` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 148 | `NA01_mlst_cam_assembly` | mlst | mlst | · | · | · |
| 149 | `NA02_mlst_sal_assembly` | mlst | mlst | · | · | · |
| 150 | `NA03_abricate_lis_assembly` | abricate | abricate | · | · | · |
| 151 | `NA04_abricate_sal_assembly` | abricate | abricate | · | · | · |
| 152 | `NA05_abricate_cam_assembly` | abricate | abricate | · | · | · |
| 153 | `NA06_prokka_sal_assembly` | prokka | prokka | · | · | · |
| 154 | `NA07_prokka_cam_assembly` | prokka | prokka | · | · | · |
| 155 | `NA08_prokka_eco_assembly` | prokka | prokka | · | · | · |
| 156 | `O01_spades_lis` | bowtie,spades | spades | bowtie | · | · |
| 157 | `O02_spades_sal` | bowtie,spades | spades | bowtie | · | · |
| 158 | `O03_spades_cam` | bowtie,spades | spades | bowtie | · | · |
| 160 | `O05_shovill_sal` | bowtie,shovill | shovill | bowtie | · | · |
| 161 | `O06_shovill_cam` | shovill | shovill | · | · | · |
| 162 | `O07_unicycler_lis` | ivar,pangolin | unicycler | ivar,pangolin | unicycler | · |
| 163 | `O08_unicycler_eco` | fastp,unicycler | unicycler | fastp | · | · |
| 164 | `O09_unicycler_cam` | bowtie,spades | unicycler | bowtie,spades | unicycler | · |
| 166 | `P01_chopper_flye_mlst_lis` | chopper,flye,mlst | chopper,flye,mlst | · | · | · |
| 167 | `P02_chopper_flye_mlst_sal` | chopper,flye,mlst | chopper,flye,mlst | · | · | · |
| 168 | `P03_chopper_flye_mlst_eco` | chopper,flye,mlst | chopper,flye,mlst | · | · | · |
| 169 | `P04_chopper_flye_mlst_cam` | flye,mlst,chopper | chopper,flye,mlst | · | · | · |
| 170 | `P05_chopper_flye_abricate_lis` | flye,abricate,chopper | chopper,flye,abricate | · | · | · |
| 171 | `P06_chopper_flye_abricate_eco` | chopper,flye,abricate | chopper,flye,abricate | · | · | · |
| 172 | `P07_chopper_flye_abricate_sal` | flye,abricate,chopper | chopper,flye,abricate | · | · | · |
| 173 | `P08_chopper_flye_prokka_lis` | ivar,pangolin | chopper,flye,prokka | ivar,pangolin | chopper,flye,prokka | · |
| 174 | `P09_chopper_flye_chewbbaca_lis` | chopper,flye,chewbbaca | chopper,flye,chewbbaca | · | · | · |
| 175 | `P10_chopper_flye_chewbbaca_sal` | chopper,flye,chewbbaca | chopper,flye,chewbbaca | · | · | · |
| 176 | `Q01_kmerfinder_fastp_spades_lis` | fastp,spades,kmerfinder | fastp,spades,kmerfinder | · | · | · |
| 177 | `Q02_kmerfinder_fastp_spades_eco` | fastp,spades,kmerfinder | fastp,spades,kmerfinder | · | · | · |
| 178 | `Q03_kmerfinder_fastp_spades_sal` | kmerfinder,fastp,spades | fastp,spades,kmerfinder | · | · | · |
| 179 | `Q04_kmerfinder_fastp_shovill_lis` | fastp,shovill,kmerfinder | fastp,shovill,kmerfinder | · | · | · |
| 180 | `Q05_kmerfinder_fastp_shovill_eco` | ivar,pangolin | fastp,shovill,kmerfinder | ivar,pangolin | fastp,shovill,kmerfinder | · |
| 181 | `Q06_kmerfinder_fastp_shovill_sal` | kmerfinder,fastp,spades | fastp,shovill,kmerfinder | spades | shovill | · |
| 182 | `Q07_mash_fastp_spades_lis` | mash,fastp,spades | fastp,spades,mash | · | · | · |
| 183 | `Q08_mash_fastp_spades_eco` | mash,fastp,spades | fastp,spades,mash | · | · | · |
| 184 | `Q09_mash_fastp_spades_sal` | kmerfinder,spades,fastp | fastp,spades,mash | kmerfinder | mash | · |
| 185 | `Q10_mash_fastp_shovill_lis` | kmerfinder,fastp,spades | fastp,shovill,mash | spades,kmerfinder | shovill,mash | · |
| 186 | `R01_kmerfinder_cam` | fastp,kmerfinder | kmerfinder | fastp | · | · |
| 187 | `R02_kmerfinder_sal` | kmerfinder,bowtie,abricate,prokka,staramr,mlst,flaA,chewbbaca | kmerfinder | bowtie,abricate,staramr,prokka,mlst,chewbbaca,flaA | · | · |
| 188 | `R03_mash_sal` | fastp,mash | mash | fastp | · | · |
| 189 | `R04_mash_eco` | ivar,pangolin | mash | ivar,pangolin | mash | · |
| 191 | `R06_kraken2_eco` | fastp,kraken2 | kraken2 | fastp | · | · |
| 192 | `R07_kraken2_sal` | kraken2 | kraken2 | · | · | · |
| 193 | `R08_kraken2_cam` | fastp,kraken2 | kraken2 | fastp | · | · |
| 194 | `S01_fastp_lis` | fastp | fastp | · | · | · |
| 195 | `S02_fastp_sal` | fastq,fastp | fastp | fastq | · | · |
| 196 | `S03_trimmomatic_eco` | trimmomatic | trimmomatic | · | · | · |
| 197 | `S04_trimmomatic_cam` | trimmomatic | trimmomatic | · | · | · |
| 199 | `S06_chopper_sal` |  | chopper | · | chopper | · |
| 200 | `S07_chopper_cam` | chopper | chopper | · | · | · |

## Failure detail (one section per failing prompt)

### `A01_mlst_listeria` — `file_not_found`

**Prompt:** I have a Listeria monocytogenes assembly and I want to run MLST typing on it.

**Steps (LLM):** `step_4TY_MLST__mlst`
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

include { getInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.LIS.1.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `A02_mlst_ecoli` — `file_not_found`

**Prompt:** Run MLST typing on an Escherichia coli assembly.

**Steps (LLM):** `step_4TY_MLST__mlst`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.ECO.1.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `A03_mlst_salmonella` — `file_not_found`

**Prompt:** Classic MLST (PubMLST) on a Salmonella enterica assembly.

**Steps (LLM):** `step_4TY_MLST__mlst`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAL.1.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `A04_cgmlst_listeria` — `silent_no_op`

**Prompt:** cgMLST allelic profile for Listeria monocytogenes from a pre-existing assembly.

**Steps (LLM):** `step_4TY_cgMLST__chewbbaca`
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

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { parseMetadataFromFileName } from '../functions/common.nf'

// --- GLOBALS ---

def SPECIES_SCHEMA = ['listeria_monocytogenes': ['l_mono_chewie_1748_220623'], 'escherichia_coli': ['e_coli_chewie_2360_210531'], 'salmonella_enterica': ['s_enterica_chewie_3255_210531']]

def SCHEMAS = ['l_mono_chewie_1748_220623': '/schemas/Listeria_monocytogenes_Pasteur_cgMLST_2022-06-23T18_03_54.613576.zip', 'e_coli_chewie_2360_210531': '/schemas/Escherichia_coli_INNUENDO_wgMLST_2021-05-31T14_24_05.304225.zip', 's_enterica_chewie_3255_210531': '/schemas/Salmonella_enterica_INNUENDO_cgMLST_2021-05-31T20_28_21.350919.zip']

def CHEWBBACA_SINGLE_END_PARAMS = ['l_mono_chewie_1748_220623': ' --minimum-length 144 --st 0.1 --bsr 0.6 ', 'e_coli_chewie_2360_210531': ' --minimum-length 0 --st 0.01 --bsr 0.6 --genes-list /schemas/Escherichia_coli_INNUENDO_cgMLST_EFSA_filterlist.txt ', 's_enterica_chewie_3255_210531': ' --minimum-length 0 --st 0.01 --bsr 0.6 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt ']

def CHEWBBACA_PAIRED_END_PARAMS = ['l_mono_chewie_1748_220623': ' --minimum-length 144 ', 'e_coli_chewie_2360_210531': ' --minimum-length 0 --genes-list /schemas/Escherichia_coli_INNUENDO_cgMLST_EFSA_filterlist.txt ', 's_enterica_chewie_3255_210531': ' --minimum-length 0 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt ']

def STEP = '4TY_cgMLST'

def METHOD = 'chewbbaca'

def ENTRYPOINT = 'step_${STEP}__${METHOD}'

// --- INLINE PROCESSES ---

process chewbbaca {
    container 'ghcr.io/genpat-it/chewbbaca-w-chewie-schemas:2.8.5--16b816c96d'
    
    input:
    
    tuple val(riscd_input), path(assembly)
    
    val genus_species
    
    val schema
    
    
    output:
    
    path '**'
    
    path("${base}_results_statistics.tsv"), emit: stats
    
    tuple path("${base}_results_alleles.tsv"), path('schema/'), emit: alleles
    
    tuple path("${base}_results_alleles.tsv"), path("${base}_new_alleles.txt"), val(schemaName), emit: alleles_with_new
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
md = parseMetadataFromFileName(assembly.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}_${METHOD}"
schemaName = getSchema(genus_species, schema)
schemaPath = SCHEMAS.get(schemaName)
newAlleleKey = assembly.getName().replaceAll('_', '-')
speciesSpecificParams = getExtraParams(schemaName)
"""
#!/bin/bash -euo pipefail
unzip ${schemaPath} -d schema > /dev/null
chmod -R 777 schema
mkdir input && cp ${assembly} input/
chewBBACA.py AlleleCall -i input -g schema -o results --cpu ${task.cpus} --force-continue --verbose ${speciesSpecificParams}
grep "${newAlleleKey}" schema/*.fasta -A1 -h | grep -v "\-\-" > ${base}_new_alleles.txt || echo "no INF alleles found"
mv results/*/results_alleles.tsv ${base}_results_alleles.tsv
mv results/*/results_contigsInfo.tsv ${base}_results_contigsInfo.tsv
mv results/*/results_statistics.tsv ${base}_results_statistics.tsv
"""
    """
}

process chewbbaca_check {
    container 'quay.io/biocontainers/python:3.9'
    
    input:
    
    path(chewbbacaStats)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    path("${base}_import_chewbbaca_check.csv"), emit: check
    
    
    script:
    """
md = parseMetadataFromFileName(chewbbacaStats.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
"""
/scripts/chewieCheck.py --stat ${chewbbacaStats} > ${base}_import_chewbbaca_check.csv
"""
    """
}

process hashing {
    container 'ghcr.io/genpat-it/hashing:1.0--29180a232f'
    
    input:
    
    tuple path(chewbbaca_result), path(schema_path)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
md = parseMetadataFromFileName(chewbbaca_result.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
"""
mask_matrix.py -i ${chewbbaca_result} -o masked_results.tsv
alleleprofile_hasher.py -p masked_results.tsv -d ${schema_path} -o ./_hashed_results.tsv
rm -Rf ${schema_path}/*
"""
    """
}

// --- SUB WORKFLOWS ---

workflow step_4TY_cgMLST__chewbbaca {
    
    take:
        
        assembly
        
        genus_species
        
        schema
        
    
    main:
        chewbbaca_result = chewbbaca(assembly, genus_species, schema)
        hashing(chewbbaca_result.alleles)
        chewbbaca_check(chewbbaca_result.stats).check
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_cgMLST__chewbbaca(getInput(), param('genus_species'), optionalOrDefault('schema', ''))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `A05_cgmlst_ecoli` — `silent_no_op`

**Prompt:** cgMLST allelic profile on an Escherichia coli assembly.

**Steps (LLM):** `step_4TY_cgMLST__chewbbaca`
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

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'

// --- GLOBALS ---

def SPECIES_SCHEMA = {'listeria_monocytogenes': ['l_mono_chewie_1748_220623'], 'escherichia_coli': ['e_coli_chewie_2360_210531'], 'salmonella_enterica': ['s_enterica_chewie_3255_210531']}

def SCHEMAS = {'l_mono_chewie_1748_220623': '/schemas/Listeria_monocytogenes_Pasteur_cgMLST_2022-06-23T18_03_54.613576.zip', 'e_coli_chewie_2360_210531': '/schemas/Escherichia_coli_INNUENDO_wgMLST_2021-05-31T14_24_05.304225.zip', 's_enterica_chewie_3255_210531': '/schemas/Salmonella_enterica_INNUENDO_cgMLST_2021-05-31T20_28_21.350919.zip'}

def CHEWBBACA_SINGLE_END_PARAMS = {'l_mono_chewie_1748_220623': ' --minimum-length 144 --st 0.1 --bsr 0.6 ', 'e_coli_chewie_2360_210531': ' --minimum-length 0 --st 0.01 --bsr 0.6 --genes-list /schemas/Escherichia_coli_INNUENDO_cgMLST_EFSA_filterlist.txt ', 's_enterica_chewie_3255_210531': ' --minimum-length 0 --st 0.01 --bsr 0.6 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt '}

def CHEWBBACA_PAIRED_END_PARAMS = {'l_mono_chewie_1748_220623': ' --minimum-length 144 ', 'e_coli_chewie_2360_210531': ' --minimum-length 0 --genes-list /schemas/Escherichia_coli_INNUENDO_cgMLST_EFSA_filterlist.txt ', 's_enterica_chewie_3255_210531': ' --minimum-length 0 --genes-list /schemas/Salmonella_enterica_INNUENDO_cgMLST_EFSA_filterlist.txt '}

// --- INLINE PROCESSES ---

process chewbbaca {
    container 'ghcr.io/genpat-it/chewbbaca-w-chewie-schemas:2.8.5--16b816c96d'
    
    input:
    
    tuple val(riscd_input), path(assembly)
    
    val genus_species
    
    val schema
    
    
    output:
    
    path '**'
    
    path('${base}_results_statistics.tsv'), emit: stats
    
    tuple path('${base}_results_alleles.tsv'), path('schema/'), emit: alleles
    
    tuple path('${base}_results_alleles.tsv'), path('${base}_new_alleles.txt'), val(schemaName), emit: alleles_with_new
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
#!/bin/bash -euo pipefail
unzip ${schemaPath} -d schema > /dev/null
chmod -R 777 schema
mkdir input && cp ${assembly} input/
chewBBACA.py AlleleCall -i input -g schema -o results --cpu ${task.cpus} --force-continue --verbose ${speciesSpecificParams}
grep "${newAlleleKey}" schema/*.fasta -A1 -h | grep -v "\-\-" > ${base}_new_alleles.txt || echo "no INF alleles found"
mv results/*/results_alleles.tsv ${base}_results_alleles.tsv
mv results/*/results_contigsInfo.tsv ${base}_results_contigsInfo.tsv
mv results/*/results_statistics.tsv ${base}_results_statistics.tsv
    """
}

process chewbbaca_check {
    container 'quay.io/biocontainers/python:3.9'
    
    input:
    
    path(chewbbacaStats)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    path('${base}_import_chewbbaca_check.csv'), emit: check
    
    
    script:
    """
/scripts/chewieCheck.py --stat ${chewbbacaStats} > ${base}_import_chewbbaca_check.csv
    """
}

process hashing {
    container 'ghcr.io/genpat-it/hashing:1.0--29180a232f'
    
    input:
    
    tuple path(chewbbaca_result), path(schema_path)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
mask_matrix.py -i ${chewbbaca_result} -o masked_results.tsv
alleleprofile_hasher.py -p masked_results.tsv -d ${schema_path} -o ./_hashed_results.tsv
rm -Rf ${schema_path}/*
    """
}

// --- SUB WORKFLOWS ---

workflow step_4TY_cgMLST__chewbbaca {
    
    take:
        
        assembly
        
        genus_species
        
        schema
        
    
    main:
        chewbbaca_result = chewbbaca(assembly, genus_species, schema)
        hashing(chewbbaca_result.alleles)
        chewbbaca_check(chewbbaca_result.stats).check
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_cgMLST__chewbbaca(getInput(), param('genus_species'), optionalOrDefault('schema', ''))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `A06_cgmlst_salmonella` — `no_code`

**Prompt:** Generate cgMLST allelic profiles starting from a Salmonella enterica assembly.

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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `A07_flaa_campylobacter` — `silent_no_op`

**Prompt:** Run flaA typing on a Campylobacter assembly.

**Steps (LLM):** `step_4TY_flaA__flaA`
**Steps (GT):**  `step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
workflow {
    step_4TY_flaA__flaA(getInput(), param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_flaA__flaA {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        mlst_flaa(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    assembly = getCampylobacterAssembly()
    flaA_typing = step_4TY_flaA__flaA(assembly, 'campylobacter')
    flaA_typing.view()
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `B02_shovill_ecoli` — `file_not_found`

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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

// --- ENTRYPOINT ---
workflow {
    step_2AS_denovo__shovill(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.ECO.3.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `B03_unicycler_salmonella` — `no_code`

**Prompt:** Assemble a Salmonella enterica genome with Unicycler from Illumina paired-end reads.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `B04_plasmidspades` — `no_code`

**Prompt:** I want to assemble plasmids only from Illumina paired-end reads using plasmidSPAdes.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_2AS_denovo__plasmidspades`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_2AS_denovo__plasmidspades } from '../steps/step_2AS_denovo__plasmidspades'
workflow {
    step_2AS_denovo__plasmidspades(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `B05_metaspades` — `no_code`

**Prompt:** Run metagenomic assembly with metaSPAdes on paired-end Illumina reads from an environmental sample.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_2MG_denovo__metaspades`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_2MG_denovo__metaspades } from '../steps/step_2MG_denovo__metaspades'
workflow {
    step_2MG_denovo__metaspades(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `C02_mash` — `none`

**Prompt:** Run Mash sketch-based species identification on paired-end Illumina reads.

**Steps (LLM):** `step_3TX_species__mash, step_1PP_trimming__fastp`
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

include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_mash_species_identification {
    
    take:
        
        trimmed
        
    
    main:
        step_3TX_species__mash(trimmed)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_mash_species_identification(trimmed)
}
```
**Error excerpt:**
```
(no excerpt)
```

### `D01_fastp_spades_lis` — `partial_dag`

**Prompt:** From Illumina paired-end FASTQ of Listeria monocytogenes: trim with fastp and assemble with SPAdes.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { extractKey } from '../functions/common.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

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
    module_denovo(getSingleInput(), getHost())
}
```
**Error excerpt:**
```
Only 5/6 expected processes appeared in the DAG
```

### `D02_fastp_shovill_eco` — `no_code`

**Prompt:** Trim Illumina paired reads with fastp then assemble with Shovill (Escherichia coli).

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
}
```
**LLM-generated (failed):**
```groovy

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `D03_trimmomatic_spades` — `silent_no_op`

**Prompt:** Pipeline: trim with Trimmomatic, assemble with SPAdes. Illumina paired-end.

**Steps (LLM):** `step_1PP_filtering__bowtie, step_2AS_denovo__spades`
**Steps (GT):**  `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
workflow {
    trimmed   = step_1PP_trimming__trimmomatic(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_1PP_filtering__bowtie } from '../steps/step_1PP_filtering__bowtie'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { extractKey } from '../functions/common.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_filtered_denovo {
    
    take:
        
        reads
        
        reference
        
    
    main:
        reads.cross(reference) { extractKey(it) }.multiMap {
            reads: it[0] // riscd, reads
            refs:  it[1][1..3] // riscd, code, path
        }.set { readsAndReferences }

        filtered = step_1PP_filtering__bowtie(readsAndReferences.reads, readsAndReferences.refs)
        assembled = step_2AS_denovo__spades(filtered)
    
    emit:
        
        assembled
        
        filtered
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_filtered_denovo(getSingleInput(), getReference('fa'))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `D05_fastp_spades_cam` — `no_code`

**Prompt:** Trim and de novo assembly (fastp + SPAdes) for a paired-end Illumina Campylobacter sample.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
}
```
**LLM-generated (failed):**
```groovy

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `E02_cgmlst_lis_fastp_spades` — `file_not_found`

**Prompt:** cgMLST allelic profile for Listeria monocytogenes from paired Illumina FASTQ (fastp + SPAdes + chewbbaca).

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_cgmlst_listeria {
    
    take:
        
        trimmed
        
        genus_species
        
        schema
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            genus_species: genus_species
            schema: schema
        }.set { prep }

        assembly = step_2AS_denovo__spades(prep.trimmed)
        step_4TY_cgMLST__chewbbaca(assembly.assembled, genus_species, schema)
    
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
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast

        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_cgMLST__chewbbaca {
    
    take:
        
        assembly
        
        genus_species
        
        schema
        
    
    main:
        chewbbaca_result = chewbbaca(assembly, genus_species, schema)
        hashing(chewbbaca_result.alleles)
        chewbbaca_check(chewbbaca_result.stats).check
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_cgmlst_listeria(trimmed, 'Listeria monocytogenes', 'l_mono_chewie_1748_220623')
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.LIS.6.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `E04_cgmlst_eco_fastp_shovill` — `silent_no_op`

**Prompt:** E. coli cgMLST typing from Illumina paired FASTQ using fastp + Shovill + chewbbaca.

**Steps (LLM):** `step_2AS_denovo__shovill, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp`
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

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_cgmlst {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
        }.set { trAndRef }

        assembly = step_2AS_denovo__shovill(trAndRef.trimmed).assembly

        step_4TY_cgMLST__chewbbaca(assembly, 'escherichia_coli', 'e_coli_chewie_2360_210531')
    
}

workflow wf_ecoli_cgmlst {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
        }.set { trAndRef }

        assembly = step_2AS_denovo__shovill(trAndRef.trimmed).assembly

        step_4TY_cgMLST__chewbbaca(assembly, 'escherichia_coli', 'e_coli_chewie_2360_210531')
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    wf_ecoli_cgmlst(trimmed)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `E08_prokka_lis` — `file_not_found`

**Prompt:** Annotate a Listeria monocytogenes genome with Prokka, starting from paired Illumina FASTQ (trim + assembly + Prokka).

**Steps (LLM):** `step_1PP_trimming__fastp`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_annotation {
    
    take:
        
        trimmed
        
    
    main:
        denovo(trimmed)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
        prokka(assembled.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_listeria_annotation(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.LIS.7.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `E14_prokka_eco` — `arity_error`

**Prompt:** Annotate an E. coli assembly with Prokka, starting from paired Illumina reads.

**Steps (LLM):** `step_2AS_denovo__spades, step_4AN_genes__prokka, step_1PP_trimming__fastp`
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def PROKKA_KINGDOM = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_ecoli_annotation {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ referenceRiscd, referenceCode, file(referencePath) ]
        }.set { trAndRef }

        assembly_out = step_2AS_denovo__spades(trAndRef.trimmed)
        assembly_out.assembled.multiMap {
            assembly: it
            kingdom: PROKKA_KINGDOM
            riscd_ref: '-'
            refid: '-'
            refpath: getEmpty()
        }.set { prokkaIn }

        step_4AN_genes__prokka(prokkaIn)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_ecoli_annotation(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_ecoli_annotation:step_4AN_genes__prokka` declares 1 input channels but 5 were given
```

### `F01_abricate_assembly` — `file_not_found`

**Prompt:** Run ABRicate to detect resistance genes on a pre-existing bacterial assembly.

**Steps (LLM):** `step_4AN_AMR__abricate`
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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4AN_AMR__abricate {
    
    take:
        
        assembly
        
    
    main:
        abricate_out = abricate(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4AN_AMR__abricate(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAM.2.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `F02_prokka_assembly` — `file_not_found`

**Prompt:** Annotate a bacterial genome assembly with Prokka.

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

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4AN_genes__prokka {
    
    take:
        
        assembly
        
    
    main:
        assembly.multiMap {
            riscd_input: it[0]
            scaffolds200: it[1]
            kingdom: it[2]
            riscd_ref: it[3]
            reference: it[4]
            gb: it[5]
        }.set { prokka_input }

        prokka(prokka_input.riscd_input, prokka_input.scaffolds200, prokka_input.kingdom, prokka_input.riscd_ref, prokka_input.reference, prokka_input.gb)
    
}

// --- ENTRYPOINT ---
workflow {
    assembly = getAssembly()
    step_4AN_genes__prokka(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAM.3.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `F03_mash_lis` — `file_not_found`

**Prompt:** Sketch-based species ID with Mash on a Listeria isolate (paired Illumina).

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__mash`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_3TX_species__mash {
    
    take:
        
        reads
        
    
    main:
        mash(reads)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    step_3TX_species__mash(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.LIS.A.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `F04_kraken2_unknown` — `no_code`

**Prompt:** Classify an unknown bacterial isolate (paired Illumina FASTQ) using Kraken2.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `G02_chopper_flye_eco` — `silent_no_op`

**Prompt:** Nanopore Escherichia coli pipeline: chopper + flye.

**Steps (LLM):** `step_1PP_trimming__chopper, step_2AS_denovo__flye`
**Steps (GT):**  `step_1PP_trimming__chopper, step_2AS_denovo__flye`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'
include { step_2AS_denovo__flye } from '../steps/step_2AS_denovo__flye'
workflow {
    trimmed   = step_1PP_trimming__chopper(getSingleInput()).trimmed
    assembled = step_2AS_denovo__flye(trimmed).assembly
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_1PP_trimming__chopper {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = chopper(rawreads).trimmed
        nanoplot(trimmed)
    
    emit:
        
        trimmed
        
    
}

workflow step_2AS_denovo__flye {
    
    take:
        
        reads
        
    
    main:
        contigs = flye(reads).assembly
        quast(contigs)
    
    emit:
        
        assembly = contigs
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__chopper(rawreads).trimmed
    assembly = step_2AS_denovo__flye(trimmed).assembly
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `H02_mlst_plus_flaa_cam` — `missing_param`

**Prompt:** Comprehensive Campylobacter typing from paired Illumina FASTQ: MLST + flaA.

**Steps (LLM):** `step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_1PP_trimming__fastp`
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

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def genus_species = 'Campylobacter'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_typing {
    
    take:
        
        trimmed
        
    
    main:
        assembled = step_2AS_denovo__spades(trimmed).assembled

        step_3TX_species__kmerfinder(assembled)
        step_4TY_MLST__mlst(assembled)
        step_4TY_flaA__flaA(assembled, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_campylobacter_typing(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `H03_prokka_plus_abricate_eco` — `file_not_found`

**Prompt:** E. coli pipeline from Illumina paired FASTQ: trim, assemble, annotate with Prokka and screen AMR with ABRicate.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka, step_4AN_AMR__abricate`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_genes__prokka(assembled)
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

def fastp_container = 'ghcr.io/genpat-it/fastp:0.23.2--16b816c96d'

def spades_container = 'ghcr.io/genpat-it/spades:3.15.5--16b816c96d'

def prokka_container = 'ghcr.io/genpat-it/prokka:1.14.6--16b816c96d'

def abricate_container = 'staphb/abricate:1.0.0'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4AN_genes__prokka {
    
    take:
        
        data
        
    
    main:
        prokka(data)
    
}

workflow step_4AN_AMR__abricate {
    
    take:
        
        data
        
    
    main:
        abricate(data)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    step_4AN_genes__prokka(assembly)
    step_4AN_AMR__abricate(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.ECO.C.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `H04_mlst_plus_abricate_sal` — `missing_param`

**Prompt:** Salmonella enterica: MLST typing and AMR screening with ABRicate from paired Illumina FASTQ.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

def referenceCode = 'NC_045512.2'

def referencePath = "${params.assets_dir}/module_covid_emergency/NC_045512.fasta"

def referenceRiscd = '220308-020220308005121273-2AS_import-external'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
        // [REMOVED BY PLAN] assigned_species = step_3TX_species__kmerfinder(assembly).assigned_species

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

### `I01_kmerfinder_fastp_spades` — `file_not_found`

**Prompt:** Identify the species with KmerFinder, in parallel trim with fastp and assemble with SPAdes (Illumina paired).

**Steps (LLM):** `(none)`
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

include { extractKey } from '../functions/common.nf'

include { getInput; getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_species_identification {
    
    take:
        
        data
        
    
    main:
        kmerfinder(data);
        assigned_species = kmerfinder.out.check.map { [ it[0], getCalculatedSpecies(it[1]), getBacterialReferencePath(it[1]) ] }
    
    emit:
        
        assigned_species
        
    
}

workflow wf_read_preprocessing {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = fastp(rawreads).trimmed;
        fastqc(trimmed);
        readsCheckInput = rawreads.cross(trimmed) { extractKey(it) }.multiMap {
          rawreads: it[0]
          trimmed: it[1]
        };
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed);
        assembly_filter(denovo(trimmed).out.scaffolds).fasta | quast;
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    wf_species_identification(getInput());
    wf_read_preprocessing(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.UNK.5.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
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

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_species_sketch_assembly {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        step_3TX_species__mash(trimmed)

        assembly = step_2AS_denovo__shovill(trimmed).assembly
    
}

// --- ENTRYPOINT ---
workflow {
    wf_species_sketch_assembly(getSingleInput())
}
```
**Error excerpt:**
```
(no excerpt)
```

### `J01_mobsuite_plasmid` — `no_code`

**Prompt:** Detect and reconstruct plasmids from paired Illumina FASTQ using MOB-suite.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_4TY_plasmid__mobsuite`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_4TY_plasmid__mobsuite } from '../steps/step_4TY_plasmid__mobsuite'
workflow {
    step_4TY_plasmid__mobsuite(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `J02_bbnorm_downsampling` — `silent_no_op`

**Prompt:** Read normalization / downsampling of paired Illumina FASTQ with BBnorm at k=25, target depth 100x.

**Steps (LLM):** `step_1PP_downsampling__bbnorm`
**Steps (GT):**  `step_1PP_downsampling__bbnorm`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_downsampling__bbnorm } from '../steps/step_1PP_downsampling__bbnorm'
workflow {
    step_1PP_downsampling__bbnorm(getSingleInput(), param('k'), param('target'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { parseMetadataFromFileName } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def k = 25

def target = 100

// --- INLINE PROCESSES ---

process bbnorm {
    container 'quay.io/biocontainers/bbmap:39.01--h5c4e2a8_0'
    
    input:
    
    tuple val(riscd_input), path(reads)
    
    val(k)
    
    val(target)
    
    
    output:
    
    path '*'
    
    path '{*.sh,*.log}', hidden: true
    
    
    script:
    """
(r1,r2) = reads
md = parseMetadataFromFileName(r1.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}_bbnorm_k${k}_t${target}"
javaHeapLimit = ((params.max_memory as nextflow.util.MemoryUnit).getMega() * 0.85) as int
"""
bbnorm.sh \
  in=${r1} \
  in2=${r2} \
  out=${base}_R1.fastq.gz \
  out2=${base}_R2.fastq.gz \
  hist=${base}.hist \
  k=${k} \
  target=${target} \
  -Xmx${javaHeapLimit}m
"""
    """
}

// --- SUB WORKFLOWS ---

workflow step_1PP_downsampling__bbnorm {
    
    take:
        
        reads
        
        k
        
        target
        
    
    main:
        bbnorm(reads, k, target)
    
}

// --- ENTRYPOINT ---
workflow {
    step_1PP_downsampling__bbnorm(getSingleInput(), k, target)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `K01_mlst_lis_fastp_spades` — `partial_dag`

**Prompt:** MLST typing on Listeria monocytogenes from paired-end Illumina FASTQ (fastp + spades + mlst).

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst`
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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_mlst_typing {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ referenceRiscd, referenceCode, file(referencePath) ]
        }.set { trAndRef }

        assembly = step_2AS_denovo__spades(trAndRef.trimmed)
        step_4TY_MLST__mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_mlst_typing(getSingleInput())
}
```
**Error excerpt:**
```
Only 4/7 expected processes appeared in the DAG
```

### `K05_chewbbaca_lis_fastp_spades` — `file_not_found`

**Prompt:** cgMLST allelic profiling on Listeria monocytogenes from paired-end Illumina FASTQ (fastp + spades + chewbbaca).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def SPECIES_SCHEMA = ['l_mono_chewie_1748_220623']

def SCHEMAS = ['/schemas/Listeria_monocytogenes_Pasteur_cgMLST_2022-06-23T18_03_54.613576.zip']

def CHEWBBACA_PAIRED_END_PARAMS = ['l_mono_chewie_1748_220623': ' --minimum-length 144 ']

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_cgMLST__chewbbaca {
    
    take:
        
        assembly
        
        genus_species
        
        schema
        
    
    main:
        chewbbaca_result = chewbbaca(assembly, genus_species, schema)
        hashing(chewbbaca_result.alleles)
        chewbbaca_check(chewbbaca_result.stats).check
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    step_4TY_cgMLST__chewbbaca(assembly, 'listeria_monocytogenes', 'l_mono_chewie_1748_220623')
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.LIS.101.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K10_abricate_sal_fastp_spades` — `file_not_found`

**Prompt:** ABRicate AMR screening on Salmonella enterica from paired-end Illumina FASTQ (fastp + spades + abricate).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4AN_AMR__abricate {
    
    take:
        
        data
        
    
    main:
        abricate(data)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembled = step_2AS_denovo__spades(trimmed)
    step_4AN_AMR__abricate(assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAL.102.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K14_prokka_sal_fastp_spades` — `file_not_found`

**Prompt:** Prokka annotation on Salmonella enterica from paired-end Illumina FASTQ (fastp + spades + prokka).

**Steps (LLM):** `step_2AS_denovo__spades, step_4AN_genes__prokka, step_1PP_trimming__fastp`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_annotation {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ referenceRiscd, referenceCode, file(referencePath) ]
        }.set { trAndRef }

        spades_out = step_2AS_denovo__spades(trAndRef.trimmed)
        step_4AN_genes__prokka(spades_out.assembled)
    
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
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4AN_genes__prokka {
    
    take:
        
        data
        
    
    main:
        prokka(data)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_salmonella_annotation(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAL.103.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K15_prokka_cam_fastp_spades` — `partial_dag`

**Prompt:** Prokka annotation on Campylobacter jejuni from paired-end Illumina FASTQ (fastp + spades + prokka).

**Steps (LLM):** `step_2AS_denovo__spades, step_4AN_genes__prokka`
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_prokka_annotation {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ referenceRiscd, referenceCode, file(referencePath) ]
        }.set { trAndRef }

        spades_out = step_2AS_denovo__spades(trAndRef.trimmed)
        step_4AN_genes__prokka(spades_out.assembled.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
    
}

// --- ENTRYPOINT ---
workflow {
    wf_prokka_annotation(getSingleInput())
}
```
**Error excerpt:**
```
Only 4/7 expected processes appeared in the DAG
```

### `K16_flaA_cam_fastp_spades` — `file_not_found`

**Prompt:** flaA typing on Campylobacter jejuni from paired-end Illumina FASTQ (fastp + spades + flaA).

**Steps (LLM):** `(none)`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_flaA_typing {
    
    take:
        
        assembly
        
    
    main:
        assembly.multiMap {
            assembly: it
            genus_species: 'Campylobacter jejuni'
        }.set { flaA_input }

        mlst_flaa(flaA_input.assembly, flaA_input.genus_species)
    
}

workflow wf_assembly {
    
    take:
        
        trimmed
        
    
    main:
        denovo(trimmed)
        assembly_filter(denovo.out.scaffolds).fasta | quast

        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow wf_trimming {
    
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

// --- ENTRYPOINT ---
workflow {
    trimmed = wf_trimming(getSingleInput()).trimmed
    assembled = wf_assembly(trimmed).assembled
    wf_flaA_typing(assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.CAM.103.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K17_staramr_cam_fastp_spades` — `file_not_found`

**Prompt:** staramr AMR profiling on Campylobacter jejuni from paired-end Illumina FASTQ (fastp + spades + staramr).

**Steps (LLM):** `step_2AS_denovo__spades, step_1PP_trimming__fastp, step_4AN_AMR__staramr`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__staramr(assembled, param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_denovo {
    
    take:
        
        trimmedReads
        
    
    main:
        assembled = step_2AS_denovo__spades(trimmedReads)
    
    emit:
        
        assembled
        
    
}

workflow step_4AN_AMR__staramr {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        staramr(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembled = module_denovo(trimmed)
    step_4AN_AMR__staramr(assembled, 'Campylobacter jejuni')
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.CAM.104.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K18_mlst_lis_fastp_shovill` — `file_not_found`

**Prompt:** MLST typing on Listeria monocytogenes from paired-end Illumina FASTQ (fastp + shovill + mlst).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__shovill(trimmed)
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.LIS.104.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K20_mlst_sal_fastp_shovill` — `file_not_found`

**Prompt:** MLST typing on Salmonella enterica from paired-end Illumina FASTQ (fastp + shovill + mlst).

**Steps (LLM):** `step_2AS_denovo__shovill, step_1PP_trimming__fastp, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_wgs_bacteria {
    
    take:
        
        trimmedReads
        
    
    main:
        step_2AS_denovo__shovill(trimmedReads)

        assembly = step_2AS_denovo__shovill.out
    
    emit:
        
        assembly
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    module_wgs_bacteria(trimmed)

    step_4TY_MLST__mlst(module_wgs_bacteria.assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAL.104.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K21_mlst_cam_fastp_shovill` — `file_not_found`

**Prompt:** MLST typing on Campylobacter jejuni from paired-end Illumina FASTQ (fastp + shovill + mlst).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__shovill(trimmed)
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.CAM.105.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K24_chewbbaca_sal_fastp_shovill` — `file_not_found`

**Prompt:** cgMLST allelic profiling on Salmonella enterica from paired-end Illumina FASTQ (fastp + shovill + chewbbaca).

**Steps (LLM):** `step_2AS_denovo__shovill, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp`
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

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def genus_species = 'Salmonella enterica'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_cgmlst_salmonella {
    
    take:
        
        trimmed
        
    
    main:
        assembly = step_2AS_denovo__shovill(trimmed).assembly
        step_4TY_cgMLST__chewbbaca(assembly, genus_species, null)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_cgmlst_salmonella(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAL.105.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K34_staramr_cam_fastp_shovill` — `file_not_found`

**Prompt:** staramr AMR profiling on Campylobacter jejuni from paired-end Illumina FASTQ (fastp + shovill + staramr).

**Steps (LLM):** `step_2AS_denovo__shovill, step_4AN_AMR__staramr, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4AN_AMR__staramr`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__shovill(trimmed).assembly
    step_4AN_AMR__staramr(assembled, param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_amr {
    
    take:
        
        trimmed
        
    
    main:
        assembly = step_2AS_denovo__shovill(trimmed).assembly
        step_4AN_AMR__staramr(assembly, 'Campylobacter jejuni')
    
    emit:
        
        assembly
        
    
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
        assembly = contigs
    
    emit:
        
        assembly
        
    
}

workflow step_4AN_AMR__staramr {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        staramr(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_campylobacter_amr(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.CAM.109.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K36_mlst_eco_fastp_unicycler` — `file_not_found`

**Prompt:** MLST typing on Escherichia coli from paired-end Illumina FASTQ (fastp + unicycler + mlst).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__unicycler, step_4TY_MLST__mlst`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__unicycler, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__unicycler(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_assemble_mlst {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembled = step_2AS_denovo__unicycler(trimmed).assembled
        step_4TY_MLST__mlst(assembled)
    
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

workflow step_2AS_denovo__unicycler {
    
    take:
        
        data
        
    
    main:
        unicycler(data).scaffolds
        assembly_filter(unicycler.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_trim_assemble_mlst(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.ECO.108.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K41_chewbbaca_sal_fastp_unicycler` — `file_not_found`

**Prompt:** cgMLST allelic profiling on Salmonella enterica from paired-end Illumina FASTQ (fastp + unicycler + chewbbaca).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__unicycler, step_4TY_cgMLST__chewbbaca`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__unicycler, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__unicycler(trimmed).assembled
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

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

// --- GLOBALS ---

def genus_species = 'Salmonella enterica'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trimming_and_assembly {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembled = step_2AS_denovo__unicycler(trimmed).assembled
    
    emit:
        
        assembled
        
    
}

workflow wf_cgmlst_profiling {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        step_4TY_cgMLST__chewbbaca(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    wf_trimming_and_assembly(rawreads).assembled.cross(genus_species).map { [ it[0], it[1] ] }.set { prepared }
    wf_cgmlst_profiling(prepared.assembly, prepared.genus_species)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAL.109.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K45_abricate_cam_fastp_unicycler` — `file_not_found`

**Prompt:** ABRicate AMR screening on Campylobacter jejuni from paired-end Illumina FASTQ (fastp + unicycler + abricate).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__unicycler, step_4AN_AMR__abricate`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_trim_and_assemble {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
        assembled = step_2AS_denovo__unicycler(trimmed).assembled
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    wf_trim_and_assemble(rawreads)
    step_4AN_AMR__abricate(wf_trim_and_assemble.assembled)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.CAM.111.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K50_flaA_cam_fastp_unicycler` — `file_not_found`

**Prompt:** flaA typing on Campylobacter jejuni from paired-end Illumina FASTQ (fastp + unicycler + flaA).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__unicycler, step_4TY_flaA__flaA`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__unicycler, step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__unicycler(trimmed).assembled
    step_4TY_flaA__flaA(assembled, param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_2AS_denovo__unicycler {
    
    take:
        
        data
        
    
    main:
        unicycler(data).scaffolds
        assembly_filter(unicycler.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_flaA__flaA {
    
    take:
        
        assembly
        
        genus_species
        
    
    main:
        mlst_flaa(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembled = step_2AS_denovo__unicycler(trimmed)
    step_4TY_flaA__flaA(assembled, 'campylobacter')
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.CAM.113.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K54_mlst_sal_trimmomatic_spades` — `file_not_found`

**Prompt:** MLST typing on Salmonella enterica from paired-end Illumina FASTQ (trimmomatic + spades + mlst).

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst, step_1PP_trimming__trimmomatic`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_mlst_typing {
    
    take:
        
        trimmed
        
    
    main:
        assembled = step_2AS_denovo__spades(trimmed).assembled
        step_4TY_MLST__mlst(assembled)
    
}

workflow step_1PP_trimming__trimmomatic {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = trimmomatic(rawreads).fastq
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
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__trimmomatic(getSingleInput()).trimmed
    wf_mlst_typing(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAL.112.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K59_abricate_lis_trimmomatic_spades` — `file_not_found`

**Prompt:** ABRicate AMR screening on Listeria monocytogenes from paired-end Illumina FASTQ (trimmomatic + spades + abricate).

**Steps (LLM):** `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades, step_4AN_AMR__abricate`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_1PP_trimming__trimmomatic {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = trimmomatic(rawreads).fastq;
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
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4AN_AMR__abricate {
    
    take:
        
        data
        
    
    main:
        abricate(data)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__trimmomatic(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    step_4AN_AMR__abricate(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.LIS.114.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `L01_mlst_chewbbaca_lis` — `file_not_found`

**Prompt:** From paired Illumina FASTQ of Listeria monocytogenes: trim with fastp, assemble with SPAdes, then run mlst and chewbbaca in parallel.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca, step_1PP_trimming__fastp`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_typing {
    
    take:
        
        trimmed
        
    
    main:
        assembled = step_2AS_denovo__spades(trimmed).assembled
        step_4TY_MLST__mlst(assembled)
        step_4TY_cgMLST__chewbbaca(assembled, 'Listeria monocytogenes', 'l_mono_chewie_1748_220623')
    
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
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

workflow step_4TY_cgMLST__chewbbaca {
    
    take:
        
        assembly
        
        genus_species
        
        schema
        
    
    main:
        chewbbaca_result = chewbbaca(assembly, genus_species, schema)
        hashing(chewbbaca_result.alleles)
        chewbbaca_check(chewbbaca_result.stats).check
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    wf_listeria_typing(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.LIS.115.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `L04_mlst_abricate_lis` — `no_code`

**Prompt:** From paired Illumina FASTQ of Listeria monocytogenes: trim with fastp, assemble with SPAdes, then run mlst and abricate in parallel.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `L08_chewbbaca_prokka_sal` — `file_not_found`

**Prompt:** From paired Illumina FASTQ of Salmonella enterica: trim with fastp, assemble with SPAdes, then run chewbbaca and prokka in parallel.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca, step_4AN_genes__prokka, step_1PP_trimming__fastp`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { extractKey } from '../functions/common.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def genus_species = 'Salmonella enterica'

def schema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_analysis {
    
    take:
        
        trimmed
        
    
    main:
        assembled = step_2AS_denovo__spades(trimmed)

        assembled.cross(genus_species) { extractKey(it) }
            .cross(schema) { extractKey(it) }
            .multiMap {
                assembly: it[0]
                genus_species: it[1]
                schema: it[2]
            }.set { prep }

        step_4TY_cgMLST__chewbbaca(prep.assembly, prep.genus_species, prep.schema)
        step_4AN_genes__prokka(assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_salmonella_analysis(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAL.115.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `L13_mlst_flaA_cam` — `file_not_found`

**Prompt:** From paired Illumina FASTQ of Campylobacter jejuni: trim with fastp, assemble with SPAdes, then run mlst and flaA in parallel.

**Steps (LLM):** `step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { extractKey } from '../functions/common.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def referenceCode = 'NC_045512.2'

def referencePath = "${params.assets_dir}/module_covid_emergency/NC_045512.fasta"

def referenceRiscd = '220308-020220308005121273-2AS_import-external'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_typing_bacteria {
    
    take:
        
        trimmed
        
        assembly
        
    
    main:
        trimmed.cross(assigned_species) { extractKey(it) }.multiMap {
          trimmed: it[0]
          species: it[1][1]
          referencePath: it[1][2]
        }.set { trimAndAndSpecies }

        assembly.cross(assigned_species) { extractKey(it) }.multiMap {
          assembly: it[0]
          species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__spades(trimmed).assembled
    module_typing_bacteria(trimmed, assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.CAM.116.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `L18_staramr_prokka_cam` — `arity_error`

**Prompt:** From paired Illumina FASTQ of Campylobacter jejuni: trim with fastp, assemble with SPAdes, then run staramr and prokka in parallel.

**Steps (LLM):** `step_4AN_genes__prokka, step_4AN_AMR__staramr, step_1PP_trimming__fastp, step_2AS_denovo__spades`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr, step_4AN_genes__prokka`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4AN_AMR__staramr(assembled, param('genus_species'))
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

def genus_species = 'campylobacter_jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_annotation_amr {
    
    take:
        
        assembly
        
    
    main:
        assembly.multiMap {
            assembly: it
            kingdom: 'Bacteria'
            riscd_ref: '-'
            reference: getEmpty()
            gb: getEmpty()
        }.set { prokkaIn }

        step_4AN_genes__prokka(prokkaIn)

        assembly.multiMap {
            assembly: it
            genus_species: genus_species
        }.set { staramrIn }

        step_4AN_AMR__staramr(staramrIn.assembly, staramrIn.genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed)
    wf_annotation_amr(assembly)
}
```
**Error excerpt:**
```
ERROR ~ Workflow `wf_annotation_amr:step_4AN_genes__prokka` declares 1 input channels but 5 were given
```

### `L19_flaA_prokka_cam` — `partial_dag`

**Prompt:** From paired Illumina FASTQ of Campylobacter jejuni: trim with fastp, assemble with SPAdes, then run flaA and prokka in parallel.

**Steps (LLM):** `step_2AS_denovo__spades, step_4AN_genes__prokka, step_4TY_flaA__flaA`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka, step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_flaA__flaA(assembled, param('genus_species'))
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

// --- GLOBALS ---

def kingdom = 'Bacteria'

def genus_species = 'campylobacter'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_analysis {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
            reference: [ referenceRiscd, referenceCode, file(referencePath) ]
        }.set { trAndRef }

        assembly = step_2AS_denovo__spades(trAndRef.trimmed)
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], kingdom, '-', '-', getEmpty() ] })
        step_4TY_flaA__flaA(assembly, genus_species)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_campylobacter_analysis(getSingleInput())
}
```
**Error excerpt:**
```
Only 5/8 expected processes appeared in the DAG
```

### `M02_mlst+chewbbaca+prokka_sal` — `file_not_found`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Salmonella enterica from paired Illumina FASTQ: trim, assemble, then run mlst, chewbbaca, prokka in parallel on the assembly.

**Steps (LLM):** `step_2AS_denovo__unicycler, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca, step_4AN_genes__prokka, step_4AN_AMR__abricate, step_1PP_trimming__fastp`
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

include { extractKey; getEmpty } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_typing_amr_annotation {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
        }.set { trAndRef }

        assembly = step_2AS_denovo__unicycler(trAndRef.trimmed)

        step_4TY_MLST__mlst(assembly)
        step_4TY_cgMLST__chewbbaca(assembly, 'Salmonella', 's_enterica_chewie_3255_210531')
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
        step_4AN_AMR__abricate(assembly)
    
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

workflow step_2AS_denovo__unicycler {
    
    take:
        
        data
        
    
    main:
        unicycler(data).scaffolds
        assembly_filter(unicycler.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

workflow step_4TY_cgMLST__chewbbaca {
    
    take:
        
        assembly
        
        genus_species
        
        schema
        
    
    main:
        chewbbaca_result = chewbbaca(assembly, genus_species, schema)
        hashing(chewbbaca_result.alleles)
        chewbbaca_check(chewbbaca_result.stats).check
    
}

workflow step_4AN_genes__prokka {
    
    take:
        
        data
        
    
    main:
        prokka(data)
    
}

workflow step_4AN_AMR__abricate {
    
    take:
        
        data
        
    
    main:
        abricate(data)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_salmonella_typing_amr_annotation(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAL.118.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `M04_mlst+abricate+prokka_lis` — `no_code`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Listeria monocytogenes from paired Illumina FASTQ: trim, assemble, then run mlst, abricate, prokka in parallel on the assembly.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `M05_mlst+flaA+staramr_cam` — `no_code`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Campylobacter jejuni from paired Illumina FASTQ: trim, assemble, then run mlst, flaA, staramr in parallel on the assembly.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4TY_flaA__flaA(assembled, param('genus_species'))
    step_4AN_AMR__staramr(assembled, param('genus_species'))
}
```
**LLM-generated (failed):**
```groovy

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `N04_canonical_mlst_cam` — `file_not_found`

**Prompt:** Canonical bacterial typing pipeline (fastp + SPAdes + mlst) on paired Illumina FASTQ of Campylobacter jejuni.

**Steps (LLM):** `step_1PP_trimming__fastp, step_4TY_MLST__mlst`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

def organism = 'Campylobacter jejuni'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        trimmed
        
    
    main:
        denovo(trimmed)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    module_surveillance(trimmed)
    step_4TY_MLST__mlst(module_surveillance.assembled, organism)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.CAM.127.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `N05_canonical_cgmlst_lis` — `file_not_found`

**Prompt:** Standard cgMLST pipeline (fastp + SPAdes + chewbbaca) on paired Illumina FASTQ of Listeria monocytogenes.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca`
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

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

def SPECIES_SCHEMA = ['listeria_monocytogenes', 'escherichia_coli', 'salmonella_enterica']

def SCHEMAS = ['/schemas/Listeria_monocytogenes_Pasteur_cgMLST_2022-06-23T18_03_54.613576.zip', '/schemas/Escherichia_coli_INNUENDO_wgMLST_2021-05-31T14_24_05.304225.zip', '/schemas/Salmonella_enterica_INNUENDO_cgMLST_2021-05-31T20_28_21.350919.zip']

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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
        denovo(data)
        assembly_filter(denovo.out.scaffolds).fasta | quast
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

workflow step_4TY_cgMLST__chewbbaca {
    
    take:
        
        assembly
        
        genus_species
        
        schema
        
    
    main:
        chewbbaca_result = chewbbaca(assembly, genus_species, schema)
        hashing(chewbbaca_result.alleles)
        chewbbaca_check(chewbbaca_result.stats).check
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembled = step_2AS_denovo__spades(trimmed)
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.LIS.125.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `NA01_mlst_cam_assembly` — `file_not_found`

**Prompt:** Run mlst on a pre-existing Campylobacter jejuni assembly.

**Steps (LLM):** `step_4TY_MLST__mlst`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.CAM.128.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `NA02_mlst_sal_assembly` — `file_not_found`

**Prompt:** Run mlst on a pre-existing Salmonella enterica assembly.

**Steps (LLM):** `step_4TY_MLST__mlst`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4TY_MLST__mlst {
    
    take:
        
        assembly
        
    
    main:
        mlst(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAL.121.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `NA03_abricate_lis_assembly` — `silent_no_op`

**Prompt:** Run abricate on a pre-existing Listeria monocytogenes assembly.

**Steps (LLM):** `step_4AN_AMR__abricate`
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

include { parseMetadataFromFileName } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

def abricateDb = 'vfdb'

// --- INLINE PROCESSES ---

process abricate {
    container 'staphb/abricate:1.0.0'
    
    input:
    
    tuple val(riscd_input), path(assembly)
    
    
    output:
    
    path '*'
    
    path '*.sh', hidden: true
    
    
    script:
    """
md = parseMetadataFromFileName(assembly.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
"""
  abricate --db ${abricateDb} --csv ${assembly} > abricate.csv
  abricate ${assembly} -db ${abricateDb} &>> ${base}_abricate.log >> ${base}_abricate_calls.txt
  abricate --summary ${base}_abricate_calls.txt > ${base}_abricate.summary
"""
    """
}

// --- SUB WORKFLOWS ---

workflow step_4AN_AMR__abricate {
    
    take:
        
        data
        
    
    main:
        abricate(data)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4AN_AMR__abricate(getSingleInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `NA04_abricate_sal_assembly` — `file_not_found`

**Prompt:** Run abricate on a pre-existing Salmonella enterica assembly.

**Steps (LLM):** `step_4AN_AMR__abricate`
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

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4AN_AMR__abricate {
    
    take:
        
        assembly
        
    
    main:
        abricate(assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4AN_AMR__abricate(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAL.122.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `NA07_prokka_cam_assembly` — `file_not_found`

**Prompt:** Run prokka on a pre-existing Campylobacter jejuni assembly.

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

include { getAssembly } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4AN_genes__prokka {
    
    take:
        
        assembly
        
    
    main:
        assembly.map { [ it[0], it[1], kingdom, '-', '-', getEmpty() ] }.set { prokkaIn }
        prokka(prokkaIn)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4AN_genes__prokka(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.CAM.130.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
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

include { getAssembly } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

def kingdom = 'Bacteria'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_4AN_genes__prokka {
    
    take:
        
        assembly
        
    
    main:
        assembly.map { [ it[0], it[1], kingdom, '-', '-', getEmpty() ] }.set { prokkaIn}
        prokka(prokkaIn)
    
}

// --- ENTRYPOINT ---
workflow {
    step_4AN_genes__prokka(getAssembly())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.ECO.122.1.1/2AS_import/DS99999-DT260224_external/result/*.fasta'
```

### `O04_shovill_lis` — `no_code`

**Prompt:** De novo assembly with shovill from paired Illumina FASTQ of Listeria monocytogenes.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `O06_shovill_cam` — `file_not_found`

**Prompt:** De novo assembly with shovill from paired Illumina FASTQ of Campylobacter jejuni.

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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

// --- ENTRYPOINT ---
workflow {
    step_2AS_denovo__shovill(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.CAM.132.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `O10_plasmidspades_eco` — `no_code`

**Prompt:** De novo assembly with plasmidspades from paired Illumina FASTQ of Escherichia coli.

**Steps (LLM):** `(none)`
**Steps (GT):**  `step_2AS_denovo__plasmidspades`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_2AS_denovo__plasmidspades } from '../steps/step_2AS_denovo__plasmidspades'
workflow {
    step_2AS_denovo__plasmidspades(getSingleInput())
}
```
**LLM-generated (failed):**
```groovy

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `P09_chopper_flye_chewbbaca_lis` — `file_not_found`

**Prompt:** Nanopore pipeline for Listeria monocytogenes: chopper trimming + Flye assembly + chewbbaca.

**Steps (LLM):** `step_1PP_trimming__chopper, step_2AS_denovo__flye, step_4TY_cgMLST__chewbbaca`
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

include { step_2AS_denovo__flye } from '../steps/step_2AS_denovo__flye'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'

// --- GLOBALS ---

def genus_species = 'Listeria monocytogenes'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_nanopore_listeria {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__chopper(rawreads)
        assembly = step_2AS_denovo__flye(trimmed)
        step_4TY_cgMLST__chewbbaca(assembly, genus_species, schema)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_nanopore_listeria(getSingleInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.LIS.133.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `Q06_kmerfinder_fastp_shovill_sal` — `file_not_found`

**Prompt:** In parallel, identify the species with kmerfinder and trim+assemble paired Illumina FASTQ of Salmonella enterica with fastp + shovill.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { getInput } from '../functions/parameters.nf'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

def KMERFINDER_SPECIES_DIR = '${params.step_3TX_species__kmerfinder__db}'

def KMERFINDER_REFERENCE_DIR = '${KMERFINDER_SPECIES_DIR}/Bacteria/Fasta/'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_3TX_species__kmerfinder {
    
    take:
        
        data
        
    
    main:
        kmerfinder(data);
        assigned_species = kmerfinder.out.check.map { [ it[0], getCalculatedSpecies(it[1]), getBacterialReferencePath(it[1]) ] }
    
    emit:
        
        assigned_species
        
    
}

workflow step_1PP_trimming__fastp {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = fastp(rawreads).trimmed;
        fastqc(trimmed);
        readsCheckInput = rawreads.cross(trimmed) { extractKey(it) }.multiMap { rawreads: it[0]; trimmed: it[1] };
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)
    
    emit:
        
        trimmed
        
    
}

workflow step_2AS_denovo__spades {
    
    take:
        
        data
        
    
    main:
        denovo(data);
        assembly_filter(denovo.out.scaffolds).fasta | quast;
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    step_3TX_species__kmerfinder(getInput());
    step_1PP_trimming__fastp(getInput());
    step_2AS_denovo__spades(getInput())
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAL.130.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `Q07_mash_fastp_spades_lis` — `none`

**Prompt:** In parallel, identify the species with mash and trim+assemble paired Illumina FASTQ of Listeria monocytogenes with fastp + spades.

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

include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'

include { extractKey } from '../functions/common.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_listeria_analysis {
    
    take:
        
        rawreads
        
    
    main:
        rawreads.cross(rawreads) { extractKey(it) }.multiMap {
          reads: it[0]
        }.set { reads_for_mash }
        step_3TX_species__mash(reads_for_mash.reads)

        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        assembly = step_2AS_denovo__spades(trimmed).assembled
    
}

// --- ENTRYPOINT ---
workflow {
    wf_listeria_analysis(getSingleInput())
}
```
**Error excerpt:**
```
(no excerpt)
```

### `Q08_mash_fastp_spades_eco` — `none`

**Prompt:** In parallel, identify the species with mash and trim+assemble paired Illumina FASTQ of Escherichia coli with fastp + spades.

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

include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_species_id {
    
    take:
        
        reads
        
    
    main:
        step_3TX_species__mash(reads)
    
}

workflow wf_trim_and_assemble {
    
    take:
        
        reads
        
    
    main:
        fastp_out = step_1PP_trimming__fastp(reads)
        assembly_filter_out = step_2AS_denovo__spades(fastp_out.trimmed)
    
    emit:
        
        trimmed = fastp_out.trimmed
        
        assembled = assembly_filter_out.fasta
        
    
}

// --- ENTRYPOINT ---
workflow {
    reads = getSingleInput()
    wf_species_id(reads)
    wf_trim_and_assemble(reads)
}
```
**Error excerpt:**
```
(no excerpt)
```

### `Q09_mash_fastp_spades_sal` — `missing_param`

**Prompt:** In parallel, identify the species with mash and trim+assemble paired Illumina FASTQ of Salmonella enterica with fastp + spades.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_denovo__spades, step_1PP_trimming__fastp`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_identification {
    
    take:
        
        rawreads
        
    
    main:
        rawreads.branch {
            species_id: true
            assembly: true
        }.set { branched }

        kmerfinder_out = step_3TX_species__kmerfinder(branched.species_id)
        spades_out = step_2AS_denovo__spades(branched.assembly)

        assigned_species = kmerfinder_out.assigned_species
        assembled = spades_out.assembled
    
    emit:
        
        assigned_species
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    wf_salmonella_identification(trimmed.trimmed)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `Q10_mash_fastp_shovill_lis` — `file_not_found`

**Prompt:** In parallel, identify the species with mash and trim+assemble paired Illumina FASTQ of Listeria monocytogenes with fastp + shovill.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { getInput } from '../functions/parameters.nf'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

def KMERFINDER_SPECIES_DIR = "${params.step_3TX_species__kmerfinder__db}"

def KMERFINDER_REFERENCE_DIR = "${KMERFINDER_SPECIES_DIR}/Bacteria/Fasta/"

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow step_3TX_species__kmerfinder {
    
    take:
        
        data
        
    
    main:
        kmerfinder(data);
        assigned_species = kmerfinder.out.check.map { [ it[0], getCalculatedSpecies(it[1]), getBacterialReferencePath(it[1]) ] }
    
    emit:
        
        assigned_species
        
    
}

workflow step_1PP_trimming__fastp {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = fastp(rawreads).trimmed;
        fastqc(trimmed);
        readsCheckInput = rawreads.cross(trimmed) { extractKey(it) }.multiMap {
          rawreads: it[0]
          trimmed: it[1]
        };
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)
    
    emit:
        
        trimmed
        
    
}

workflow step_2AS_denovo__spades {
    
    take:
        
        data
        
    
    main:
        denovo(data);
        assembly_filter(denovo.out.scaffolds).fasta | quast;
        assembled = assembly_filter.out.fasta
    
    emit:
        
        assembled
        
    
}

// --- ENTRYPOINT ---
workflow {
    step_3TX_species__kmerfinder(getInput());
    step_1PP_trimming__fastp(getInput());
    step_2AS_denovo__spades(step_1PP_trimming__fastp.out.trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.LIS.137.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `R02_kmerfinder_sal` — `silent_no_op`

**Prompt:** kmerfinder on paired Illumina FASTQ of Salmonella enterica.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { extractKey; getEmpty } from '../functions/common.nf'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

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
No process placeholders appeared. when: clause filtered everything?
```

### `R03_mash_sal` — `file_not_found`

**Prompt:** mash on paired Illumina FASTQ of Salmonella enterica.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_species__mash`
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

include { getInput } from '../functions/parameters.nf'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

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

workflow step_3TX_species__mash {
    
    take:
        
        reads
        
    
    main:
        mash(reads)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getInput()).trimmed
    step_3TX_species__mash(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAL.133.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `R05_kraken2_lis` — `no_code`

**Prompt:** kraken2 on paired Illumina FASTQ of Listeria monocytogenes.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `R07_kraken2_sal` — `file_not_found`

**Prompt:** kraken2 on paired Illumina FASTQ of Salmonella enterica.

**Steps (LLM):** `step_3TX_class__kraken2`
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

include { extractKey } from '../functions/common.nf'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_class__kraken2 } from '../steps/step_3TX_class__kraken2'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_salmonella_classification {
    
    take:
        
        trimmed
        
    
    main:
        trimmed.multiMap {
            trimmed: it
        }.set { trAndRef }

        kraken2_out = step_3TX_class__kraken2(trAndRef.trimmed)
    
    emit:
        
        genus_report = kraken2_out.genus_report
        
    
}

workflow wf_trimming {
    
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

// --- ENTRYPOINT ---
workflow {
    rawreads = getSingleInput()
    trimmed = wf_trimming(rawreads).trimmed
    wf_salmonella_classification(trimmed)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_bench/scratch/llm_full_200_devstral_2507/_shared_inputdir/2026/2026.SAL.134.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `S03_trimmomatic_eco` — `silent_no_op`

**Prompt:** trimmomatic read trimming on illumina paired FASTQ of Escherichia coli.

**Steps (LLM):** `step_1PP_trimming__trimmomatic`
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

include { extractKey; getRisCd; parseMetadataFromFileName } from '../functions/common.nf'

include { getInput; isIlluminaPaired; isIonTorrent } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

process trimmomatic {
    container 'quay.io/biocontainers/trimmomatic:0.36--6'
    
    input:
    
    tuple val(riscd_input), path(reads)
    
    
    output:
    
    tuple val(riscd), path('*.fastq.gz'), emit: fastq
    
    path '{*trimmomatic.log,*.json}'
    
    path '*.sh', hidden: true
    
    
    script:
    """
(r1,r2) = (reads instanceof java.util.Collection) ? reads : [reads, null]
md = parseMetadataFromFileName(r1.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
riscd = getRisCd(md, ex, STEP, METHOD)
if (isIlluminaPaired(reads)) {
  """
    trimmomatic PE -threads 2 -phred33 $r1 $r2 ${base}_R1_trimmomatic.fastq.gz ${base}_R1_unpaired.fastq.gz ${base}_R2_trimmomatic.fastq.gz ${base}_R2_unpaired.fastq.gz ILLUMINACLIP:/usr/local/share/trimmomatic-0.36-6/adapters/NexteraPE-PE.fa:2:30:10 LEADING:25 TRAILING:25 SLIDINGWINDOW:20:25 MINLEN:36 2>> ${base}_trimmomatic.log;
    cat ${base}_R1_unpaired.fastq.gz ${base}_R2_unpaired.fastq.gz > ${base}_unpaired_trimmomatic.fastq.gz
    rm  ${base}_R1_unpaired.fastq.gz ${base}_R2_unpaired.fastq.gz
  """
} else if (isIonTorrent(reads)) {
  """
    trimmomatic SE -threads 2 -phred33 $r1 ${base}_R1_trimmomatic.fastq.gz LEADING:3 TRAILING:3 SLIDINGWINDOW:5:20 MINLEN:55 2>> ${base}_trimmomatic.log
  """
}
    """
}

// --- SUB WORKFLOWS ---

workflow step_1PP_trimming__trimmomatic {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = trimmomatic(rawreads).fastq;
        fastqc(trimmed)
        readsCheckInput = rawreads.cross(trimmed) { extractKey(it) }.multiMap {
          rawreads: it[0]
          trimmed: it[1]
        }
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)
    
    emit:
        
        trimmed
        
    
}

// --- ENTRYPOINT ---
workflow {
    step_1PP_trimming__trimmomatic(getInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `S04_trimmomatic_cam` — `silent_no_op`

**Prompt:** trimmomatic read trimming on illumina paired FASTQ of Campylobacter jejuni.

**Steps (LLM):** `step_1PP_trimming__trimmomatic`
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

include { extractKey; getRisCd; parseMetadataFromFileName } from '../functions/common.nf'

include { getInput; isIlluminaPaired; isIonTorrent } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

process trimmomatic {
    container 'quay.io/biocontainers/trimmomatic:0.36--6'
    
    input:
    
    tuple val(riscd_input), path(reads)
    
    
    output:
    
    tuple val(riscd), path('*.fastq.gz'), emit: fastq
    
    path '{*trimmomatic.log,*.json}'
    
    path '*.sh', hidden: true
    
    
    script:
    """
(r1,r2) = (reads instanceof java.util.Collection) ? reads : [reads, null]
md = parseMetadataFromFileName(r1.getName())
base = "${md.ds}-${ex.dt}_${md.cmp}"
riscd = getRisCd(md, ex, STEP, METHOD)
if (isIlluminaPaired(reads)) {
  """
    trimmomatic PE -threads 2 -phred33 $r1 $r2 ${base}_R1_trimmomatic.fastq.gz ${base}_R1_unpaired.fastq.gz ${base}_R2_trimmomatic.fastq.gz ${base}_R2_unpaired.fastq.gz ILLUMINACLIP:/usr/local/share/trimmomatic-0.36-6/adapters/NexteraPE-PE.fa:2:30:10 LEADING:25 TRAILING:25 SLIDINGWINDOW:20:25 MINLEN:36 2>> ${base}_trimmomatic.log;
    cat ${base}_R1_unpaired.fastq.gz ${base}_R2_unpaired.fastq.gz > ${base}_unpaired_trimmomatic.fastq.gz
    rm  ${base}_R1_unpaired.fastq.gz ${base}_R2_unpaired.fastq.gz
  """
} else if (isIonTorrent(reads)) {
  """
    trimmomatic SE -threads 2 -phred33 $r1 ${base}_R1_trimmomatic.fastq.gz LEADING:3 TRAILING:3 SLIDINGWINDOW:5:20 MINLEN:55 2>> ${base}_trimmomatic.log
  """
}
    """
}

// --- SUB WORKFLOWS ---

workflow step_1PP_trimming__trimmomatic {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = trimmomatic(rawreads).fastq;
        fastqc(trimmed)
        readsCheckInput = rawreads.cross(trimmed) { extractKey(it) }.multiMap {
          rawreads: it[0]
          trimmed: it[1]
        }
        sample_reads_check(readsCheckInput.rawreads, readsCheckInput.trimmed)
    
    emit:
        
        trimmed
        
    
}

// --- ENTRYPOINT ---
workflow {
    step_1PP_trimming__trimmomatic(getInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `S05_chopper_lis` — `no_code`

**Prompt:** chopper read trimming on nanopore FASTQ of Listeria monocytogenes.

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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `S06_chopper_sal` — `silent_no_op`

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

include { optionalOrDefault; param } from '../functions/parameters.nf'

include { multi_clustering__reportree } from '../multi/multi_clustering__reportree'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    main:
        if (getReportreeInputType() == 'alleles') {
          include { multi_clustering__reportree } from "../multi/multi_clustering__reportree_alleles"
          include { getAlleles as inputFn } from "../multi/multi_clustering__reportree_alleles"
        } else if (getReportreeInputType() == 'alignment') {
          include { multi_clustering__reportree } from "../multi/multi_clustering__reportree_alignment"
          include { getInput as inputFn } from '../functions/parameters.nf'
        } else {
          include { multi_clustering__reportree } from "../multi/multi_clustering__reportree_vcf"
          include { getVCFs as inputFn } from '../functions/parameters.nf'
        }

        def getReportreeInputType() {
            def res = param('multi_clustering__reportree__input')
            if (!(res in ['alleles', 'vcf', 'alignment'])) {
                exit 2, "params (multi_clustering__reportree__input) not valid"
            }
            return res
        }

        multi_clustering__reportree(inputFn(),  param('metadata'), param('geodata'), optionalOrDefault('multi_clustering__reportree__nomenclature', getEmpty()))
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance()
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```
