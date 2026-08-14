#!/usr/bin/env python3
"""Deterministic structural validator for the RIGOR methodology repository."""
from __future__ import annotations
import re, sys
from pathlib import Path
REQUIRED=("README.md","AGENTS.md","CLAUDE.md","moda.yaml","SPEC.md","CONSTITUTION.md","GETTING-STARTED.md","BEST-PRACTICES.md","DISCLAIMER.md","CHANGELOG.md","ROADMAP.md","UPGRADE.md","MIGRATIONS.md","conformance/moda.yaml","changes/2026-08-13-initial-rigor/proposal.md","changes/2026-08-13-initial-rigor/impact.yaml","changes/2026-08-14-dossier-and-agent-architecture/proposal.md","changes/2026-08-14-dossier-and-agent-architecture/impact.yaml","changes/2026-08-14-executable-research-artifacts/proposal.md","changes/2026-08-14-executable-research-artifacts/impact.yaml","schemas/research-bundle.schema.json","templates/research-bundle.yaml","docs/executable-research-artifacts.md","scripts/validate_artifacts.py","tests/fixtures/valid-research-bundle.json","tests/fixtures/invalid-unknown-citation.json")
LINK=re.compile(r"(?<!!)\[[^]]*\]\(([^)]+)\)"); failures=[]
def require(c,m):
 if not c: failures.append(m)
def main():
 root=Path(sys.argv[1] if len(sys.argv)>1 else ".").resolve()
 for p in REQUIRED: require((root/p).is_file(),f"missing required file: {p}")
 moda=(root/"moda.yaml").read_text(encoding="utf-8")
 for t in ('compatibility: "^1.0.0"','kind: "methodology"','version: "0.1.0"','lifecycle: "embedded"'): require(t in moda,f"moda.yaml missing {t}")
 for md in root.rglob("*.md"):
  for raw in LINK.findall(md.read_text(encoding="utf-8")):
   target=raw.split("#",1)[0].strip()
   if target and not target.startswith(("http://","https://","mailto:","#")): require(((root/target.lstrip("/")) if target.startswith("/") else (md.parent/target)).exists(),f"broken local link in {md.relative_to(root)}: {raw}")
 if failures:
  print("RIGOR repository validation: FAILED"); [print("- "+x) for x in failures]; return 1
 print("RIGOR repository validation: PASSED"); print(f"Checked {len(REQUIRED)} required files and local Markdown links."); return 0
if __name__=="__main__": raise SystemExit(main())
