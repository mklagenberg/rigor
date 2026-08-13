# Agency and orchestration

## Agency classes

| Activity | Default class | Constraint |
|---|---|---|
| Validate file shape, required fields, links, calculations | Deterministic | Script output is preserved and rerun after repair |
| Frame question, propose workstreams, rank sources | Agent-reasoned | Human may override scope and level |
| Search, retrieve, extract, query approved sources | Tool-executed | Respect permissions, terms, and access boundaries |
| Assess uncertainty and alternative explanations | Hybrid | Evidence must be inspectable |
| Approve scope, risk, external action, final decision | Human-decided | Mandatory for Level 5 and high-stakes work |

## Orchestration pattern

RIGOR uses adaptive planning with bounded fan-out/fan-in:

1. a supervisor maintains the brief, claim map, evidence ledger, and stop conditions;
2. independent workstreams pursue distinct evidence lineages or question types;
3. a verifier normalizes and groups evidence;
4. a challenger independently attacks the leading interpretation;
5. a synthesizer merges only evidence that survived verification;
6. a human owner resolves escalations and approves consequential use.

Parallelism is justified only when workstreams are independent enough to reduce shared blind spots. Splitting the same web search across several models does not create independent evidence.

## Research engines and models

ChatGPT, Gemini, Claude, and other capable systems MAY be used as complementary lenses for planning, retrieval, extraction, analysis, and challenge. Select them by task fit, permissions, source access, language support, reproducibility, and known limitations—not brand preference.

Each model output enters the ledger as an unverified claim until it is tied to inspectable evidence. Agreement among models can reveal convergence in interpretation; it cannot satisfy corroboration requirements.

## Escalation

Stop and request human direction when:

- scope or permission is ambiguous;
- work would contact, profile, accuse, or materially affect a person or organization;
- evidence cannot support the required confidence;
- a source has an undisclosed but potentially material conflict;
- the decision is legal, medical, financial, safety-critical, rights-affecting, or reputationally harmful.
