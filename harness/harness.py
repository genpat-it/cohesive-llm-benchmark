#!/usr/bin/env python3.11
"""
Validation harness for 50 prompt/nextflow training pairs.

For each example dict, this:
  1. writes the .nf into cohesive-ngsmanager/pipelines/_dataset_<id>.nf
  2. materialises the dummy inputs declared in `inputs` under inputdir
  3. writes a params.json
  4. runs `nextflow -stub-run` (or -preview for syntax-only)
  5. checks expected outcomes (placeholders / errors / "DAG OK")
  6. cleans up and returns a verdict

Used by generate_dataset.py.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

_NGSMANAGER_DIR = os.environ.get("NGSMANAGER_DIR")
if not _NGSMANAGER_DIR:
    raise SystemExit(
        "NGSMANAGER_DIR is not set.\n"
        "Point it at your cohesive-ngsmanager checkout, e.g.:\n"
        "    export NGSMANAGER_DIR=/path/to/cohesive-ngsmanager\n"
        "See INSTALL.md for details."
    )
FW = Path(_NGSMANAGER_DIR).resolve()

if not (FW / "steps").is_dir():
    raise SystemExit(
        f"cohesive-ngsmanager not found at {FW}\n"
        f"NGSMANAGER_DIR must point at the cohesive-ngsmanager repo root "
        f"(the directory that contains steps/, functions/, modules/, multi/)."
    )

NEXTFLOW = shutil.which("nextflow") or "/usr/local/bin/nextflow"
if not Path(NEXTFLOW).exists():
    raise SystemExit("nextflow not on PATH")


# ---------------------------------------------------------------------------
# input file utilities
# ---------------------------------------------------------------------------
def _empty_gz(path: Path) -> None:
    """Create a tiny valid gzip file (1-byte content)."""
    path.parent.mkdir(parents=True, exist_ok=True)
    # `gzip -c < /dev/null` makes a valid empty gzip header
    subprocess.run(
        ["bash", "-c", f"gzip -c < /dev/null > {path.as_posix()}"],
        check=True,
    )


def _dummy_fasta(path: Path, seq: str = "ACGTACGTACGTACGTACGTACGT") -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f">contig_1\n{seq}\n")


def _dummy_vcf(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "##fileformat=VCFv4.2\n"
        "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n"
        "chr1\t1\t.\tA\tT\t100\tPASS\t.\n"
    )


# ---------------------------------------------------------------------------
# layouts based on the framework's getResult() conventions
# ---------------------------------------------------------------------------
def fastq_paired_layout(inputdir: Path, anno: str, cmp: str,
                        ds: str = "DS99999", dt: str = "DT260224",
                        met: str = "import") -> tuple[Path, Path]:
    base = inputdir / anno / cmp / "0SQ_rawreads" / f"{ds}-{dt}_{met}" / "result"
    r1 = base / f"{ds}-{dt}_{cmp}_R1.fastq.gz"
    r2 = base / f"{ds}-{dt}_{cmp}_R2.fastq.gz"
    _empty_gz(r1); _empty_gz(r2)
    return r1, r2


def fastq_single_layout(inputdir: Path, anno: str, cmp: str,
                        ds: str = "DS99999", dt: str = "DT260224",
                        met: str = "import") -> Path:
    base = inputdir / anno / cmp / "0SQ_rawreads" / f"{ds}-{dt}_{met}" / "result"
    r1 = base / f"{ds}-{dt}_{cmp}_R1.fastq.gz"
    _empty_gz(r1)
    return r1


def assembly_layout(inputdir: Path, anno: str, cmp: str,
                    ds: str = "DS99999", dt: str = "DT260224",
                    met: str = "external") -> Path:
    base = inputdir / anno / cmp / "2AS_import" / f"{ds}-{dt}_{met}" / "result"
    fa = base / f"{ds}-{dt}_{cmp}_{met}.fasta"
    _dummy_fasta(fa)
    return fa


def trimmed_layout(inputdir: Path, anno: str, cmp: str,
                   ds: str = "DS99999", dt: str = "DT260224",
                   met: str = "fastp") -> tuple[Path, Path]:
    base = inputdir / anno / cmp / "1PP_trimming" / f"{ds}-{dt}_{met}" / "result"
    r1 = base / f"{ds}-{dt}_{cmp}_{met}_R1.fastq.gz"
    r2 = base / f"{ds}-{dt}_{cmp}_{met}_R2.fastq.gz"
    _empty_gz(r1); _empty_gz(r2)
    return r1, r2


def gff_layout(inputdir: Path, anno: str, cmp: str,
               ds: str = "DS99999", dt: str = "DT260224",
               met: str = "prokka") -> Path:
    """4AN_genes/<DS>-<DT>_prokka/result/<base>.gff — for panaroo etc."""
    base_dir = inputdir / anno / cmp / "4AN_genes" / f"{ds}-{dt}_{met}" / "result"
    gff = base_dir / f"{ds}-{dt}_{cmp}_{met}.gff"
    base_dir.mkdir(parents=True, exist_ok=True)
    gff.write_text("##gff-version 3\n##sequence-region contig1 1 1000\n")
    return gff


def alleles_chewbbaca_layout(inputdir: Path, anno: str, cmp: str,
                              ds: str = "DS99999", dt: str = "DT260224",
                              met: str = "chewbbaca") -> Path:
    """4TY_cgMLST/<DS>-<DT>_chewbbaca/result/<base>_results_crc32.tsv — for grapetree."""
    base_dir = inputdir / anno / cmp / "4TY_cgMLST" / f"{ds}-{dt}_{met}" / "result"
    tsv = base_dir / f"{ds}-{dt}_{cmp}_{met}_results_crc32.tsv"
    base_dir.mkdir(parents=True, exist_ok=True)
    tsv.write_text("FILE\tlocus1\tlocus2\nsample1\t1\t2\n")
    return tsv


def vcf_layout(inputdir: Path, anno: str, cmp: str,
               ds: str = "DS99999", dt: str = "DT260224",
               met: str = "snippy") -> Path:
    """2AS_mapping/<DS>-<DT>_snippy/result/<base>.vcf — for vcf2mst etc."""
    base_dir = inputdir / anno / cmp / "2AS_mapping" / f"{ds}-{dt}_{met}" / "result"
    vcf = base_dir / f"{ds}-{dt}_{cmp}_{met}_0.vcf"
    base_dir.mkdir(parents=True, exist_ok=True)
    vcf.write_text(
        "##fileformat=VCFv4.2\n"
        "#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\n"
        "chr1\t1\t.\tA\tT\t100\tPASS\t.\n"
    )
    return vcf


def metadata_csv(path: Path) -> Path:
    """A 2-row metadata CSV with strain/date/region — enough for prepare_metadata."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "strain,date,region,country\n"
        "sample1,2024-01-01,EU,IT\n"
        "sample2,2024-01-02,EU,IT\n"
    )
    return path


def geodata_tsv(path: Path) -> Path:
    """A minimal geo coordinates TSV for augur etc."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "country\tregion\tlatitude\tlongitude\n"
        "IT\tEU\t42.0\t12.0\n"
    )
    return path


# ---------------------------------------------------------------------------
# datatypes
# ---------------------------------------------------------------------------
@dataclass
class Example:
    eid: str
    category: str
    prompt: str
    nextflow_code: str
    params: dict[str, Any]
    inputs: list[str] = field(default_factory=list)
    # inputs is a list of layout strings: "fastq_paired:2026.LIS.1.1.1",
    #                                     "assembly:2026.CAMP.1.1.1",
    #                                     "trimmed:2026.LIS.1.1.1",
    expected_processes: int = 0   # number of distinct process placeholders to expect
    expected_error: str | None = None   # if set, success means this regex appears in log
    notes: str = ""

    def to_serializable(self) -> dict:
        return {
            "id": self.eid,
            "category": self.category,
            "prompt": self.prompt,
            "nextflow_code": self.nextflow_code,
            "params": self.params,
            "notes": self.notes,
        }


# ---------------------------------------------------------------------------
# validation runner
# ---------------------------------------------------------------------------
@dataclass
class Verdict:
    eid: str
    passed: bool
    reason: str
    log_tail: str = ""


class Harness:
    def __init__(self, scratch_root: Path | None = None):
        # Default scratch root: <system tempdir>/cohesive_llm_bench
        # Override by passing scratch_root explicitly or by setting BENCH_SCRATCH_DIR.
        default_root = Path(tempfile.gettempdir()) / "cohesive_llm_bench"
        env_root = os.environ.get("BENCH_SCRATCH_DIR")
        self.scratch = Path(scratch_root or env_root or default_root).resolve()
        self.scratch.mkdir(parents=True, exist_ok=True)
        self.pipelines = FW / "pipelines"
        # internal cache: avoid re-creating identical input layouts
        self._materialised: set[str] = set()

    # ----------------------- inputs --------------------------------------
    def _materialise(self, inputdir: Path, spec: str) -> None:
        if spec in self._materialised:
            return
        try:
            kind, cmp = spec.split(":", 1)
        except ValueError:
            raise ValueError(f"bad input spec: {spec!r}")
        anno = cmp[:4]
        if kind == "fastq_paired":
            fastq_paired_layout(inputdir, anno, cmp)
        elif kind == "fastq_single":
            fastq_single_layout(inputdir, anno, cmp)
        elif kind == "assembly":
            assembly_layout(inputdir, anno, cmp)
        elif kind == "trimmed":
            trimmed_layout(inputdir, anno, cmp)
        elif kind == "gff":
            gff_layout(inputdir, anno, cmp)
        elif kind == "alleles":
            alleles_chewbbaca_layout(inputdir, anno, cmp)
        elif kind == "vcf":
            vcf_layout(inputdir, anno, cmp)
        else:
            raise ValueError(f"unknown input kind: {kind}")
        self._materialised.add(spec)

    # ----------------------- run -----------------------------------------
    def run(self, ex: Example) -> Verdict:
        scratch = self.scratch / ex.eid
        scratch.mkdir(parents=True, exist_ok=True)
        # Reuse one shared inputdir across all examples: dummy files are tiny
        # and cmp values are unique, so layouts don't collide. Avoids piling
        # up ~50 copies of the framework's directory tree.
        inputdir = self.scratch / "_shared_inputdir"
        outdir = scratch / "out"
        workdir = scratch / "work"

        # ----------- materialise inputs --------------
        for spec in ex.inputs:
            self._materialise(inputdir, spec)

        # ----------- pipeline file -------------------
        pipe = self.pipelines / f"_dataset_{ex.eid}.nf"
        pipe.write_text(ex.nextflow_code)

        # ----------- params --------------------------
        params = {**ex.params,
                  "inputdir": str(inputdir),
                  "outdir": str(outdir),
                  "assets_dir": str(FW / "assets")}
        params_file = scratch / "params.json"
        params_file.write_text(json.dumps(params, indent=2))

        # ----------- run -----------------------------
        log = scratch / "nextflow.log"
        cmd = [NEXTFLOW, "run", str(pipe),
               "-stub-run",
               "-params-file", str(params_file),
               "-work-dir", str(workdir)]
        env = os.environ.copy()
        try:
            p = subprocess.run(cmd, cwd=str(FW), env=env,
                               capture_output=True, text=True, timeout=120)
            stdout = p.stdout
            stderr = p.stderr
        except subprocess.TimeoutExpired:
            return Verdict(ex.eid, False, "nextflow timed out (>120 s)")
        finally:
            pipe.unlink(missing_ok=True)
            # purge the per-example work dir to save space; the log is
            # written below and is enough for postmortem.
            if workdir.exists():
                import shutil
                shutil.rmtree(workdir, ignore_errors=True)
            # also drop framework-side work/ that nextflow creates by default
            fw_work = FW / "work"
            if fw_work.exists():
                shutil.rmtree(fw_work, ignore_errors=True)
        combined = (stdout + "\n" + stderr)
        log.write_text(combined)

        # ----------- judge ---------------------------
        return self._judge(ex, combined)

    # ----------------------- judges --------------------------------------
    def _judge(self, ex: Example, log: str) -> Verdict:
        if ex.expected_error:
            if re.search(ex.expected_error, log):
                return Verdict(ex.eid, True,
                               f"expected error matched: {ex.expected_error}")
            return Verdict(ex.eid, False,
                           f"expected error '{ex.expected_error}' not found",
                           log_tail="\n".join(log.splitlines()[-12:]))

        # default: count distinct process placeholders in the DAG
        # pattern: ":<name>" followed by spaces and end-of-name marker (-, |, or eol).
        # process names may contain digits (kraken2, braken2, shovill_se, etc.)
        names = set(re.findall(r":([A-Za-z][A-Za-z0-9_]*)\s+[-|]", log))
        # Also count any process actually executed (executor rows)
        executed = re.findall(r"\[[a-f0-9]{2}/[a-f0-9]+\] [^\n]+:([A-Za-z][A-Za-z0-9_]*)", log)
        names.update(executed)
        n = len(names)
        if n >= ex.expected_processes:
            return Verdict(ex.eid, True,
                           f"{n} distinct processes in DAG (expected >= {ex.expected_processes})")
        return Verdict(ex.eid, False,
                       f"only {n} processes in DAG (expected >= {ex.expected_processes})",
                       log_tail="\n".join(log.splitlines()[-12:]))


# ---------------------------------------------------------------------------
def run_examples(examples: list[Example], stop_on_fail: bool = False) -> list[Verdict]:
    """Run all examples sequentially, return list of verdicts in same order."""
    H = Harness()
    verdicts: list[Verdict] = []
    import time
    t0_all = time.time()
    for i, ex in enumerate(examples, start=1):
        t0 = time.time()
        line_prefix = f"[{i:3d}/{len(examples)}] {ex.eid:35s}  ({ex.category})"
        print(line_prefix + "  RUNNING...", flush=True)
        v = H.run(ex)
        verdicts.append(v)
        dt = time.time() - t0
        status = "PASS" if v.passed else "FAIL"
        print(f"{line_prefix}  {status}  ({dt:.1f}s)  - {v.reason}", flush=True)
        if not v.passed and v.log_tail:
            for line in v.log_tail.splitlines():
                print(f"      | {line}", flush=True)
        if stop_on_fail and not v.passed:
            break
    elapsed = time.time() - t0_all
    print(f"\nTotal time: {elapsed/60:.1f} min", flush=True)
    return verdicts


def summary(verdicts: list[Verdict]) -> None:
    p = sum(1 for v in verdicts if v.passed)
    f = len(verdicts) - p
    print("=" * 70)
    print(f"  SUMMARY: {p}/{len(verdicts)} passed, {f} failed")
    print("=" * 70)


if __name__ == "__main__":
    # CLI entry: validate all blueprints. Add repo root to path so we can
    # import the dataset module regardless of where we are invoked from.
    import sys as _sys
    from pathlib import Path as _Path
    _sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
    from dataset.blueprints import build_all   # noqa: E402

    examples = build_all()
    if "--extended" in sys.argv:
        from dataset.blueprints_extended import build_extended  # noqa: E402
        examples = examples + build_extended()
    # filter: --only=eid1,eid2,...   or   --first=N
    only = None
    for arg in sys.argv[1:]:
        if arg.startswith("--only="):
            only = set(arg.split("=", 1)[1].split(","))
        elif arg.startswith("--first="):
            examples = examples[: int(arg.split("=", 1)[1])]
    if only:
        examples = [e for e in examples if e.eid in only]
    print(f"Will run {len(examples)} examples", flush=True)
    verdicts = run_examples(examples)
    summary(verdicts)
