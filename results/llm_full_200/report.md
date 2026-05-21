# LLM evaluation — detailed report

Total prompts: **200**  ·  generated code: **196**  ·  syntactically valid: **190**  ·  semantically valid: **137**

Step-set vs. ground truth:  exact match **159**  ·  extra steps **35**  ·  missing steps **11**  ·  hallucinated (non-existent) steps **0**

## Error category breakdown

| Category | Count | Meaning |
|----|----|----|
| `none` | 131 | no error — pipeline passes |
| `silent_no_op` | 37 | DAG empty — pipeline runs but produces no output |
| `missing_param` | 13 | step requires a param() that was not supplied |
| `file_not_found` | 8 | expected input file is not in the framework layout |
| `ngsmanager_naming` | 6 | input file name does not match parseMetadataFromFileName regex |
| `no_code` | 4 | LLM did not return any .nf code |
| `arity_error` | 1 | workflow called with wrong number of arguments |

## Per-prompt outcome

| # | id | code? | syntax | semantic | procs | error category | first 80 chars of detail |
|---|----|-------|--------|----------|-------|----------------|------|
| 1 | `A01_mlst_listeria` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 2 | `A02_mlst_ecoli` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 3 | `A03_mlst_salmonella` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 4 | `A04_cgmlst_listeria` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 5 | `A05_cgmlst_ecoli` | ✅ | ✅ | ❌ | 0/3 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 6 | `A06_cgmlst_salmonella` | ✅ | ✅ | ❌ | 0/3 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 7 | `A07_flaa_campylobacter` | ✅ | ✅ | ❌ | 0/1 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 8 | `A08_staramr_campylobacter` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 9 | `B01_spades_listeria` | ✅ | ✅ | ❌ | 0/3 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 10 | `B02_shovill_ecoli` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 11 | `B03_unicycler_salmonella` | ✅ | ✅ | ❌ | 0/3 | `missing_param` | ERROR ~ missing required param: hosts_dir |
| 12 | `B04_plasmidspades` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 13 | `B05_metaspades` | ✅ | ✅ | ✅ | 8/3 | `none` |  |
| 14 | `C01_kmerfinder` | ✅ | ✅ | ✅ | 4/1 | `none` |  |
| 15 | `C02_mash` | ✅ | ✅ | ❌ | 0/1 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 16 | `C03_kraken2` | ✅ | ✅ | ❌ | 0/2 | `missing_param` | ERROR ~ missing required param: multi_clustering__reportree__summary_columns |
| 17 | `D01_fastp_spades_lis` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 18 | `D02_fastp_shovill_eco` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 19 | `D03_trimmomatic_spades` | ✅ | ✅ | ❌ | 0/6 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 20 | `D04_fastp_unicycler_sal` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 21 | `D05_fastp_spades_cam` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 22 | `E01_mlst_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 23 | `E02_cgmlst_lis_fastp_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 24 | `E03_cgmlst_sal_fastp_spades` | ✅ | ✅ | ❌ | 0/9 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 25 | `E04_cgmlst_eco_fastp_shovill` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 26 | `E05_flaa_cam` | ✅ | ❌ | ❌ | 6/7 | `arity_error` | ERROR ~ Workflow `module_surveillance:step_4TY_flaA__flaA` declares 2 input chan |
| 27 | `E06_staramr_cam` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 28 | `E07_abricate_eco` | ✅ | ✅ | ❌ | 0/7 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 29 | `E08_prokka_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 30 | `E09_mlst_eco_trimmomatic` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 31 | `E10_mlst_sal_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 32 | `E11_cgmlst_lis_shovill` | ✅ | ✅ | ❌ | 0/9 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 33 | `E12_mlst_cam` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 34 | `E13_abricate_sal` | ✅ | ✅ | ❌ | 0/7 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 35 | `E14_prokka_eco` | ✅ | ✅ | ❌ | 0/7 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 36 | `E15_cgmlst_lis_trimmomatic` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 37 | `F01_abricate_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 38 | `F02_prokka_assembly` | ✅ | ✅ | ❌ | 0/1 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 39 | `F03_mash_lis` | ✅ | ✅ | ✅ | 4/1 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.LIS.A.1.1_R1.fastq.gz |
| 40 | `F04_kraken2_unknown` | ✅ | ✅ | ✅ | 7/2 | `none` |  |
| 41 | `G01_chopper_flye_lis` | ✅ | ✅ | ✅ | 4/4 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.LIS.B.1.1_R1.fastq.gz |
| 42 | `G02_chopper_flye_eco` | ✅ | ✅ | ✅ | 4/4 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.ECO.B.1.1_R1.fastq.gz |
| 43 | `H01_mlst_plus_cgmlst_lis` | ✅ | ✅ | ✅ | 10/10 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.LIS.C.1.1_R1.fastq.gz |
| 44 | `H02_mlst_plus_flaa_cam` | ✅ | ✅ | ❌ | 0/8 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 45 | `H03_prokka_plus_abricate_eco` | ✅ | ✅ | ✅ | 8/8 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.ECO.C.1.1_R1.fastq.gz |
| 46 | `H04_mlst_plus_abricate_sal` | ✅ | ✅ | ✅ | 8/8 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.SAL.C.1.1_R1.fastq.gz |
| 47 | `I01_kmerfinder_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 48 | `I02_mash_fastp_shovill` | ⚪ | ❌ | ❌ | 0/7 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 49 | `J01_mobsuite_plasmid` | ✅ | ✅ | ✅ | 4/1 | `none` |  |
| 50 | `J02_bbnorm_downsampling` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 51 | `K01_mlst_lis_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 52 | `K02_mlst_eco_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 53 | `K03_mlst_sal_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 54 | `K04_mlst_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 55 | `K05_chewbbaca_lis_fastp_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 56 | `K06_chewbbaca_eco_fastp_spades` | ✅ | ✅ | ❌ | 0/9 | `missing_param` | ERROR ~ missing required param: multi_clustering__reportree__summary_columns |
| 57 | `K07_chewbbaca_sal_fastp_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 58 | `K08_abricate_lis_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 59 | `K09_abricate_eco_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 60 | `K10_abricate_sal_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 61 | `K11_abricate_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 62 | `K12_prokka_lis_fastp_spades` | ✅ | ✅ | ❌ | 0/7 | `missing_param` | ERROR ~ missing required param: hosts_dir |
| 63 | `K13_prokka_eco_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 64 | `K14_prokka_sal_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 65 | `K15_prokka_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 66 | `K16_flaA_cam_fastp_spades` | ✅ | ✅ | ❌ | 0/7 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 67 | `K17_staramr_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 68 | `K18_mlst_lis_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 69 | `K19_mlst_eco_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 70 | `K20_mlst_sal_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 71 | `K21_mlst_cam_fastp_shovill` | ✅ | ✅ | ❌ | 0/7 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 72 | `K22_chewbbaca_lis_fastp_shovill` | ⚪ | ❌ | ❌ | 0/9 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 73 | `K23_chewbbaca_eco_fastp_shovill` | ✅ | ✅ | ❌ | 6/9 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/202 |
| 74 | `K24_chewbbaca_sal_fastp_shovill` | ✅ | ✅ | ❌ | 6/9 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/202 |
| 75 | `K25_abricate_lis_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 76 | `K26_abricate_eco_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 77 | `K27_abricate_sal_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 78 | `K28_abricate_cam_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 79 | `K29_prokka_lis_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 80 | `K30_prokka_eco_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
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
| 91 | `K41_chewbbaca_sal_fastp_unicycler` | ✅ | ✅ | ❌ | 0/9 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 92 | `K42_abricate_lis_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 93 | `K43_abricate_eco_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 94 | `K44_abricate_sal_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 95 | `K45_abricate_cam_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 96 | `K46_prokka_lis_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 97 | `K47_prokka_eco_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 98 | `K48_prokka_sal_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 99 | `K49_prokka_cam_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 100 | `K50_flaA_cam_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 101 | `K51_staramr_cam_fastp_unicycler` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 102 | `K52_mlst_lis_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 103 | `K53_mlst_eco_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 104 | `K54_mlst_sal_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 105 | `K55_mlst_cam_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 106 | `K56_chewbbaca_lis_trimmomatic_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 107 | `K57_chewbbaca_eco_trimmomatic_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 108 | `K58_chewbbaca_sal_trimmomatic_spades` | ✅ | ✅ | ❌ | 0/9 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 109 | `K59_abricate_lis_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 110 | `K60_abricate_eco_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 111 | `L01_mlst_chewbbaca_lis` | ✅ | ✅ | ❌ | 7/10 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/202 |
| 112 | `L02_mlst_chewbbaca_eco` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 113 | `L03_mlst_chewbbaca_sal` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 114 | `L04_mlst_abricate_lis` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 115 | `L05_mlst_abricate_eco` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 116 | `L06_chewbbaca_abricate_lis` | ✅ | ✅ | ❌ | 0/10 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 117 | `L07_chewbbaca_prokka_lis` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 118 | `L08_chewbbaca_prokka_sal` | ✅ | ✅ | ❌ | 0/10 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 119 | `L09_mlst_prokka_eco` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 120 | `L10_mlst_prokka_sal` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 121 | `L11_abricate_prokka_lis` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 122 | `L12_abricate_prokka_sal` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 123 | `L13_mlst_flaA_cam` | ✅ | ✅ | ❌ | 0/8 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 124 | `L14_mlst_staramr_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 125 | `L15_flaA_staramr_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 126 | `L16_flaA_abricate_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 127 | `L17_staramr_abricate_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 128 | `L18_staramr_prokka_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 129 | `L19_flaA_prokka_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 130 | `L20_mlst_prokka_lis` | ✅ | ✅ | ❌ | 0/8 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 131 | `M01_mlst+chewbbaca+abricate_lis` | ✅ | ✅ | ❌ | 7/11 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/202 |
| 132 | `M02_mlst+chewbbaca+prokka_sal` | ✅ | ✅ | ❌ | 7/11 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/202 |
| 133 | `M03_mlst+abricate+prokka_eco` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 134 | `M04_mlst+abricate+prokka_lis` | ✅ | ✅ | ❌ | 0/9 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 135 | `M05_mlst+flaA+staramr_cam` | ✅ | ✅ | ❌ | 0/9 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 136 | `M06_mlst+flaA+abricate_cam` | ✅ | ✅ | ✅ | 10/9 | `none` |  |
| 137 | `M07_flaA+staramr+prokka_cam` | ✅ | ❌ | ❌ | 0/9 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 138 | `M08_mlst+staramr+prokka_cam` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 139 | `M09_chewbbaca+abricate+prokka_lis` | ✅ | ✅ | ❌ | 6/11 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/202 |
| 140 | `M10_chewbbaca+abricate+prokka_eco` | ✅ | ✅ | ✅ | 11/11 | `none` |  |
| 141 | `N01_canonical_mlst_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 142 | `N02_canonical_mlst_eco` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 143 | `N03_canonical_mlst_sal` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 144 | `N04_canonical_mlst_cam` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 145 | `N05_canonical_cgmlst_lis` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 146 | `N06_canonical_cgmlst_eco` | ✅ | ✅ | ❌ | 6/9 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/202 |
| 147 | `N07_canonical_cgmlst_sal` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 148 | `NA01_mlst_cam_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 149 | `NA02_mlst_sal_assembly` | ✅ | ✅ | ❌ | 0/1 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 150 | `NA03_abricate_lis_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 151 | `NA04_abricate_sal_assembly` | ✅ | ✅ | ❌ | 0/1 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 152 | `NA05_abricate_cam_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 153 | `NA06_prokka_sal_assembly` | ✅ | ❌ | ❌ | 0/1 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 154 | `NA07_prokka_cam_assembly` | ✅ | ✅ | ❌ | 0/1 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 155 | `NA08_prokka_eco_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 156 | `O01_spades_lis` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 157 | `O02_spades_sal` | ✅ | ✅ | ❌ | 0/3 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 158 | `O03_spades_cam` | ✅ | ✅ | ❌ | 0/3 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 159 | `O04_shovill_lis` | ✅ | ✅ | ❌ | 0/3 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 160 | `O05_shovill_sal` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 161 | `O06_shovill_cam` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 162 | `O07_unicycler_lis` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 163 | `O08_unicycler_eco` | ✅ | ❌ | ❌ | 0/3 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 164 | `O09_unicycler_cam` | ✅ | ✅ | ❌ | 0/3 | `missing_param` | ERROR ~ missing required param: hosts_dir |
| 165 | `O10_plasmidspades_eco` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 166 | `P01_chopper_flye_mlst_lis` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 167 | `P02_chopper_flye_mlst_sal` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 168 | `P03_chopper_flye_mlst_eco` | ✅ | ❌ | ❌ | 0/5 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 169 | `P04_chopper_flye_mlst_cam` | ✅ | ✅ | ❌ | 0/5 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 170 | `P05_chopper_flye_abricate_lis` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 171 | `P06_chopper_flye_abricate_eco` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 172 | `P07_chopper_flye_abricate_sal` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 173 | `P08_chopper_flye_prokka_lis` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 174 | `P09_chopper_flye_chewbbaca_lis` | ✅ | ✅ | ❌ | 4/7 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/202 |
| 175 | `P10_chopper_flye_chewbbaca_sal` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 176 | `Q01_kmerfinder_fastp_spades_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 177 | `Q02_kmerfinder_fastp_spades_eco` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 178 | `Q03_kmerfinder_fastp_spades_sal` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 179 | `Q04_kmerfinder_fastp_shovill_lis` | ✅ | ✅ | ❌ | 0/7 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 180 | `Q05_kmerfinder_fastp_shovill_eco` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 181 | `Q06_kmerfinder_fastp_shovill_sal` | ⚪ | ❌ | ❌ | 0/7 | `no_code` | no nextflow_code after max turns |
| 182 | `Q07_mash_fastp_spades_lis` | ⚪ | ❌ | ❌ | 0/7 | `no_code` | http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. |
| 183 | `Q08_mash_fastp_spades_eco` | ✅ | ❌ | ❌ | 0/7 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 184 | `Q09_mash_fastp_spades_sal` | ✅ | ✅ | ❌ | 0/7 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 185 | `Q10_mash_fastp_shovill_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 186 | `R01_kmerfinder_cam` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 187 | `R02_kmerfinder_sal` | ✅ | ✅ | ❌ | 0/1 | `missing_param` | ERROR ~ missing required param: step_3TX_class__kraken__db_kraken |
| 188 | `R03_mash_sal` | ✅ | ✅ | ❌ | 0/1 | `missing_param` | ERROR ~ missing required param: step_3TX_class__kraken__db_kraken |
| 189 | `R04_mash_eco` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 190 | `R05_kraken2_lis` | ✅ | ✅ | ❌ | 0/2 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 191 | `R06_kraken2_eco` | ✅ | ✅ | ✅ | 5/2 | `none` |  |
| 192 | `R07_kraken2_sal` | ✅ | ✅ | ✅ | 5/2 | `none` |  |
| 193 | `R08_kraken2_cam` | ✅ | ✅ | ❌ | 0/2 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 194 | `S01_fastp_lis` | ✅ | ✅ | ❌ | 0/3 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 195 | `S02_fastp_sal` | ✅ | ✅ | ❌ | 0/3 | `missing_param` | ERROR ~ missing required param: step_3TX_class__kraken__db_kraken |
| 196 | `S03_trimmomatic_eco` | ✅ | ✅ | ❌ | 0/3 | `missing_param` | ERROR ~ missing required param: step_3TX_class__kraken__db_kraken |
| 197 | `S04_trimmomatic_cam` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 198 | `S05_chopper_lis` | ✅ | ✅ | ✅ | 2/2 | `none` |  |
| 199 | `S06_chopper_sal` | ✅ | ✅ | ✅ | 2/2 | `none` |  |
| 200 | `S07_chopper_cam` | ✅ | ✅ | ❌ | 0/2 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |

## Step-set comparison vs ground truth

| # | id | LLM steps | GT steps | extra | missing | hallucinated |
|---|----|-----------|----------|-------|---------|--------------|
| 1 | `A01_mlst_listeria` | mlst | mlst | · | · | · |
| 2 | `A02_mlst_ecoli` | mlst | mlst | · | · | · |
| 3 | `A03_mlst_salmonella` | mlst | mlst | · | · | · |
| 4 | `A04_cgmlst_listeria` | chewbbaca | chewbbaca | · | · | · |
| 5 | `A05_cgmlst_ecoli` | chewbbaca | chewbbaca | · | · | · |
| 6 | `A06_cgmlst_salmonella` | kmerfinder,bowtie,abricate,prokka,staramr,mlst,flaA,chewbbaca | chewbbaca | bowtie,kmerfinder,abricate,staramr,prokka,mlst,flaA | · | · |
| 7 | `A07_flaa_campylobacter` | kmerfinder,bowtie,abricate,prokka,staramr,mlst,flaA,chewbbaca | flaA | bowtie,kmerfinder,abricate,staramr,prokka,mlst,chewbbaca | · | · |
| 8 | `A08_staramr_campylobacter` | staramr | staramr | · | · | · |
| 9 | `B01_spades_listeria` | fastp,spades | spades | fastp | · | · |
| 10 | `B02_shovill_ecoli` | fastp,shovill | shovill | fastp | · | · |
| 11 | `B03_unicycler_salmonella` |  | unicycler | · | unicycler | · |
| 12 | `B04_plasmidspades` | fastp,plasmidspades | plasmidspades | fastp | · | · |
| 13 | `B05_metaspades` | fastq,fastp,metaspades | metaspades | fastq,fastp | · | · |
| 14 | `C01_kmerfinder` | fastp,kmerfinder | kmerfinder | fastp | · | · |
| 15 | `C02_mash` | mash | mash | · | · | · |
| 16 | `C03_kraken2` | kraken2 | kraken2 | · | · | · |
| 17 | `D01_fastp_spades_lis` | fastp,spades | fastp,spades | · | · | · |
| 18 | `D02_fastp_shovill_eco` | fastp,shovill | fastp,shovill | · | · | · |
| 19 | `D03_trimmomatic_spades` | bowtie,spades | trimmomatic,spades | bowtie | trimmomatic | · |
| 20 | `D04_fastp_unicycler_sal` | fastp,unicycler | fastp,unicycler | · | · | · |
| 21 | `D05_fastp_spades_cam` | fastp,spades | fastp,spades | · | · | · |
| 22 | `E01_mlst_lis` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 23 | `E02_cgmlst_lis_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 24 | `E03_cgmlst_sal_fastp_spades` | fastp,bowtie,ivar,chewbbaca | fastp,spades,chewbbaca | bowtie,ivar | spades | · |
| 25 | `E04_cgmlst_eco_fastp_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 26 | `E05_flaa_cam` | fastp,spades,flaA | fastp,spades,flaA | · | · | · |
| 27 | `E06_staramr_cam` | fastp,spades,staramr | fastp,spades,staramr | · | · | · |
| 28 | `E07_abricate_eco` | fastp,spades,prokka,abricate | fastp,spades,abricate | prokka | · | · |
| 29 | `E08_prokka_lis` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 30 | `E09_mlst_eco_trimmomatic` | trimmomatic,spades,mlst | trimmomatic,spades,mlst | · | · | · |
| 31 | `E10_mlst_sal_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 32 | `E11_cgmlst_lis_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 33 | `E12_mlst_cam` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 34 | `E13_abricate_sal` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 35 | `E14_prokka_eco` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 36 | `E15_cgmlst_lis_trimmomatic` | trimmomatic,spades,chewbbaca | trimmomatic,spades,chewbbaca | · | · | · |
| 37 | `F01_abricate_assembly` | abricate | abricate | · | · | · |
| 38 | `F02_prokka_assembly` | kmerfinder,bowtie,abricate,prokka,staramr,mlst,flaA,chewbbaca | prokka | bowtie,kmerfinder,abricate,staramr,mlst,chewbbaca,flaA | · | · |
| 39 | `F03_mash_lis` | fastp,mash | mash | fastp | · | · |
| 40 | `F04_kraken2_unknown` | fastq,fastp,kraken2 | kraken2 | fastq,fastp | · | · |
| 41 | `G01_chopper_flye_lis` | chopper,flye | chopper,flye | · | · | · |
| 42 | `G02_chopper_flye_eco` | chopper,flye | chopper,flye | · | · | · |
| 43 | `H01_mlst_plus_cgmlst_lis` | fastp,spades,mlst,chewbbaca | fastp,spades,mlst,chewbbaca | · | · | · |
| 44 | `H02_mlst_plus_flaa_cam` | kmerfinder,bowtie,abricate,prokka,staramr,mlst,flaA,chewbbaca | fastp,spades,mlst,flaA | bowtie,kmerfinder,abricate,staramr,prokka,chewbbaca | fastp,spades | · |
| 45 | `H03_prokka_plus_abricate_eco` | fastp,spades,prokka,abricate | fastp,spades,abricate,prokka | · | · | · |
| 46 | `H04_mlst_plus_abricate_sal` | fastp,unicycler,mlst,abricate | fastp,spades,abricate,mlst | unicycler | spades | · |
| 47 | `I01_kmerfinder_fastp_spades` | fastp,kmerfinder,spades | fastp,spades,kmerfinder | · | · | · |
| 49 | `J01_mobsuite_plasmid` | fastp,mobsuite | mobsuite | fastp | · | · |
| 50 | `J02_bbnorm_downsampling` | bbnorm | bbnorm | · | · | · |
| 51 | `K01_mlst_lis_fastp_spades` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 52 | `K02_mlst_eco_fastp_spades` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 53 | `K03_mlst_sal_fastp_spades` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 54 | `K04_mlst_cam_fastp_spades` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 55 | `K05_chewbbaca_lis_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 56 | `K06_chewbbaca_eco_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 57 | `K07_chewbbaca_sal_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 58 | `K08_abricate_lis_fastp_spades` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 59 | `K09_abricate_eco_fastp_spades` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 60 | `K10_abricate_sal_fastp_spades` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 61 | `K11_abricate_cam_fastp_spades` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 62 | `K12_prokka_lis_fastp_spades` |  | fastp,spades,prokka | · | fastp,spades,prokka | · |
| 63 | `K13_prokka_eco_fastp_spades` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 64 | `K14_prokka_sal_fastp_spades` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 65 | `K15_prokka_cam_fastp_spades` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 66 | `K16_flaA_cam_fastp_spades` | fastp,spades,flaA | fastp,spades,flaA | · | · | · |
| 67 | `K17_staramr_cam_fastp_spades` | fastp,spades,staramr | fastp,spades,staramr | · | · | · |
| 68 | `K18_mlst_lis_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 69 | `K19_mlst_eco_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 70 | `K20_mlst_sal_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 71 | `K21_mlst_cam_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 73 | `K23_chewbbaca_eco_fastp_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 74 | `K24_chewbbaca_sal_fastp_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 75 | `K25_abricate_lis_fastp_shovill` | fastp,shovill,abricate | fastp,shovill,abricate | · | · | · |
| 76 | `K26_abricate_eco_fastp_shovill` | fastp,shovill,abricate | fastp,shovill,abricate | · | · | · |
| 77 | `K27_abricate_sal_fastp_shovill` | fastp,shovill,abricate | fastp,shovill,abricate | · | · | · |
| 78 | `K28_abricate_cam_fastp_shovill` | fastp,shovill,abricate | fastp,shovill,abricate | · | · | · |
| 79 | `K29_prokka_lis_fastp_shovill` | fastp,shovill,prokka | fastp,shovill,prokka | · | · | · |
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
| 93 | `K43_abricate_eco_fastp_unicycler` | fastp,unicycler,abricate | fastp,unicycler,abricate | · | · | · |
| 94 | `K44_abricate_sal_fastp_unicycler` | fastp,unicycler,abricate | fastp,unicycler,abricate | · | · | · |
| 95 | `K45_abricate_cam_fastp_unicycler` | fastp,unicycler,abricate | fastp,unicycler,abricate | · | · | · |
| 96 | `K46_prokka_lis_fastp_unicycler` | fastp,unicycler,prokka | fastp,unicycler,prokka | · | · | · |
| 97 | `K47_prokka_eco_fastp_unicycler` | fastp,unicycler,prokka | fastp,unicycler,prokka | · | · | · |
| 98 | `K48_prokka_sal_fastp_unicycler` | fastp,unicycler,prokka | fastp,unicycler,prokka | · | · | · |
| 99 | `K49_prokka_cam_fastp_unicycler` | fastp,unicycler,prokka | fastp,unicycler,prokka | · | · | · |
| 100 | `K50_flaA_cam_fastp_unicycler` | fastp,unicycler,flaA | fastp,unicycler,flaA | · | · | · |
| 101 | `K51_staramr_cam_fastp_unicycler` | fastp,unicycler,staramr | fastp,unicycler,staramr | · | · | · |
| 102 | `K52_mlst_lis_trimmomatic_spades` | trimmomatic,spades,mlst | trimmomatic,spades,mlst | · | · | · |
| 103 | `K53_mlst_eco_trimmomatic_spades` | trimmomatic,spades,mlst | trimmomatic,spades,mlst | · | · | · |
| 104 | `K54_mlst_sal_trimmomatic_spades` | trimmomatic,spades,mlst | trimmomatic,spades,mlst | · | · | · |
| 105 | `K55_mlst_cam_trimmomatic_spades` | trimmomatic,spades,mlst | trimmomatic,spades,mlst | · | · | · |
| 106 | `K56_chewbbaca_lis_trimmomatic_spades` | trimmomatic,spades,chewbbaca | trimmomatic,spades,chewbbaca | · | · | · |
| 107 | `K57_chewbbaca_eco_trimmomatic_spades` | trimmomatic,spades,chewbbaca | trimmomatic,spades,chewbbaca | · | · | · |
| 108 | `K58_chewbbaca_sal_trimmomatic_spades` | trimmomatic,spades,chewbbaca | trimmomatic,spades,chewbbaca | · | · | · |
| 109 | `K59_abricate_lis_trimmomatic_spades` | trimmomatic,spades,abricate | trimmomatic,spades,abricate | · | · | · |
| 110 | `K60_abricate_eco_trimmomatic_spades` | trimmomatic,spades,abricate | trimmomatic,spades,abricate | · | · | · |
| 111 | `L01_mlst_chewbbaca_lis` | fastp,spades,mlst,chewbbaca | fastp,spades,mlst,chewbbaca | · | · | · |
| 112 | `L02_mlst_chewbbaca_eco` | fastp,spades,mlst,chewbbaca | fastp,spades,mlst,chewbbaca | · | · | · |
| 113 | `L03_mlst_chewbbaca_sal` | fastp,spades,mlst,chewbbaca | fastp,spades,mlst,chewbbaca | · | · | · |
| 114 | `L04_mlst_abricate_lis` | fastp,spades,mlst,abricate | fastp,spades,abricate,mlst | · | · | · |
| 115 | `L05_mlst_abricate_eco` | fastp,spades,mlst,abricate | fastp,spades,abricate,mlst | · | · | · |
| 116 | `L06_chewbbaca_abricate_lis` | fastp,spades,chewbbaca,abricate | fastp,spades,abricate,chewbbaca | · | · | · |
| 117 | `L07_chewbbaca_prokka_lis` | fastp,spades,chewbbaca,prokka | fastp,spades,prokka,chewbbaca | · | · | · |
| 118 | `L08_chewbbaca_prokka_sal` | spades,chewbbaca,prokka,fastp | fastp,spades,prokka,chewbbaca | · | · | · |
| 119 | `L09_mlst_prokka_eco` | fastp,spades,mlst,prokka | fastp,spades,prokka,mlst | · | · | · |
| 120 | `L10_mlst_prokka_sal` | fastp,spades,mlst,prokka | fastp,spades,prokka,mlst | · | · | · |
| 121 | `L11_abricate_prokka_lis` | fastp,spades,abricate,prokka | fastp,spades,abricate,prokka | · | · | · |
| 122 | `L12_abricate_prokka_sal` | spades,prokka,abricate,fastp | fastp,spades,abricate,prokka | · | · | · |
| 123 | `L13_mlst_flaA_cam` | fastp,spades,mlst,flaA | fastp,spades,mlst,flaA | · | · | · |
| 124 | `L14_mlst_staramr_cam` | fastp,spades,mlst,staramr | fastp,spades,staramr,mlst | · | · | · |
| 125 | `L15_flaA_staramr_cam` | fastp,spades,flaA,staramr | fastp,spades,staramr,flaA | · | · | · |
| 126 | `L16_flaA_abricate_cam` | fastp,spades,flaA,abricate | fastp,spades,abricate,flaA | · | · | · |
| 127 | `L17_staramr_abricate_cam` | fastp,spades,staramr,abricate | fastp,spades,abricate,staramr | · | · | · |
| 128 | `L18_staramr_prokka_cam` | fastp,spades,staramr,prokka | fastp,spades,staramr,prokka | · | · | · |
| 129 | `L19_flaA_prokka_cam` | fastp,spades,flaA,prokka | fastp,spades,prokka,flaA | · | · | · |
| 130 | `L20_mlst_prokka_lis` | fastp,spades,mlst,prokka | fastp,spades,prokka,mlst | · | · | · |
| 131 | `M01_mlst+chewbbaca+abricate_lis` | fastp,spades,mlst,chewbbaca,abricate | fastp,spades,abricate,mlst,chewbbaca | · | · | · |
| 132 | `M02_mlst+chewbbaca+prokka_sal` | fastp,spades,mlst,chewbbaca,prokka | fastp,spades,prokka,mlst,chewbbaca | · | · | · |
| 133 | `M03_mlst+abricate+prokka_eco` | spades,mlst,abricate,prokka,fastp | fastp,spades,abricate,prokka,mlst | · | · | · |
| 134 | `M04_mlst+abricate+prokka_lis` | spades,mlst,abricate,prokka,fastp | fastp,spades,abricate,prokka,mlst | · | · | · |
| 135 | `M05_mlst+flaA+staramr_cam` | fastp,spades,mlst,flaA,staramr | fastp,spades,staramr,mlst,flaA | · | · | · |
| 136 | `M06_mlst+flaA+abricate_cam` | fastp,spades,mlst,flaA,prokka,abricate | fastp,spades,abricate,mlst,flaA | prokka | · | · |
| 137 | `M07_flaA+staramr+prokka_cam` | fastp,spades,flaA,staramr,prokka | fastp,spades,staramr,prokka,flaA | · | · | · |
| 138 | `M08_mlst+staramr+prokka_cam` | fastp,spades,mlst,staramr,prokka | fastp,spades,staramr,prokka,mlst | · | · | · |
| 139 | `M09_chewbbaca+abricate+prokka_lis` | fastp,spades,chewbbaca,abricate,prokka | fastp,spades,abricate,prokka,chewbbaca | · | · | · |
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
| 150 | `NA03_abricate_lis_assembly` | abricate | abricate | · | · | · |
| 151 | `NA04_abricate_sal_assembly` | abricate | abricate | · | · | · |
| 152 | `NA05_abricate_cam_assembly` | abricate | abricate | · | · | · |
| 153 | `NA06_prokka_sal_assembly` | prokka | prokka | · | · | · |
| 154 | `NA07_prokka_cam_assembly` | prokka | prokka | · | · | · |
| 155 | `NA08_prokka_eco_assembly` | prokka | prokka | · | · | · |
| 156 | `O01_spades_lis` | fastp,spades | spades | fastp | · | · |
| 157 | `O02_spades_sal` | fastp,spades | spades | fastp | · | · |
| 158 | `O03_spades_cam` | fastp,spades | spades | fastp | · | · |
| 159 | `O04_shovill_lis` | fastp,shovill | shovill | fastp | · | · |
| 160 | `O05_shovill_sal` | fastp,shovill | shovill | fastp | · | · |
| 161 | `O06_shovill_cam` | fastp,shovill | shovill | fastp | · | · |
| 162 | `O07_unicycler_lis` | fastp,unicycler | unicycler | fastp | · | · |
| 163 | `O08_unicycler_eco` | fastp,unicycler | unicycler | fastp | · | · |
| 164 | `O09_unicycler_cam` | bowtie,spades | unicycler | bowtie,spades | unicycler | · |
| 165 | `O10_plasmidspades_eco` | fastp,plasmidspades | plasmidspades | fastp | · | · |
| 166 | `P01_chopper_flye_mlst_lis` | chopper,flye,mlst | chopper,flye,mlst | · | · | · |
| 167 | `P02_chopper_flye_mlst_sal` | chopper,flye,mlst | chopper,flye,mlst | · | · | · |
| 168 | `P03_chopper_flye_mlst_eco` | chopper,flye,mlst | chopper,flye,mlst | · | · | · |
| 169 | `P04_chopper_flye_mlst_cam` | chopper,flye,mlst | chopper,flye,mlst | · | · | · |
| 170 | `P05_chopper_flye_abricate_lis` | chopper,flye,abricate | chopper,flye,abricate | · | · | · |
| 171 | `P06_chopper_flye_abricate_eco` | chopper,flye,abricate | chopper,flye,abricate | · | · | · |
| 172 | `P07_chopper_flye_abricate_sal` | chopper,flye,abricate | chopper,flye,abricate | · | · | · |
| 173 | `P08_chopper_flye_prokka_lis` | chopper,flye,prokka | chopper,flye,prokka | · | · | · |
| 174 | `P09_chopper_flye_chewbbaca_lis` | chopper,flye,chewbbaca | chopper,flye,chewbbaca | · | · | · |
| 175 | `P10_chopper_flye_chewbbaca_sal` | chopper,flye,chewbbaca | chopper,flye,chewbbaca | · | · | · |
| 176 | `Q01_kmerfinder_fastp_spades_lis` | fastp,spades,kmerfinder | fastp,spades,kmerfinder | · | · | · |
| 177 | `Q02_kmerfinder_fastp_spades_eco` | fastp,spades,kmerfinder | fastp,spades,kmerfinder | · | · | · |
| 178 | `Q03_kmerfinder_fastp_spades_sal` | fastp,spades,kmerfinder | fastp,spades,kmerfinder | · | · | · |
| 179 | `Q04_kmerfinder_fastp_shovill_lis` | fastp,shovill,kmerfinder | fastp,shovill,kmerfinder | · | · | · |
| 180 | `Q05_kmerfinder_fastp_shovill_eco` | fastp,shovill,kmerfinder | fastp,shovill,kmerfinder | · | · | · |
| 183 | `Q08_mash_fastp_spades_eco` | fastp,spades,mash | fastp,spades,mash | · | · | · |
| 184 | `Q09_mash_fastp_spades_sal` | fastp,spades,mash | fastp,spades,mash | · | · | · |
| 185 | `Q10_mash_fastp_shovill_lis` | fastp,shovill,mash | fastp,shovill,mash | · | · | · |
| 186 | `R01_kmerfinder_cam` | kmerfinder | kmerfinder | · | · | · |
| 187 | `R02_kmerfinder_sal` | kraken,kmerfinder,fastq,fastp | kmerfinder | fastq,fastp,kraken | · | · |
| 188 | `R03_mash_sal` | fastp,fastq,kraken,mash | mash | fastq,fastp,kraken | · | · |
| 189 | `R04_mash_eco` | mash | mash | · | · | · |
| 190 | `R05_kraken2_lis` | kraken2 | kraken2 | · | · | · |
| 191 | `R06_kraken2_eco` | fastp,kraken2 | kraken2 | fastp | · | · |
| 192 | `R07_kraken2_sal` | fastp,kraken2 | kraken2 | fastp | · | · |
| 193 | `R08_kraken2_cam` | fastp,kraken2 | kraken2 | fastp | · | · |
| 194 | `S01_fastp_lis` | fastq,trimmomatic,fastp,kraken | fastp | fastq,trimmomatic,kraken | · | · |
| 195 | `S02_fastp_sal` | fastq,trimmomatic,fastp,kraken | fastp | fastq,trimmomatic,kraken | · | · |
| 196 | `S03_trimmomatic_eco` | fastq,trimmomatic,fastp,kraken | trimmomatic | fastq,fastp,kraken | · | · |
| 197 | `S04_trimmomatic_cam` | trimmomatic | trimmomatic | · | · | · |
| 198 | `S05_chopper_lis` | chopper | chopper | · | · | · |
| 199 | `S06_chopper_sal` | chopper | chopper | · | · | · |
| 200 | `S07_chopper_cam` | chopper | chopper | · | · | · |

## Failure detail (one section per failing prompt)

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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    step_4TY_cgMLST__chewbbaca(getAssembly(), params.genus_species, params.schema)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `A06_cgmlst_salmonella` — `missing_param`

**Prompt:** Generate cgMLST allelic profiles starting from a Salmonella enterica assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `A07_flaa_campylobacter` — `missing_param`

**Prompt:** Run flaA typing on a Campylobacter assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `B01_spades_listeria` — `silent_no_op`

**Prompt:** De novo genome assembly with SPAdes from Illumina paired-end reads of Listeria monocytogenes.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `B03_unicycler_salmonella` — `missing_param`

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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { getDS; getHost; getReference; getReferenceOptional; getSingleInput } from '../functions/parameters.nf'

include { module_denovo } from '../modules/module_denovo'

include { module_draft_genome } from '../modules/module_draft_genome'

include { module_scaffolds_filtering } from '../modules/module_scaffolds_filtering'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_vdraft {
    
    take:
        
        reads
        
        host
        
        reference
        
        referenceGB
        
        abricateDatabase
        
    
    main:
        denovoOut = module_denovo(reads, host)

        denovoOut.assembled
            .cross(reference) { extractKey(it) }
            .cross(abricateDatabase) { extractKey(it) }.multiMap {
                assembly: it[0][0][0..1]
                reference: it[0][1]
                abricateDatabase: it[1]
            }.set { cARA }
        module_scaffolds_filtering(cARA.assembly, cARA.reference, cARA.abricateDatabase)

        denovoOut.depleted
            .cross(reference) { extractKey(it) }
            .cross(referenceGB) { extractKey(it) }
            .multiMap {
                depleted: it[0][0][0..1]
                reference: it[0][1]
                referenceGB: it[1]
            }
            .set { cDR }
        module_draft_genome(cDR.depleted, cDR.reference, cDR.referenceGB)
    
}

// --- ENTRYPOINT ---
workflow {
    module_vdraft(getSingleInput(), getHost(), getReference('fa'), getReferenceOptional('gb'), Channel.of([ getDS(), 'viruses_TREF' ]))
}
```
**Error excerpt:**
```
ERROR ~ missing required param: hosts_dir
```

### `C02_mash` — `silent_no_op`

**Prompt:** Run Mash sketch-based species identification on paired-end Illumina reads.

**Steps (LLM):** `step_3TX_species__mash`
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

include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    step_3TX_species__mash(getSingleInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `C03_kraken2` — `missing_param`

**Prompt:** Taxonomic classification of paired-end Illumina reads with Kraken2.

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

include { getEmpty } from '../functions/common.nf'

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_3TX_class__kraken2 } from '../steps/step_3TX_class__kraken2'

include { multi_clustering__reportree } from '../multi/multi_clustering__reportree'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        reads
        
    
    main:
        kraken2_out = step_3TX_class__kraken2(reads)
        multi_clustering__reportree(inputFn(), param('metadata'), param('geodata'), optionalOrDefault('multi_clustering__reportree__nomenclature', getEmpty()))
    
    emit:
        
        genus_report = kraken2_out.genus_report
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: multi_clustering__reportree__summary_columns
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_filtering__bowtie } from '../steps/step_1PP_filtering__bowtie'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_filtered_denovo {
    
    take:
        
        reads
        
        reference
        
    
    main:
        reads.cross(reference) { extractKey(it) }.multiMap {
            reads: it[0]
            refs:  it[1][1..3]
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

### `E03_cgmlst_sal_fastp_spades` — `silent_no_op`

**Prompt:** Generate cgMLST profiles for Salmonella enterica starting from paired-end Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_mapping__bowtie, step_2AS_mapping__ivar, step_4TY_cgMLST__chewbbaca`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getReference; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_mapping__ivar } from '../steps/step_2AS_mapping__ivar'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    trimmed.cross(getReference('fa')) { extractKey(it) }
        .multiMap {
            reads: it[0]
            refs:  it[1][1..3]
        }.set { input }

    mapped = step_2AS_mapping__bowtie(input.reads, input.refs).consensus

    ivar_out = step_2AS_mapping__ivar(input.reads, input.refs)

    step_4TY_cgMLST__chewbbaca(ivar_out.consensus, params.genus_species, params.schema)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `E05_flaa_cam` — `arity_error`

**Prompt:** flaA typing pipeline for Campylobacter from paired-end Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_flaA__flaA`
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

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        trimmed
        
    
    main:
        trimmed_out = step_1PP_trimming__fastp(trimmed)
        assembly_out = step_2AS_denovo__spades(trimmed_out.trimmed)
        step_4TY_flaA__flaA(assembly_out.assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance(getSingleInput())
}
```
**Error excerpt:**
```
ERROR ~ Workflow `module_surveillance:step_4TY_flaA__flaA` declares 2 input channels but 1 were given
```

### `E07_abricate_eco` — `silent_no_op`

**Prompt:** Resistance gene detection with ABRicate on Escherichia coli from Illumina paired FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka, step_4AN_AMR__abricate`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getEmpty } from '../functions/common.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4AN_genes__prokka(assembled.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

    step_4AN_AMR__abricate(assembled)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `E11_cgmlst_lis_shovill` — `silent_no_op`

**Prompt:** Listeria cgMLST starting from Illumina paired reads: trim, Shovill assembly, chewbbaca typing.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_cgMLST__chewbbaca`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__shovill(trimmed).assembly
    step_4TY_cgMLST__chewbbaca(assembly, params.genus_species, params.schema)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `E13_abricate_sal` — `silent_no_op`

**Prompt:** Antimicrobial resistance gene screening with ABRicate for Salmonella enterica from paired Illumina FASTQ.

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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads)

        assembly = step_2AS_denovo__spades(trimmed.trimmed)

        step_4AN_AMR__abricate(assembly.assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance(getSingleInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `E14_prokka_eco` — `silent_no_op`

**Prompt:** Annotate an E. coli assembly with Prokka, starting from paired Illumina reads.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka`
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

include { getEmpty } from '../functions/common.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4AN_genes__prokka(assembled.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `F02_prokka_assembly` — `missing_param`

**Prompt:** Annotate a bacterial genome assembly with Prokka.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `H02_mlst_plus_flaa_cam` — `missing_param`

**Prompt:** Comprehensive Campylobacter typing from paired Illumina FASTQ: MLST + flaA.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4AN_AMR__staramr, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4TY_cgMLST__chewbbaca`
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getAssembly; getTrimmedReads } from '../functions/parameters.nf'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

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

### `I02_mash_fastp_shovill` — `no_code`

**Prompt:** Species sketch with Mash plus assembly via fastp + Shovill from paired Illumina reads.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `K06_chewbbaca_eco_fastp_spades` — `missing_param`

**Prompt:** cgMLST allelic profiling on Escherichia coli from paired-end Illumina FASTQ (fastp + spades + chewbbaca).

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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput; getVCFs; optionalOrDefault; param } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { multi_clustering__reportree } from '../multi/multi_clustering__reportree'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        input
        
    
    main:
        multi_clustering__reportree(input, param('metadata'), param('geodata'), optionalOrDefault('multi_clustering__reportree__nomenclature', getEmpty()))
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_cgMLST__chewbbaca(assembled, 'Escherichia coli', 'ecoli')

    module_surveillance(getVCFs())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: multi_clustering__reportree__summary_columns
```

### `K12_prokka_lis_fastp_spades` — `missing_param`

**Prompt:** Prokka annotation on Listeria monocytogenes from paired-end Illumina FASTQ (fastp + spades + prokka).

**Steps (LLM):** `(none)`
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

include { getDS; getHost; getReference; getReferenceOptional; getSingleInput } from '../functions/parameters.nf'

include { module_denovo } from '../modules/module_denovo'

include { module_draft_genome } from '../modules/module_draft_genome'

include { module_scaffolds_filtering } from '../modules/module_scaffolds_filtering'

include { extractKey } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_vdraft {
    
    take:
        
        reads
        
        host
        
        reference
        
        referenceGB
        
        abricateDatabase
        
    
    main:
        denovoOut = module_denovo(reads, host)

        denovoOut.assembled
            .cross(reference) { extractKey(it) }
            .cross(abricateDatabase) { extractKey(it) }.multiMap {
                assembly: it[0][0][0..1]
                reference: it[0][1]
                abricateDatabase: it[1]
            }.set { cARA }
        module_scaffolds_filtering(cARA.assembly, cARA.reference, cARA.abricateDatabase)

        denovoOut.depleted
            .cross(reference) { extractKey(it) }
            .cross(referenceGB) { extractKey(it) }
            .multiMap {
                depleted: it[0][0][0..1]
                reference: it[0][1]
                referenceGB: it[1]
            }
            .set { cDR }
        module_draft_genome(cDR.depleted, cDR.reference, cDR.referenceGB)
    
}

// --- ENTRYPOINT ---
workflow {
    module_vdraft(getSingleInput(), getHost(), getReference('fa'), getReferenceOptional('gb'), Channel.of([ getDS(), 'viruses_TREF' ]))
}
```
**Error excerpt:**
```
ERROR ~ missing required param: hosts_dir
```

### `K16_flaA_cam_fastp_spades` — `silent_no_op`

**Prompt:** flaA typing on Campylobacter jejuni from paired-end Illumina FASTQ (fastp + spades + flaA).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_flaA__flaA`
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

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput; param } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_flaA__flaA(assembled, param('genus_species'))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `K21_mlst_cam_fastp_shovill` — `silent_no_op`

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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembly = step_2AS_denovo__shovill(trimmed).assembly

    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `K22_chewbbaca_lis_fastp_shovill` — `no_code`

**Prompt:** cgMLST allelic profiling on Listeria monocytogenes from paired-end Illumina FASTQ (fastp + shovill + chewbbaca).

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `K23_chewbbaca_eco_fastp_shovill` — `file_not_found`

**Prompt:** cgMLST allelic profiling on Escherichia coli from paired-end Illumina FASTQ (fastp + shovill + chewbbaca).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_cgMLST__chewbbaca`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__shovill(trimmed).assembly
    step_4TY_cgMLST__chewbbaca(assembly, params.genus_species, params.schema)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.105.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K24_chewbbaca_sal_fastp_shovill` — `file_not_found`

**Prompt:** cgMLST allelic profiling on Salmonella enterica from paired-end Illumina FASTQ (fastp + shovill + chewbbaca).

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill, step_4TY_cgMLST__chewbbaca`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__shovill(trimmed).assembly
    step_4TY_cgMLST__chewbbaca(assembly, params.genus_species, params.schema)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.105.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `K41_chewbbaca_sal_fastp_unicycler` — `silent_no_op`

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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__unicycler(trimmed).assembled

    step_4TY_cgMLST__chewbbaca(assembled, params.genus_species, params.schema)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `K58_chewbbaca_sal_trimmomatic_spades` — `silent_no_op`

**Prompt:** cgMLST allelic profiling on Salmonella enterica from paired-end Illumina FASTQ (trimmomatic + spades + chewbbaca).

**Steps (LLM):** `step_1PP_trimming__trimmomatic, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'

// --- GLOBALS ---

def species = 'salmonella_enterica'

def schema = 's_enterica_chewie_3255_210531'

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__trimmomatic(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_cgMLST__chewbbaca(assembled, species, schema)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `L01_mlst_chewbbaca_lis` — `file_not_found`

**Prompt:** From paired Illumina FASTQ of Listeria monocytogenes: trim with fastp, assemble with SPAdes, then run mlst and chewbbaca in parallel.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_MLST__mlst(assembled)
    step_4TY_cgMLST__chewbbaca(assembled, 'listeria_monocytogenes', null)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.115.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `L06_chewbbaca_abricate_lis` — `silent_no_op`

**Prompt:** From paired Illumina FASTQ of Listeria monocytogenes: trim with fastp, assemble with SPAdes, then run chewbbaca and abricate in parallel.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca, step_4AN_AMR__abricate`
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_cgMLST__chewbbaca(assembled, params.genus_species, params.schema)
    step_4AN_AMR__abricate(assembled)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `L08_chewbbaca_prokka_sal` — `silent_no_op`

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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { extractKey; getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_assembly_and_typing {
    
    take:
        
        trimmed
        
    
    main:
        assembly = step_2AS_denovo__spades(trimmed).assembled

        assembly.cross(params.genus_species) { extractKey(it) }
            .cross(params.schema) { extractKey(it) }
            .multiMap {
                assembly: it[0][0]
                genus_species: it[0][1]
                schema: it[1]
            }.set { cgmlst_input }

        step_4TY_cgMLST__chewbbaca(cgmlst_input.assembly, cgmlst_input.genus_species, cgmlst_input.schema)

        prokka_input = assembly.map { [ it[0], it[1], params.kingdom, '-', '-', getEmpty() ] }
        step_4AN_genes__prokka(prokka_input)
    
}

// --- ENTRYPOINT ---
workflow {
    wf_assembly_and_typing(step_1PP_trimming__fastp(getSingleInput()).trimmed)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `L13_mlst_flaA_cam` — `silent_no_op`

**Prompt:** From paired Illumina FASTQ of Campylobacter jejuni: trim with fastp, assemble with SPAdes, then run mlst and flaA in parallel.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_flaA__flaA`
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

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput; param } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_MLST__mlst(assembled)
    step_4TY_flaA__flaA(assembled, param('genus_species'))
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `L20_mlst_prokka_lis` — `silent_no_op`

**Prompt:** From paired Illumina FASTQ of Listeria monocytogenes: trim with fastp, assemble with SPAdes, then run mlst and prokka in parallel.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4AN_genes__prokka`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_genes__prokka, step_4TY_MLST__mlst`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getEmpty } from '../functions/common.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_MLST__mlst(assembled)

    step_4AN_genes__prokka(assembled.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `M01_mlst+chewbbaca+abricate_lis` — `file_not_found`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Listeria monocytogenes from paired Illumina FASTQ: trim, assemble, then run mlst, chewbbaca, abricate in parallel on the assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca, step_4AN_AMR__abricate`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__abricate, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'
include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'
include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4TY_cgMLST__chewbbaca(assembled, param('genus_species'), optionalOrDefault('schema', ''))
    step_4AN_AMR__abricate(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembly = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_MLST__mlst(assembly)
    step_4TY_cgMLST__chewbbaca(assembly, params.genus_species, params.schema)
    step_4AN_AMR__abricate(assembly)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.121.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `M02_mlst+chewbbaca+prokka_sal` — `file_not_found`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Salmonella enterica from paired Illumina FASTQ: trim, assemble, then run mlst, chewbbaca, prokka in parallel on the assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca, step_4AN_genes__prokka`
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getEmpty } from '../functions/common.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembly = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_MLST__mlst(assembly)
    step_4TY_cgMLST__chewbbaca(assembly, params.genus_species, params.schema)
    step_4AN_genes__prokka(assembly.map { [ it[0], it[1], params.kingdom, '-', '-', getEmpty() ] })
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.SAL.118.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `M04_mlst+abricate+prokka_lis` — `silent_no_op`

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

include { getEmpty } from '../functions/common.nf'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_assembly_and_typing {
    
    take:
        
        trimmed
        
    
    main:
        assembly = step_2AS_denovo__spades(trimmed).assembled
        step_4TY_MLST__mlst(assembly)
        step_4AN_AMR__abricate(assembly)
        step_4AN_genes__prokka(assembly.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
    
    emit:
        
        assembly
        
    
}

workflow wf_trimming {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed
    
    emit:
        
        trimmed
        
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = wf_trimming(getSingleInput())
    assembly = wf_assembly_and_typing(trimmed)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `M05_mlst+flaA+staramr_cam` — `silent_no_op`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Campylobacter jejuni from paired Illumina FASTQ: trim, assemble, then run mlst, flaA, staramr in parallel on the assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_flaA__flaA, step_4AN_AMR__staramr`
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
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_surveillance {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads)

        assembly = step_2AS_denovo__spades(trimmed.trimmed)

        step_4TY_MLST__mlst(assembly.assembled)
        step_4TY_flaA__flaA(assembly.assembled)
        step_4AN_AMR__staramr(assembly.assembled)
    
}

// --- ENTRYPOINT ---
workflow {
    module_surveillance(getSingleInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `M07_flaA+staramr+prokka_cam` — `silent_no_op`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Campylobacter jejuni from paired Illumina FASTQ: trim, assemble, then run flaA, staramr, prokka in parallel on the assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_flaA__flaA, step_4AN_AMR__staramr, step_4AN_genes__prokka`
**Steps (GT):**  `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4AN_AMR__staramr, step_4AN_genes__prokka, step_4TY_flaA__flaA`

**Ground truth (passes validation):**
```groovy
nextflow.enable.dsl=2

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'
include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'
include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'
include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'
include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'
include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'
workflow {
    trimmed   = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_flaA__flaA(assembled, param('genus_species'))
    step_4AN_AMR__staramr(assembled, param('genus_species'))
    step_4AN_genes__prokka(assembled)
}
```
**LLM-generated (failed):**
```groovy
nextflow.enable.dsl=2

// --- IMPORTS ---

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getEmpty } from '../functions/common.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4AN_AMR__staramr } from '../steps/step_4AN_AMR__staramr'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput())
    assembly = step_2AS_denovo__spades(trimmed.trimmed)

    step_4TY_flaA__flaA(assembly.assembled)
    step_4AN_AMR__staramr(assembly.assembled)
    step_4AN_genes__prokka(assembly.assembled.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `M09_chewbbaca+abricate+prokka_lis` — `file_not_found`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Listeria monocytogenes from paired Illumina FASTQ: trim, assemble, then run chewbbaca, abricate, prokka in parallel on the assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_cgMLST__chewbbaca, step_4AN_AMR__abricate, step_4AN_genes__prokka`
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

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getEmpty } from '../functions/common.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_cgMLST__chewbbaca(assembled, params.genus_species, params.schema)
    step_4AN_AMR__abricate(assembled)
    step_4AN_genes__prokka(assembled.map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.123.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `N06_canonical_cgmlst_eco` — `file_not_found`

**Prompt:** Standard cgMLST pipeline (fastp + SPAdes + chewbbaca) on paired Illumina FASTQ of Escherichia coli.

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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_4TY_cgMLST__chewbbaca(assembled, params.genus_species, params.schema)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.ECO.121.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `NA02_mlst_sal_assembly` — `silent_no_op`

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

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { getAssembly } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    step_4TY_MLST__mlst(getAssembly())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `NA04_abricate_sal_assembly` — `silent_no_op`

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

include { getAssembly } from '../functions/parameters.nf'

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    step_4AN_AMR__abricate(getAssembly())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `NA06_prokka_sal_assembly` — `silent_no_op`

**Prompt:** Run prokka on a pre-existing Salmonella enterica assembly.

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

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getAssembly } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    step_4AN_genes__prokka(getAssembly().map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `NA07_prokka_cam_assembly` — `silent_no_op`

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

include { step_4AN_genes__prokka } from '../steps/step_4AN_genes__prokka'

include { getAssembly } from '../functions/parameters.nf'

include { getEmpty } from '../functions/common.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    step_4AN_genes__prokka(getAssembly().map { [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `O02_spades_sal` — `silent_no_op`

**Prompt:** De novo assembly with spades from paired Illumina FASTQ of Salmonella enterica.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `O03_spades_cam` — `silent_no_op`

**Prompt:** De novo assembly with spades from paired Illumina FASTQ of Campylobacter jejuni.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `O04_shovill_lis` — `silent_no_op`

**Prompt:** De novo assembly with shovill from paired Illumina FASTQ of Listeria monocytogenes.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__shovill`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembly = step_2AS_denovo__shovill(trimmed).assembly
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `O08_unicycler_eco` — `silent_no_op`

**Prompt:** De novo assembly with unicycler from paired Illumina FASTQ of Escherichia coli.

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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__unicycler(trimmed).assembled
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `O09_unicycler_cam` — `missing_param`

**Prompt:** De novo assembly with unicycler from paired Illumina FASTQ of Campylobacter jejuni.

**Steps (LLM):** `step_1PP_hostdepl__bowtie, step_2AS_denovo__spades`
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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { extractKey } from '../functions/common.nf'

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
ERROR ~ missing required param: hosts_dir
```

### `P03_chopper_flye_mlst_eco` — `silent_no_op`

**Prompt:** Nanopore pipeline for Escherichia coli: chopper trimming + Flye assembly + mlst.

**Steps (LLM):** `step_1PP_trimming__chopper, step_2AS_denovo__flye, step_4TY_MLST__mlst`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'

include { step_2AS_denovo__flye } from '../steps/step_2AS_denovo__flye'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__chopper(getSingleInput()).trimmed
    assembly = step_2AS_denovo__flye(trimmed).assembly
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `P04_chopper_flye_mlst_cam` — `silent_no_op`

**Prompt:** Nanopore pipeline for Campylobacter jejuni: chopper trimming + Flye assembly + mlst.

**Steps (LLM):** `step_1PP_trimming__chopper, step_2AS_denovo__flye, step_4TY_MLST__mlst`
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'

include { step_2AS_denovo__flye } from '../steps/step_2AS_denovo__flye'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__chopper(getSingleInput()).trimmed
    assembly = step_2AS_denovo__flye(trimmed).assembly
    step_4TY_MLST__mlst(assembly)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'

include { step_2AS_denovo__flye } from '../steps/step_2AS_denovo__flye'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__chopper(getSingleInput()).trimmed
    assembly = step_2AS_denovo__flye(trimmed).assembly
    step_4TY_cgMLST__chewbbaca(assembly, params.genus_species, params.schema)
}
```
**Error excerpt:**
```
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.133.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `Q04_kmerfinder_fastp_shovill_lis` — `silent_no_op`

**Prompt:** In parallel, identify the species with kmerfinder and trim+assemble paired Illumina FASTQ of Listeria monocytogenes with fastp + shovill.

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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembly = step_2AS_denovo__shovill(trimmed).assembly

    species = step_3TX_species__kmerfinder(assembly).assigned_species
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `Q06_kmerfinder_fastp_shovill_sal` — `no_code`

**Prompt:** In parallel, identify the species with kmerfinder and trim+assemble paired Illumina FASTQ of Salmonella enterica with fastp + shovill.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
no nextflow_code after max turns
```

### `Q07_mash_fastp_spades_lis` — `no_code`

**Prompt:** In parallel, identify the species with mash and trim+assemble paired Illumina FASTQ of Listeria monocytogenes with fastp + spades.

**Steps (LLM):** `(none)`
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

```
**Error excerpt:**
```
http exception: HTTPConnectionPool(host='127.0.0.1', port=8765): Read timed out. (read timeout=180)
```

### `Q08_mash_fastp_spades_eco` — `silent_no_op`

**Prompt:** In parallel, identify the species with mash and trim+assemble paired Illumina FASTQ of Escherichia coli with fastp + spades.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__mash`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_3TX_species__mash(assembled)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `Q09_mash_fastp_spades_sal` — `silent_no_op`

**Prompt:** In parallel, identify the species with mash and trim+assemble paired Illumina FASTQ of Salmonella enterica with fastp + spades.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__mash`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'

include { getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    step_3TX_species__mash(assembled)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `R02_kmerfinder_sal` — `missing_param`

**Prompt:** kmerfinder on paired Illumina FASTQ of Salmonella enterica.

**Steps (LLM):** `step_3TX_class__kraken, step_3TX_species__kmerfinder, step_0SQ_rawreads__fastq, step_1PP_trimming__fastp`
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

include { getInput } from '../functions/parameters.nf'

include { step_3TX_class__kraken } from '../steps/step_3TX_class__kraken'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_taxonomy_classification {
    
    take:
        
        trimmed
        
    
    main:
        kraken_out = step_3TX_class__kraken(trimmed)
    
    emit:
        
        genus_report = kraken_out.genus_report
        
    
}

workflow wf_species_identification {
    
    take:
        
        trimmed
        
    
    main:
        kmerfinder_out = step_3TX_species__kmerfinder(trimmed)
    
    emit:
        
        assigned_species = kmerfinder_out.assigned_species
        
    
}

// --- ENTRYPOINT ---
workflow {
    step_0SQ_rawreads__fastq(getInput())
    trimmed = step_1PP_trimming__fastp(getInput()).trimmed
    wf_taxonomy_classification(trimmed)
    wf_species_identification(trimmed)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_class__kraken__db_kraken
```

### `R03_mash_sal` — `missing_param`

**Prompt:** mash on paired Illumina FASTQ of Salmonella enterica.

**Steps (LLM):** `step_1PP_trimming__fastp, step_0SQ_rawreads__fastq, step_3TX_class__kraken, step_3TX_species__mash`
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

include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_3TX_class__kraken } from '../steps/step_3TX_class__kraken'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(step_0SQ_rawreads__fastq(getSingleInput()))

    kraken_out = step_3TX_class__kraken(trimmed.trimmed)

    step_3TX_species__mash(kraken_out.genus_report)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_class__kraken__db_kraken
```

### `R05_kraken2_lis` — `silent_no_op`

**Prompt:** kraken2 on paired Illumina FASTQ of Listeria monocytogenes.

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

include { step_3TX_class__kraken2 } from '../steps/step_3TX_class__kraken2'

include { getSingleInput } from '../functions/parameters.nf'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    step_3TX_class__kraken2(getSingleInput()).genus_report
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `R08_kraken2_cam` — `silent_no_op`

**Prompt:** kraken2 on paired Illumina FASTQ of Campylobacter jejuni.

**Steps (LLM):** `step_1PP_trimming__fastp, step_3TX_class__kraken2`
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

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_class__kraken2 } from '../steps/step_3TX_class__kraken2'

include { module_qc_fastqc } from '../modules/module_qc_fastqc'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    module_qc_fastqc(getSingleInput())

    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    kraken_out = step_3TX_class__kraken2(trimmed)

    module_qc_fastqc(trimmed)

    kraken_out.genus_report
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `S01_fastp_lis` — `silent_no_op`

**Prompt:** fastp read trimming on illumina paired FASTQ of Listeria monocytogenes.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__trimmomatic, step_1PP_trimming__fastp, step_3TX_class__kraken`
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

include { getInput; hasEnoughFastqData; hasFastqData; isIlluminaPaired; isIonTorrent; isNanopore } from '../functions/parameters.nf'

include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'

include { isBacterium } from '../functions/sampletypes.nf'

include { step_3TX_class__kraken } from '../steps/step_3TX_class__kraken'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_reads_processing {
    
    take:
        
        rawReads
        
    
    main:
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

        trimming_by_seqtype.illumina.branch {
            bacteria: isBacterium(it)
            other: true
        }
        .set { trimming_illumina }

        // trimmomatic
        trimmed_by_trimmomatic = step_1PP_trimming__trimmomatic(trimming_illumina.other).trimmed

        // fastp
        trimmed_by_fastp = step_1PP_trimming__fastp(trimming_by_seqtype.ion.mix(trimming_illumina.bacteria)).trimmed

        trimmed_by_trimmomatic.mix(trimmed_by_fastp).branch {
            with_data: hasEnoughFastqData(it[1])
            insufficient_number_of_reads: true
        }
        .set { trimmed_branched }
        step_3TX_class__kraken(trimmed_branched.with_data)
    
    emit:
        
        no_reads = rawreads_branched.no_reads
        
        trimmed_with_data = trimmed_branched.with_data
        
        insufficient_number_of_reads = trimmed_branched.insufficient_number_of_reads
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_reads_processing(getInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `S02_fastp_sal` — `missing_param`

**Prompt:** fastp read trimming on illumina paired FASTQ of Salmonella enterica.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__trimmomatic, step_1PP_trimming__fastp, step_3TX_class__kraken`
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

include { getInput; hasEnoughFastqData; hasFastqData; isIlluminaPaired; isIonTorrent; isNanopore } from '../functions/parameters.nf'

include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'

include { isBacterium } from '../functions/sampletypes.nf'

include { step_3TX_class__kraken } from '../steps/step_3TX_class__kraken'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_reads_processing {
    
    take:
        
        rawReads
        
    
    main:
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

        trimming_by_seqtype.illumina.branch {
            bacteria: isBacterium(it)
            other: true
        }
        .set { trimming_illumina }

        // trimmomatic
        trimmed_by_trimmomatic = step_1PP_trimming__trimmomatic(trimming_illumina.other).trimmed

        // fastp
        trimmed_by_fastp = step_1PP_trimming__fastp(trimming_by_seqtype.ion.mix(trimming_illumina.bacteria)).trimmed

        trimmed_by_trimmomatic.mix(trimmed_by_fastp).branch {
            with_data: hasEnoughFastqData(it[1])
            insufficient_number_of_reads: true
        }
        .set { trimmed_branched }
        step_3TX_class__kraken(trimmed_branched.with_data)
    
    emit:
        
        no_reads = rawreads_branched.no_reads
        
        trimmed_with_data = trimmed_branched.with_data
        
        insufficient_number_of_reads = trimmed_branched.insufficient_number_of_reads
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_reads_processing(getInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_class__kraken__db_kraken
```

### `S03_trimmomatic_eco` — `missing_param`

**Prompt:** trimmomatic read trimming on illumina paired FASTQ of Escherichia coli.

**Steps (LLM):** `step_0SQ_rawreads__fastq, step_1PP_trimming__trimmomatic, step_1PP_trimming__fastp, step_3TX_class__kraken`
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

include { getInput; hasEnoughFastqData; hasFastqData; isIlluminaPaired; isIonTorrent; isNanopore } from '../functions/parameters.nf'

include { step_1PP_trimming__trimmomatic } from '../steps/step_1PP_trimming__trimmomatic'

include { isBacterium } from '../functions/sampletypes.nf'

include { step_3TX_class__kraken } from '../steps/step_3TX_class__kraken'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_0SQ_rawreads__fastq } from '../steps/step_0SQ_rawreads__fastq'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow module_reads_processing {
    
    take:
        
        rawReads
        
    
    main:
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

        trimming_by_seqtype.illumina.branch {
            bacteria: isBacterium(it)
            other: true
        }
        .set { trimming_illumina }

        // trimmomatic
        trimmed_by_trimmomatic = step_1PP_trimming__trimmomatic(trimming_illumina.other).trimmed

        // fastp
        trimmed_by_fastp = step_1PP_trimming__fastp(trimming_by_seqtype.ion.mix(trimming_illumina.bacteria)).trimmed

        trimmed_by_trimmomatic.mix(trimmed_by_fastp).branch {
            with_data: hasEnoughFastqData(it[1])
            insufficient_number_of_reads: true
        }
        .set { trimmed_branched }
        step_3TX_class__kraken(trimmed_branched.with_data)
    
    emit:
        
        no_reads = rawreads_branched.no_reads
        
        trimmed_with_data = trimmed_branched.with_data
        
        insufficient_number_of_reads = trimmed_branched.insufficient_number_of_reads
        
    
}

// --- ENTRYPOINT ---
workflow {
    module_reads_processing(getInput())
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_class__kraken__db_kraken
```

### `S07_chopper_cam` — `silent_no_op`

**Prompt:** chopper read trimming on nanopore FASTQ of Campylobacter jejuni.

**Steps (LLM):** `step_1PP_trimming__chopper`
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

include { step_1PP_trimming__chopper } from '../steps/step_1PP_trimming__chopper'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    step_1PP_trimming__chopper(getSingleInput())
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```
