#!/usr/bin/env python3
"""Deterministic structural validator for the RIGOR methodology repository."""
from __future__ import annotations
import re, sys
from pathlib import Path
REQUIRED=(
 "README.md","AGENTS.md","CLAUDE.md","LICENSE","CONTRIBUTING.md","moda.yaml","SPEC.md","CONSTITUTION.md","GETTING-STARTED.md","BEST-PRACTICES.md","DISCLAIMER.md","CHANGELOG.md","ROADMAP.md","UPGRADE.md","MIGRATIONS.md","conformance/moda.yaml",
 "decisions/0006-apache-2.0-and-dco-contributions.md","decisions/0007-portable-core-and-installable-skill.md","decisions/0008-hypothesis-driven-adaptive-exhaustion.md",
 "changes/2026-08-13-initial-rigor/proposal.md","changes/2026-08-13-initial-rigor/impact.yaml",
 "changes/2026-08-14-dossier-and-agent-architecture/proposal.md","changes/2026-08-14-dossier-and-agent-architecture/impact.yaml",
 "changes/2026-08-14-executable-research-artifacts/proposal.md","changes/2026-08-14-executable-research-artifacts/impact.yaml",
 "changes/2026-08-14-license-and-contributions/proposal.md","changes/2026-08-14-license-and-contributions/impact.yaml",
 "changes/2026-08-14-installable-rigor-skill/proposal.md","changes/2026-08-14-installable-rigor-skill/impact.yaml",
 "changes/2026-08-14-hypothesis-and-adaptive-exhaustion/proposal.md","changes/2026-08-14-hypothesis-and-adaptive-exhaustion/impact.yaml",
 "schemas/research-bundle.schema.json","templates/research-bundle.yaml","docs/executable-research-artifacts.md","docs/hypotheses-and-research-loops.md",
 "scripts/validate_artifacts.py","scripts/validate_evaluation_corpus.py","scripts/validate_skill.py",
 "skills/rigor/SKILL.md","skills/rigor/agents/openai.yaml","skills/rigor/manifest.yaml",
 "skills/rigor/references/activation.md","skills/rigor/references/orchestration.md","skills/rigor/references/artifacts.md","skills/rigor/references/hypotheses-and-loops.md","skills/rigor/references/host-capabilities.md",
 "skills/rigor/assets/research-bundle.json","skills/rigor/scripts/validate_bundle.py",
 "tests/fixtures/valid-research-bundle.json","tests/fixtures/invalid-unknown-citation.json","tests/fixtures/invalid-frontier-reference.json"
)
LINK=re.compile(r"(?<!!)\[[^]]*\]\(([^)]+)\)"); failures=[]
def require(c,m):
 if not c: failures.append(m)
def main():
 root=Path(sys.argv[1] if len(sys.argv)>1 else ".").resolve()
 for p in REQUIRED: require((root/p).is_file(),f"missing required file: {p}")
 moda=(root/"moda.yaml").read_text(encoding="utf-8")
 for t in ('compatibility: "^1.0.0"','kind: "methodology"','version: "0.2.0"','license: "Apache-2.0"','lifecycle: "embedded"','role: "installable-orchestration-skill"'): require(t in moda,f"moda.yaml missing {t}")
 license_text=(root/"LICENSE").read_text(encoding="utf-8")
 contributing=(root/"CONTRIBUTING.md").read_text(encoding="utf-8")
 require("Apache License" in license_text and "Version 2.0" in license_text,"LICENSE is not Apache-2.0 text")
 require("Developer Certificate of Origin 1.1" in contributing and "Signed-off-by:" in contributing,"CONTRIBUTING.md missing DCO 1.1 sign-off contract")
 for md in root.rglob("*.md"):
  for raw in LINK.findall(md.read_text(encoding="utf-8")):
   target=raw.split("#",1)[0].strip()
   if target and not target.startswith(("http://","https://","mailto:","#")): require(((root/target.lstrip("/")) if target.startswith("/") else (md.parent/target)).exists(),f"broken local link in {md.relative_to(root)}: {raw}")
 if failures:
  print("RIGOR repository validation: FAILED"); [print("- "+x) for x in failures]; return 1
 print("RIGOR repository validation: PASSED"); print(f"Checked {len(REQUIRED)} required files and local Markdown links."); return 0
if __name__=="__main__": raise SystemExit(main())
