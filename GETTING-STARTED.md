# Getting started with RIGOR

## Fastest path: use the skill

Invoke `@rigor` in ChatGPT Work or `$rigor` in Codex, followed by the question, learning/decision goal, scope, and stakes if wrong. The installable package is [`skills/rigor`](skills/rigor/SKILL.md).

RIGOR will reject disproportionate Level 0–2 activation, create one master plan for Level 3–5 work, reconcile any provider-native Deep Research plan, and delegate bounded roles when subagents are available. If they are not, it uses a declared sequential fallback; this is not equivalent to independent review.

## 1. Decide whether to activate it

Use [the activation guide](docs/activation-and-proportionality.md). RIGOR begins at Level 3. For Levels 0–2, answer directly or use a narrower retrieval/synthesis workflow.

## 2. Create an investigation brief

Record:

- the question and the decision, learning, or discovery outcome it serves;
- scope, exclusions, jurisdiction, period, and audience;
- consequences of error and required confidence;
- known stakeholders, hypotheses, claims, and constraints;
- permitted tools, data, budget, time, and external actions;
- whether source discovery, community evidence, or specialist input is material.

Use the artifact shapes in [research artifacts](docs/research-artifacts.md).

## 3. Select an investigation level

- **Level 3 — Structured inquiry:** multiple sources and a bounded comparison.
- **Level 4 — Corroborated investigation:** material decision, contested claims, or meaningful risk; requires independent corroboration and a challenge pass.
- **Level 5 — Adversarial investigation:** high consequence, deception risk, major uncertainty, or a powerful incentive structure; requires enhanced provenance, counterevidence, escalation, and a human approval gate.

## 4. Run the process

Follow [the research process](docs/research-process.md): frame, map, plan, collect, verify, analyze, challenge, iterate, synthesize, approve, and revalidate. During mapping, record credible alternative hypotheses. During iteration, convert material next steps into a prioritized frontier and continue only within the approved mandate.

The default loop includes the initial pass: 2 iterations at Level 3, 3 at Level 4, and 4 at Level 5. Override it explicitly when needed: `Research loop limit: 6 iterations.` The loop must stop early when no material discriminating task remains; it must ask before a material expansion, private/paid/sensitive access, contact, or other external action.

## 5. Deliver a decision-ready result

A final RIGOR report contains:

- answer or recommendation, confidence, and scope;
- material facts and their evidence lineages;
- credible counterevidence and unresolved disagreements;
- key assumptions, limitations, incentives, and missing evidence;
- research ledger and source register;
- revalidation triggers and human decision owner where applicable.
- hypothesis register, iteration journal, and an explicit frontier outcome (`exhausted-within-scope`, `blocked`, `paused-by-limit`, `ready-for-revalidation`, or `escalated`).

## Minimum prompt

> Use $rigor to investigate: [question]. The decision or learning goal is [goal]. Scope: [scope]. Stakes if wrong: [stakes].

The skill adds the research plan, discovery strategy, evidence ledger, counterevidence pass, confidence assessment, Research Bundle, dense dossier, and revalidation triggers automatically.
