# Rejected alternatives

Design options that were considered and rejected, so they are not re-argued from scratch.

This file is an **index**, not an authority. The argument lives in the *Alternatives considered* section of the Decision Record named in each entry; entries here point at it. Per [0011](0011-rejected-alternatives-register.md), every entry carries a **reopening condition** — the new fact, evidence, or observed failure that would make re-discussion worthwhile. A rejection with no falsifier is dogma, not a decision.

Entries are appended, never rewritten. A reopened entry keeps its ID, is marked `reopened`, and names the record that reopened it.

## Register

### RJ-001 — Fixed taxonomy of context types

- **Rejected option:** require historical, market, and temporal context nodes as named categories in every decomposition.
- **Reason:** node type is relational, not intrinsic — it follows from the edge, not from a category list. Market structure is context in a genealogical question and the primary object in a market question. A fixed list produces ritual template-filling rather than investigation.
- **Evidence:** `evaluations/bundles/02-ai-market-bubble.json`, where market analysis is the object of the question rather than context for it.
- **Argued in:** [0009](0009-typed-decomposition-graph.md) · **Status:** rejected
- **Reopening condition:** relational typing is observed to produce systematic under-declaration of context nodes across three or more evaluated runs.

### RJ-002 — Temporality as a node

- **Rejected option:** model period or "temporal context" as its own workstream node.
- **Reason:** it produces an orphan node with no evidence target. Time is an attribute of every node, captured by `temporal_scope` and `jurisdiction`, which also gives an anachronism check. Chronology *reconstruction* remains a legitimate workstream and is unaffected.
- **Argued in:** [0009](0009-typed-decomposition-graph.md) · **Status:** rejected
- **Reopening condition:** a chronology workstream is shown to need a node type structurally distinct from a provenance workstream.

### RJ-003 — Untyped theme graph

- **Rejected option:** record decomposition as related themes without typed edges.
- **Reason:** adjacency without edge types is a mind map and constrains nothing at execution time. The `interprets` edge is what makes the coverage/survival/access rule for missing records executable.
- **Argued in:** [0009](0009-typed-decomposition-graph.md) · **Status:** rejected
- **Reopening condition:** the edge vocabulary is shown to be unassignable for a material class of investigations.

### RJ-004 — Decomposition as narrative only

- **Rejected option:** keep the decomposition in dossier prose rather than as a typed register.
- **Reason:** every other register is typed and cross-checked; the untyped one is where themes leak. `04-klagenberg-origin` is a Level 5 bundle with one workstream and no onomastics node, although the case's own evaluation lists onomastics as an evidence regime.
- **Argued in:** [0009](0009-typed-decomposition-graph.md) · **Status:** rejected
- **Reopening condition:** structural decomposition is shown to cost more than the coverage failures it prevents.

### RJ-005 — Single node-count limit as the primary control

- **Rejected option:** bound expansion with one total-nodes number.
- **Reason:** gameable by granularity — three questions merge into one fat node to fit the cap, yielding fewer and worse nodes. Same category error as counting sources instead of evidence lineages ([0003](0003-evidence-lineage-over-source-count.md)). Depth and per-parent breadth are the controls; total count is a backstop.
- **Argued in:** [0010](0010-deterministic-expansion-budget-and-escalation.md) · **Status:** rejected
- **Reopening condition:** depth and breadth caps are observed to bind ineffectively while the total ceiling is what actually stops runaway expansion.

### RJ-006 — Escalation by orchestrator judgement

- **Rejected option:** allow the orchestrator to interrupt the investigation whenever it judges a blocked node "fundamental to rigor".
- **Reason:** the role that wants to expand would validate its own request, which RIGOR forbids everywhere else. The incentive is asymmetric — an agent under-stops far more often than it over-stops — so an always-available override stops being a limit.
- **Argued in:** [0010](0010-deterministic-expansion-budget-and-escalation.md) · **Status:** rejected
- **Reopening condition:** the P1/P2 predicates are shown to miss load-bearing nodes in two or more evaluated runs. The remedy is then to extend the predicate, not to restore judgement-based escalation.

### RJ-007 — Stop the investigation on every blocked spawn

- **Rejected option:** treat any budget-blocked node as grounds to halt and ask the user.
- **Reason:** it converts a budget into a permission prompt and spends a human turn on nodes of low decision impact. The default is `deny-record`: preserve the node as `blocked-by-budget`, name it in the limitations, and continue. Not stopping is a valid, recorded outcome.
- **Argued in:** [0010](0010-deterministic-expansion-budget-and-escalation.md) · **Status:** rejected
- **Reopening condition:** nodes recorded as `blocked-by-budget` are shown to correlate with materially wrong conclusions.

### RJ-008 — Enforce the expansion budget only in final validation

- **Rejected option:** check budget compliance in `validate_artifacts.py` when the bundle is emitted.
- **Reason:** a control that fires at the end cannot prevent cost that is already spent. The gate runs before the spawn; final validation only enforces that the gate's verdict was recorded.
- **Argued in:** [0010](0010-deterministic-expansion-budget-and-escalation.md) · **Status:** rejected
- **Reopening condition:** pre-spawn gating proves impractical on a host that cannot execute scripts mid-investigation, in which case the fallback must be declared as reduced control, not silently accepted.

### RJ-009 — Correctness seal ("audited by RIGOR vX")

- **Rejected option:** a document-level mark asserting that the content was audited and is therefore reliable.
- **Reason:** wrong granularity. Rigor is a property of the process, truth a property of the claim. Averaging over a ledger that ranges from `supported` to `insufficient` lets a `judgment` travel as verified, defeating the typed ledger. All four Batch 4 runs passed with a named limitation and `04-klagenberg-origin` passed as a calibrated non-conclusion, so a binary mark cannot describe the outcome. It would also manufacture exactly the authority-without-lineage RIGOR treats as an evidence input with its own failure modes.
- **Argued in:** [0012](0012-process-attestation-not-verification-seal.md) · **Status:** rejected, replaced by process attestation
- **Reopening condition:** an external standard emerges that binds claim-level verification with independent audit, making a correctness assertion checkable rather than reputational.

### RJ-010 — Attestation only on clean runs

- **Rejected option:** emit the label only when validation passes with full independence and no insufficient claims.
- **Reason:** a label that appears only on good outcomes is a marketing badge. The informative version carries `paused-by-limit`, `procedural_independence: limited`, and non-zero insufficient counts — a nutrition label, not a star rating. RIGOR does not erase adverse states.
- **Argued in:** [0012](0012-process-attestation-not-verification-seal.md) · **Status:** rejected
- **Reopening condition:** carrying adverse states is shown to cause systematic misreading by consumers who treat any label as endorsement.

### RJ-011 — Calendar TTL for information validity

- **Rejected option:** assign each claim a time-to-live in days or months.
- **Reason:** calendar age is the symptom; the decay mechanism is the cause. A claim about an officeholder decays when the person leaves, not on a schedule. TTLs err in both directions at once — re-checking what did not change, and missing what changed early, which opens a false-confidence window until the scheduled check. Only `measured` claims legitimately use a calendar, because their cadence is known.
- **Argued in:** [0013](0013-validity-classes-by-decay-mechanism.md) · **Status:** rejected
- **Reopening condition:** decay-mechanism classes prove unassignable in practice and a calendar approximation outperforms them in evaluation.

### RJ-012 — Dossier asserts its own validity class

- **Rejected option:** let the synthesizer state the conclusion's durability directly.
- **Reason:** it would permit a volatile conclusion to be presented as durable. The class is derived from the weakest cited claim, which is computable from the ledger and therefore validated.
- **Argued in:** [0013](0013-validity-classes-by-decay-mechanism.md) · **Status:** rejected
- **Reopening condition:** the weakest-class rule is shown to mislabel conclusions whose volatile inputs are immaterial to the reasoning.

### RJ-013 — Four lifecycle phases

- **Rejected option:** separate acquisition, maintenance, update, and revalidation.
- **Reason:** maintenance and update carry no controls distinct from revalidation; they would be the same mechanism under different names. Methodologies degrade through taxonomy inflation. Two phases carry distinct controls; the rest are verdicts inside a revalidation entry.
- **Argued in:** [0014](0014-two-phase-acquisition-and-revalidation-lifecycle.md) · **Status:** rejected
- **Reopening condition:** a maintenance activity is identified with controls, triggers, or approval boundaries distinct from both acquisition and revalidation.

### RJ-014 — Revalidation recorded as a loop iteration

- **Rejected option:** append revalidation passes to `iterations[]`.
- **Reason:** it collides with the enforced `current_iteration <= max_iterations` rule and erases the distinction between bounded acquisition and open-ended post-acceptance maintenance.
- **Argued in:** [0014](0014-two-phase-acquisition-and-revalidation-lifecycle.md) · **Status:** rejected
- **Reopening condition:** the two registers are shown to duplicate each other in practice with no divergent control.
