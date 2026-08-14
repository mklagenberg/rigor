#!/usr/bin/env python3
"""Deterministically validate the installable RIGOR skill package."""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

REQUIRED = (
    "SKILL.md",
    "agents/openai.yaml",
    "manifest.yaml",
    "references/activation.md",
    "references/orchestration.md",
    "references/artifacts.md",
    "references/host-capabilities.md",
    "assets/research-bundle.json",
    "scripts/validate_bundle.py",
)


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else "skills/rigor").resolve()
    failures: list[str] = []
    for relative in REQUIRED:
        if not (root / relative).is_file():
            failures.append(f"missing required skill file: {relative}")

    if not failures:
        skill = (root / "SKILL.md").read_text(encoding="utf-8")
        frontmatter = re.match(r"^---\n(.*?)\n---\n", skill, flags=re.DOTALL)
        if not frontmatter:
            failures.append("SKILL.md has no YAML frontmatter")
        else:
            keys = [line.split(":", 1)[0].strip() for line in frontmatter.group(1).splitlines() if ":" in line]
            if keys != ["name", "description"]:
                failures.append("SKILL.md frontmatter must contain only name and description")
        for token in ("name: rigor", "Level 0–2", "Research Bundle", "dense dossier", "Never instantiate MODA"):
            if token not in skill:
                failures.append(f"SKILL.md missing contract token: {token}")
        if "TODO" in skill:
            failures.append("SKILL.md contains TODO placeholder")

        openai = (root / "agents/openai.yaml").read_text(encoding="utf-8")
        if 'display_name: "RIGOR"' not in openai or "Use $rigor" not in openai:
            failures.append("agents/openai.yaml lacks RIGOR invocation metadata")

        manifest = (root / "manifest.yaml").read_text(encoding="utf-8")
        for token in ('version: "0.1.0"', 'source_path: "skills/rigor"', "silent_update: false"):
            if token not in manifest:
                failures.append(f"manifest.yaml missing {token}")

    if failures:
        print("RIGOR skill validation: FAILED")
        for failure in failures:
            print("- " + failure)
        return 1

    validator = root / "scripts/validate_bundle.py"
    fixture = root.parents[1] / "tests/fixtures/valid-research-bundle.json"
    result = subprocess.run([sys.executable, str(validator), str(fixture)], check=False, capture_output=True, text=True)
    if result.returncode:
        print("RIGOR skill validation: FAILED")
        print("- portable validator rejected the valid fixture")
        print(result.stdout + result.stderr)
        return 1

    print("RIGOR skill validation: PASSED")
    print(f"Checked {len(REQUIRED)} package files and the portable bundle validator.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
