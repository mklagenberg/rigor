#!/usr/bin/env python3
"""Validate RIGOR Research Bundle traceability without external dependencies."""
from __future__ import annotations

import json
import sys
from pathlib import Path

TOP = {"schema_version", "brief", "plan", "sources", "claims", "hypotheses", "research_frontier", "iterations", "handoffs", "dossier"}
SOURCE = {"source_id", "author", "title", "source_type", "venue", "published_at", "accessed_at", "url", "status", "independence_group"}
CLAIM = {"claim_id", "claim_type", "statement", "citations", "support_status"}
HYPOTHESIS = {"hypothesis_id", "statement", "hypothesis_type", "status", "alternative_hypothesis_ids", "expected_traces", "disconfirming_evidence", "supporting_claim_ids", "conflicting_claim_ids", "confidence_rationale"}
FRONTIER = {"task_id", "linked_hypothesis_ids", "question", "evidence_target", "discriminating_value", "decision_impact", "priority", "status", "next_action", "iteration_created", "reason"}
ITERATION = {"iteration_id", "objective", "task_ids", "new_source_ids", "changed_hypothesis_ids", "closed_task_ids", "outcome", "frontier_decision"}
HANDOFF = {"handoff_id", "role", "work_performed", "claim_ids", "source_ids", "gaps", "recommended_next_action"}
DOSSIER = {"dossier_id", "title", "plan_id", "claim_ids", "conclusion", "confidence_rationale", "limitations", "revalidation"}
SOURCE_STATUSES = {"discovered", "verified", "validated", "contested", "insufficient", "actionable"}
CLAIM_TYPES = {"observation", "source_claim", "derived_fact", "inference", "judgment", "open_question"}
HYPOTHESIS_TYPES = {"retrospective", "prospective", "causal", "counterfactual"}
HYPOTHESIS_STATUSES = {"open", "strengthened", "weakened", "supported", "contested", "rejected", "blocked"}
FRONTIER_STATUSES = {"ready", "running", "blocked", "deferred", "closed"}
LOOP_STATUSES = {"open", "exhausted-within-scope", "blocked", "paused-by-limit", "ready-for-revalidation", "escalated"}


def fail(message: str) -> None:
    raise ValueError(message)


def ids(rows: list[dict], key: str, label: str, allow_empty: bool = False) -> set[str]:
    values = [row.get(key) for row in rows]
    if not allow_empty and not values:
        fail(f"{label} contains no {key}")
    if any(not value for value in values):
        fail(f"{label} contains missing {key}")
    if len(values) != len(set(values)):
        fail(f"{label} contains duplicate {key}")
    return set(values)


def require_fields(row: dict, required: set[str], label: str) -> None:
    missing = required - set(row)
    if missing:
        fail(f"{label} missing {', '.join(sorted(missing))}")


def validate(bundle: dict) -> None:
    missing = TOP - set(bundle)
    if missing:
        fail("missing top-level fields: " + ", ".join(sorted(missing)))
    if bundle["schema_version"] != "0.2.0":
        fail("unsupported schema_version")

    brief = bundle["brief"]
    for key in ("question", "outcome", "scope", "level", "level_rationale", "permissions"):
        if key not in brief or (key != "permissions" and not brief[key]):
            fail(f"brief missing {key}")
    if brief["level"] not in (3, 4, 5):
        fail("brief level must be 3, 4, or 5")

    plan = bundle["plan"]
    if not {"plan_id", "workstreams", "stop_conditions", "research_loop"} <= set(plan) or not plan["plan_id"]:
        fail("plan missing required fields")
    loop = plan["research_loop"]
    if not {"max_iterations", "current_iteration", "status", "stop_conditions", "reapproval_triggers"} <= set(loop):
        fail("plan research_loop missing required fields")
    if not isinstance(loop["max_iterations"], int) or loop["max_iterations"] < 1:
        fail("plan research_loop max_iterations must be a positive integer")
    if not isinstance(loop["current_iteration"], int) or not 1 <= loop["current_iteration"] <= loop["max_iterations"]:
        fail("plan research_loop current_iteration is outside configured limit")
    if loop["status"] not in LOOP_STATUSES:
        fail("plan research_loop has invalid status")

    source_ids = ids(bundle["sources"], "source_id", "sources")
    for source in bundle["sources"]:
        require_fields(source, SOURCE, f"source {source.get('source_id', '?')}")
        if source["status"] not in SOURCE_STATUSES:
            fail(f"source {source['source_id']} has invalid status")
        if not source["url"].startswith(("https://", "http://", "doi:", "archive:")):
            fail(f"source {source['source_id']} has invalid URL or persistent identifier")

    claim_ids = ids(bundle["claims"], "claim_id", "claims")
    for claim in bundle["claims"]:
        require_fields(claim, CLAIM, f"claim {claim.get('claim_id', '?')}")
        if claim["claim_type"] not in CLAIM_TYPES:
            fail(f"claim {claim['claim_id']} has invalid claim_type")
        if not claim["citations"] and claim["support_status"] != "insufficient":
            fail(f"claim {claim['claim_id']} needs citation or insufficient status")
        if any(source_id not in source_ids for source_id in claim["citations"]):
            fail(f"claim {claim['claim_id']} cites unknown source")

    hypothesis_ids = ids(bundle["hypotheses"], "hypothesis_id", "hypotheses", allow_empty=True)
    for hypothesis in bundle["hypotheses"]:
        require_fields(hypothesis, HYPOTHESIS, f"hypothesis {hypothesis.get('hypothesis_id', '?')}")
        if hypothesis["hypothesis_type"] not in HYPOTHESIS_TYPES or hypothesis["status"] not in HYPOTHESIS_STATUSES:
            fail(f"hypothesis {hypothesis['hypothesis_id']} has invalid type or status")
        for key in ("alternative_hypothesis_ids",):
            if any(item not in hypothesis_ids for item in hypothesis[key]):
                fail(f"hypothesis {hypothesis['hypothesis_id']} references unknown alternative")
        for key in ("supporting_claim_ids", "conflicting_claim_ids"):
            if any(item not in claim_ids for item in hypothesis[key]):
                fail(f"hypothesis {hypothesis['hypothesis_id']} references unknown claim")

    task_ids = ids(bundle["research_frontier"], "task_id", "research_frontier", allow_empty=True)
    for task in bundle["research_frontier"]:
        require_fields(task, FRONTIER, f"frontier task {task.get('task_id', '?')}")
        if task["status"] not in FRONTIER_STATUSES or task["priority"] not in {"P0", "P1", "P2", "P3"}:
            fail(f"frontier task {task['task_id']} has invalid status or priority")
        if task["discriminating_value"] not in {"high", "medium", "low"} or task["decision_impact"] not in {"high", "medium", "low"}:
            fail(f"frontier task {task['task_id']} has invalid value or impact")
        if any(item not in hypothesis_ids for item in task["linked_hypothesis_ids"]):
            fail(f"frontier task {task['task_id']} references unknown hypothesis")

    iteration_ids = ids(bundle["iterations"], "iteration_id", "iterations")
    for iteration in bundle["iterations"]:
        require_fields(iteration, ITERATION, f"iteration {iteration.get('iteration_id', '?')}")
        if any(item not in task_ids for item in iteration["task_ids"] + iteration["closed_task_ids"]):
            fail(f"iteration {iteration['iteration_id']} references unknown frontier task")
        if any(item not in source_ids for item in iteration["new_source_ids"]):
            fail(f"iteration {iteration['iteration_id']} references unknown source")
        if any(item not in hypothesis_ids for item in iteration["changed_hypothesis_ids"]):
            fail(f"iteration {iteration['iteration_id']} references unknown hypothesis")
    if len(iteration_ids) != loop["current_iteration"]:
        fail("iteration count does not match plan research_loop current_iteration")
    if loop["status"] == "exhausted-within-scope" and any(task["status"] == "ready" for task in bundle["research_frontier"]):
        fail("exhausted frontier retains ready task")

    ids(bundle["handoffs"], "handoff_id", "handoffs")
    for handoff in bundle["handoffs"]:
        require_fields(handoff, HANDOFF, f"handoff {handoff.get('handoff_id', '?')}")
        if any(item not in claim_ids for item in handoff["claim_ids"]) or any(item not in source_ids for item in handoff["source_ids"]):
            fail(f"handoff {handoff['handoff_id']} references unknown source or claim")

    dossier = bundle["dossier"]
    require_fields(dossier, DOSSIER, "dossier")
    if dossier["plan_id"] != plan["plan_id"] or any(item not in claim_ids for item in dossier["claim_ids"]):
        fail("dossier references an unknown plan or claim")
    if not isinstance(dossier["revalidation"], dict) or not {"triggers", "owner"} <= set(dossier["revalidation"]):
        fail("dossier revalidation needs triggers and owner")


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_artifacts.py BUNDLE.json")
        return 2
    try:
        validate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print("RIGOR artifact validation: FAILED\n- " + str(error))
        return 1
    print("RIGOR artifact validation: PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

