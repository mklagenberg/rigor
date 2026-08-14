#!/usr/bin/env python3
"""Validate RIGOR Research Bundle structural traceability without external dependencies."""
from __future__ import annotations
import json, sys
from pathlib import Path

REQUIRED_TOP = {"schema_version", "brief", "plan", "sources", "claims", "handoffs", "dossier"}
SOURCE_REQUIRED = {"source_id", "author", "title", "source_type", "venue", "published_at", "accessed_at", "url", "status", "independence_group"}
CLAIM_REQUIRED = {"claim_id", "claim_type", "statement", "citations", "support_status"}
HANDOFF_REQUIRED = {"handoff_id", "role", "work_performed", "claim_ids", "source_ids", "gaps", "recommended_next_action"}
DOSSIER_REQUIRED = {"dossier_id", "title", "plan_id", "claim_ids", "conclusion", "confidence_rationale", "limitations", "revalidation"}

def fail(message: str) -> None: raise ValueError(message)
def ids(rows, key, label):
    values=[row.get(key) for row in rows]
    if any(not value for value in values): fail(f"{label} contains missing {key}")
    if len(values)!=len(set(values)): fail(f"{label} contains duplicate {key}")
    return set(values)

def validate(bundle):
    missing=REQUIRED_TOP-set(bundle)
    if missing: fail("missing top-level fields: "+", ".join(sorted(missing)))
    if bundle["schema_version"]!="0.1.0": fail("unsupported schema_version")
    brief=bundle["brief"]
    for field in ("question","outcome","scope","level","level_rationale","permissions"):
        if field not in brief: fail(f"brief missing {field}")
    if brief["level"] not in (3,4,5): fail("brief level must be 3, 4, or 5")
    plan=bundle["plan"]
    if not {"plan_id","workstreams","stop_conditions"}<=set(plan): fail("plan missing required fields")
    source_ids=ids(bundle["sources"],"source_id","sources")
    for source in bundle["sources"]:
        if SOURCE_REQUIRED-set(source): fail(f"source {source.get('source_id','?')} missing required fields")
    claim_ids=ids(bundle["claims"],"claim_id","claims")
    for claim in bundle["claims"]:
        if CLAIM_REQUIRED-set(claim): fail(f"claim {claim.get('claim_id','?')} missing required fields")
        for citation in claim["citations"]:
            if citation not in source_ids: fail(f"claim {claim['claim_id']} cites unknown source {citation}")
    ids(bundle["handoffs"],"handoff_id","handoffs")
    for handoff in bundle["handoffs"]:
        if HANDOFF_REQUIRED-set(handoff): fail(f"handoff {handoff.get('handoff_id','?')} missing required fields")
        for claim in handoff["claim_ids"]:
            if claim not in claim_ids: fail(f"handoff {handoff['handoff_id']} references unknown claim {claim}")
        for source in handoff["source_ids"]:
            if source not in source_ids: fail(f"handoff {handoff['handoff_id']} references unknown source {source}")
    dossier=bundle["dossier"]
    if DOSSIER_REQUIRED-set(dossier): fail("dossier missing required fields")
    if dossier["plan_id"] != plan["plan_id"]: fail("dossier plan_id does not match plan")
    for claim in dossier["claim_ids"]:
        if claim not in claim_ids: fail(f"dossier references unknown claim {claim}")

def main():
    if len(sys.argv)!=2: print("usage: validate_artifacts.py BUNDLE.json"); return 2
    try:
        bundle=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")); validate(bundle)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print("RIGOR artifact validation: FAILED\n- "+str(exc)); return 1
    print("RIGOR artifact validation: PASSED"); return 0
if __name__=="__main__": raise SystemExit(main())
