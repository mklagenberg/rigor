# RIGOR Specification

Version: **0.1.0**  
Status: development

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHOULD**, **SHOULD NOT**, and **MAY** indicate requirement strength.

## 1. Purpose

RIGOR is an end-to-end methodology for planning, executing, validating, challenging, and maintaining complex evidence-grounded investigations. It is designed for questions whose answer may depend on multiple sources, hidden incentives, contested interpretations, changing data, or material consequences.

Its outcome is not merely an answer. It is a decision- or learning-ready evidence package with a traceable conclusion, calibrated confidence, dissent, limitations, and revalidation conditions.

## 2. Scope and exclusions

RIGOR applies to Levels 3–5 of the activation model in [docs/activation-and-proportionality.md](docs/activation-and-proportionality.md).

RIGOR MUST NOT be imposed on Level 0–2 work unless an explicit trigger raises the investigation level. It does not replace domain professionals, legal discovery, forensic investigation, peer review, due diligence with access to non-public records, or human accountability.

## 3. Human reference practice

A competent investigator first clarifies the actual question and decision, maps what could change the answer, seeks the closest available evidence, checks the provenance and incentives of sources, compares independent accounts, looks for counterevidence, distinguishes what is known from what is inferred, and records what would change the conclusion.

RIGOR distributes parts of this practice to agents and tools, but humans remain accountable for mandate, permissions, final action, material risk acceptance, and high-stakes judgment.

## 4. Inputs and outputs

### Required inputs

An investigation MUST record a question, intended outcome, scope, material stakes, time or cost constraints, and permitted data/tools/actions. It MUST name any known limitations or conflicts of interest.

### Required outputs

A completed Level 3–5 investigation MUST produce:

1. an investigation brief and level rationale;
2. a research plan and source-discovery strategy;
3. a source register and evidence ledger;
4. typed claims with evidence lineage;
5. a conclusion with confidence, dissent, limitations, and uncertainty;
6. revalidation triggers and an owner for Level 4–5 work;
7. a record of escalation and human approvals when applicable.

The exact artifact shapes are defined in [docs/research-artifacts.md](docs/research-artifacts.md).

## 5. Activation and proportionality

The investigation level is selected before substantive collection and may be raised if new evidence changes consequence, volatility, deception risk, or uncertainty. Lowering a level requires a written rationale.

- **Level 3:** structured inquiry; source register, cross-source comparison, and limitations are required.
- **Level 4:** corroborated investigation; independent corroboration, counterevidence search, source assessment, and challenge pass are required.
- **Level 5:** adversarial investigation; enhanced provenance, incentive analysis, explicit alternative hypotheses, human approval gate, and revalidation plan are required.

See [docs/activation-and-proportionality.md](docs/activation-and-proportionality.md).

## 6. Process

RIGOR follows ten stages:

1. **Frame** — define the question, outcome, scope, risk, constraints, and level.
2. **Map** — identify claims, entities, stakeholders, evidence types, incentives, and unknowns.
3. **Plan** — form workstreams, search strategies, stop conditions, and expected artifacts.
4. **Collect** — retrieve evidence and preserve source metadata.
5. **Verify** — evaluate provenance, method, independence, freshness, and claim support.
6. **Analyze** — build claim-evidence relationships, compare data, and calculate only reproducible derivations.
7. **Challenge** — seek disconfirming evidence, alternative explanations, missing denominators, and incentive-driven framing.
8. **Synthesize** — make a typed, traceable conclusion with calibrated confidence.
9. **Approve** — obtain the required human decision or risk acceptance before an external or high-stakes action.
10. **Revalidate** — monitor explicit triggers and refresh volatile conclusions.

Stages may iterate. No stage may silently erase uncertainty, failed searches, or material conflicts.

## 7. Evidence and source requirements

Every material claim MUST be typed and linked to a source or derivation. Source assessment MUST distinguish authority from evidence quality and record, where relevant: source identity, original publication, access date, methodology, directness, independence, incentives, coverage, freshness, and limitations.

At Level 4–5, material claims MUST have either independent corroboration or an explicit single-source exception with rationale. A source’s official status is not a substitute for inspection. Multiple secondary sources repeating one origin are not independent corroboration.

See [docs/evidence-model.md](docs/evidence-model.md).

## 8. Agency and orchestration

RIGOR classifies consequential work as deterministic, agent-reasoned, tool-executed, human-decided, or hybrid. Agents MAY plan, retrieve, extract, classify, compare, and challenge within permissions. They MUST NOT autonomously publish, contact persons, make binding commitments, accuse identifiable persons, or take external action.

Multiple research models or engines MAY be used for diversity of retrieval, framing, and challenge. Their agreement is a prompt to inspect sources, not evidence of truth. See [docs/agency-and-orchestration.md](docs/agency-and-orchestration.md).

## 9. Evaluation, safety, and escalation

Each implementation MUST evaluate representative and adversarial cases. It MUST test at least: official but misleading sources, correlated citations, conflicting data, missing denominators, stale information, and model-generated unsupported claims.

Level 5 and all high-stakes work require a named human decision owner. Escalation is mandatory when evidence is materially insufficient, access/permissions are unclear, claims could cause material harm, or a conclusion would trigger an external effect. See [docs/evaluation-and-safety.md](docs/evaluation-and-safety.md).

## 10. Completion and stop conditions

An investigation is complete when the required artifacts for its level exist, material claims are typed and evidenced, material counterevidence has been addressed, limitations and revalidation triggers are recorded, and required human approvals are present.

It MUST stop or escalate when permissions are absent, evidence cannot support the required confidence, costs exceed the mandate, or further collection is unlikely to change the decision.

## 11. Evolution

Normative and operational changes require a Change Set under `changes/`. Durable structural choices require a Decision Record. Deterministic repository validation is mandatory for substantive changes. Release and versioning rules are defined in [docs/git-and-release-workflow.md](docs/git-and-release-workflow.md).
