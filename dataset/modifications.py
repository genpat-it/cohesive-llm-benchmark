#!/usr/bin/env python3.11
"""
Multi-turn modification examples.

Each `ConversationExample` is a sequence of (user message, expected `.nf`)
turns simulating a user who asks for an initial pipeline, then iteratively
modifies it. Inspired by Grady's feedback on the v1 single-turn dataset.

Four canonical transformations are covered:

  - `add`             — add a step in parallel or downstream of the existing chain
  - `replace`         — swap one component for another in the same role
  - `drop`            — remove a step from the chain
  - `switch_species`  — change `genus_species` to a different supported species

Every turn is fully validated via `nextflow -stub-run` exactly like the
single-turn examples in `blueprints.py`.
"""

from __future__ import annotations

import sys
import textwrap
from dataclasses import dataclass, field
from pathlib import Path

# Make repo root importable so `harness.harness` works.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from harness.harness import Example   # noqa: E402

from dataset.blueprints import (   # noqa: E402
    PROCS, ASM_EMIT, _nf_header,
    _params_fastq, _params_assembly, _build_typing_call,
)


# ---------------------------------------------------------------------------
# datatype
# ---------------------------------------------------------------------------
@dataclass
class Turn:
    prompt: str
    nextflow_code: str
    params: dict
    inputs: list[str]
    expected_processes: int

    def as_example(self, eid: str, category: str, notes: str = "") -> Example:
        return Example(
            eid=eid, category=category, prompt=self.prompt,
            nextflow_code=self.nextflow_code, params=self.params,
            inputs=self.inputs, expected_processes=self.expected_processes,
            notes=notes,
        )


@dataclass
class ConversationExample:
    eid: str
    category: str            # always "modification" for now
    base_id: str             # id of the single-turn example this builds on
    modification_kind: str   # "add" | "replace" | "drop" | "switch_species"
    turns: list[Turn]
    notes: str = ""

    def to_serializable(self) -> dict:
        return {
            "id": self.eid,
            "category": self.category,
            "base_id": self.base_id,
            "modification_kind": self.modification_kind,
            "turns": [
                {"prompt": t.prompt,
                 "nextflow_code": t.nextflow_code,
                 "params": t.params,
                 "expected_processes": t.expected_processes}
                for t in self.turns
            ],
            "notes": self.notes,
        }


# ---------------------------------------------------------------------------
# Code-construction helpers (literal builders mirroring blueprints.py style)
# ---------------------------------------------------------------------------
def _wf(*lines: str) -> str:
    """Wrap workflow body lines inside a `workflow { … }` block."""
    body = "\n    ".join(lines)
    return f"workflow {{\n    {body}\n}}\n"


# -- shared turn-1 / turn-2 builders for each chain ---------------------------
def chain_trim_asm(trim: str, asm: str) -> str:
    emit = ASM_EMIT[asm]
    return _nf_header([trim, asm]) + _wf(
        f"trimmed   = {trim}(getSingleInput()).trimmed",
        f"assembled = {asm}(trimmed).{emit}",
    )


def chain_trim_asm_typing(trim: str, asm: str, typing: str) -> str:
    emit = ASM_EMIT[asm]
    call = _build_typing_call(typing)
    return _nf_header([trim, asm, typing]) + _wf(
        f"trimmed   = {trim}(getSingleInput()).trimmed",
        f"assembled = {asm}(trimmed).{emit}",
        call,
    )


def chain_trim_asm_two_typing(trim: str, asm: str, typing1: str, typing2: str) -> str:
    emit = ASM_EMIT[asm]
    c1 = _build_typing_call(typing1)
    c2 = _build_typing_call(typing2)
    return _nf_header([trim, asm, typing1, typing2]) + _wf(
        f"trimmed   = {trim}(getSingleInput()).trimmed",
        f"assembled = {asm}(trimmed).{emit}",
        c1, c2,
    )


def chain_mono_asm(asm: str) -> str:
    return _nf_header([asm]) + _wf(f"{asm}(getSingleInput())")


def chain_mono_typing_assembly(typing: str) -> str:
    """Mono-step typing/AMR starting from an existing assembly (getInput form)."""
    nf_header = _nf_header([typing], use_getsingle=False)
    if typing == "step_4TY_MLST__mlst":
        return nf_header + _wf(f"{typing}(getInput())")
    if typing == "step_4TY_cgMLST__chewbbaca":
        return nf_header + _wf(
            f"{typing}(getInput(), param('genus_species'), optionalOrDefault('schema', ''))"
        )
    if typing == "step_4TY_flaA__flaA":
        return nf_header + _wf(f"{typing}(getInput(), param('genus_species'))")
    if typing in ("step_4AN_AMR__abricate", "step_4AN_genes__prokka"):
        return nf_header + _wf(f"{typing}(getInput())")
    return nf_header + _wf(f"{typing}(getInput(), param('genus_species'))")


def chain_mono_two_typing_assembly(typing1: str, typing2: str) -> str:
    """Two parallel typing steps starting from the same assembly."""
    nf_header = _nf_header([typing1, typing2], use_getsingle=False)
    c1 = _build_typing_call(typing1).replace("assembled", "asm")
    c2 = _build_typing_call(typing2).replace("assembled", "asm")
    return nf_header + _wf(
        "asm = getInput()",
        c1, c2,
    )


# ===========================================================================
#                    THE 17 MODIFICATION CONVERSATIONS
# ===========================================================================
def build_modifications() -> list[ConversationExample]:
    L: list[ConversationExample] = []

    # --------------------------------------------------------------------- ADD
    # M01 — base E02 (fastp+spades+cgMLST listeria); add MLST in parallel
    L.append(_add_typing_to_chain(
        eid="MOD_M01_E02_add_mlst",
        base_id="E02_cgmlst_lis_fastp_spades",
        trim="step_1PP_trimming__fastp", asm="step_2AS_denovo__spades",
        base_typing="step_4TY_cgMLST__chewbbaca",
        new_typing="step_4TY_MLST__mlst",
        cmp="2026.LIS.6.1.1", genus_species="listeria_monocytogenes",
        turn1_prompt="cgMLST allelic profile for Listeria monocytogenes "
                     "from paired Illumina FASTQ (fastp + SPAdes + chewbbaca).",
        turn2_prompt="Now also run classic MLST in parallel on the same assembly.",
    ))

    # M02 — base D01 (fastp+spades); add chewbbaca downstream
    L.append(ConversationExample(
        eid="MOD_M02_D01_add_chewbbaca",
        category="modification", base_id="D01_fastp_spades_lis",
        modification_kind="add",
        notes="add a downstream typing step (cgMLST) to a trim+assembly chain",
        turns=[
            Turn(prompt="From Illumina paired-end FASTQ of Listeria monocytogenes: "
                        "trim with fastp and assemble with SPAdes.",
                 nextflow_code=chain_trim_asm("step_1PP_trimming__fastp",
                                              "step_2AS_denovo__spades"),
                 params=_params_fastq("2026.LIS.4.1.1"),
                 inputs=["fastq_paired:2026.LIS.4.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]),
            Turn(prompt="Now also compute cgMLST allelic profiles on the resulting assembly.",
                 nextflow_code=chain_trim_asm_typing(
                     "step_1PP_trimming__fastp", "step_2AS_denovo__spades",
                     "step_4TY_cgMLST__chewbbaca"),
                 params=_params_fastq("2026.LIS.4.1.1", "listeria_monocytogenes"),
                 inputs=["fastq_paired:2026.LIS.4.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]
                                  + PROCS["step_4TY_cgMLST__chewbbaca"]),
        ],
    ))

    # M03 — base B01 (spades only); add fastp trimming upstream
    L.append(ConversationExample(
        eid="MOD_M03_B01_add_trimming",
        category="modification", base_id="B01_spades_listeria",
        modification_kind="add",
        notes="add a pre-processing trimming step upstream of an assembly mono-step",
        turns=[
            Turn(prompt="De novo genome assembly with SPAdes from Illumina paired-end "
                        "reads of Listeria monocytogenes.",
                 nextflow_code=chain_mono_asm("step_2AS_denovo__spades"),
                 params=_params_fastq("2026.LIS.3.1.1"),
                 inputs=["fastq_paired:2026.LIS.3.1.1"],
                 expected_processes=PROCS["step_2AS_denovo__spades"]),
            Turn(prompt="Add a fastp trimming step before the assembly.",
                 nextflow_code=chain_trim_asm("step_1PP_trimming__fastp",
                                              "step_2AS_denovo__spades"),
                 params=_params_fastq("2026.LIS.3.1.1"),
                 inputs=["fastq_paired:2026.LIS.3.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]),
        ],
    ))

    # M04 — base A04 (mono cgMLST listeria); add MLST in parallel
    L.append(ConversationExample(
        eid="MOD_M04_A04_add_mlst_parallel",
        category="modification", base_id="A04_cgmlst_listeria",
        modification_kind="add",
        notes="add a second typing step in parallel on an existing assembly",
        turns=[
            Turn(prompt="cgMLST allelic profile for Listeria monocytogenes "
                        "from a pre-existing assembly.",
                 nextflow_code=chain_mono_typing_assembly("step_4TY_cgMLST__chewbbaca"),
                 params=_params_assembly("2026.LIS.2.1.1", "listeria_monocytogenes"),
                 inputs=["assembly:2026.LIS.2.1.1"],
                 expected_processes=PROCS["step_4TY_cgMLST__chewbbaca"]),
            Turn(prompt="Also run classic MLST on the same assembly.",
                 nextflow_code=chain_mono_two_typing_assembly(
                     "step_4TY_cgMLST__chewbbaca", "step_4TY_MLST__mlst"),
                 params=_params_assembly("2026.LIS.2.1.1", "listeria_monocytogenes"),
                 inputs=["assembly:2026.LIS.2.1.1"],
                 expected_processes=PROCS["step_4TY_cgMLST__chewbbaca"]
                                  + PROCS["step_4TY_MLST__mlst"]),
        ],
    ))

    # M05 — base E07 (fastp+spades+abricate); add prokka annotation in parallel
    L.append(_add_typing_to_chain(
        eid="MOD_M05_E07_add_prokka",
        base_id="E07_abricate_eco",
        trim="step_1PP_trimming__fastp", asm="step_2AS_denovo__spades",
        base_typing="step_4AN_AMR__abricate",
        new_typing="step_4AN_genes__prokka",
        cmp="2026.ECO.6.1.1", genus_species="escherichia_coli",
        turn1_prompt="Resistance gene detection with ABRicate on Escherichia coli "
                     "from Illumina paired FASTQ.",
        turn2_prompt="Also annotate the assembly with Prokka.",
    ))

    # ----------------------------------------------------------------- REPLACE
    # M06 — D01 swap spades -> shovill
    L.append(ConversationExample(
        eid="MOD_M06_D01_replace_spades_with_shovill",
        category="modification", base_id="D01_fastp_spades_lis",
        modification_kind="replace",
        notes="swap one de-novo assembler for another (emit name changes)",
        turns=[
            Turn(prompt="From Illumina paired-end FASTQ of Listeria monocytogenes: "
                        "trim with fastp and assemble with SPAdes.",
                 nextflow_code=chain_trim_asm("step_1PP_trimming__fastp",
                                              "step_2AS_denovo__spades"),
                 params=_params_fastq("2026.LIS.4.1.1"),
                 inputs=["fastq_paired:2026.LIS.4.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]),
            Turn(prompt="Use Shovill instead of SPAdes for the assembly.",
                 nextflow_code=chain_trim_asm("step_1PP_trimming__fastp",
                                              "step_2AS_denovo__shovill"),
                 params=_params_fastq("2026.LIS.4.1.1"),
                 inputs=["fastq_paired:2026.LIS.4.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__shovill"]),
        ],
    ))

    # M07 — D03 swap trimmomatic -> fastp
    L.append(ConversationExample(
        eid="MOD_M07_D03_replace_trimmomatic_with_fastp",
        category="modification", base_id="D03_trimmomatic_spades",
        modification_kind="replace",
        notes="swap one trimmer for another",
        turns=[
            Turn(prompt="Pipeline: trim with Trimmomatic, assemble with SPAdes. Illumina paired-end.",
                 nextflow_code=chain_trim_asm("step_1PP_trimming__trimmomatic",
                                              "step_2AS_denovo__spades"),
                 params=_params_fastq("2026.SAM.1.1.1"),
                 inputs=["fastq_paired:2026.SAM.1.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__trimmomatic"]
                                  + PROCS["step_2AS_denovo__spades"]),
            Turn(prompt="Replace Trimmomatic with fastp.",
                 nextflow_code=chain_trim_asm("step_1PP_trimming__fastp",
                                              "step_2AS_denovo__spades"),
                 params=_params_fastq("2026.SAM.1.1.1"),
                 inputs=["fastq_paired:2026.SAM.1.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]),
        ],
    ))

    # M08 — E01 swap spades -> unicycler
    L.append(ConversationExample(
        eid="MOD_M08_E01_replace_spades_with_unicycler",
        category="modification", base_id="E01_mlst_lis",
        modification_kind="replace",
        notes="swap assembler inside a 3-step chain",
        turns=[
            Turn(prompt="Classic MLST on Listeria monocytogenes from paired-end "
                        "Illumina FASTQ (trim + assembly + MLST).",
                 nextflow_code=chain_trim_asm_typing(
                     "step_1PP_trimming__fastp", "step_2AS_denovo__spades",
                     "step_4TY_MLST__mlst"),
                 params=_params_fastq("2026.LIS.5.1.1", "listeria_monocytogenes"),
                 inputs=["fastq_paired:2026.LIS.5.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]
                                  + PROCS["step_4TY_MLST__mlst"]),
            Turn(prompt="Use Unicycler instead of SPAdes.",
                 nextflow_code=chain_trim_asm_typing(
                     "step_1PP_trimming__fastp", "step_2AS_denovo__unicycler",
                     "step_4TY_MLST__mlst"),
                 params=_params_fastq("2026.LIS.5.1.1", "listeria_monocytogenes"),
                 inputs=["fastq_paired:2026.LIS.5.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__unicycler"]
                                  + PROCS["step_4TY_MLST__mlst"]),
        ],
    ))

    # M09 — E07 swap abricate -> prokka
    L.append(ConversationExample(
        eid="MOD_M09_E07_replace_abricate_with_prokka",
        category="modification", base_id="E07_abricate_eco",
        modification_kind="replace",
        notes="swap downstream tool",
        turns=[
            Turn(prompt="Resistance gene detection with ABRicate on Escherichia coli "
                        "from Illumina paired FASTQ.",
                 nextflow_code=chain_trim_asm_typing(
                     "step_1PP_trimming__fastp", "step_2AS_denovo__spades",
                     "step_4AN_AMR__abricate"),
                 params=_params_fastq("2026.ECO.6.1.1", "escherichia_coli"),
                 inputs=["fastq_paired:2026.ECO.6.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]
                                  + PROCS["step_4AN_AMR__abricate"]),
            Turn(prompt="Switch from ABRicate to Prokka annotation.",
                 nextflow_code=chain_trim_asm_typing(
                     "step_1PP_trimming__fastp", "step_2AS_denovo__spades",
                     "step_4AN_genes__prokka"),
                 params=_params_fastq("2026.ECO.6.1.1", "escherichia_coli"),
                 inputs=["fastq_paired:2026.ECO.6.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]
                                  + PROCS["step_4AN_genes__prokka"]),
        ],
    ))

    # M10 — A05 swap chewbbaca -> mlst (different typing tool on existing assembly)
    L.append(ConversationExample(
        eid="MOD_M10_A05_replace_cgmlst_with_mlst",
        category="modification", base_id="A05_cgmlst_ecoli",
        modification_kind="replace",
        notes="swap one typing approach for another (cgMLST → MLST)",
        turns=[
            Turn(prompt="cgMLST allelic profile on an Escherichia coli assembly.",
                 nextflow_code=chain_mono_typing_assembly("step_4TY_cgMLST__chewbbaca"),
                 params=_params_assembly("2026.ECO.2.1.1", "escherichia_coli"),
                 inputs=["assembly:2026.ECO.2.1.1"],
                 expected_processes=PROCS["step_4TY_cgMLST__chewbbaca"]),
            Turn(prompt="Switch from cgMLST to classic 7-gene MLST.",
                 nextflow_code=chain_mono_typing_assembly("step_4TY_MLST__mlst"),
                 params=_params_assembly("2026.ECO.2.1.1", "escherichia_coli"),
                 inputs=["assembly:2026.ECO.2.1.1"],
                 expected_processes=PROCS["step_4TY_MLST__mlst"]),
        ],
    ))

    # -------------------------------------------------------------------- DROP
    # M11 — H01 (mlst+cgmlst) drop cgmlst
    L.append(ConversationExample(
        eid="MOD_M11_H01_drop_cgmlst",
        category="modification", base_id="H01_mlst_plus_cgmlst_lis",
        modification_kind="drop",
        notes="remove one of two parallel downstream steps",
        turns=[
            Turn(prompt="Run both MLST and cgMLST typing on Listeria monocytogenes "
                        "from paired Illumina FASTQ.",
                 nextflow_code=chain_trim_asm_two_typing(
                     "step_1PP_trimming__fastp", "step_2AS_denovo__spades",
                     "step_4TY_MLST__mlst", "step_4TY_cgMLST__chewbbaca"),
                 params=_params_fastq("2026.LIS.C.1.1", "listeria_monocytogenes"),
                 inputs=["fastq_paired:2026.LIS.C.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]
                                  + PROCS["step_4TY_MLST__mlst"]
                                  + PROCS["step_4TY_cgMLST__chewbbaca"]),
            Turn(prompt="Drop the cgMLST step, only keep MLST.",
                 nextflow_code=chain_trim_asm_typing(
                     "step_1PP_trimming__fastp", "step_2AS_denovo__spades",
                     "step_4TY_MLST__mlst"),
                 params=_params_fastq("2026.LIS.C.1.1", "listeria_monocytogenes"),
                 inputs=["fastq_paired:2026.LIS.C.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]
                                  + PROCS["step_4TY_MLST__mlst"]),
        ],
    ))

    # M12 — D01 drop spades (keep just fastp trimming)
    L.append(ConversationExample(
        eid="MOD_M12_D01_drop_assembly",
        category="modification", base_id="D01_fastp_spades_lis",
        modification_kind="drop",
        notes="remove the assembly step, leave only trimming",
        turns=[
            Turn(prompt="From Illumina paired-end FASTQ of Listeria monocytogenes: "
                        "trim with fastp and assemble with SPAdes.",
                 nextflow_code=chain_trim_asm("step_1PP_trimming__fastp",
                                              "step_2AS_denovo__spades"),
                 params=_params_fastq("2026.LIS.4.1.1"),
                 inputs=["fastq_paired:2026.LIS.4.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]),
            Turn(prompt="Actually, drop the assembly and just trim the reads.",
                 nextflow_code=_nf_header(["step_1PP_trimming__fastp"]) + _wf(
                     "step_1PP_trimming__fastp(getSingleInput())"
                 ),
                 params=_params_fastq("2026.LIS.4.1.1"),
                 inputs=["fastq_paired:2026.LIS.4.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]),
        ],
    ))

    # M13 — I01 drop kmerfinder
    L.append(ConversationExample(
        eid="MOD_M13_I01_drop_kmerfinder",
        category="modification", base_id="I01_kmerfinder_fastp_spades",
        modification_kind="drop",
        notes="remove the upstream species-id branch",
        turns=[
            Turn(prompt="Identify the species with KmerFinder, in parallel trim with "
                        "fastp and assemble with SPAdes (Illumina paired).",
                 nextflow_code=_nf_header(
                     ["step_3TX_species__kmerfinder", "step_1PP_trimming__fastp",
                      "step_2AS_denovo__spades"]
                 ) + _wf(
                     "raw = getSingleInput()",
                     "step_3TX_species__kmerfinder(raw)",
                     "trimmed   = step_1PP_trimming__fastp(raw).trimmed",
                     "assembled = step_2AS_denovo__spades(trimmed).assembled",
                 ),
                 params={**_params_fastq("2026.UNK.5.1.1"),
                         "step_3TX_species__kmerfinder__db": "/tmp/_dummy_kmerfinder_db"},
                 inputs=["fastq_paired:2026.UNK.5.1.1"],
                 expected_processes=PROCS["step_3TX_species__kmerfinder"]
                                  + PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]),
            Turn(prompt="Drop the KmerFinder species ID. Keep only trim + assembly.",
                 nextflow_code=chain_trim_asm("step_1PP_trimming__fastp",
                                              "step_2AS_denovo__spades"),
                 params=_params_fastq("2026.UNK.5.1.1"),
                 inputs=["fastq_paired:2026.UNK.5.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]),
        ],
    ))

    # ---------------------------------------------------------- SWITCH_SPECIES
    # M14 — E02 listeria → salmonella
    L.append(ConversationExample(
        eid="MOD_M14_E02_switch_species_to_salmonella",
        category="modification", base_id="E02_cgmlst_lis_fastp_spades",
        modification_kind="switch_species",
        notes="re-target the same pipeline at a different supported species",
        turns=[
            Turn(prompt="cgMLST allelic profile for Listeria monocytogenes from "
                        "paired Illumina FASTQ (fastp + SPAdes + chewbbaca).",
                 nextflow_code=chain_trim_asm_typing(
                     "step_1PP_trimming__fastp", "step_2AS_denovo__spades",
                     "step_4TY_cgMLST__chewbbaca"),
                 params=_params_fastq("2026.LIS.6.1.1", "listeria_monocytogenes"),
                 inputs=["fastq_paired:2026.LIS.6.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]
                                  + PROCS["step_4TY_cgMLST__chewbbaca"]),
            Turn(prompt="Run the same pipeline for Salmonella enterica instead "
                        "of Listeria monocytogenes.",
                 nextflow_code=chain_trim_asm_typing(
                     "step_1PP_trimming__fastp", "step_2AS_denovo__spades",
                     "step_4TY_cgMLST__chewbbaca"),
                 params=_params_fastq("2026.SAL.5.1.1", "salmonella_enterica"),
                 inputs=["fastq_paired:2026.SAL.5.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]
                                  + PROCS["step_4TY_cgMLST__chewbbaca"]),
        ],
    ))

    # M15 — A04 listeria → ecoli (mono cgMLST)
    L.append(ConversationExample(
        eid="MOD_M15_A04_switch_species_to_ecoli",
        category="modification", base_id="A04_cgmlst_listeria",
        modification_kind="switch_species",
        notes="same step, different species (both supported by chewbbaca)",
        turns=[
            Turn(prompt="cgMLST allelic profile for Listeria monocytogenes from "
                        "a pre-existing assembly.",
                 nextflow_code=chain_mono_typing_assembly("step_4TY_cgMLST__chewbbaca"),
                 params=_params_assembly("2026.LIS.2.1.1", "listeria_monocytogenes"),
                 inputs=["assembly:2026.LIS.2.1.1"],
                 expected_processes=PROCS["step_4TY_cgMLST__chewbbaca"]),
            Turn(prompt="Same thing but for Escherichia coli.",
                 nextflow_code=chain_mono_typing_assembly("step_4TY_cgMLST__chewbbaca"),
                 params=_params_assembly("2026.ECO.2.1.1", "escherichia_coli"),
                 inputs=["assembly:2026.ECO.2.1.1"],
                 expected_processes=PROCS["step_4TY_cgMLST__chewbbaca"]),
        ],
    ))

    # M16 — E07 ecoli → salmonella
    L.append(ConversationExample(
        eid="MOD_M16_E07_switch_species_to_salmonella",
        category="modification", base_id="E07_abricate_eco",
        modification_kind="switch_species",
        notes="same AMR pipeline retargeted",
        turns=[
            Turn(prompt="Resistance gene detection with ABRicate on Escherichia coli "
                        "from Illumina paired FASTQ.",
                 nextflow_code=chain_trim_asm_typing(
                     "step_1PP_trimming__fastp", "step_2AS_denovo__spades",
                     "step_4AN_AMR__abricate"),
                 params=_params_fastq("2026.ECO.6.1.1", "escherichia_coli"),
                 inputs=["fastq_paired:2026.ECO.6.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]
                                  + PROCS["step_4AN_AMR__abricate"]),
            Turn(prompt="Switch to Salmonella enterica.",
                 nextflow_code=chain_trim_asm_typing(
                     "step_1PP_trimming__fastp", "step_2AS_denovo__spades",
                     "step_4AN_AMR__abricate"),
                 params=_params_fastq("2026.SAL.7.1.1", "salmonella_enterica"),
                 inputs=["fastq_paired:2026.SAL.7.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]
                                  + PROCS["step_4AN_AMR__abricate"]),
        ],
    ))

    # M17 — D05 campylobacter → ecoli
    L.append(ConversationExample(
        eid="MOD_M17_D05_switch_species_to_ecoli",
        category="modification", base_id="D05_fastp_spades_cam",
        modification_kind="switch_species",
        notes="trim+assembly chain retargeted, no species filter to satisfy",
        turns=[
            Turn(prompt="Trim and de novo assembly (fastp + SPAdes) for a paired-end "
                        "Illumina Campylobacter sample.",
                 nextflow_code=chain_trim_asm("step_1PP_trimming__fastp",
                                              "step_2AS_denovo__spades"),
                 params=_params_fastq("2026.CAM.3.1.1"),
                 inputs=["fastq_paired:2026.CAM.3.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]),
            Turn(prompt="Apply the same pipeline to an Escherichia coli sample.",
                 nextflow_code=chain_trim_asm("step_1PP_trimming__fastp",
                                              "step_2AS_denovo__spades"),
                 params=_params_fastq("2026.ECO.4.1.1"),
                 inputs=["fastq_paired:2026.ECO.4.1.1"],
                 expected_processes=PROCS["step_1PP_trimming__fastp"]
                                  + PROCS["step_2AS_denovo__spades"]),
        ],
    ))

    return L


# ---------------------------------------------------------------------------
# Generic helper for ADD-typing transformations
# ---------------------------------------------------------------------------
def _add_typing_to_chain(eid, base_id, trim, asm, base_typing, new_typing,
                         cmp, genus_species, turn1_prompt, turn2_prompt,
                         notes="add a second typing step in parallel"):
    return ConversationExample(
        eid=eid, category="modification", base_id=base_id,
        modification_kind="add", notes=notes,
        turns=[
            Turn(prompt=turn1_prompt,
                 nextflow_code=chain_trim_asm_typing(trim, asm, base_typing),
                 params=_params_fastq(cmp, genus_species),
                 inputs=[f"fastq_paired:{cmp}"],
                 expected_processes=PROCS[trim] + PROCS[asm] + PROCS[base_typing]),
            Turn(prompt=turn2_prompt,
                 nextflow_code=chain_trim_asm_two_typing(trim, asm, base_typing, new_typing),
                 params=_params_fastq(cmp, genus_species),
                 inputs=[f"fastq_paired:{cmp}"],
                 expected_processes=PROCS[trim] + PROCS[asm]
                                  + PROCS[base_typing] + PROCS[new_typing]),
        ],
    )


if __name__ == "__main__":
    L = build_modifications()
    print(f"Built {len(L)} modification conversations")
    for c in L:
        print(f"  {c.eid:50s}  base={c.base_id:35s}  kind={c.modification_kind}")
