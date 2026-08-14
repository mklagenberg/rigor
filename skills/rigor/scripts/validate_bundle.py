#!/usr/bin/env python3
"""Validate a RIGOR Research Bundle without external dependencies."""
from __future__ import annotations

import json
import sys
from pathlib import Path

TOP = {"schema_version", "brief", "plan", "sources", "claims", "handoffs", "dossier"}
SOURCE = {"source_id", "author", "title", "source_type", "venue", "published_at", "accessed_at", "url", "status", "independence_group"}
CLAIM = {"claim_id", "claim_type", "statement", "citations", "support_status"}
HANDOFF = {"handoff_id", "role", "work_performed", "claim_ids", "source_ids", "gaps", "recommended_next_action"}
DOSSIER = {"dossier_id", "title", "plan_id", "claim_ids", "conclusion", "confidence_rationale", "limitations", "revalidation"}
STATUSES = {"discovered", "verified", "validated", "contested", "insufficient", "actionable"}
CLAIM_TYPES = {"observation", "source_claim", "derived_fact", "inference", "judgment", "open_question"}


def fail(message: str) -> None:
    raise ValueError(message)


def collect_ids(rows: list[dict], key: str, label: str) -> set[str]:
    values = [row.get(key) for row in rows]
    if not values:
        fail(f"{label} must not be empty")
    if any(not value for value in values):
        fail(f"{label} contains missing {key}")
    if len(values) != len(set(values)):
        fail(f"{label} contains duplicate {key}")
    return set(values)


def validate(bundle: dict) -> None:
    missing = TOP - set(bundle)
    if missing:
        fail("missing top-level fields: " + ", ".join(sorted(missing)))
    if bundle["schema_version"] != "0.1.0":
        fail("unsupported schema_version")

    brief = bundle["brief"]
    for key in ("question", "outcome", "scope", "level", "level_rationale", "permissions"):
        if key not in brief or (key != "permissions" and not brief[key]):
            fail(f"brief missing {key}")
    if brief["level"] not in (3, 4, 5):
        fail("brief level must be 3, 4, or 5")

    plan = bundle["plan"]
    if not {"plan_id", "workstreams", "stop_conditions"} <= set(plan) or not plan["plan_id"]:
        fail("plan missing required fields")

    source_ids = collect_ids(bundle["sources"], "source_id", "sources")
    for source in bundle["sources"]:
        missing = SOURCE - set(source)
        if missing:
            fail(f"source {source.get('source_id', '?')} missing {', '.join(sorted(missing))}")
        if source["status"] not in STATUSES:
            fail(f"source {source['source_id']} has invalid status")
        if not source["url"].startswith(("https://", "http://", "doi:", "archive:")):
            fail(f"source {source['source_id']} has invalid URL or persistent identifier")

    claim_ids = collect_ids(bundle["claims"], "claim_id", "claims")
    for claim in bundle["claims"]:
        missing = CLAIM - set(claim)
        if missing:
            fail(f"claim {claim.get('claim_id', '?')} missing {', '.join(sorted(missing))}")
        if claim["claim_type"] not in CLAIM_TYPES:
            fail(f"claim {claim['claim_id']} has invalid claim_type")
        if not claim["citations"] and claim["support_status"] != "insufficient":
            fail(f"claim {claim['claim_id']} needs citations or insufficient status")
        for source_id in claim["citations"]:
            if source_id not in source_ids:
                fail(f"claim {claim['claim_id']} cites unknown source {source_id}")

    collect_ids(bundle["handoffs"], "handoff_id", "handoffs")
    for handoff in bundle["handoffs"]:
        missing = HANDOFF - set(handoff)
        if missing:
            fail(f"handoff {handoff.get('handoff_id', '?')} missing {', '.join(sorted(missing))}")
        if any(claim_id not in claim_ids for claim_id in handoff["claim_ids"]):
            fail(f"handoff {handoff['handoff_id']} references unknown claim")
        if any(source_id not in source_ids for source_id in handoff["source_ids"]):
            fail(f"handoff {handoff['handoff_id']} references unknown source")

    dossier = bundle["dossier"]
    missing = DOSSIER - set(dossier)
    if missing:
        fail("dossier missing required fields: " + ", ".join(sorted(missing)))
    if dossier["plan_id"] != plan["plan_id"]:
        fail("dossier plan_id does not match plan")
    if any(claim_id not in claim_ids for claim_id in dossier["claim_ids"]):
        fail("dossier references unknown claim")
    revalidation = dossier["revalidation"]
    if not isinstance(revalidation, dict) or not {"triggers", "owner"} <= set(revalidation):
        fail("dossier revalidation needs triggers and owner")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_bundle.py BUNDLE.json")
        return 2
    try:
        validate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print("RIGOR bundle validation: FAILED\n- " + str(exc))
        return 1
    print("RIGOR bundle validation: PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

