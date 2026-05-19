#!/usr/bin/env python3.11
"""
Blueprints for the 50 training examples.

Each entry is a high-level recipe that the `make_example` helpers turn into a
fully fledged Example (prompt, nextflow_code, params, inputs, expected_processes).

The Nextflow code we emit is what we would *expect* a good LLM to produce,
i.e. it follows the canonical pattern from each step's bottom `workflow { }`
block: chain channels via .trimmed / .assembled, never fuse take: into a
single map.
"""

from __future__ import annotations

import sys
import textwrap
from dataclasses import asdict
from pathlib import Path

# Add repo root to path so `harness.harness` is importable when this module
# is loaded as `dataset.blueprints` or simply `blueprints`.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from harness.harness import Example   # noqa: E402

# ---------------------------------------------------------------------------
# Per-step process counts (from steps/*.nf "^process" declarations).
# Used to set expected_processes accurately per chain.
# ---------------------------------------------------------------------------
PROCS = {
    "step_0SQ_rawreads__fastq":            3,
    "step_1PP_downsampling__bbnorm":       1,
    "step_1PP_filtering__bowtie":          2,
    "step_1PP_filtering__minimap2":        2,
    "step_1PP_generated__fasta2fastq":     1,
    "step_1PP_hostdepl__bowtie":           2,
    "step_1PP_hostdepl__minimap2":         2,
    "step_1PP_trimming__chopper":          2,
    "step_1PP_trimming__fastp":            3,
    "step_1PP_trimming__trimmomatic":      3,
    "step_2AS_denovo__flye":               2,
    "step_2AS_denovo__plasmidspades":      3,
    "step_2AS_denovo__shovill":            3,   # 4 declared, 1 (checkm) skipped by default (skip_checkm=true)
    "step_2AS_denovo__spades":             3,
    "step_2AS_denovo__unicycler":          3,
    "step_2AS_hybrid__unicycler":          2,
    "step_2AS_mapping__bowtie":            9,
    "step_2AS_mapping__ivar":              10,
    "step_2AS_mapping__medaka":            6,
    "step_2AS_mapping__minimap2":          8,
    "step_2AS_mapping__snippy":            1,
    "step_2MG_denovo__metaspades":         3,
    "step_3TX_class__centrifuge":          2,
    "step_3TX_class__kraken":              2,
    "step_3TX_class__kraken2":             2,
    "step_3TX_species__kmerfinder":        1,
    "step_3TX_species__mash":              1,
    "step_3TX_species__vdabricate":        1,
    "step_4AN_AMR__abricate":              1,
    "step_4AN_AMR__resfinder":             1,
    "step_4AN_AMR__staramr":               1,
    "step_4AN_genes__prokka":              1,
    "step_4TY_MLST__mlst":                 1,
    "step_4TY_cgMLST__chewbbaca":          3,
    "step_4TY_flaA__flaA":                 1,
    "step_4TY_lineage__pangolin":          1,
    "step_4TY_lineage__westnile":          3,
    "step_4TY_plasmid__mobsuite":          1,
}


# ---------------------------------------------------------------------------
# Helpers to build .nf strings + matching params.json
# ---------------------------------------------------------------------------
def _nf_header(steps: list[str], use_getsingle: bool = True) -> str:
    """Generate the include block."""
    if use_getsingle:
        getters = "getSingleInput; optionalOrDefault; param"
    else:
        getters = "getInput; optionalOrDefault; param"
    lines = [
        "nextflow.enable.dsl=2",
        "",
        f"include {{ {getters} }} from '../functions/parameters.nf'",
    ]
    for s in steps:
        lines.append(f"include {{ {s} }} from '../steps/{s}'")
    lines.append("")
    return "\n".join(lines)


def _params_fastq(cmp: str, genus_species: str | None = None,
                  seq_type: str = "illumina_paired") -> dict:
    p: dict = {
        "cmp": cmp,
        "riscd": "260224-99999-0SQ_rawreads-import",
        "seq_type": seq_type,
    }
    if genus_species:
        p["genus_species"] = genus_species
    return p


def _params_assembly(cmp: str, genus_species: str | None = None) -> dict:
    p: dict = {
        "cmp": cmp,
        "input": [{"cmp": cmp, "riscd": "260224-99999-2AS_import-external"}],
    }
    if genus_species:
        p["genus_species"] = genus_species
    return p


# ===========================================================================
# Builders per pipeline shape
# ===========================================================================
def mono_typing(eid, prompt, step, cmp, genus_species,
                category="mono-typing", notes=""):
    """Single typing/AMR/annotation step from an assembly already in inputdir."""
    # Dispatch the call signature based on the step's workflow take: arity.
    # These mirror the bottom workflow{} of each step .nf file.
    if step == "step_4TY_MLST__mlst":
        call = f"{step}(getInput())"
    elif step == "step_4TY_cgMLST__chewbbaca":
        call = f"{step}(getInput(), param('genus_species'), optionalOrDefault('schema', ''))"
    elif step == "step_4TY_flaA__flaA":
        call = f"{step}(getInput(), param('genus_species'))"
    elif step == "step_4AN_AMR__staramr":
        # Use the canonical getter from the step file's example
        call = f"{step}(getSingleInput(), param('genus_species'))"
    elif step in ("step_4AN_AMR__abricate",
                  "step_4AN_genes__prokka"):
        # take: data  -- single argument only
        call = f"{step}(getInput())"
    else:
        # default: 2-arg (assembly, genus_species)
        call = f"{step}(getInput(), param('genus_species'))"

    # use getSingleInput in the includes header when staramr is the step
    use_single = (step == "step_4AN_AMR__staramr")
    nf = _nf_header([step], use_getsingle=use_single) + textwrap.dedent(f"""
        workflow {{
            {call}
        }}
    """).strip() + "\n"

    params = _params_assembly(cmp, genus_species)
    if step == "step_4AN_AMR__staramr":
        # staramr uses getSingleInput which needs cmp+riscd directly
        params = {
            "cmp": cmp,
            "riscd": "260224-99999-2AS_import-external",
            "genus_species": genus_species,
        }
    return Example(
        eid=eid, category=category, prompt=prompt,
        nextflow_code=nf,
        params=params,
        inputs=[f"assembly:{cmp}"],
        expected_processes=PROCS[step],
        notes=notes,
    )


def mono_assembly(eid, prompt, asm_step, cmp, seq_type="illumina_paired",
                  category="mono-assembly", notes=""):
    """Single de-novo assembly step from FASTQ."""
    nf = _nf_header([asm_step], use_getsingle=True) + textwrap.dedent(f"""
        workflow {{
            {asm_step}(getSingleInput())
        }}
    """).strip() + "\n"
    fastq_kind = "fastq_paired" if seq_type == "illumina_paired" else "fastq_single"
    return Example(
        eid=eid, category=category, prompt=prompt,
        nextflow_code=nf,
        params=_params_fastq(cmp, seq_type=seq_type),
        inputs=[f"{fastq_kind}:{cmp}"],
        expected_processes=PROCS[asm_step],
        notes=notes,
    )


SPECIES_ID_REQUIRED_PARAMS = {
    "step_3TX_species__kmerfinder":   {"step_3TX_species__kmerfinder__db":      "/tmp/_dummy_kmerfinder_db"},
    "step_3TX_class__kraken2":        {"step_3TX_class__kraken2__db":           "/tmp/_dummy_kraken2_db"},
    "step_3TX_class__kraken":         {"step_3TX_class__kraken__db_kraken":     "/tmp/_dummy_kraken_db",
                                       "step_3TX_class__kraken__db_bracken":   "/tmp/_dummy_bracken_db"},
    "step_3TX_class__centrifuge":     {"step_3TX_class__centrifuge__db_path":   "/tmp/_dummy_centrifuge",
                                       "step_3TX_class__centrifuge__db_name":   "dummy"},
    "step_3TX_species__vdabricate":   {"step_3TX_species__vdabricate__db":      "/tmp/_dummy_vd"},
}


def mono_species_id(eid, prompt, step, cmp, category="mono-species-id", notes=""):
    """Single species-id step from FASTQ."""
    if step in ("step_3TX_species__kmerfinder",
                "step_3TX_species__mash",
                "step_3TX_class__kraken",
                "step_3TX_class__kraken2",
                "step_3TX_class__centrifuge"):
        getter = "getSingleInput"
        # kmerfinder's canonical example uses getInput, but getSingleInput also works
        if step == "step_3TX_species__kmerfinder":
            getter = "getInput"
        use_single = getter == "getSingleInput"
        nf = _nf_header([step], use_getsingle=use_single) + textwrap.dedent(f"""
            workflow {{
                {step}({getter}())
            }}
        """).strip() + "\n"
    else:
        raise ValueError(f"unsupported species-id step: {step}")

    p = _params_fastq(cmp)
    # add any step-specific required db params
    p.update(SPECIES_ID_REQUIRED_PARAMS.get(step, {}))

    return Example(
        eid=eid, category=category, prompt=prompt,
        nextflow_code=nf,
        params=p,
        inputs=[f"fastq_paired:{cmp}"],
        expected_processes=PROCS[step],
        notes=notes,
    )


ASM_EMIT = {
    "step_2AS_denovo__spades":         "assembled",
    "step_2AS_denovo__shovill":        "assembly",   # shovill emits 'assembly'
    "step_2AS_denovo__unicycler":      "assembled",
    "step_2AS_denovo__plasmidspades":  "assembled",
    "step_2AS_denovo__flye":           "assembly",   # flye emits 'assembly'
    "step_2MG_denovo__metaspades":     "assembled",
}


def trim_assembly(eid, prompt, trim_step, asm_step, cmp,
                  seq_type="illumina_paired",
                  category="2step-trim-assembly", notes=""):
    emit_name = ASM_EMIT[asm_step]
    nf = _nf_header([trim_step, asm_step]) + textwrap.dedent(f"""
        workflow {{
            trimmed   = {trim_step}(getSingleInput()).trimmed
            assembled = {asm_step}(trimmed).{emit_name}
        }}
    """).strip() + "\n"
    fastq_kind = "fastq_paired" if seq_type == "illumina_paired" else "fastq_single"
    return Example(
        eid=eid, category=category, prompt=prompt,
        nextflow_code=nf,
        params=_params_fastq(cmp, seq_type=seq_type),
        inputs=[f"{fastq_kind}:{cmp}"],
        expected_processes=PROCS[trim_step] + PROCS[asm_step],
        notes=notes,
    )


def trim_assembly_typing(eid, prompt, trim_step, asm_step, typing_step, cmp,
                         genus_species, seq_type="illumina_paired",
                         category="3step", notes=""):
    """Trim + assembly + typing. Adapts the typing call to its take: arity."""
    typing_call = _build_typing_call(typing_step)
    emit_name = ASM_EMIT[asm_step]
    nf = _nf_header([trim_step, asm_step, typing_step]) + textwrap.dedent(f"""
        workflow {{
            trimmed   = {trim_step}(getSingleInput()).trimmed
            assembled = {asm_step}(trimmed).{emit_name}
            {typing_call}
        }}
    """).strip() + "\n"
    fastq_kind = "fastq_paired" if seq_type == "illumina_paired" else "fastq_single"
    return Example(
        eid=eid, category=category, prompt=prompt,
        nextflow_code=nf,
        params=_params_fastq(cmp, genus_species, seq_type),
        inputs=[f"{fastq_kind}:{cmp}"],
        expected_processes=PROCS[trim_step] + PROCS[asm_step] + PROCS[typing_step],
        notes=notes,
    )


def _build_typing_call(step: str) -> str:
    """Return the workflow-call line for a typing/AMR step, using `assembled`."""
    if step == "step_4TY_MLST__mlst":
        return f"{step}(assembled)"
    if step == "step_4TY_cgMLST__chewbbaca":
        return f"{step}(assembled, param('genus_species'), optionalOrDefault('schema', ''))"
    if step == "step_4TY_flaA__flaA":
        return f"{step}(assembled, param('genus_species'))"
    if step == "step_4AN_AMR__staramr":
        return f"{step}(assembled, param('genus_species'))"
    if step == "step_4AN_AMR__abricate":
        return f"{step}(assembled)"
    if step == "step_4AN_genes__prokka":
        return f"{step}(assembled)"
    raise ValueError(f"unknown typing/AMR step: {step}")


# ===========================================================================
# Build all 50 examples
# ===========================================================================
def build_all() -> list[Example]:
    L: list[Example] = []

    # ------------------ A. Mono-step typing (assembly input) ---------------
    L.append(mono_typing(
        eid="A01_mlst_listeria",
        prompt="I have a Listeria monocytogenes assembly and I want to run MLST typing on it.",
        step="step_4TY_MLST__mlst",
        cmp="2026.LIS.1.1.1",
        genus_species="listeria_monocytogenes",
        notes="MLST classico; il take: del workflow ha solo 'assembly'",
    ))
    L.append(mono_typing(
        eid="A02_mlst_ecoli",
        prompt="Run MLST typing on an Escherichia coli assembly.",
        step="step_4TY_MLST__mlst",
        cmp="2026.ECO.1.1.1",
        genus_species="escherichia_coli",
    ))
    L.append(mono_typing(
        eid="A03_mlst_salmonella",
        prompt="Classic MLST (PubMLST) on a Salmonella enterica assembly.",
        step="step_4TY_MLST__mlst",
        cmp="2026.SAL.1.1.1",
        genus_species="salmonella_enterica",
        notes="",
    ))
    L.append(mono_typing(
        eid="A04_cgmlst_listeria",
        prompt="cgMLST allelic profile for Listeria monocytogenes from a pre-existing assembly.",
        step="step_4TY_cgMLST__chewbbaca",
        cmp="2026.LIS.2.1.1",
        genus_species="listeria_monocytogenes",
    ))
    L.append(mono_typing(
        eid="A05_cgmlst_ecoli",
        prompt="cgMLST allelic profile on an Escherichia coli assembly.",
        step="step_4TY_cgMLST__chewbbaca",
        cmp="2026.ECO.2.1.1",
        genus_species="escherichia_coli",
    ))
    L.append(mono_typing(
        eid="A06_cgmlst_salmonella",
        prompt="Generate cgMLST allelic profiles starting from a Salmonella enterica assembly.",
        step="step_4TY_cgMLST__chewbbaca",
        cmp="2026.SAL.2.1.1",
        genus_species="salmonella_enterica",
    ))
    L.append(mono_typing(
        eid="A07_flaa_campylobacter",
        prompt="Run flaA typing on a Campylobacter assembly.",
        step="step_4TY_flaA__flaA",
        cmp="2026.CAM.1.1.1",
        genus_species="campylobacter_jejuni",
    ))
    L.append(mono_typing(
        eid="A08_staramr_campylobacter",
        prompt="AMR profiling with staramr on a Campylobacter assembly.",
        step="step_4AN_AMR__staramr",
        cmp="2026.CAM.2.1.1",
        genus_species="campylobacter_jejuni",
        notes="staramr uses POINTFINDER_ORGANISM only for campylobacter",
    ))

    # ------------------ B. Mono-step assembly (FASTQ -> assembly) ----------
    L.append(mono_assembly(
        eid="B01_spades_listeria",
        prompt="De novo genome assembly with SPAdes from Illumina paired-end reads of Listeria monocytogenes.",
        asm_step="step_2AS_denovo__spades",
        cmp="2026.LIS.3.1.1",
    ))
    L.append(mono_assembly(
        eid="B02_shovill_ecoli",
        prompt="Quick bacterial genome assembly with Shovill from Illumina reads (Escherichia coli).",
        asm_step="step_2AS_denovo__shovill",
        cmp="2026.ECO.3.1.1",
    ))
    L.append(mono_assembly(
        eid="B03_unicycler_salmonella",
        prompt="Assemble a Salmonella enterica genome with Unicycler from Illumina paired-end reads.",
        asm_step="step_2AS_denovo__unicycler",
        cmp="2026.SAL.3.1.1",
    ))
    L.append(mono_assembly(
        eid="B04_plasmidspades",
        prompt="I want to assemble plasmids only from Illumina paired-end reads using plasmidSPAdes.",
        asm_step="step_2AS_denovo__plasmidspades",
        cmp="2026.PLA.1.1.1",
    ))
    L.append(mono_assembly(
        eid="B05_metaspades",
        prompt="Run metagenomic assembly with metaSPAdes on paired-end Illumina reads from an environmental sample.",
        asm_step="step_2MG_denovo__metaspades",
        cmp="2026.MGS.1.1.1",
    ))

    # ------------------ C. Mono-step species ID ---------------------------
    L.append(mono_species_id(
        eid="C01_kmerfinder",
        prompt="Identify the species of an unknown bacterial isolate from Illumina paired FASTQ using KmerFinder.",
        step="step_3TX_species__kmerfinder",
        cmp="2026.UNK.1.1.1",
    ))
    L.append(mono_species_id(
        eid="C02_mash",
        prompt="Run Mash sketch-based species identification on paired-end Illumina reads.",
        step="step_3TX_species__mash",
        cmp="2026.UNK.2.1.1",
    ))
    L.append(mono_species_id(
        eid="C03_kraken2",
        prompt="Taxonomic classification of paired-end Illumina reads with Kraken2.",
        step="step_3TX_class__kraken2",
        cmp="2026.UNK.3.1.1",
    ))

    # ------------------ D. 2-step trim + assembly --------------------------
    L.append(trim_assembly(
        eid="D01_fastp_spades_lis",
        prompt="From Illumina paired-end FASTQ of Listeria monocytogenes: trim with fastp and assemble with SPAdes.",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__spades",
        cmp="2026.LIS.4.1.1",
    ))
    L.append(trim_assembly(
        eid="D02_fastp_shovill_eco",
        prompt="Trim Illumina paired reads with fastp then assemble with Shovill (Escherichia coli).",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__shovill",
        cmp="2026.ECO.4.1.1",
    ))
    L.append(trim_assembly(
        eid="D03_trimmomatic_spades",
        prompt="Pipeline: trim with Trimmomatic, assemble with SPAdes. Illumina paired-end.",
        trim_step="step_1PP_trimming__trimmomatic",
        asm_step="step_2AS_denovo__spades",
        cmp="2026.SAM.1.1.1",
    ))
    L.append(trim_assembly(
        eid="D04_fastp_unicycler_sal",
        prompt="Trim and assemble a Salmonella isolate from Illumina paired-end FASTQ (fastp + Unicycler).",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__unicycler",
        cmp="2026.SAL.4.1.1",
    ))
    L.append(trim_assembly(
        eid="D05_fastp_spades_cam",
        prompt="Trim and de novo assembly (fastp + SPAdes) for a paired-end Illumina Campylobacter sample.",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__spades",
        cmp="2026.CAM.3.1.1",
    ))

    # ------------------ E. 3-step trim+asm+typing (15) --------------------
    L.append(trim_assembly_typing(
        eid="E01_mlst_lis",
        prompt="Classic MLST on Listeria monocytogenes from paired-end Illumina FASTQ (trim + assembly + MLST).",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__spades",
        typing_step="step_4TY_MLST__mlst",
        cmp="2026.LIS.5.1.1",
        genus_species="listeria_monocytogenes",
    ))
    L.append(trim_assembly_typing(
        eid="E02_cgmlst_lis_fastp_spades",
        prompt="cgMLST allelic profile for Listeria monocytogenes from paired Illumina FASTQ (fastp + SPAdes + chewbbaca).",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__spades",
        typing_step="step_4TY_cgMLST__chewbbaca",
        cmp="2026.LIS.6.1.1",
        genus_species="listeria_monocytogenes",
    ))
    L.append(trim_assembly_typing(
        eid="E03_cgmlst_sal_fastp_spades",
        prompt="Generate cgMLST profiles for Salmonella enterica starting from paired-end Illumina FASTQ.",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__spades",
        typing_step="step_4TY_cgMLST__chewbbaca",
        cmp="2026.SAL.5.1.1",
        genus_species="salmonella_enterica",
    ))
    L.append(trim_assembly_typing(
        eid="E04_cgmlst_eco_fastp_shovill",
        prompt="E. coli cgMLST typing from Illumina paired FASTQ using fastp + Shovill + chewbbaca.",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__shovill",
        typing_step="step_4TY_cgMLST__chewbbaca",
        cmp="2026.ECO.5.1.1",
        genus_species="escherichia_coli",
    ))
    L.append(trim_assembly_typing(
        eid="E05_flaa_cam",
        prompt="flaA typing pipeline for Campylobacter from paired-end Illumina FASTQ.",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__spades",
        typing_step="step_4TY_flaA__flaA",
        cmp="2026.CAM.4.1.1",
        genus_species="campylobacter_jejuni",
    ))
    L.append(trim_assembly_typing(
        eid="E06_staramr_cam",
        prompt="AMR analysis with staramr for Campylobacter from paired Illumina FASTQ (trim + assembly + staramr).",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__spades",
        typing_step="step_4AN_AMR__staramr",
        cmp="2026.CAM.5.1.1",
        genus_species="campylobacter_jejuni",
    ))
    L.append(trim_assembly_typing(
        eid="E07_abricate_eco",
        prompt="Resistance gene detection with ABRicate on Escherichia coli from Illumina paired FASTQ.",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__spades",
        typing_step="step_4AN_AMR__abricate",
        cmp="2026.ECO.6.1.1",
        genus_species="escherichia_coli",
    ))
    L.append(trim_assembly_typing(
        eid="E08_prokka_lis",
        prompt="Annotate a Listeria monocytogenes genome with Prokka, starting from paired Illumina FASTQ (trim + assembly + Prokka).",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__spades",
        typing_step="step_4AN_genes__prokka",
        cmp="2026.LIS.7.1.1",
        genus_species="listeria_monocytogenes",
    ))
    L.append(trim_assembly_typing(
        eid="E09_mlst_eco_trimmomatic",
        prompt="MLST on E. coli paired Illumina reads: Trimmomatic + SPAdes + mlst.",
        trim_step="step_1PP_trimming__trimmomatic",
        asm_step="step_2AS_denovo__spades",
        typing_step="step_4TY_MLST__mlst",
        cmp="2026.ECO.7.1.1",
        genus_species="escherichia_coli",
    ))
    L.append(trim_assembly_typing(
        eid="E10_mlst_sal_shovill",
        prompt="Salmonella enterica MLST: fastp + Shovill + mlst.",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__shovill",
        typing_step="step_4TY_MLST__mlst",
        cmp="2026.SAL.6.1.1",
        genus_species="salmonella_enterica",
    ))
    L.append(trim_assembly_typing(
        eid="E11_cgmlst_lis_shovill",
        prompt="Listeria cgMLST starting from Illumina paired reads: trim, Shovill assembly, chewbbaca typing.",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__shovill",
        typing_step="step_4TY_cgMLST__chewbbaca",
        cmp="2026.LIS.8.1.1",
        genus_species="listeria_monocytogenes",
    ))
    L.append(trim_assembly_typing(
        eid="E12_mlst_cam",
        prompt="MLST analysis for Campylobacter from paired Illumina FASTQ (fastp + SPAdes + mlst).",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__spades",
        typing_step="step_4TY_MLST__mlst",
        cmp="2026.CAM.6.1.1",
        genus_species="campylobacter_jejuni",
    ))
    L.append(trim_assembly_typing(
        eid="E13_abricate_sal",
        prompt="Antimicrobial resistance gene screening with ABRicate for Salmonella enterica from paired Illumina FASTQ.",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__spades",
        typing_step="step_4AN_AMR__abricate",
        cmp="2026.SAL.7.1.1",
        genus_species="salmonella_enterica",
    ))
    L.append(trim_assembly_typing(
        eid="E14_prokka_eco",
        prompt="Annotate an E. coli assembly with Prokka, starting from paired Illumina reads.",
        trim_step="step_1PP_trimming__fastp",
        asm_step="step_2AS_denovo__spades",
        typing_step="step_4AN_genes__prokka",
        cmp="2026.ECO.8.1.1",
        genus_species="escherichia_coli",
    ))
    L.append(trim_assembly_typing(
        eid="E15_cgmlst_lis_trimmomatic",
        prompt="Listeria monocytogenes cgMLST allelic profiles: Trimmomatic + SPAdes + chewbbaca.",
        trim_step="step_1PP_trimming__trimmomatic",
        asm_step="step_2AS_denovo__spades",
        typing_step="step_4TY_cgMLST__chewbbaca",
        cmp="2026.LIS.9.1.1",
        genus_species="listeria_monocytogenes",
    ))

    # ------------------ F. Mono-step AMR/species from assembly (4) ---------
    L.append(mono_typing(
        eid="F01_abricate_assembly",
        prompt="Run ABRicate to detect resistance genes on a pre-existing bacterial assembly.",
        step="step_4AN_AMR__abricate",
        cmp="2026.SAM.2.1.1",
        genus_species="escherichia_coli",
        category="mono-amr",
        notes="abricate workflow take is just the assembly",
    ))
    L.append(mono_typing(
        eid="F02_prokka_assembly",
        prompt="Annotate a bacterial genome assembly with Prokka.",
        step="step_4AN_genes__prokka",
        cmp="2026.SAM.3.1.1",
        genus_species="listeria_monocytogenes",
        category="mono-annotation",
    ))
    L.append(mono_species_id(
        eid="F03_mash_lis",
        prompt="Sketch-based species ID with Mash on a Listeria isolate (paired Illumina).",
        step="step_3TX_species__mash",
        cmp="2026.LIS.A.1.1",
    ))
    L.append(mono_species_id(
        eid="F04_kraken2_unknown",
        prompt="Classify an unknown bacterial isolate (paired Illumina FASTQ) using Kraken2.",
        step="step_3TX_class__kraken2",
        cmp="2026.UNK.4.1.1",
    ))

    # ------------------ G. Long-read Nanopore (2) -------------------------
    L.append(trim_assembly(
        eid="G01_chopper_flye_lis",
        prompt="Long-read Nanopore pipeline for Listeria: chopper trimming followed by Flye assembly.",
        trim_step="step_1PP_trimming__chopper",
        asm_step="step_2AS_denovo__flye",
        cmp="2026.LIS.B.1.1",
        seq_type="nanopore",
        category="2step-nanopore",
    ))
    L.append(trim_assembly(
        eid="G02_chopper_flye_eco",
        prompt="Nanopore Escherichia coli pipeline: chopper + flye.",
        trim_step="step_1PP_trimming__chopper",
        asm_step="step_2AS_denovo__flye",
        cmp="2026.ECO.B.1.1",
        seq_type="nanopore",
        category="2step-nanopore",
    ))

    # ------------------ H. 4-step combinations (4) -------------------------
    # We need a helper for 4-step. Define inline.
    def four_step(eid, prompt, trim, asm, typing1, typing2, cmp, genus_species, notes=""):
        c1 = _build_typing_call(typing1)
        c2 = _build_typing_call(typing2)
        emit_name = ASM_EMIT[asm]
        nf = _nf_header([trim, asm, typing1, typing2]) + textwrap.dedent(f"""
            workflow {{
                trimmed   = {trim}(getSingleInput()).trimmed
                assembled = {asm}(trimmed).{emit_name}
                {c1}
                {c2}
            }}
        """).strip() + "\n"
        return Example(
            eid=eid, category="4step", prompt=prompt,
            nextflow_code=nf,
            params=_params_fastq(cmp, genus_species),
            inputs=[f"fastq_paired:{cmp}"],
            expected_processes=PROCS[trim] + PROCS[asm] + PROCS[typing1] + PROCS[typing2],
            notes=notes,
        )

    L.append(four_step(
        eid="H01_mlst_plus_cgmlst_lis",
        prompt="Run both MLST and cgMLST typing on Listeria monocytogenes from paired Illumina FASTQ.",
        trim="step_1PP_trimming__fastp",
        asm="step_2AS_denovo__spades",
        typing1="step_4TY_MLST__mlst",
        typing2="step_4TY_cgMLST__chewbbaca",
        cmp="2026.LIS.C.1.1",
        genus_species="listeria_monocytogenes",
    ))
    L.append(four_step(
        eid="H02_mlst_plus_flaa_cam",
        prompt="Comprehensive Campylobacter typing from paired Illumina FASTQ: MLST + flaA.",
        trim="step_1PP_trimming__fastp",
        asm="step_2AS_denovo__spades",
        typing1="step_4TY_MLST__mlst",
        typing2="step_4TY_flaA__flaA",
        cmp="2026.CAM.C.1.1",
        genus_species="campylobacter_jejuni",
    ))
    L.append(four_step(
        eid="H03_prokka_plus_abricate_eco",
        prompt="E. coli pipeline from Illumina paired FASTQ: trim, assemble, annotate with Prokka and screen AMR with ABRicate.",
        trim="step_1PP_trimming__fastp",
        asm="step_2AS_denovo__spades",
        typing1="step_4AN_genes__prokka",
        typing2="step_4AN_AMR__abricate",
        cmp="2026.ECO.C.1.1",
        genus_species="escherichia_coli",
    ))
    L.append(four_step(
        eid="H04_mlst_plus_abricate_sal",
        prompt="Salmonella enterica: MLST typing and AMR screening with ABRicate from paired Illumina FASTQ.",
        trim="step_1PP_trimming__fastp",
        asm="step_2AS_denovo__spades",
        typing1="step_4TY_MLST__mlst",
        typing2="step_4AN_AMR__abricate",
        cmp="2026.SAL.C.1.1",
        genus_species="salmonella_enterica",
    ))

    # ------------------ I. Species ID + downstream (2) --------------------
    def species_then_assembly(eid, prompt, species_step, trim, asm, cmp):
        emit_name = ASM_EMIT[asm]
        nf = _nf_header([species_step, trim, asm]) + textwrap.dedent(f"""
            workflow {{
                raw = getSingleInput()
                {species_step}(raw)
                trimmed   = {trim}(raw).trimmed
                assembled = {asm}(trimmed).{emit_name}
            }}
        """).strip() + "\n"
        p = _params_fastq(cmp)
        p.update(SPECIES_ID_REQUIRED_PARAMS.get(species_step, {}))
        return Example(
            eid=eid, category="3step-with-species-id", prompt=prompt,
            nextflow_code=nf,
            params=p,
            inputs=[f"fastq_paired:{cmp}"],
            expected_processes=PROCS[species_step] + PROCS[trim] + PROCS[asm],
            notes="species id + trim + assembly running in parallel branches",
        )

    L.append(species_then_assembly(
        eid="I01_kmerfinder_fastp_spades",
        prompt="Identify the species with KmerFinder, in parallel trim with fastp and assemble with SPAdes (Illumina paired).",
        species_step="step_3TX_species__kmerfinder",
        trim="step_1PP_trimming__fastp",
        asm="step_2AS_denovo__spades",
        cmp="2026.UNK.5.1.1",
    ))
    L.append(species_then_assembly(
        eid="I02_mash_fastp_shovill",
        prompt="Species sketch with Mash plus assembly via fastp + Shovill from paired Illumina reads.",
        species_step="step_3TX_species__mash",
        trim="step_1PP_trimming__fastp",
        asm="step_2AS_denovo__shovill",
        cmp="2026.UNK.6.1.1",
    ))

    # ------------------ J. Mono-step plasmid / others (2) ------------------
    def mono_from_reads(eid, prompt, step, cmp, category, seq="illumina_paired"):
        nf = _nf_header([step], use_getsingle=True) + textwrap.dedent(f"""
            workflow {{
                {step}(getSingleInput())
            }}
        """).strip() + "\n"
        fastq_kind = "fastq_paired" if seq == "illumina_paired" else "fastq_single"
        return Example(
            eid=eid, category=category, prompt=prompt,
            nextflow_code=nf,
            params=_params_fastq(cmp, seq_type=seq),
            inputs=[f"{fastq_kind}:{cmp}"],
            expected_processes=PROCS[step],
        )

    L.append(mono_from_reads(
        eid="J01_mobsuite_plasmid",
        prompt="Detect and reconstruct plasmids from paired Illumina FASTQ using MOB-suite.",
        step="step_4TY_plasmid__mobsuite",
        cmp="2026.PLA.2.1.1",
        category="mono-plasmid",
    ))
    # bbnorm has take=[reads, k, target] -- must pass all three
    def mono_bbnorm(eid, prompt, cmp):
        step = "step_1PP_downsampling__bbnorm"
        nf = _nf_header([step], use_getsingle=True) + textwrap.dedent(f"""
            workflow {{
                {step}(getSingleInput(), param('k'), param('target'))
            }}
        """).strip() + "\n"
        return Example(
            eid=eid, category="mono-downsampling", prompt=prompt,
            nextflow_code=nf,
            params={**_params_fastq(cmp), "k": 25, "target": 100},
            inputs=[f"fastq_paired:{cmp}"],
            expected_processes=PROCS[step],
            notes="bbnorm take has 3 parameters (reads, k, target)",
        )
    L.append(mono_bbnorm(
        eid="J02_bbnorm_downsampling",
        prompt="Read normalization / downsampling of paired Illumina FASTQ with BBnorm at k=25, target depth 100x.",
        cmp="2026.SAM.4.1.1",
    ))

    return L


if __name__ == "__main__":
    L = build_all()
    print(f"Built {len(L)} examples")
    for ex in L[:5]:
        print(f"\n--- {ex.eid} ({ex.category}) ---")
        print(f"PROMPT: {ex.prompt}")
        print("CODE:")
        print(ex.nextflow_code)
