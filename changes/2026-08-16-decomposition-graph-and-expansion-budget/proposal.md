# Change proposal — Decomposition graph and expansion budget

- **ID:** 2026-08-16-decomposition-graph-and-expansion-budget
- **Class:** normative
- **Status:** proposed
- **Owner:** Mauricio M. Klagenberg
- **Base:** b3d5d75d07282020b34bae18230f1ce84497315e

## Problem

`plan.workstreams` is the only Research Bundle register with no item contract. Every other register — `sources`, `claims`, `hypotheses`, `research_frontier`, `iterations`, `handoffs` — declares required item fields and is cross-checked; `workstreams` is declared as `{"type": "array"}` and no register points back to it. Coverage of the declared decomposition therefore cannot be audited: a claim does not know which part of the question it belongs to, and a theme raised in prose can disappear from the structure with nothing to notice.

`evaluations/bundles/04-klagenberg-origin.json` shows the cost. It is a Level 5 investigation with a single workstream, no node for nineteenth-century record-keeping practice in Feliz/RS, and no node for onomastics — although `evaluations/summary.md` lists onomastics among the case's evidence regimes and `SR-006` records a subject name carrying the German alias marker `gen.` (*genannt*), which identity resolution must interpret before treating a surname as a lineage match. The theme was named in the evaluation and lost in the artifact.

RIGOR already requires that a missing record weakens a hypothesis only after coverage, survival, access, and search adequacy are assessed. That assessment is a context node. The obligation exists; the node it depends on is not required to exist.

Formalizing decomposition introduces a second problem the current contract cannot bound. `research_loop` limits iterations, not ramification. If every node may spawn context children, the graph grows combinatorially — at branching factor 3, depth 1 yields 3 nodes, depth 2 yields 12, depth 3 yields 39 — and the bundle fills with claims of low decision impact, contradicting the existing instruction to stop when no task carries material expected information gain.

## Current and proposed contract

| Surface | Current | Proposed (`0.3.0`) |
|---|---|---|
| `plan.workstreams` | untyped array | rooted graph of typed nodes: `node_role`, `relation`, `parent_id`, `depth`, `interprets_workstream_ids`, `evidence_regimes`, `temporal_scope`, `jurisdiction`, `decision_impact`, `status` |
| Backlinks | none | `claims[].workstream_ids`, `research_frontier[].workstream_id`, `handoffs[].workstream_id` |
| Evidence regimes | investigation-wide, in `brief` | additionally per node |
| Expansion control | none | `brief.expansion_budget` with `max_depth`, `max_children_per_node`, `max_nodes`, `set_by` |
| Expansion decisions | none | `plan.expansion_decisions[]` with verdict, predicate, and predicate result |
| Determinism | post-hoc validation only | pre-spawn gate (`scripts/check_expansion.py`) plus post-hoc enforcement that its verdict was recorded |

## Decision

Adopt the typed decomposition graph ([0009](../../decisions/0009-typed-decomposition-graph.md)) and the deterministic expansion budget with predicate-based escalation ([0010](../../decisions/0010-deterministic-expansion-budget-and-escalation.md)). Establish the rejected-alternatives register ([0011](../../decisions/0011-rejected-alternatives-register.md)) as shared governance infrastructure.

A node exists only when it answers part of the question or is required to interpret another node's evidence. Escalation past the budget is decided by a machine-evaluated predicate over the existing ledger, never by the orchestrator's judgement that a node feels important. When no predicate fires, the node is recorded as `blocked-by-budget`, named in the dossier limitations, and the investigation continues.

The operational contract is [docs/decomposition-and-expansion.md](../../docs/decomposition-and-expansion.md).

## Alternatives considered

Indexed with reopening conditions in [decisions/rejected-alternatives.md](../../decisions/rejected-alternatives.md): fixed context taxonomy (RJ-001), temporality as a node (RJ-002), untyped theme graph (RJ-003), narrative-only decomposition (RJ-004), single node-count limit (RJ-005), escalation by orchestrator judgement (RJ-006), stopping on every blocked spawn (RJ-007), budget enforced only at final validation (RJ-008).

## Risks and safeguards

- **Coverage theatre.** Structural validation proves coverage of the *declared* graph and can never prove the graph was complete; a missing node is invisible to every check. Safeguard: challenging the decomposition itself becomes an explicit challenge-pass responsibility, recorded as a frontier task or a limitation.
- **Node inflation.** A typed register invites more nodes. Safeguard: depth is a hard cap defaulting by level, breadth is capped per parent, and the spawn criterion excludes thematic affinity.
- **Advisory gate.** An agent can decline to run a script. Safeguard: the recorded verdict is required downstream — a non-root node without a matching `allow`, or a `blocked-by-budget` node without a `deny-record`, fails validation.
- **Predicate too narrow.** P1/P2 may miss a load-bearing node. Safeguard: the remedy is to extend the predicate and preserve the case as regression evidence, never to restore judgement-based escalation.
- **Migration burden.** Four corpus bundles and three fixtures predate the contract. Safeguard: the validator is version-aware; `0.2.0` bundles are checked against `0.2.0` and remain valid.

## Acceptance criteria

- `plan.workstreams` items are typed, rooted, acyclic, and reachable; exactly one root exists.
- A context node declares the workstreams it interprets; a primary node declares none.
- Every claim, frontier task, and handoff resolves to an existing node.
- Depth, per-parent breadth, and total explored nodes respect `brief.expansion_budget`; a `blocked-by-budget` node consumes no budget and is named in the dossier limitations.
- Every non-root node carries a recorded expansion verdict; an `escalate` verdict alongside a still-running loop fails validation.
- A loop reporting `exhausted-within-scope` retains no `unexplored` or `open` node.
- The gate returns `allow`, `deny-record`, and `escalate` on the corresponding inputs with distinct exit codes.
- All `0.2.0` bundles and the existing invalid fixtures behave exactly as before.

## Compatibility

Additive and version-gated. `semver_impact: minor`. Bundles declaring `0.2.0` remain conformant with `0.2.0`; the new obligations attach to `0.3.0`. Consumers MUST NOT represent an unmigrated `0.2.0` bundle as conformant with `0.3.0`.

## Migration

1. Preserve the `0.2.0` artifact unchanged outside an approved migration copy.
2. Set `schema_version` to `0.3.0` and add `brief.expansion_budget`, using the level default for `max_depth` with `set_by: default`.
3. Promote the existing workstreams into a rooted graph: add one root node for the whole question, attach existing workstreams with `relation: decomposes`, and add the context nodes the investigation actually depended on.
4. Backfill `workstream_ids` on every claim and `workstream_id` on every frontier task and handoff.
5. Record one `allow` decision per non-root node; record `deny-record` for any node the budget blocked.
6. Run `python scripts/validate_artifacts.py BUNDLE.json` and retain the result with the artifact.

Corpus migration is deliberately **not** in this Change Set: it changes evaluation evidence and belongs in its own linear change with its own review.

## Implementation sequence

1. `SPEC.md` — normative text first, per `AGENTS.md`.
2. `docs/decomposition-and-expansion.md`, and cross-references from `docs/research-process.md`, `docs/executable-research-artifacts.md`, `docs/agent-architecture.md`.
3. `schemas/research-bundle.0.3.0.schema.json`, `templates/research-bundle.yaml`.
4. `scripts/validate_artifacts.py` (version-aware), `scripts/check_expansion.py`, and the mirrored `skills/rigor/scripts/`.
5. Fixtures: one valid `0.3.0` bundle and the `invalid-orphan-context-node` / `invalid-expansion-budget` regressions.
6. `skills/rigor/` and `skills/rigor-core/` — decomposition contract, spawn criterion, gate invocation, and the decomposition-challenge step.
7. `moda.yaml`, `conformance/moda.yaml`, `scripts/validate_repository.py`, `.github/workflows/validate.yml`, `CHANGELOG.md`, `MIGRATIONS.md`, `ROADMAP.md`, `UPGRADE.md`.
8. Run every command in `impact.yaml`; correct causes and rerun until clean.

## Recovery

Supersede this Change Set or revert its commit. No user-data migration is required in this pre-release repository, and no `0.2.0` artifact is altered.
