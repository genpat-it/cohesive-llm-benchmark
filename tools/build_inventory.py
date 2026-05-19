#!/usr/bin/env python3.11
"""
Inventory every step + multi workflow in cohesive-ngsmanager.

Extracts: take signature, emit list, example workflow invocation, when conditions,
hard-coded SPECIES_SCHEMA / SCHEMAS maps, included functions, input-getter used.

Writes to _inventory.json beside this script.
"""

from __future__ import annotations
import json
import os
import re
from pathlib import Path

_NGSMANAGER_DIR = os.environ.get("NGSMANAGER_DIR")
if not _NGSMANAGER_DIR:
    raise SystemExit(
        "NGSMANAGER_DIR is not set.\n"
        "Point it at your cohesive-ngsmanager checkout, e.g.:\n"
        "    export NGSMANAGER_DIR=/path/to/cohesive-ngsmanager"
    )
FW = Path(_NGSMANAGER_DIR).resolve()
OUT = Path(__file__).resolve().parent / "_inventory.json"


# ---------------------------------------------------------------------------
INPUT_GETTERS = {
    "getInput", "getSingleInput", "getInputFolders", "getAssembly",
    "getTrimmedReads", "getVCFs", "getReads", "getRawReads",
    "getDepletedReads", "getReferences", "getReferenceUnkeyed",
    "getReferenceCodes", "getSingleReference",
}

WF_OPEN = re.compile(r"^workflow\s+(\w+)\s*\{", re.M)
WF_BOTTOM = re.compile(r"^workflow\s*\{[^}]*?\}\s*$", re.M | re.S)
TAKE_BLOCK = re.compile(
    r"^workflow\s+(\w+)\s*\{[^}]*?\btake\s*:\s*([^\n]*\n(?:\s*\w+\s*\n)*)",
    re.M | re.S,
)
EMIT_BLOCK = re.compile(r"\bemit\s*:\s*\n((?:[^\n}]*\n?)+)")
WHEN_BLOCK = re.compile(r"^\s*when\s*:\s*\n?\s*(.+?)$", re.M)
SCHEMA_MAP_HEAD = re.compile(r"\b(SPECIES_SCHEMA|SCHEMAS|SCHEMAS_BY_GENUS|PARAMS_BY_GENUS|GENUS_SPECIES|GENUS|SPECIES|SCHEMA_BY_SPECIES)\s*=\s*\[")
MAP_KEYS = re.compile(r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*:", re.M)


def extract_bracket_map_body(text: str, start: int) -> str:
    """Given the index right after `[`, return body up to balanced `]`."""
    depth = 1
    i = start
    while i < len(text) and depth > 0:
        c = text[i]
        if c == '[':
            depth += 1
        elif c == ']':
            depth -= 1
        i += 1
    return text[start:i - 1]


def find_species_keys(text: str) -> list[str]:
    keys: list[str] = []
    for m in SCHEMA_MAP_HEAD.finditer(text):
        body = extract_bracket_map_body(text, m.end())
        keys += MAP_KEYS.findall(body)
    return sorted(set(keys))


def parse_step(nf_path: Path) -> dict:
    txt = nf_path.read_text()
    step_id = nf_path.stem

    info: dict = {
        "id": step_id,
        "rel_path": str(nf_path.relative_to(FW)),
        "containers": sorted(set(re.findall(r"container\s+['\"]([^'\"]+)['\"]", txt))),
        "subworkflows": [m.group(1) for m in WF_OPEN.finditer(txt) if m.group(1) != ""],
    }

    # take blocks per sub-workflow
    takes = {}
    for m in TAKE_BLOCK.finditer(txt):
        wf_name = m.group(1)
        raw = m.group(2)
        # collect identifier tokens, ignoring keywords main:/emit:/when:
        params: list[str] = []
        for line in raw.split("\n"):
            ln = line.strip()
            if not ln:
                continue
            if ln.startswith(("main", "emit", "when", "//")):
                break
            tok = ln.split("//", 1)[0].strip()
            if re.match(r"^[A-Za-z_]\w*$", tok):
                params.append(tok)
        takes[wf_name] = params
    info["take"] = takes

    # All sub-workflows declared and their emit blocks
    emits = []
    for m in EMIT_BLOCK.finditer(txt):
        body = m.group(1)
        for line in body.splitlines():
            ln = line.strip().split("//", 1)[0].strip()
            if not ln or ln.startswith("}") or ln.startswith("workflow"):
                continue
            name = ln.split("=", 1)[0].strip()
            if re.match(r"^[A-Za-z_]\w*$", name):
                emits.append(name)
    info["emits"] = sorted(set(emits))

    # Bottom workflow {} block (example invocation)
    bottom = list(WF_BOTTOM.finditer(txt))
    if bottom:
        example = bottom[-1].group(0).strip()
        info["example_invocation"] = example
        # input getter used in example
        for g in INPUT_GETTERS:
            if re.search(r"\b" + g + r"\b", example):
                info.setdefault("input_getters", []).append(g)

    # Conditions in when:
    info["when_clauses"] = [m.group(1).strip() for m in WHEN_BLOCK.finditer(txt)]

    # Hard-coded species/schema maps (bracket-balanced)
    info["supported_species_or_schemas"] = find_species_keys(txt)

    # Input file expectations (heuristic from getResult acc & default patterns)
    info["uses_assembly"] = bool(re.search(r"\bgetAssembly\b|2AS_import|2AS_mapping|2AS_denovo", txt))
    info["uses_fastq"]    = bool(re.search(r"\bgetReads\b|getRawReads|0SQ_rawreads|1PP_trimming|getTrimmedReads", txt))
    info["uses_vcf"]      = bool(re.search(r"\bgetVCFs\b|\\.vcf", txt))

    # Includes (dependencies on other steps)
    info["includes"] = sorted(set(re.findall(
        r"include\s*\{\s*([^}]+?)\s*\}\s*from\s*'([^']+)'", txt)) | set())  # type: ignore[list-item]
    # Cleanup: flatten the tuples into strings
    info["includes"] = [f"{a} from {b}" for a, b in re.findall(
        r"include\s*\{\s*([^}]+?)\s*\}\s*from\s*'([^']+)'", txt)]

    return info


def main() -> None:
    inv: dict = {"steps": {}, "multi": {}, "pipelines_examples": {}}
    for d, bucket in [("steps", "steps"), ("multi", "multi")]:
        for nf in sorted((FW / d).glob("*.nf")):
            try:
                inv[bucket][nf.stem] = parse_step(nf)
            except Exception as e:
                inv[bucket][nf.stem] = {"error": str(e)}
    OUT.write_text(json.dumps(inv, indent=2))
    print(f"Wrote {OUT}")
    print(f"  steps: {len(inv['steps'])}")
    print(f"  multi: {len(inv['multi'])}")


if __name__ == "__main__":
    main()
