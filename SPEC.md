# RIGOR Specification

Version: **0.1.0**  
Status: development

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, and **MAY** indicate requirement strength.

## 1. Purpose

RIGOR is an end-to-end methodology for planning, executing, validating, challenging, and maintaining complex evidence-grounded investigations. It is designed for questions whose answer may depend on multiple sources, hidden incentives, contested interpretations, changing data, or material consequences.

Its canonical outcome is a dense, reusable **dossier**: a decision- or learning-ready evidence package with traceable claims, citations, complete references, calibrated confidence, dissent, limitations, and revalidation conditions. Presentations, executive briefs, and encyclopedia entries are derived formats, not replacements for the dossier.

## 2. Scope and exclusions

RIGOR applies to Levels 3–5 of the activation model in [docs/activation-and-proportionality.md](docs/activation-and-proportionality.md). It MUST NOT be imposed on Level 0–2 work unless an explicit trigger raises the investigation level. It does not replace domain professionals, legal discovery, forensic investigation, peer review, due diligence with non-public records, or human accountability.

## 3. Human reference practice

A competent investigator clarifies the actual question and decision, maps what could change the answer, seeks the closest available evidence, checks provenance and incentives, compares independent accounts, looks for counterevidence, distinguishes what is known from what is inferred, and records what would change the conclusion.

RIGOR distributes parts of this practice to agents and tools, but humans remain accountable for mandate, permissions, final action, material risk acceptance, and high-stakes judgment.

## 4. Inputs and outputs

An investigation MUST record a question, intended outcome, scope, material stakes, time or cost constraints, permitted data/tools/actions, and known limitations or conflicts.

A completed Level 3–5 investigation MUST produce a dossier containing: an investigation brief and level rationale; the RIGOR master plan and any provider-plan reconciliation; a source register and evidence ledger; typed claims with evidence lineage; local citations resolving to complete references; conclusion, confidence, dissent, limitations, uncertainty, and revalidation triggers; and escalation and approval records where applicable.

Exact shapes are defined in [docs/research-artifacts.md](docs/research-artifacts.md), [docs/dossier-and-derivations.md](docs/dossier-and-derivations.md), and [docs/citation-and-reference-contract.md](docs/citation-and-reference-contract.md).

## 5. Activation and proportionality

The level is selected before substantive collection and may be raised if new evidence changes consequence, volatility, deception risk, or uncertainty. Lowering requires a written rationale.

- **Level 3:** structured inquiry; source register, cross-source comparison, and limitations.
- **Level 4:** corroborated investigation; independent corroboration, counterevidence search, source assessment, and challenge pass.
- **Level 5:** adversarial investigation; enhanced provenance, incentives/interests analysis, explicit alternatives, human approval gate, and revalidation plan.

Claim-specific overlays are selected through [docs/evidence-regimes.md](docs/evidence-regimes.md).

## 6. Process

RIGOR follows ten iterative stages:

1. **Frame** — define question, outcome, scope, risk, constraints, and level.
2. **Map** — identify claims, entities, stakeholders, evidence types, interests, and unknowns.
3. **Plan** — create the RIGOR master plan, workstreams, search strategies, stop conditions, and provider-plan reconciliation when relevant.
4. **Collect** — retrieve evidence and preserve source metadata.
5. **Verify** — evaluate provenance, method, independence, freshness, context, and claim support.
6. **Analyze** — build claim-evidence links and reproducible derivations.
7. **Challenge** — seek disconfirming evidence, alternatives, missing denominators, and incentive-driven framing.
8. **Synthesize** — produce the dossier with typed, traceable conclusions.
9. **Approve** — obtain required human decision or risk acceptance before an external or high-stakes action.
10. **Revalidate** — monitor explicit triggers and refresh volatile conclusions.

No stage may silently erase uncertainty, failed searches, or material conflicts.

## 7. Evidence and source requirements

Every material claim MUST be typed and linked to a source, complete reference, or reproducible derivation. Source assessment distinguishes authority from quality and records identity, original publication, access date, methodology, directness, independence, incentives/interests, coverage, freshness, and limitations.

At Level 4–5, material claims MUST have independent corroboration or an explicit single-source exception. Official status is not a substitute for inspection; repeated secondary accounts of one origin are not independent corroboration. Contextual source intelligence MAY guide scrutiny but never replaces an investigation-specific assessment. See [docs/evidence-model.md](docs/evidence-model.md) and [docs/source-intelligence.md](docs/source-intelligence.md).

## 8. Agency and orchestration

RIGOR classifies work as deterministic, agent-reasoned, tool-executed, human-decided, or hybrid. It uses composable roles with explicit handoffs. The RIGOR master plan is canonical; a plan generated by Gemini, ChatGPT, Claude, or another system is a reviewable candidate and MUST be reconciled before execution.

Agents MAY plan, retrieve, extract, classify, compare, and challenge within permissions. They MUST NOT autonomously publish, contact persons, make binding commitments, accuse identifiable persons, or take external action. See [docs/agent-architecture.md](docs/agent-architecture.md) and [docs/plan-reconciliation.md](docs/plan-reconciliation.md).

## 9. Evaluation, safety, and escalation

Each implementation MUST evaluate representative and adversarial cases. It MUST test official but misleading sources, correlated citations, conflicting data, missing denominators, stale information, and model-generated unsupported claims.

Level 5 and high-stakes work require a named human decision owner. Escalation is mandatory when evidence is materially insufficient, access/permissions are unclear, claims could cause material harm, or a conclusion would trigger an external effect.

## 10. Completion and stop conditions

An investigation is complete when its required dossier sections exist, material claims are typed and evidenced, citations resolve to complete references, counterevidence is addressed, limitations and revalidation triggers are recorded, and required approvals are present.

It MUST stop or escalate when permissions are absent, evidence cannot support required confidence, costs exceed mandate, or further collection is unlikely to change the decision.

## 11. Evolution

Normative and operational changes require a Change Set under `changes/`. Durable structural choices require a Decision Record. Deterministic repository validation is mandatory for substantive changes.
