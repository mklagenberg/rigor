# 0010 — Deterministic expansion budget and escalation

- Status: proposed
- Date: 2026-08-16
- Decision owners: Mauricio M. Klagenberg
- Change Set: 2026-08-16-decomposition-graph-and-expansion-budget

## Context

Making decomposition a first-class register introduces a failure mode the loop policy does not cover. `research_loop` bounds iterations — how many times the investigation passes — not ramification. If each node may spawn context children and those children may spawn their own, the graph grows combinatorially and the bundle fills with claims of low decision impact, contradicting the existing instruction to stop when no task carries material expected information gain.

The obvious escape hatch is worse than the problem. If the orchestrator may declare a blocked node "fundamental" and request a wider budget, the role that wants to expand is validating its own request, which is the one thing RIGOR forbids everywhere else. The incentive is asymmetric: an agent under-stops far more often than it over-stops, so a judgement-based override would be exercised routinely and the budget would stop binding.

## Decision

Expansion is bounded on two independent axes recorded in `brief.expansion_budget`: `max_depth` (hard, defaulting to 1/2/3 by level) and `max_children_per_node` (breadth per parent). `max_nodes` exists only as a backstop. `set_by` records whether the budget is the default, was set by the user at intake, or was widened by re-approval.

`scripts/check_expansion.py` evaluates a proposed node *before* it is spawned and returns `allow`, `deny-record`, or `escalate`. Escalation requires a machine-evaluated predicate over the existing ledger:

- **P1** — the proposed context node interprets a workstream holding a `contested` or `insufficient` claim that the conclusion cites;
- **P2** — the proposed node links at least two open, mutually alternative hypotheses that no ready high-value frontier task already discriminates.

If neither predicate fires, the node is recorded as `blocked-by-budget`, named in the dossier limitations, and the investigation continues. Interruption is the exception.

Every non-root node must carry a matching verdict in `plan.expansion_decisions`, and the bundle validator rejects a node without one. An `escalate` verdict recorded alongside a loop that kept running is a validation failure.

## Consequences

- Breadth is bounded where the explosion actually lives. With branching factor 3, depth 1 yields 3 nodes, depth 2 yields 12, and depth 3 yields 39.
- The decision to stop or continue is auditable, and a refusal to expand is preserved as a finding rather than silently dropped.
- A node blocked by the budget consumes no budget, so a refusal cannot permanently occupy a slot.
- Determinism moves from post-hoc validation to a pre-spawn gate. A control that fires only at the end cannot prevent cost that is already spent.
- Requiring the recorded verdict downstream is what makes calling the gate binding rather than advisory.
- The predicate may prove too narrow. The remedy is to extend the predicate, never to restore judgement-based escalation.

## Alternatives considered

- **A single node-count limit as the primary control.** Rejected: gameable by granularity, since questions can be merged into one fat node to fit the cap. This is the same category error as counting sources instead of evidence lineages ([0003](0003-evidence-lineage-over-source-count.md)).
- **Escalate whenever the orchestrator judges the node fundamental.** Rejected: self-validation, and an override that is always available is not a limit.
- **Stop the investigation on every blocked spawn.** Rejected: it converts a bounded budget into a permission prompt and costs a human turn for nodes of low decision impact.
- **Enforce the budget only in final validation.** Rejected: the cost is already spent by then.

## Follow-up

Evaluate predicate coverage against the corpus once bundles are migrated, and record any node the predicate wrongly denied as regression evidence.
