# Artifact and evidence contract

The Research Bundle is the machine-readable investigation state. The dossier is its dense human-readable canonical output. Presentations, executive briefs, encyclopedia entries, FAQs, and teaching material are derivatives.

## Research Bundle registers

- `brief`: question, outcome, scope, exclusions, force, regimes, permissions, owner, version status.
- `plan`: canonical workstreams, provider reconciliation, stop conditions, challenge routes.
- `sources`: one source record per inspectable item or upstream origin.
- `claims`: typed claim ledger with citations and support state.
- `hypotheses`: testable working explanations, alternatives, expected traces, and disconfirming tests.
- `research_frontier`: prioritized, bounded next tasks arising from evidence and hypotheses.
- `iterations`: journal of completed bounded passes and their frontier decisions.
- `handoffs`: role outputs and deviations.
- `dossier`: conclusion, confidence, limitations, and revalidation.

Start from `assets/research-bundle.json`. Use stable IDs: `PLAN-`, `WS-`, `SR-`, `CL-`, `HY-`, `FT-`, `IT-`, `HO-`, and `DOS-`.

## Claim types

- `observation`: directly inspected content or event in a source.
- `source_claim`: what an attributed source says.
- `derived_fact`: reproducible transformation or calculation from evidence.
- `inference`: reasoned implication that could be challenged.
- `judgment`: evaluation under explicit criteria.
- `open_question`: unresolved claim or missing evidence.

Never silently convert a source claim, inference, or judgment into fact. A material claim must cite source IDs, or be marked insufficient.

## Hypotheses, frontier, and iterations

A hypothesis is not a claim and has no evidentiary weight on its own. It records type (`retrospective`, `prospective`, `causal`, or `counterfactual`), alternatives, testable traces, disconfirming conditions, linked claims, and status. A missing trace weakens it only after coverage, survival, access, and search adequacy are recorded.

The frontier is a prioritized task queue. Each task names a hypothesis or question, expected information gain, cost, permission boundary, status, and reason. An iteration journal records executed task IDs, evidence/claim effects, frontier changes, and its stop decision. Preserve blocked and deferred tasks rather than replacing them with a narrative recommendation.

## Source presentation

Every immediate citation must resolve to one complete reference. Put the citation directly below or beside the supported statement. Use source IDs consistently.

A complete reference records:

```text
source_id; author or responsible organization; title;
source type (article, report, filing, post, discussion, book, dataset,
documentation, interview, archival record, paper, review, guidance, etc.);
venue/place and publisher; publication date; locator/URL/DOI/archive ID;
access date; source status; independence group; upstream origin;
method or data lineage; incentives/interests; limitations.
```

`official`, `peer-reviewed`, `community`, and `primary` are attributes, not blanket quality verdicts. Evaluate what the source can establish.

## Evidence lineage and source status

Use source status carefully:

- `discovered`: candidate not yet inspected;
- `verified`: identity, accessibility, and relevant content checked;
- `validated`: method/provenance and claim fit passed the applicable audit;
- `contested`: credible conflict remains;
- `insufficient`: cannot support the intended claim;
- `actionable`: sufficiently validated for the stated decision context, with limitations.

Map dependence to the upstream source. Ten articles copying one press release form one evidence lineage. Corporate investor filings, regulatory filings, technical documentation, marketing pages, commissioned reports, executive interviews, employee posts, and community discussions receive separate source records and interest assessments.

## Dense dossier order

1. question, scope, force, regimes, and decision owner;
2. executive conclusion with claim-type label and confidence;
3. definitions, decomposition, and research plan;
4. evidence ledger and source lineage;
5. method/data audit and calculations;
6. incentives and explicit or hidden interests;
7. counterevidence, alternatives, dissent, and challenge result;
8. detailed findings with immediate citations;
9. limitations, open questions, and calibrated non-conclusions;
10. hypothesis register, alternatives, and tests;
11. research frontier, iteration journal, loop outcome, and remaining work;
12. revalidation triggers, owner, and cadence when relevant;
13. complete references and reproducibility appendices.

A derivative must name its source dossier and preserve material qualifications, claim types, citations, and complete reference linkage.
