# 0009 — Typed decomposition graph

- Status: proposed
- Date: 2026-08-16
- Decision owners: Mauricio M. Klagenberg
- Change Set: 2026-08-16-decomposition-graph-and-expansion-budget

## Context

`plan.workstreams` was the only Research Bundle register with no item contract. `sources`, `claims`, `hypotheses`, `research_frontier`, `iterations`, and `handoffs` each declare required item fields and are cross-checked; `workstreams` was declared as `{"type": "array"}` and nothing pointed back to it. Coverage of the declared decomposition could therefore not be audited: a claim did not know which part of the question it belonged to.

The Batch 4 corpus shows the cost. `evaluations/bundles/04-klagenberg-origin.json` is a Level 5 investigation carrying a single workstream. It has no node for nineteenth-century record-keeping practice in Feliz/RS and none for onomastics, although `evaluations/summary.md` lists onomastics among the case's evidence regimes and `SR-006` records a subject name containing the German alias marker `gen.` (*genannt*). The theme was raised in prose and lost in the structure, and no check could notice.

RIGOR already requires that a missing record weakens a hypothesis only after coverage, survival, access, and search adequacy are assessed. That assessment is a context node. The obligation existed; the node it depends on was never required to exist.

## Decision

The decomposition becomes a first-class register: a rooted graph of typed nodes with typed edges (`root`, `decomposes`, `interprets`, `enables`, `competes`) and an explicit `node_role` of `primary` or `context`. A context node names the workstreams it interprets. Claims, frontier tasks, and handoffs carry a node backlink. Evidence regimes, temporal scope, and jurisdiction are declared per node.

A node exists only when it answers part of the question or is required to interpret another node's evidence. Thematic affinity is not a spawn criterion.

## Consequences

- Coverage of the declared decomposition becomes machine-auditable, and a node closed without gain must say so rather than vanish.
- Evidence regimes stop being investigation-wide, so a regime that applies to one branch is no longer dropped.
- The missing-record rule becomes executable, because the context node it presupposes is now a structural object.
- Structural validation proves coverage of the declared graph only. A node that should exist and does not remains invisible, so challenging the decomposition itself becomes an explicit challenger responsibility before the loop closes.
- Bundles declaring `0.2.0` remain valid against `0.2.0`; the new contract applies from `0.3.0`.

## Alternatives considered

- **Leave decomposition as narrative in the dossier.** Rejected: every other register is typed and cross-checked, and the corpus demonstrates that narrative themes are lost.
- **A fixed taxonomy of context types (historical, market, temporal).** Rejected: node type is relational, not intrinsic. Market structure is context in a genealogical question and the primary object in `02-ai-market-bubble`. A fixed list would produce ritual template-filling.
- **Temporality as a node type.** Rejected: it creates an orphan node with no evidence target. Time is an attribute of every node. Chronology *reconstruction* remains a legitimate workstream.
- **An untyped theme graph.** Rejected: adjacency without edge types is a mind map and constrains nothing.

## Follow-up

Add the decomposition-challenge step to the challenge pass, migrate the four corpus bundles to `0.3.0` in a separate Change Set, and mirror the contract into `skills/rigor` and `skills/rigor-core`.
