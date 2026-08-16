# Decomposition and expansion

A question is rarely one investigation. It decomposes into nodes, and some nodes exist only so that another node's evidence can be read correctly. Before `0.3.0` the Research Bundle carried `plan.workstreams` as an untyped array: no fields, no edges, and no register pointing back to it. Coverage of the declared decomposition could not be audited, and a theme raised in prose could disappear from the structure without any check noticing.

## The graph

The decomposition is a rooted directed graph of workstream nodes with typed edges. An untyped adjacency is a mind map; it does not constrain execution.

| Relation | Meaning |
|---|---|
| `root` | The whole question. Exactly one node, depth 0, null parent. |
| `decomposes` | The child answers a bounded part of the parent. |
| `interprets` | The child conditions how the parent's evidence must be read. |
| `enables` | The child is a prerequisite for work in the parent. |
| `competes` | The child pursues a rival account of the parent's question. |

Each node declares `node_role`:

- **primary** — answers part of the question;
- **context** — required to interpret evidence held by another node, named in `interprets_workstream_ids`.

`interprets` is the edge that earns its keep. RIGOR already requires that a missing record weakens a hypothesis only after coverage, survival, access, and search adequacy are assessed (see [hypotheses and research loops](hypotheses-and-research-loops.md)). That assessment *is* a context node. The rule was mandatory and the node it depends on was never required to exist.

## Spawn criterion

A node MUST exist only when it (a) answers part of the question or (b) is necessary to interpret evidence held by another node. Thematic affinity is not sufficient. There is no fixed taxonomy of context types: whether a theme is context or primary is decided by the edge, not by a category list. Market structure is context in a genealogical question and the primary object in a market question.

Time is an attribute of every node (`temporal_scope`, `jurisdiction`), not a node of its own. Chronology *reconstruction* remains a legitimate workstream; "the period" is not.

Evidence regimes are declared per node. A single investigation-wide regime list loses the regime that applies to one branch only.

## Expansion budget

Breadth explodes faster than depth is usually appreciated: with a branching factor of 3, depth 1 yields 3 nodes, depth 2 yields 12, and depth 3 yields 39. Depth is therefore the hard control.

`brief.expansion_budget` carries `max_depth`, `max_children_per_node`, `max_nodes`, and `set_by`. Defaults for `max_depth` follow the level — 1 at Level 3, 2 at Level 4, 3 at Level 5 — mirroring the loop-iteration defaults. `max_nodes` is a backstop, never the primary control: a single total-node count is gameable by granularity, since three questions can be merged into one fat node to fit the cap. That is the same category error as counting sources instead of evidence lineages (see [0003](../decisions/0003-evidence-lineage-over-source-count.md)).

`set_by` records whether the budget is the methodology default, was set by the user at intake, or was widened through re-approval. Without it, a wide search authorized by the decision owner is indistinguishable from a model that expanded on its own.

## The gate

`scripts/check_expansion.py` runs **before** a node is spawned and returns one of three verdicts:

- `allow` — the node fits the approved budget;
- `deny-record` — the budget blocks it and no predicate fires: the node is recorded with status `blocked-by-budget`, named in the dossier limitations, and **the investigation continues**;
- `escalate` — the budget blocks it but the node is load-bearing: the investigation stops and the decision owner is asked for a wider budget.

Escalation is decided by a machine-evaluated predicate over the existing ledger, never by the orchestrator's own sense that a node feels important. A role that wants to expand is not permitted to validate its own request; that is the same separation RIGOR already requires between discovery and verification.

- **P1 — load-bearing interpretation:** the proposed context node interprets a workstream holding a claim whose `support_status` is `contested` or `insufficient` and which the conclusion cites.
- **P2 — sole discriminator:** the proposed node links at least two open, mutually alternative hypotheses that no ready high-value frontier task already discriminates.

Interruption is the exception, not the default. A recorded `blocked-by-budget` node is a finding about the investigation's boundary, not a failure to hide.

A node blocked by the budget consumes no budget: it was never explored, and counting it would let a refusal permanently occupy a slot.

## Binding the gate

A deterministic script only binds when the artifact it produces is required downstream. Every non-root node MUST carry a matching entry in `plan.expansion_decisions`: an `allow` for explored nodes, a `deny-record` for `blocked-by-budget` nodes. `scripts/validate_artifacts.py` rejects a bundle whose node has no recorded verdict, and rejects an `escalate` verdict recorded alongside a research loop that kept running.

## What validation cannot do

The validator proves that the declared decomposition was covered. It cannot prove that the decomposition was correct. A node that should exist and does not is invisible to every structural check.

Attacking the graph is therefore a challenger responsibility, distinct from attacking claims: before the loop closes, the challenge pass MUST ask which node should exist and does not, and record the answer as a frontier task or an explicit limitation. Formalizing coverage of the map does not create coverage of the territory.

## Node lifecycle states

`unexplored`, `open`, `closed-productive`, `closed-no-gain`, `blocked`, `blocked-by-budget`. A loop that reports `exhausted-within-scope` MUST NOT retain an `unexplored` or `open` node — the same rule that already forbids declaring exhaustion while a `ready` frontier task remains.
