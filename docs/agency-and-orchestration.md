# Agency and orchestration

## Agency classes

| Activity | Default class | Constraint |
|---|---|---|
| Validate file shape, required fields, links, calculations | Deterministic | Preserve and rerun script output |
| Frame question, propose workstreams, rank sources | Agent-reasoned | Human may override scope and level |
| Search, retrieve, extract, query approved sources | Tool-executed | Respect permissions and access boundaries |
| Assess uncertainty and alternatives | Hybrid | Evidence must be inspectable |
| Approve scope, risk, external action, final decision | Human-decided | Mandatory for Level 5 and high-stakes work |

## Orchestration pattern

The orchestrator maintains the brief, canonical plan, evidence ledger, and stop conditions. Discovery, verification, challenge, and synthesis use separate handoffs. Specialist auditors are activated only when their evidence regime applies. See [agent architecture](agent-architecture.md).

Parallelism is justified only when workstreams are independent enough to reduce shared blind spots. Splitting the same web search across several models does not create independent evidence.

## Research engines and models

ChatGPT, Gemini, Claude, and other capable systems MAY be complementary lenses for planning, retrieval, extraction, analysis, and challenge. Select by task fit, permissions, source access, language support, reproducibility, and known limitations—not brand preference.

Provider output enters the ledger as an unverified claim until tied to inspectable evidence. Provider plans are reconciled to the RIGOR master plan under [plan reconciliation](plan-reconciliation.md).

## Escalation

Stop and request human direction when scope or permission is ambiguous; work would materially affect a person or organization; evidence cannot support required confidence; a conflict is materially undisclosed; or the decision is legal, medical, financial, safety-critical, rights-affecting, or reputationally harmful.
