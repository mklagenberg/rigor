#!/usr/bin/env python3
"""Deterministic expansion gate for the RIGOR decomposition graph.

Runs BEFORE a node is spawned, not after the bundle is written. A budget control
that only fires at the end is useless: the cost is already spent.

Returns one of three verdicts and the exact `plan.expansion_decisions` entry to
append. `scripts/validate_artifacts.py` refuses any 0.3.0+ bundle containing a
non-root node without a recorded `allow`, which is what makes calling this gate
binding rather than advisory.

    allow        the node fits the approved budget
    deny-record  the budget blocks it and no rigor predicate fires; record the
                 node as blocked-by-budget, carry it into dossier limitations,
                 and continue the investigation
    escalate     the budget blocks it but the node is load-bearing; stop and ask
                 the decision owner for a widened budget

Escalation is decided by a machine-evaluated predicate over the existing ledger,
never by the orchestrator's own judgement that a node feels important. A role
that wants to expand is not allowed to validate its own request.

usage: check_expansion.py BUNDLE.json PROPOSED_NODE.json
exit:  0 allow | 3 deny-record | 4 escalate | 1 error | 2 usage
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

BLOCKING_SUPPORT = {"contested", "insufficient"}
EXIT = {"allow": 0, "deny-record": 3, "escalate": 4}


def budget_violation(bundle: dict, node: dict) -> str | None:
    budget = bundle["brief"]["expansion_budget"]
    all_nodes = bundle["plan"]["workstreams"]
    by_id = {item["workstream_id"]: item for item in all_nodes}
    # A previously blocked node was never explored, so it does not hold budget hostage.
    nodes = [item for item in all_nodes if item.get("status") != "blocked-by-budget"]
    parent_id = node.get("parent_id")
    if parent_id not in by_id:
        return f"parent {parent_id} does not exist in the current plan"
    depth = by_id[parent_id]["depth"] + 1
    if depth > budget["max_depth"]:
        return f"depth {depth} exceeds max_depth {budget['max_depth']}"
    siblings = sum(1 for item in nodes if item.get("parent_id") == parent_id)
    if siblings + 1 > budget["max_children_per_node"]:
        return f"parent {parent_id} would hold {siblings + 1} explored children, above max_children_per_node {budget['max_children_per_node']}"
    if len(nodes) + 1 > budget["max_nodes"]:
        return f"plan would hold {len(nodes) + 1} explored nodes, above max_nodes {budget['max_nodes']}"
    return None


def p1_load_bearing_interpretation(bundle: dict, node: dict) -> tuple[bool, str]:
    """The node interprets evidence that the conclusion currently rests on and cannot settle."""
    if node.get("node_role") != "context":
        return False, "P1 requires a context node"
    targets = set(node.get("interprets_workstream_ids") or [])
    if not targets:
        return False, "P1 requires at least one interpreted workstream"
    cited = set(bundle["dossier"]["claim_ids"])
    for claim in bundle["claims"]:
        if claim["claim_id"] not in cited:
            continue
        if claim["support_status"] not in BLOCKING_SUPPORT:
            continue
        if targets & set(claim.get("workstream_ids") or []):
            return True, (
                f"claim {claim['claim_id']} is {claim['support_status']}, is cited by the conclusion, "
                f"and belongs to a workstream this node interprets"
            )
    return False, "no cited claim in the interpreted workstreams is contested or insufficient"


def p2_sole_discriminator(bundle: dict, node: dict) -> tuple[bool, str]:
    """The node is the only remaining route between competing open hypotheses."""
    proposed = set(node.get("linked_hypothesis_ids") or [])
    if len(proposed) < 2:
        return False, "P2 requires at least two linked hypotheses"
    hypotheses = {item["hypothesis_id"]: item for item in bundle["hypotheses"]}
    open_ids = {hid for hid in proposed if hypotheses.get(hid, {}).get("status") == "open"}
    if len(open_ids) < 2:
        return False, "P2 requires at least two open linked hypotheses"
    competing = any(
        other in set(hypotheses[hid].get("alternative_hypothesis_ids") or [])
        for hid in open_ids
        for other in open_ids
        if other != hid
    )
    if not competing:
        return False, "the open linked hypotheses are not registered alternatives of each other"
    for task in bundle["research_frontier"]:
        if task.get("status") != "ready":
            continue
        if task.get("discriminating_value") != "high":
            continue
        if len(open_ids & set(task.get("linked_hypothesis_ids") or [])) >= 2:
            return False, f"frontier task {task['task_id']} already discriminates the same hypotheses"
    return True, "no ready high-value frontier task discriminates these competing open hypotheses"


def decide(bundle: dict, node: dict) -> dict:
    iterations = bundle.get("iterations") or []
    iteration_id = iterations[-1]["iteration_id"] if iterations else "IT-001"
    decision_id = f"EX-{len(bundle['plan'].get('expansion_decisions') or []) + 1:03d}"
    base = {
        "decision_id": decision_id,
        "workstream_id": node.get("workstream_id", "?"),
        "iteration_id": iteration_id,
    }

    violation = budget_violation(bundle, node)
    if violation is None:
        return {**base, "verdict": "allow", "predicate": "within-budget", "predicate_result": True,
                "rationale": "Within the approved expansion budget."}

    p1, p1_reason = p1_load_bearing_interpretation(bundle, node)
    if p1:
        return {**base, "verdict": "escalate", "predicate": "P1-load-bearing-interpretation", "predicate_result": True,
                "rationale": f"Budget blocked ({violation}), but {p1_reason}."}
    p2, p2_reason = p2_sole_discriminator(bundle, node)
    if p2:
        return {**base, "verdict": "escalate", "predicate": "P2-sole-discriminator", "predicate_result": True,
                "rationale": f"Budget blocked ({violation}), but {p2_reason}."}
    return {**base, "verdict": "deny-record", "predicate": "none", "predicate_result": False,
            "rationale": f"Budget blocked ({violation}). Neither predicate fired: {p1_reason}; {p2_reason}."}


def main() -> int:
    if len(sys.argv) != 3:
        print(__doc__.strip().splitlines()[-2])
        return 2
    try:
        bundle = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        node = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
        decision = decide(bundle, node)
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as error:
        print(f"RIGOR expansion gate: ERROR\n- {error}")
        return 1
    print(json.dumps(decision, indent=2, ensure_ascii=False))
    if decision["verdict"] == "deny-record":
        print("\nRecord the node with status blocked-by-budget and name its ID in dossier limitations.", file=sys.stderr)
    if decision["verdict"] == "escalate":
        print("\nStop the investigation and request a widened budget from the decision owner.", file=sys.stderr)
    return EXIT[decision["verdict"]]


if __name__ == "__main__":
    raise SystemExit(main())
