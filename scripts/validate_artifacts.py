#!/usr/bin/env python3
"""Validate RIGOR Research Bundle traceability without external dependencies."""
from __future__ import annotations
import json, sys
from pathlib import Path

TOP={"schema_version","brief","plan","sources","claims","handoffs","dossier"}
SRC={"source_id","author","title","source_type","venue","published_at","accessed_at","url","status","independence_group"}
CLM={"claim_id","claim_type","statement","citations","support_status"}
HOF={"handoff_id","role","work_performed","claim_ids","source_ids","gaps","recommended_next_action"}
DOS={"dossier_id","title","plan_id","claim_ids","conclusion","confidence_rationale","limitations","revalidation"}
STATUSES={"discovered","verified","validated","contested","insufficient","actionable"}
TYPES={"observation","source_claim","derived_fact","inference","judgment","open_question"}

def fail(m): raise ValueError(m)
def ids(rows,key,label):
 values=[x.get(key) for x in rows]
 if not values or any(not x for x in values): fail(f"{label} contains missing {key}")
 if len(values)!=len(set(values)): fail(f"{label} contains duplicate {key}")
 return set(values)
def validate(b):
 if TOP-set(b): fail("missing top-level fields")
 if b["schema_version"]!="0.1.0": fail("unsupported schema_version")
 brief=b["brief"]
 for key in ("question","outcome","scope","level","level_rationale","permissions"):
  if not brief.get(key) and key!="permissions": fail(f"brief missing {key}")
 if brief["level"] not in (3,4,5): fail("brief level must be 3, 4, or 5")
 plan=b["plan"]
 if not {"plan_id","workstreams","stop_conditions"}<=set(plan) or not plan["plan_id"]: fail("plan missing required fields")
 sids=ids(b["sources"],"source_id","sources")
 for s in b["sources"]:
  missing=SRC-set(s)
  if missing: fail(f"source {s.get('source_id','?')} missing {', '.join(sorted(missing))}")
  if s["status"] not in STATUSES: fail(f"source {s['source_id']} has invalid status")
  if not s["url"].startswith(("https://","http://","doi:","archive:")): fail(f"source {s['source_id']} has invalid URL or persistent identifier")
 cids=ids(b["claims"],"claim_id","claims")
 for c in b["claims"]:
  if CLM-set(c): fail(f"claim {c.get('claim_id','?')} missing required fields")
  if c["claim_type"] not in TYPES: fail(f"claim {c['claim_id']} has invalid claim_type")
  if not c["citations"] and c["support_status"]!="insufficient": fail(f"claim {c['claim_id']} needs citation or insufficient status")
  for sid in c["citations"]:
   if sid not in sids: fail(f"claim {c['claim_id']} cites unknown source {sid}")
 ids(b["handoffs"],"handoff_id","handoffs")
 for h in b["handoffs"]:
  if HOF-set(h): fail(f"handoff {h.get('handoff_id','?')} missing required fields")
  if any(i not in cids for i in h["claim_ids"]): fail(f"handoff {h['handoff_id']} references unknown claim")
  if any(i not in sids for i in h["source_ids"]): fail(f"handoff {h['handoff_id']} references unknown source")
 d=b["dossier"]
 if DOS-set(d): fail("dossier missing required fields")
 if d["plan_id"]!=plan["plan_id"]: fail("dossier plan_id does not match plan")
 if any(i not in cids for i in d["claim_ids"]): fail("dossier references unknown claim")
 if not isinstance(d["revalidation"],dict) or "triggers" not in d["revalidation"] or "owner" not in d["revalidation"]: fail("dossier revalidation needs triggers and owner")
def main():
 if len(sys.argv)!=2: print("usage: validate_artifacts.py BUNDLE.json"); return 2
 try: validate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
 except (OSError,json.JSONDecodeError,ValueError) as e: print("RIGOR artifact validation: FAILED\n- "+str(e)); return 1
 print("RIGOR artifact validation: PASSED"); return 0
if __name__=="__main__": raise SystemExit(main())
