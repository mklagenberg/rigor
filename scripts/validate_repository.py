#!/usr/bin/env python3
"""Deterministic structural validator for the RIGOR methodology repository."""
from __future__ import annotations

import re
import sys
from pathlib import Path

REQUIRED = (
    "README.md", "AGENTS.md", "CLAUDE.md", "moda.yaml", "SPEC.md",
    "CONSTITUTION.md", "GETTING-STARTED.md", "BEST-PRACTICES.md",
    "DISCLAIMER.md", "CHANGELOG.md", "ROADMAP.md", "UPGRADE.md",
    "MIGRATIONS.md", "conformance/moda.yaml",
    "changes/2026-08-13-initial-rigor/proposal.md",
    "changes/2026-08-13-initial-rigor/impact.yaml",
    "docs/activation-and-proportionality.md", "docs/evidence-model.md",
    "docs/research-process.md", "docs/source-discovery.md",
    "docs/agency-and-orchestration.md", "docs/evaluation-and-safety.md",
    "docs/validation-and-repair.md", "docs/change-management.md",
    "docs/decision-records.md", "docs/git-and-release-workflow.md",
    "docs/synchronization.md", "scripts/validate_repository.py",
)

LINK = re.compile(r"(?<!!)[[^]]*](([^)]+))")
failures: list[str] = []

def require(condition: bool, message: str) -> None:
    if not condition:
        failures.append(message)

def local_target(root: Path, source: Path, target: str) -> Path | None:
    target = target.split("#", 1)[0].strip()
    if not target or target.startswith(("http://", "https://", "mailto:", "#")):
        return None
    return (root / target.lstrip("/")) if target.startswith("/") else (source.parent / target)

def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    for relative in REQUIRED:
        require((root / relative).is_file(), f"missing required file: {relative}")

    moda = (root / "moda.yaml")
    if moda.is_file():
        text = moda.read_text(encoding="utf-8")
        for token in ('compatibility: "^1.0.0"', 'kind: "methodology"', 'version: "0.1.0"', 'claim_stage: "mapped"'):
            require(token in text, f"moda.yaml missing expected declaration: {token}")

    agents = root / "AGENTS.md"
    if agents.is_file():
        text = agents.read_text(encoding="utf-8")
        require("<!-- moda:disclosure:start -->" in text, "AGENTS.md is missing MODA disclosure start marker")
        require("<!-- moda:disclosure:end -->" in text, "AGENTS.md is missing MODA disclosure end marker")

    for markdown in root.rglob("*.md"):
        text = markdown.read_text(encoding="utf-8")
        for raw_target in LINK.findall(text):
            target = local_target(root, markdown, raw_target)
            if target is not None:
                require(target.exists(), f"broken local link in {markdown.relative_to(root)}: {raw_target}")

    if failures:
        print("RIGOR repository validation: FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("RIGOR repository validation: PASSED")
    print(f"Checked {len(REQUIRED)} required files and local Markdown links.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
