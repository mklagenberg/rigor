#!/usr/bin/env python3
"""Validate RIGOR Research Bundle traceability without external dependencies.

Version-aware. A bundle is checked against the contract it declares:

- 0.2.0: the original traceability contract.
- 0.3.0: adds the typed decomposition graph, node backlinks, the expansion
  budget, and recorded expansion verdicts.
- 0.4.0: adds claim validity classes, derived conclusion validity, the process
  attestation, and the acquisition/revalidation lifecycle.

Legacy bundles remain valid against the version they declare. This validator
proves that the declared decomposition was covered; it cannot prove that the
decomposition itself was complete. A missing node is invisible here and remains
the challenger's responsibility.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

SUPPORTED_VERSIONS = ("0.2.0", "0.3.0", "0.4.0")

TOP = {"schema_version", "brief", "plan", "sources", "claims", "hypotheses", "research_frontier", "iterations", "handoffs", "dossier"}
TOP_040 = {"bundle_version", "attestation", "revalidations"}
SOURCE = {"source_id", "author", "title", "source_type", "venue", "published_at", "accessed_at", "url", "status", "independence_group"}
CLAIM = {"claim_id", "claim_type", "statement", "citations", "support_status"}
HYPOTHESIS = {"hypothesis_id", "statement", "hypothesis_type", "status", "alternative_hypothesis_ids", "expected_traces", "disconfirming_evidence", "supporting_claim_ids", "conflicting_claim_ids", "confidence_rationale"}
FRONTIER = {"task_id", "linked_hypothesis_ids", "question", "evidence_target", "discriminating_value", "decision_impact", "priority", "status", "next_action", "iteration_created", "reason"}
ITERATION = {"iteration_id", "objective", "task_ids", "new_source_ids", "changed_hypothesis_ids", "closed_task_ids", "outcome", "frontier_decision"}
HANDOFF = {"handoff_id", "role", "work_performed", "claim_ids", "source_ids", "gaps", "recommended_next_action"}
DOSSIER = {"dossier_id", "title", "plan_id", "claim_ids", "conclusion", "confidence_rationale", "limitations", "revalidation"}
WORKSTREAM = {"workstream_id", "question", "evidence_target", "role", "stop_condition", "node_role", "relation", "parent_id", "depth", "interprets_workstream_ids", "evidence_regimes", "temporal_scope", "jurisdiction", "decision_impact", "status"}
EXPANSION = {"decision_id", "workstream_id", "verdict", "predicate", "predicate_result", "iteration_id", "rationale"}
BUDGET = {"max_depth", "max_children_per_node", "max_nodes", "set_by"}
ATTESTATION = {"methodology", "methodology_version", "schema_version", "bundle_id", "level", "validator_status", "procedural_independence", "loop_status", "claim_profile", "validity_class", "latest_revalidation_id", "resolves_to"}
REVALIDATION = {"revalidation_id", "triggered_by", "date", "claims_rechecked", "claims_changed", "verdict", "produces_bundle_version"}

SOURCE_STATUSES = {"discovered", "verified", "validated", "contested", "insufficient", "actionable"}
CLAIM_TYPES = {"observation", "source_claim", "derived_fact", "inference", "judgment", "open_question"}
HYPOTHESIS_TYPES = {"retrospective", "prospective", "causal", "counterfactual"}
HYPOTHESIS_STATUSES = {"open", "strengthened", "weakened", "supported", "contested", "rejected", "blocked"}
FRONTIER_STATUSES = {"ready", "running", "blocked", "deferred", "closed"}
LOOP_STATUSES = {"open", "exhausted-within-scope", "blocked", "paused-by-limit", "ready-for-revalidation", "escalated"}
NODE_ROLES = {"primary", "context"}
RELATIONS = {"root", "decomposes", "interprets", "enables", "competes"}
NODE_STATUSES = {"unexplored", "open", "closed-productive", "closed-no-gain", "blocked", "blocked-by-budget"}
NODE_OPEN_STATUSES = {"unexplored", "open"}
VERDICTS = {"allow", "deny-record", "escalate"}
PREDICATES = {"within-budget", "P1-load-bearing-interpretation", "P2-sole-discriminator", "none"}
BUDGET_SETTERS = {"default", "user", "reapproved"}
REVALIDATION_VERDICTS = {"confirmed", "amended", "superseded", "withdrawn"}
INDEPENDENCE = {"full", "limited", "pending"}
VALIDATOR_STATUSES = {"passed", "failed", "not-run"}

# Ordered by how long a wrong claim can survive unnoticed, weakest last.
VALIDITY_ORDER = ("static", "institutional", "consensus", "measured", "volatile")
VALIDITY_CLASSES = set(VALIDITY_ORDER)
DEFAULT_MAX_DEPTH = {3: 1, 4: 2, 5: 3}


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


def validate_decomposition(bundle: dict) -> None:
    """0.3.0+ — typed decomposition graph, budget, backlinks, expansion verdicts."""
    brief, plan = bundle["brief"], bundle["plan"]
    if "expansion_budget" not in brief:
        fail("brief missing expansion_budget")
    budget = brief["expansion_budget"]
    require_fields(budget, BUDGET, "brief expansion_budget")
    if budget["set_by"] not in BUDGET_SETTERS:
        fail("brief expansion_budget set_by must be default, user, or reapproved")
    for key in ("max_depth", "max_children_per_node", "max_nodes"):
        if not isinstance(budget[key], int) or budget[key] < 0:
            fail(f"brief expansion_budget {key} must be a non-negative integer")
    if budget["set_by"] == "default" and budget["max_depth"] != DEFAULT_MAX_DEPTH[brief["level"]]:
        fail(f"default expansion_budget max_depth for level {brief['level']} must be {DEFAULT_MAX_DEPTH[brief['level']]}")

    if "expansion_decisions" not in plan:
        fail("plan missing expansion_decisions")
    nodes = plan["workstreams"]
    if not nodes:
        fail("plan workstreams contains no node")
    node_ids = ids(nodes, "workstream_id", "plan workstreams")
    by_id = {node["workstream_id"]: node for node in nodes}

    roots, children = [], {}
    for node in nodes:
        label = f"workstream {node.get('workstream_id', '?')}"
        require_fields(node, WORKSTREAM, label)
        if node["node_role"] not in NODE_ROLES:
            fail(f"{label} has invalid node_role")
        if node["relation"] not in RELATIONS:
            fail(f"{label} has invalid relation")
        if node["status"] not in NODE_STATUSES:
            fail(f"{label} has invalid status")
        if node["decision_impact"] not in {"high", "medium", "low"}:
            fail(f"{label} has invalid decision_impact")
        if not isinstance(node["depth"], int) or node["depth"] < 0:
            fail(f"{label} depth must be a non-negative integer")
        if node["relation"] == "root":
            roots.append(node)
            if node["parent_id"] is not None or node["depth"] != 0:
                fail(f"{label} is the root and must have null parent_id and depth 0")
        else:
            if not node["parent_id"]:
                fail(f"{label} has no parent_id and is not the root")
            if node["parent_id"] not in node_ids:
                fail(f"{label} references unknown parent {node['parent_id']}")
            children.setdefault(node["parent_id"], []).append(node["workstream_id"])
        if node["node_role"] == "context":
            if not node["interprets_workstream_ids"]:
                fail(f"{label} is a context node and must declare interprets_workstream_ids")
            if any(item not in node_ids for item in node["interprets_workstream_ids"]):
                fail(f"{label} interprets an unknown workstream")
        elif node["interprets_workstream_ids"]:
            fail(f"{label} is a primary node and must not declare interprets_workstream_ids")
        if node["relation"] == "interprets" and node["node_role"] != "context":
            fail(f"{label} uses the interprets relation but is not a context node")

    if len(roots) != 1:
        fail(f"plan workstreams must contain exactly one root node, found {len(roots)}")

    # A node blocked by the budget is preserved as a finding but was never explored,
    # so it consumes no budget. Erasing it would hide the boundary of the investigation.
    explored = [node for node in nodes if node["status"] != "blocked-by-budget"]
    explored_ids = {node["workstream_id"] for node in explored}
    for node in nodes:
        if node["relation"] != "root" and node["depth"] != by_id[node["parent_id"]]["depth"] + 1:
            fail(f"workstream {node['workstream_id']} depth is not parent depth plus one")
        if node["workstream_id"] in explored_ids and node["depth"] > budget["max_depth"]:
            fail(f"workstream {node['workstream_id']} exceeds expansion_budget max_depth")
    for parent_id, kids in children.items():
        if len([kid for kid in kids if kid in explored_ids]) > budget["max_children_per_node"]:
            fail(f"workstream {parent_id} exceeds expansion_budget max_children_per_node")
    if len(explored) > budget["max_nodes"]:
        fail("plan workstreams exceeds expansion_budget max_nodes")

    reachable, frontier = set(), [roots[0]["workstream_id"]]
    while frontier:
        current = frontier.pop()
        if current in reachable:
            continue
        reachable.add(current)
        frontier.extend(children.get(current, []))
    if reachable != node_ids:
        fail("plan workstreams contains a node unreachable from the root")

    decisions = plan["expansion_decisions"]
    ids(decisions, "decision_id", "plan expansion_decisions", allow_empty=True)
    allowed, denied, escalated = set(), set(), False
    for decision in decisions:
        label = f"expansion decision {decision.get('decision_id', '?')}"
        require_fields(decision, EXPANSION, label)
        if decision["verdict"] not in VERDICTS:
            fail(f"{label} has invalid verdict")
        if decision["predicate"] not in PREDICATES:
            fail(f"{label} has invalid predicate")
        if not isinstance(decision["predicate_result"], bool):
            fail(f"{label} predicate_result must be a boolean")
        if decision["workstream_id"] not in node_ids:
            fail(f"{label} references an unknown workstream")
        if decision["verdict"] == "allow":
            if decision["workstream_id"] in allowed:
                fail(f"{label} duplicates an allow verdict for {decision['workstream_id']}")
            allowed.add(decision["workstream_id"])
        if decision["verdict"] == "deny-record":
            denied.add(decision["workstream_id"])
        if decision["verdict"] == "escalate":
            escalated = True
    for node in nodes:
        if node["relation"] == "root":
            continue
        if node["status"] == "blocked-by-budget":
            if node["workstream_id"] not in denied:
                fail(f"workstream {node['workstream_id']} is blocked-by-budget without a recorded deny-record verdict")
            if node["workstream_id"] in allowed:
                fail(f"workstream {node['workstream_id']} is blocked-by-budget but also carries an allow verdict")
        elif node["workstream_id"] not in allowed:
            fail(f"workstream {node['workstream_id']} has no recorded allow verdict in plan expansion_decisions")

    loop_status = plan["research_loop"]["status"]
    if escalated and loop_status not in {"escalated", "paused-by-limit", "blocked"}:
        fail("an escalate verdict was recorded but the research loop did not stop for direction")
    if loop_status == "exhausted-within-scope":
        stalled = [node["workstream_id"] for node in nodes if node["status"] in NODE_OPEN_STATUSES]
        if stalled:
            fail("exhausted decomposition retains an unexplored or open node: " + ", ".join(sorted(stalled)))

    limitations = " ".join(str(item) for item in bundle["dossier"]["limitations"])
    for node in nodes:
        if node["status"] == "blocked-by-budget" and node["workstream_id"] not in limitations:
            fail(f"workstream {node['workstream_id']} is blocked-by-budget but is not recorded in dossier limitations")

    for claim in bundle["claims"]:
        linked = claim.get("workstream_ids")
        if not linked:
            fail(f"claim {claim['claim_id']} has no workstream_ids backlink")
        if any(item not in node_ids for item in linked):
            fail(f"claim {claim['claim_id']} references an unknown workstream")
    for task in bundle["research_frontier"]:
        if task.get("workstream_id") not in node_ids:
            fail(f"frontier task {task['task_id']} references an unknown workstream")
    for handoff in bundle["handoffs"]:
        if handoff.get("workstream_id") not in node_ids:
            fail(f"handoff {handoff['handoff_id']} references an unknown workstream")


def validate_validity_and_lifecycle(bundle: dict) -> None:
    """0.4.0+ — validity classes, derived conclusion validity, attestation, lifecycle."""
    missing = TOP_040 - set(bundle)
    if missing:
        fail("missing top-level fields: " + ", ".join(sorted(missing)))

    claims = {claim["claim_id"]: claim for claim in bundle["claims"]}
    for claim in bundle["claims"]:
        label = f"claim {claim['claim_id']}"
        if claim.get("validity_class") not in VALIDITY_CLASSES:
            fail(f"{label} has invalid or missing validity_class")
        if not claim.get("validity_trigger"):
            fail(f"{label} has no validity_trigger")
        if claim["claim_type"] == "judgment" and not claim.get("criteria"):
            fail(f"{label} is a judgment and must record explicit criteria")
        if claim["claim_type"] == "derived_fact" and not claim.get("method"):
            fail(f"{label} is a derived_fact and must record a reproducible method")

    dossier = bundle["dossier"]
    for key in ("validity_class", "validity_driver_claim_ids"):
        if key not in dossier:
            fail(f"dossier missing {key}")
    cited = [claims[cid] for cid in dossier["claim_ids"]]
    if not cited:
        fail("dossier cites no claim")
    weakest = max(cited, key=lambda claim: VALIDITY_ORDER.index(claim["validity_class"]))["validity_class"]
    if dossier["validity_class"] != weakest:
        fail(f"dossier validity_class must be the weakest cited claim class ({weakest})")
    drivers = {claim["claim_id"] for claim in cited if claim["validity_class"] == weakest}
    if set(dossier["validity_driver_claim_ids"]) != drivers:
        fail("dossier validity_driver_claim_ids must list exactly the cited claims at the weakest class")

    revalidations = bundle["revalidations"]
    ids(revalidations, "revalidation_id", "revalidations", allow_empty=True)
    for index, entry in enumerate(revalidations, start=2):
        label = f"revalidation {entry.get('revalidation_id', '?')}"
        require_fields(entry, REVALIDATION, label)
        if entry["verdict"] not in REVALIDATION_VERDICTS:
            fail(f"{label} has invalid verdict")
        if any(cid not in claims for cid in entry["claims_rechecked"] + entry["claims_changed"]):
            fail(f"{label} references an unknown claim")
        if entry["produces_bundle_version"] != index:
            fail(f"{label} produces_bundle_version must be {index}")
    if bundle["bundle_version"] != 1 + len(revalidations):
        fail("bundle_version must be one plus the number of recorded revalidations")

    attestation = bundle["attestation"]
    require_fields(attestation, ATTESTATION, "attestation")
    if attestation["methodology"] != "RIGOR":
        fail("attestation methodology must be RIGOR")
    if attestation["schema_version"] != bundle["schema_version"]:
        fail("attestation schema_version does not match the bundle")
    if attestation["bundle_id"] != dossier["dossier_id"]:
        fail("attestation bundle_id does not match the dossier")
    if attestation["level"] != bundle["brief"]["level"]:
        fail("attestation level does not match the brief")
    if attestation["loop_status"] != bundle["plan"]["research_loop"]["status"]:
        fail("attestation loop_status does not match the research loop")
    if attestation["validity_class"] != dossier["validity_class"]:
        fail("attestation validity_class does not match the dossier")
    if attestation["validator_status"] not in VALIDATOR_STATUSES:
        fail("attestation validator_status is invalid")
    if attestation["procedural_independence"] not in INDEPENDENCE:
        fail("attestation procedural_independence is invalid")
    if not attestation["resolves_to"]:
        fail("attestation must resolve to the bundle it labels")
    expected_latest = revalidations[-1]["revalidation_id"] if revalidations else None
    if attestation["latest_revalidation_id"] != expected_latest:
        fail("attestation latest_revalidation_id does not match the last recorded revalidation")
    profile = attestation["claim_profile"]
    counted = {"supported": 0, "contested": 0, "insufficient": 0, "other": 0}
    for claim in bundle["claims"]:
        key = claim["support_status"] if claim["support_status"] in counted else "other"
        counted[key] += 1
    if {key: profile.get(key) for key in counted} != counted:
        fail(f"attestation claim_profile does not match the claim ledger: expected {counted}")


def validate(bundle: dict) -> None:
    missing = TOP - set(bundle)
    if missing:
        fail("missing top-level fields: " + ", ".join(sorted(missing)))
    version = bundle["schema_version"]
    if version not in SUPPORTED_VERSIONS:
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

    if version in ("0.3.0", "0.4.0"):
        validate_decomposition(bundle)
    if version == "0.4.0":
        validate_validity_and_lifecycle(bundle)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_artifacts.py BUNDLE.json")
        return 2
    try:
        bundle = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
        validate(bundle)
    except (OSError, json.JSONDecodeError, ValueError, KeyError) as error:
        print("RIGOR artifact validation: FAILED\n- " + str(error))
        return 1
    print(f"RIGOR artifact validation: PASSED (schema_version {bundle['schema_version']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
