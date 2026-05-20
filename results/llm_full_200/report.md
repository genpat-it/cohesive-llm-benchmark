# LLM evaluation — detailed report

Total prompts: **200**  ·  generated code: **200**  ·  syntactically valid: **200**  ·  semantically valid: **185**

Step-set vs. ground truth:  exact match **161**  ·  extra steps **36**  ·  missing steps **13**  ·  hallucinated (non-existent) steps **0**

## Error category breakdown

| Category | Count | Meaning |
|----|----|----|
| `none` | 181 | no error — pipeline passes |
| `missing_param` | 8 | step requires a param() that was not supplied |
| `ngsmanager_naming` | 5 | input file name does not match parseMetadataFromFileName regex |
| `silent_no_op` | 3 | DAG empty — pipeline runs but produces no output |
| `partial_dag` | 2 | only some of the expected processes appeared in the DAG |
| `file_not_found` | 1 | expected input file is not in the framework layout |

## Per-prompt outcome

| # | id | code? | syntax | semantic | procs | error category | first 80 chars of detail |
|---|----|-------|--------|----------|-------|----------------|------|
| 1 | `A01_mlst_listeria` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 2 | `A02_mlst_ecoli` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 3 | `A03_mlst_salmonella` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 4 | `A04_cgmlst_listeria` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 5 | `A05_cgmlst_ecoli` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 6 | `A06_cgmlst_salmonella` | ✅ | ✅ | ❌ | 0/3 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 7 | `A07_flaa_campylobacter` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 8 | `A08_staramr_campylobacter` | ✅ | ✅ | ❌ | 0/1 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 9 | `B01_spades_listeria` | ✅ | ✅ | ❌ | 0/3 | `missing_param` | ERROR ~ missing required param: hosts_dir |
| 10 | `B02_shovill_ecoli` | ✅ | ✅ | ❌ | 0/3 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 11 | `B03_unicycler_salmonella` | ✅ | ✅ | ❌ | 0/3 | `missing_param` | ERROR ~ missing required param: hosts_dir |
| 12 | `B04_plasmidspades` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 13 | `B05_metaspades` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 14 | `C01_kmerfinder` | ✅ | ✅ | ✅ | 7/1 | `none` |  |
| 15 | `C02_mash` | ✅ | ✅ | ✅ | 4/1 | `none` |  |
| 16 | `C03_kraken2` | ✅ | ✅ | ✅ | 2/2 | `none` |  |
| 17 | `D01_fastp_spades_lis` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 18 | `D02_fastp_shovill_eco` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 19 | `D03_trimmomatic_spades` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 20 | `D04_fastp_unicycler_sal` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 21 | `D05_fastp_spades_cam` | ✅ | ✅ | ✅ | 6/6 | `none` |  |
| 22 | `E01_mlst_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 23 | `E02_cgmlst_lis_fastp_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 24 | `E03_cgmlst_sal_fastp_spades` | ✅ | ✅ | ❌ | 0/9 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 25 | `E04_cgmlst_eco_fastp_shovill` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 26 | `E05_flaa_cam` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 27 | `E06_staramr_cam` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 28 | `E07_abricate_eco` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
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
| 43 | `H01_mlst_plus_cgmlst_lis` | ✅ | ✅ | ❌ | 7/10 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.LIS.C.1.1_R1.fastq.gz |
| 44 | `H02_mlst_plus_flaa_cam` | ✅ | ✅ | ❌ | 0/8 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 45 | `H03_prokka_plus_abricate_eco` | ✅ | ✅ | ✅ | 8/8 | `ngsmanager_naming` | ERROR ~ unexpected file name: DS99999-DT260224_2026.ECO.C.1.1_R1.fastq.gz |
| 46 | `H04_mlst_plus_abricate_sal` | ✅ | ✅ | ❌ | 0/8 | `missing_param` | ERROR ~ missing required param: step_3TX_species__kmerfinder__db |
| 47 | `I01_kmerfinder_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 48 | `I02_mash_fastp_shovill` | ✅ | ✅ | ❌ | 4/7 | `partial_dag` | Only 4/7 expected processes appeared in the DAG |
| 49 | `J01_mobsuite_plasmid` | ✅ | ✅ | ✅ | 4/1 | `none` |  |
| 50 | `J02_bbnorm_downsampling` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 51 | `K01_mlst_lis_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 52 | `K02_mlst_eco_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 53 | `K03_mlst_sal_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 54 | `K04_mlst_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 55 | `K05_chewbbaca_lis_fastp_spades` | ✅ | ✅ | ❌ | 6/9 | `file_not_found` | WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/202 |
| 56 | `K06_chewbbaca_eco_fastp_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 57 | `K07_chewbbaca_sal_fastp_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 58 | `K08_abricate_lis_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 59 | `K09_abricate_eco_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 60 | `K10_abricate_sal_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 61 | `K11_abricate_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 62 | `K12_prokka_lis_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 63 | `K13_prokka_eco_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 64 | `K14_prokka_sal_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 65 | `K15_prokka_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 66 | `K16_flaA_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 67 | `K17_staramr_cam_fastp_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 68 | `K18_mlst_lis_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 69 | `K19_mlst_eco_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 70 | `K20_mlst_sal_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 71 | `K21_mlst_cam_fastp_shovill` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 72 | `K22_chewbbaca_lis_fastp_shovill` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 73 | `K23_chewbbaca_eco_fastp_shovill` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 74 | `K24_chewbbaca_sal_fastp_shovill` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
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
| 91 | `K41_chewbbaca_sal_fastp_unicycler` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
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
| 108 | `K58_chewbbaca_sal_trimmomatic_spades` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 109 | `K59_abricate_lis_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 110 | `K60_abricate_eco_trimmomatic_spades` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 111 | `L01_mlst_chewbbaca_lis` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 112 | `L02_mlst_chewbbaca_eco` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 113 | `L03_mlst_chewbbaca_sal` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 114 | `L04_mlst_abricate_lis` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 115 | `L05_mlst_abricate_eco` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 116 | `L06_chewbbaca_abricate_lis` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 117 | `L07_chewbbaca_prokka_lis` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 118 | `L08_chewbbaca_prokka_sal` | ✅ | ✅ | ✅ | 10/10 | `none` |  |
| 119 | `L09_mlst_prokka_eco` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 120 | `L10_mlst_prokka_sal` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 121 | `L11_abricate_prokka_lis` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 122 | `L12_abricate_prokka_sal` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 123 | `L13_mlst_flaA_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 124 | `L14_mlst_staramr_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 125 | `L15_flaA_staramr_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 126 | `L16_flaA_abricate_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 127 | `L17_staramr_abricate_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 128 | `L18_staramr_prokka_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 129 | `L19_flaA_prokka_cam` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 130 | `L20_mlst_prokka_lis` | ✅ | ✅ | ✅ | 8/8 | `none` |  |
| 131 | `M01_mlst+chewbbaca+abricate_lis` | ✅ | ✅ | ❌ | 8/11 | `partial_dag` | Only 8/11 expected processes appeared in the DAG |
| 132 | `M02_mlst+chewbbaca+prokka_sal` | ✅ | ✅ | ✅ | 11/11 | `none` |  |
| 133 | `M03_mlst+abricate+prokka_eco` | ✅ | ✅ | ❌ | 0/9 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 134 | `M04_mlst+abricate+prokka_lis` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 135 | `M05_mlst+flaA+staramr_cam` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 136 | `M06_mlst+flaA+abricate_cam` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 137 | `M07_flaA+staramr+prokka_cam` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 138 | `M08_mlst+staramr+prokka_cam` | ✅ | ✅ | ✅ | 9/9 | `none` |  |
| 139 | `M09_chewbbaca+abricate+prokka_lis` | ✅ | ✅ | ✅ | 11/11 | `none` |  |
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
| 150 | `NA03_abricate_lis_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 151 | `NA04_abricate_sal_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 152 | `NA05_abricate_cam_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 153 | `NA06_prokka_sal_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 154 | `NA07_prokka_cam_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 155 | `NA08_prokka_eco_assembly` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 156 | `O01_spades_lis` | ✅ | ✅ | ❌ | 0/3 | `missing_param` | ERROR ~ missing required param: hosts_dir |
| 157 | `O02_spades_sal` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 158 | `O03_spades_cam` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 159 | `O04_shovill_lis` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 160 | `O05_shovill_sal` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 161 | `O06_shovill_cam` | ✅ | ✅ | ✅ | 8/3 | `none` |  |
| 162 | `O07_unicycler_lis` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 163 | `O08_unicycler_eco` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 164 | `O09_unicycler_cam` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 165 | `O10_plasmidspades_eco` | ✅ | ✅ | ✅ | 6/3 | `none` |  |
| 166 | `P01_chopper_flye_mlst_lis` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 167 | `P02_chopper_flye_mlst_sal` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 168 | `P03_chopper_flye_mlst_eco` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 169 | `P04_chopper_flye_mlst_cam` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 170 | `P05_chopper_flye_abricate_lis` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 171 | `P06_chopper_flye_abricate_eco` | ✅ | ✅ | ✅ | 6/5 | `none` |  |
| 172 | `P07_chopper_flye_abricate_sal` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 173 | `P08_chopper_flye_prokka_lis` | ✅ | ✅ | ✅ | 5/5 | `none` |  |
| 174 | `P09_chopper_flye_chewbbaca_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 175 | `P10_chopper_flye_chewbbaca_sal` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 176 | `Q01_kmerfinder_fastp_spades_lis` | ✅ | ✅ | ❌ | 0/7 | `silent_no_op` | No process placeholders appeared. when: clause filtered everything? |
| 177 | `Q02_kmerfinder_fastp_spades_eco` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 178 | `Q03_kmerfinder_fastp_spades_sal` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 179 | `Q04_kmerfinder_fastp_shovill_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 180 | `Q05_kmerfinder_fastp_shovill_eco` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 181 | `Q06_kmerfinder_fastp_shovill_sal` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 182 | `Q07_mash_fastp_spades_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 183 | `Q08_mash_fastp_spades_eco` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 184 | `Q09_mash_fastp_spades_sal` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 185 | `Q10_mash_fastp_shovill_lis` | ✅ | ✅ | ✅ | 7/7 | `none` |  |
| 186 | `R01_kmerfinder_cam` | ✅ | ✅ | ✅ | 4/1 | `none` |  |
| 187 | `R02_kmerfinder_sal` | ✅ | ✅ | ✅ | 6/1 | `none` |  |
| 188 | `R03_mash_sal` | ✅ | ✅ | ✅ | 1/1 | `none` |  |
| 189 | `R04_mash_eco` | ✅ | ✅ | ✅ | 6/1 | `none` |  |
| 190 | `R05_kraken2_lis` | ✅ | ✅ | ✅ | 7/2 | `none` |  |
| 191 | `R06_kraken2_eco` | ✅ | ✅ | ✅ | 5/2 | `none` |  |
| 192 | `R07_kraken2_sal` | ✅ | ✅ | ✅ | 5/2 | `none` |  |
| 193 | `R08_kraken2_cam` | ✅ | ✅ | ✅ | 7/2 | `none` |  |
| 194 | `S01_fastp_lis` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 195 | `S02_fastp_sal` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 196 | `S03_trimmomatic_eco` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 197 | `S04_trimmomatic_cam` | ✅ | ✅ | ✅ | 3/3 | `none` |  |
| 198 | `S05_chopper_lis` | ✅ | ✅ | ✅ | 2/2 | `none` |  |
| 199 | `S06_chopper_sal` | ✅ | ✅ | ✅ | 2/2 | `none` |  |
| 200 | `S07_chopper_cam` | ✅ | ✅ | ✅ | 2/2 | `none` |  |

## Step-set comparison vs ground truth

| # | id | LLM steps | GT steps | extra | missing | hallucinated |
|---|----|-----------|----------|-------|---------|--------------|
| 1 | `A01_mlst_listeria` | mlst | mlst | · | · | · |
| 2 | `A02_mlst_ecoli` | mlst | mlst | · | · | · |
| 3 | `A03_mlst_salmonella` | mlst | mlst | · | · | · |
| 4 | `A04_cgmlst_listeria` | chewbbaca | chewbbaca | · | · | · |
| 5 | `A05_cgmlst_ecoli` | chewbbaca | chewbbaca | · | · | · |
| 6 | `A06_cgmlst_salmonella` | kmerfinder,chewbbaca | chewbbaca | kmerfinder | · | · |
| 7 | `A07_flaa_campylobacter` | flaA | flaA | · | · | · |
| 8 | `A08_staramr_campylobacter` | kmerfinder,staramr | staramr | kmerfinder | · | · |
| 9 | `B01_spades_listeria` | bowtie,spades | spades | bowtie | · | · |
| 10 | `B02_shovill_ecoli` | shovill | shovill | · | · | · |
| 11 | `B03_unicycler_salmonella` | fastp,bowtie,unicycler | unicycler | bowtie,fastp | · | · |
| 12 | `B04_plasmidspades` | fastp,plasmidspades | plasmidspades | fastp | · | · |
| 13 | `B05_metaspades` | metaspades | metaspades | · | · | · |
| 14 | `C01_kmerfinder` | fastp,spades,kmerfinder | kmerfinder | fastp,spades | · | · |
| 15 | `C02_mash` | fastp,mash | mash | fastp | · | · |
| 16 | `C03_kraken2` | kraken2 | kraken2 | · | · | · |
| 17 | `D01_fastp_spades_lis` | fastp,spades | fastp,spades | · | · | · |
| 18 | `D02_fastp_shovill_eco` | fastp,shovill | fastp,shovill | · | · | · |
| 19 | `D03_trimmomatic_spades` | trimmomatic,spades | trimmomatic,spades | · | · | · |
| 20 | `D04_fastp_unicycler_sal` | fastp,unicycler | fastp,unicycler | · | · | · |
| 21 | `D05_fastp_spades_cam` | fastp,spades | fastp,spades | · | · | · |
| 22 | `E01_mlst_lis` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 23 | `E02_cgmlst_lis_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 24 | `E03_cgmlst_sal_fastp_spades` | fastp,spades,kmerfinder,bowtie,chewbbaca | fastp,spades,chewbbaca | bowtie,kmerfinder | · | · |
| 25 | `E04_cgmlst_eco_fastp_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 26 | `E05_flaa_cam` | fastp,spades,flaA | fastp,spades,flaA | · | · | · |
| 27 | `E06_staramr_cam` | fastp,spades,staramr | fastp,spades,staramr | · | · | · |
| 28 | `E07_abricate_eco` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
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
| 43 | `H01_mlst_plus_cgmlst_lis` | spades,mlst,chewbbaca | fastp,spades,mlst,chewbbaca | · | fastp | · |
| 44 | `H02_mlst_plus_flaa_cam` | fastp,spades,kmerfinder,mlst,flaA | fastp,spades,mlst,flaA | kmerfinder | · | · |
| 45 | `H03_prokka_plus_abricate_eco` | fastp,spades,prokka,abricate | fastp,spades,abricate,prokka | · | · | · |
| 46 | `H04_mlst_plus_abricate_sal` | kmerfinder,bowtie,abricate,prokka,staramr,mlst,flaA,chewbbaca | fastp,spades,abricate,mlst | bowtie,kmerfinder,staramr,prokka,chewbbaca,flaA | fastp,spades | · |
| 47 | `I01_kmerfinder_fastp_spades` | kmerfinder,fastp,spades | fastp,spades,kmerfinder | · | · | · |
| 48 | `I02_mash_fastp_shovill` | mash,shovill | fastp,shovill,mash | · | fastp | · |
| 49 | `J01_mobsuite_plasmid` | fastp,mobsuite | mobsuite | fastp | · | · |
| 50 | `J02_bbnorm_downsampling` | bbnorm | bbnorm | · | · | · |
| 51 | `K01_mlst_lis_fastp_spades` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 52 | `K02_mlst_eco_fastp_spades` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 53 | `K03_mlst_sal_fastp_spades` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 54 | `K04_mlst_cam_fastp_spades` | fastp,spades,mlst | fastp,spades,mlst | · | · | · |
| 55 | `K05_chewbbaca_lis_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 56 | `K06_chewbbaca_eco_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 57 | `K07_chewbbaca_sal_fastp_spades` | fastp,spades,chewbbaca | fastp,spades,chewbbaca | · | · | · |
| 58 | `K08_abricate_lis_fastp_spades` | fastp,spades,resfinder | fastp,spades,abricate | resfinder | abricate | · |
| 59 | `K09_abricate_eco_fastp_spades` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 60 | `K10_abricate_sal_fastp_spades` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 61 | `K11_abricate_cam_fastp_spades` | fastp,spades,abricate | fastp,spades,abricate | · | · | · |
| 62 | `K12_prokka_lis_fastp_spades` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 63 | `K13_prokka_eco_fastp_spades` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 64 | `K14_prokka_sal_fastp_spades` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 65 | `K15_prokka_cam_fastp_spades` | fastp,spades,prokka | fastp,spades,prokka | · | · | · |
| 66 | `K16_flaA_cam_fastp_spades` | fastp,spades,flaA | fastp,spades,flaA | · | · | · |
| 67 | `K17_staramr_cam_fastp_spades` | fastp,spades,staramr | fastp,spades,staramr | · | · | · |
| 68 | `K18_mlst_lis_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 69 | `K19_mlst_eco_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 70 | `K20_mlst_sal_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 71 | `K21_mlst_cam_fastp_shovill` | fastp,shovill,mlst | fastp,shovill,mlst | · | · | · |
| 72 | `K22_chewbbaca_lis_fastp_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 73 | `K23_chewbbaca_eco_fastp_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 74 | `K24_chewbbaca_sal_fastp_shovill` | fastp,shovill,chewbbaca | fastp,shovill,chewbbaca | · | · | · |
| 75 | `K25_abricate_lis_fastp_shovill` | fastp,shovill,abricate | fastp,shovill,abricate | · | · | · |
| 76 | `K26_abricate_eco_fastp_shovill` | fastp,shovill,resfinder | fastp,shovill,abricate | resfinder | abricate | · |
| 77 | `K27_abricate_sal_fastp_shovill` | fastp,shovill,abricate | fastp,shovill,abricate | · | · | · |
| 78 | `K28_abricate_cam_fastp_shovill` | fastp,shovill,abricate | fastp,shovill,abricate | · | · | · |
| 79 | `K29_prokka_lis_fastp_shovill` | fastp,shovill,prokka | fastp,shovill,prokka | · | · | · |
| 80 | `K30_prokka_eco_fastp_shovill` | fastp,spades,prokka | fastp,shovill,prokka | spades | shovill | · |
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
| 95 | `K45_abricate_cam_fastp_unicycler` | fastp,unicycler,staramr | fastp,unicycler,abricate | staramr | abricate | · |
| 96 | `K46_prokka_lis_fastp_unicycler` | fastp,spades,prokka | fastp,unicycler,prokka | spades | unicycler | · |
| 97 | `K47_prokka_eco_fastp_unicycler` | fastp,unicycler,prokka | fastp,unicycler,prokka | · | · | · |
| 98 | `K48_prokka_sal_fastp_unicycler` | fastp,spades,prokka | fastp,unicycler,prokka | spades | unicycler | · |
| 99 | `K49_prokka_cam_fastp_unicycler` | fastp,spades,prokka | fastp,unicycler,prokka | spades | unicycler | · |
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
| 118 | `L08_chewbbaca_prokka_sal` | fastp,spades,chewbbaca,prokka | fastp,spades,prokka,chewbbaca | · | · | · |
| 119 | `L09_mlst_prokka_eco` | fastp,spades,mlst,prokka | fastp,spades,prokka,mlst | · | · | · |
| 120 | `L10_mlst_prokka_sal` | fastp,spades,mlst,prokka | fastp,spades,prokka,mlst | · | · | · |
| 121 | `L11_abricate_prokka_lis` | fastp,spades,abricate,prokka | fastp,spades,abricate,prokka | · | · | · |
| 122 | `L12_abricate_prokka_sal` | fastp,spades,abricate,prokka | fastp,spades,abricate,prokka | · | · | · |
| 123 | `L13_mlst_flaA_cam` | fastp,spades,mlst,flaA | fastp,spades,mlst,flaA | · | · | · |
| 124 | `L14_mlst_staramr_cam` | fastp,spades,mlst,staramr | fastp,spades,staramr,mlst | · | · | · |
| 125 | `L15_flaA_staramr_cam` | fastp,spades,flaA,staramr | fastp,spades,staramr,flaA | · | · | · |
| 126 | `L16_flaA_abricate_cam` | fastp,spades,flaA,abricate | fastp,spades,abricate,flaA | · | · | · |
| 127 | `L17_staramr_abricate_cam` | fastp,spades,staramr,abricate | fastp,spades,abricate,staramr | · | · | · |
| 128 | `L18_staramr_prokka_cam` | fastp,spades,staramr,prokka | fastp,spades,staramr,prokka | · | · | · |
| 129 | `L19_flaA_prokka_cam` | fastp,spades,flaA,prokka | fastp,spades,prokka,flaA | · | · | · |
| 130 | `L20_mlst_prokka_lis` | fastp,spades,mlst,prokka | fastp,spades,prokka,mlst | · | · | · |
| 131 | `M01_mlst+chewbbaca+abricate_lis` | fastp,spades,mlst,abricate | fastp,spades,abricate,mlst,chewbbaca | · | chewbbaca | · |
| 132 | `M02_mlst+chewbbaca+prokka_sal` | fastp,spades,mlst,chewbbaca,prokka | fastp,spades,prokka,mlst,chewbbaca | · | · | · |
| 133 | `M03_mlst+abricate+prokka_eco` | abricate,prokka,mlst,fastp,spades | fastp,spades,abricate,prokka,mlst | · | · | · |
| 134 | `M04_mlst+abricate+prokka_lis` | fastp,spades,mlst,abricate,prokka | fastp,spades,abricate,prokka,mlst | · | · | · |
| 135 | `M05_mlst+flaA+staramr_cam` | mlst,flaA,staramr,fastp,spades | fastp,spades,staramr,mlst,flaA | · | · | · |
| 136 | `M06_mlst+flaA+abricate_cam` | fastp,spades,mlst,flaA,abricate | fastp,spades,abricate,mlst,flaA | · | · | · |
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
| 156 | `O01_spades_lis` | bowtie,spades | spades | bowtie | · | · |
| 157 | `O02_spades_sal` | fastp,spades | spades | fastp | · | · |
| 158 | `O03_spades_cam` | fastp,spades | spades | fastp | · | · |
| 159 | `O04_shovill_lis` | fastp,shovill | shovill | fastp | · | · |
| 160 | `O05_shovill_sal` | fastp,shovill | shovill | fastp | · | · |
| 161 | `O06_shovill_cam` | fastq,fastp,shovill | shovill | fastq,fastp | · | · |
| 162 | `O07_unicycler_lis` | fastp,unicycler | unicycler | fastp | · | · |
| 163 | `O08_unicycler_eco` | fastp,unicycler | unicycler | fastp | · | · |
| 164 | `O09_unicycler_cam` | unicycler | unicycler | · | · | · |
| 165 | `O10_plasmidspades_eco` | fastp,plasmidspades | plasmidspades | fastp | · | · |
| 166 | `P01_chopper_flye_mlst_lis` | chopper,flye,mlst | chopper,flye,mlst | · | · | · |
| 167 | `P02_chopper_flye_mlst_sal` | chopper,flye,mlst | chopper,flye,mlst | · | · | · |
| 168 | `P03_chopper_flye_mlst_eco` | chopper,flye,mlst | chopper,flye,mlst | · | · | · |
| 169 | `P04_chopper_flye_mlst_cam` | chopper,flye,mlst | chopper,flye,mlst | · | · | · |
| 170 | `P05_chopper_flye_abricate_lis` | chopper,flye,abricate | chopper,flye,abricate | · | · | · |
| 171 | `P06_chopper_flye_abricate_eco` | chopper,spades,abricate | chopper,flye,abricate | spades | flye | · |
| 172 | `P07_chopper_flye_abricate_sal` | chopper,flye,abricate | chopper,flye,abricate | · | · | · |
| 173 | `P08_chopper_flye_prokka_lis` | chopper,flye,prokka | chopper,flye,prokka | · | · | · |
| 174 | `P09_chopper_flye_chewbbaca_lis` | chopper,flye,chewbbaca | chopper,flye,chewbbaca | · | · | · |
| 175 | `P10_chopper_flye_chewbbaca_sal` | chopper,flye,chewbbaca | chopper,flye,chewbbaca | · | · | · |
| 176 | `Q01_kmerfinder_fastp_spades_lis` | kmerfinder,fastp,spades | fastp,spades,kmerfinder | · | · | · |
| 177 | `Q02_kmerfinder_fastp_spades_eco` | kmerfinder,fastp,spades | fastp,spades,kmerfinder | · | · | · |
| 178 | `Q03_kmerfinder_fastp_spades_sal` | fastp,spades,kmerfinder | fastp,spades,kmerfinder | · | · | · |
| 179 | `Q04_kmerfinder_fastp_shovill_lis` | kmerfinder,fastp,shovill | fastp,shovill,kmerfinder | · | · | · |
| 180 | `Q05_kmerfinder_fastp_shovill_eco` | kmerfinder,fastp,shovill | fastp,shovill,kmerfinder | · | · | · |
| 181 | `Q06_kmerfinder_fastp_shovill_sal` | fastp,shovill,kmerfinder | fastp,shovill,kmerfinder | · | · | · |
| 182 | `Q07_mash_fastp_spades_lis` | mash,fastp,spades | fastp,spades,mash | · | · | · |
| 183 | `Q08_mash_fastp_spades_eco` | mash,fastp,spades | fastp,spades,mash | · | · | · |
| 184 | `Q09_mash_fastp_spades_sal` | mash,fastp,spades | fastp,spades,mash | · | · | · |
| 185 | `Q10_mash_fastp_shovill_lis` | mash,fastp,shovill | fastp,shovill,mash | · | · | · |
| 186 | `R01_kmerfinder_cam` | spades,kmerfinder | kmerfinder | spades | · | · |
| 187 | `R02_kmerfinder_sal` | fastq,fastp,kmerfinder | kmerfinder | fastq,fastp | · | · |
| 188 | `R03_mash_sal` | mash | mash | · | · | · |
| 189 | `R04_mash_eco` | mash,spades,mlst,abricate | mash | spades,abricate,mlst | · | · |
| 190 | `R05_kraken2_lis` | fastq,fastp,kraken2 | kraken2 | fastq,fastp | · | · |
| 191 | `R06_kraken2_eco` | fastp,kraken2 | kraken2 | fastp | · | · |
| 192 | `R07_kraken2_sal` | fastp,kraken2 | kraken2 | fastp | · | · |
| 193 | `R08_kraken2_cam` | fastq,fastp,kraken2 | kraken2 | fastq,fastp | · | · |
| 194 | `S01_fastp_lis` | fastp | fastp | · | · | · |
| 195 | `S02_fastp_sal` | fastp | fastp | · | · | · |
| 196 | `S03_trimmomatic_eco` | trimmomatic | trimmomatic | · | · | · |
| 197 | `S04_trimmomatic_cam` | trimmomatic | trimmomatic | · | · | · |
| 198 | `S05_chopper_lis` | chopper | chopper | · | · | · |
| 199 | `S06_chopper_sal` | chopper | chopper | · | · | · |
| 200 | `S07_chopper_cam` | chopper | chopper | · | · | · |

## Failure detail (one section per failing prompt)

### `A06_cgmlst_salmonella` — `missing_param`

**Prompt:** Generate cgMLST allelic profiles starting from a Salmonella enterica assembly.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_4TY_cgMLST__chewbbaca`
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

include { getAssembly } from '../functions/parameters.nf'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    kmerfinder_out = step_3TX_species__kmerfinder(getAssembly())
    chewbbaca_out = step_4TY_cgMLST__chewbbaca(kmerfinder_out.assigned_species.map { [ it[0], it[1], it[2][1] ] }, kmerfinder_out.assigned_species.map { it[1] }, kmerfinder_out.assigned_species.map { it[2][1] })
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
    step_4AN_AMR__staramr(kmerfinder_out.assigned_species.map { [it[0], it[1]] }, kmerfinder_out.assigned_species.map { it[2] })
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `B01_spades_listeria` — `missing_param`

**Prompt:** De novo genome assembly with SPAdes from Illumina paired-end reads of Listeria monocytogenes.

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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] }
            .branch {
                with_host: it[1][1]
                without_host: true
            }
            .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set { denovoInput }

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

### `B03_unicycler_salmonella` — `missing_param`

**Prompt:** Assemble a Salmonella enterica genome with Unicycler from Illumina paired-end reads.

**Steps (LLM):** `step_1PP_trimming__fastp, step_1PP_hostdepl__bowtie, step_2AS_denovo__unicycler`
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

include { step_2AS_denovo__unicycler } from '../steps/step_2AS_denovo__unicycler'

include { getHostUnkeyed; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    trimmedAndHost = trimmed.combine(getHostUnkeyed())
    depleted = step_1PP_hostdepl__bowtie(trimmedAndHost)

    assembled = step_2AS_denovo__unicycler(depleted)
}
```
**Error excerpt:**
```
ERROR ~ missing required param: hosts_dir
```

### `E03_cgmlst_sal_fastp_spades` — `missing_param`

**Prompt:** Generate cgMLST profiles for Salmonella enterica starting from paired-end Illumina FASTQ.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_3TX_species__kmerfinder, step_2AS_mapping__bowtie, step_4TY_cgMLST__chewbbaca`
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

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_2AS_mapping__bowtie } from '../steps/step_2AS_mapping__bowtie'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    species_out = step_3TX_species__kmerfinder(assembled)

    consensus = step_2AS_mapping__bowtie(trimmed, species_out.assigned_species.map { [ it[0], it[1][1], it[1][2] ] })

    step_4TY_cgMLST__chewbbaca(assembled, 'salmonella_enterica', 's_enterica_chewie_3255_210531')
}
```
**Error excerpt:**
```
ERROR ~ missing required param: step_3TX_species__kmerfinder__db
```

### `H01_mlst_plus_cgmlst_lis` — `ngsmanager_naming`

**Prompt:** Run both MLST and cgMLST typing on Listeria monocytogenes from paired Illumina FASTQ.

**Steps (LLM):** `step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4TY_cgMLST__chewbbaca`
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

include { getSingleInput; optionalOrDefault; param } from '../functions/parameters.nf'

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    assembled = step_2AS_denovo__spades(getSingleInput())
    step_4TY_MLST__mlst(assembled.assembled)
    step_4TY_cgMLST__chewbbaca(assembled.assembled, param('genus_species'), optionalOrDefault('schema', ''))
}
```
**Error excerpt:**
```
ERROR ~ unexpected file name: DS99999-DT260224_2026.LIS.C.1.1_R1.fastq.gz
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

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { extractKey } from '../functions/common.nf'

include { step_4TY_flaA__flaA } from '../steps/step_4TY_flaA__flaA'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

workflow wf_campylobacter_typing {
    
    take:
        
        rawreads
        
    
    main:
        trimmed = step_1PP_trimming__fastp(rawreads).trimmed

        assembled = step_2AS_denovo__spades(trimmed).assembled

        assigned_species = step_3TX_species__kmerfinder(assembled).assigned_species

        assemblyAndSpecies = assembled.cross(assigned_species) { extractKey(it) }.multiMap {
            assembly: it[0]
            species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
        step_4TY_flaA__flaA(assemblyAndSpecies.assembly, assemblyAndSpecies.species)
    
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

### `I02_mash_fastp_shovill` — `partial_dag`

**Prompt:** Species sketch with Mash plus assembly via fastp + Shovill from paired Illumina reads.

**Steps (LLM):** `step_3TX_species__mash, step_2AS_denovo__shovill`
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

include { step_2AS_denovo__shovill } from '../steps/step_2AS_denovo__shovill'

include { getSingleInput } from '../functions/parameters.nf'

include { step_3TX_species__mash } from '../steps/step_3TX_species__mash'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    step_3TX_species__mash(getSingleInput())
    step_2AS_denovo__shovill(getSingleInput())
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

include { step_4TY_cgMLST__chewbbaca } from '../steps/step_4TY_cgMLST__chewbbaca'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { getSingleInput } from '../functions/parameters.nf'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

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
WARN: file not found: '/mnt/data/cohesive_llm_bench_scratch/_shared_inputdir/2026/2026.LIS.101.1.1/0SQ_rawreads/DS99999-DT260224_import/result/*.fastq*'
```

### `M01_mlst+chewbbaca+abricate_lis` — `partial_dag`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Listeria monocytogenes from paired Illumina FASTQ: trim, assemble, then run mlst, chewbbaca, abricate in parallel on the assembly.

**Steps (LLM):** `step_1PP_trimming__fastp, step_2AS_denovo__spades, step_4TY_MLST__mlst, step_4AN_AMR__abricate`
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

include { step_4AN_AMR__abricate } from '../steps/step_4AN_AMR__abricate'

include { getSingleInput } from '../functions/parameters.nf'

include { step_4TY_MLST__mlst } from '../steps/step_4TY_MLST__mlst'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    assembled = step_2AS_denovo__spades(trimmed).assembled
    step_4TY_MLST__mlst(assembled)
    step_4AN_AMR__abricate(assembled)
}
```
**Error excerpt:**
```
Only 8/11 expected processes appeared in the DAG
```

### `M03_mlst+abricate+prokka_eco` — `silent_no_op`

**Prompt:** Comprehensive typing+AMR+annotation pipeline for Escherichia coli from paired Illumina FASTQ: trim, assemble, then run mlst, abricate, prokka in parallel on the assembly.

**Steps (LLM):** `step_4AN_AMR__abricate, step_4AN_genes__prokka, step_4TY_MLST__mlst, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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
        step_4AN_AMR__abricate(assembly)

        step_4AN_genes__prokka(assembly.map{ [ it[0], it[1], 'Bacteria', '-', '-', getEmpty() ] })

        assembly.cross(assigned_species) { extractKey(it) }.multiMap { 
          assembly: it[0]
          species: it[1][1]
        }.set { assemblyAndSpecies }

        step_4TY_MLST__mlst(assemblyAndSpecies.assembly)
    
}

// --- ENTRYPOINT ---
workflow {
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed

    assembled = step_2AS_denovo__spades(trimmed).assembled

    module_typing_bacteria(trimmed, assembled)
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```

### `O01_spades_lis` — `missing_param`

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

include { getHost; getSingleInput } from '../functions/parameters.nf'

include { step_1PP_hostdepl__bowtie } from '../steps/step_1PP_hostdepl__bowtie'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

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
            .map { [ it[0][0], it[0][1], it[1][1] ] }
            .branch {
                with_host: it[1][1]
                without_host: true
            }
            .set { branchedTrimmed }

        depleted = step_1PP_hostdepl__bowtie(branchedTrimmed.with_host)

        branchedTrimmed.without_host
            .mix(depleted)
            .map { it[0,1] }
            .set { denovoInput }

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

### `Q01_kmerfinder_fastp_spades_lis` — `silent_no_op`

**Prompt:** In parallel, identify the species with kmerfinder and trim+assemble paired Illumina FASTQ of Listeria monocytogenes with fastp + spades.

**Steps (LLM):** `step_3TX_species__kmerfinder, step_1PP_trimming__fastp, step_2AS_denovo__spades`
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

include { getAssembly; getSingleInput } from '../functions/parameters.nf'

include { step_2AS_denovo__spades } from '../steps/step_2AS_denovo__spades'

include { step_3TX_species__kmerfinder } from '../steps/step_3TX_species__kmerfinder'

include { step_1PP_trimming__fastp } from '../steps/step_1PP_trimming__fastp'

// --- GLOBALS ---

// --- INLINE PROCESSES ---

// --- SUB WORKFLOWS ---

// --- ENTRYPOINT ---
workflow {
    kmerfinder_out = step_3TX_species__kmerfinder(getAssembly())
    trimmed = step_1PP_trimming__fastp(getSingleInput()).trimmed
    spades_out = step_2AS_denovo__spades(trimmed)
    spades_out.assembled
}
```
**Error excerpt:**
```
No process placeholders appeared. when: clause filtered everything?
```
