# Implementation plan

This plan is intentionally executed and validated in **batches**, not step-by-step approvals.

## Batch 1 — Canonical contracts and agent architecture

Define the dossier, citation/reference chain, plan reconciliation, evidence regimes, source intelligence, and composable agent roles. Repair MODA manifest validity and add deterministic contract validation.

**Exit gate:** repository and canonical MODA validation pass; a Change Set and Decision Records explain the structural choices.

## Batch 2 — Executable artifacts

Create machine-readable schemas and templates for brief, plan, source register, citation/reference register, evidence ledger, agent handoff, and dossier. Add cross-link validation.

**Exit gate:** valid and invalid fixtures prove the validator catches missing lineage, references, and required fields.

## Batch 3 — Orchestration core and provider adapters

Package the role protocol and master-plan/reconciliation workflow; add adapters for ChatGPT, Claude, and Gemini while preserving the same output contracts.

**Exit gate:** each adapter can produce compatible artifacts and cannot silently weaken an activation or approval gate.

## Batch 4 — Evaluation corpus

Implement and run adversarial exercises: chloroquine/COVID-19 scientific claim, AI-market bubble, U.S. responsibility in Brazil's dictatorship, and Klagenberg-family origin. Add scoring and red-team tests.

**Exit gate:** evidence-backed dossiers, evaluation records, and remediation of failed controls.

## Batch 5 — Governance and pre-release

Choose license/contribution policy, finalize documentation, configure release gates, publish a pre-release package, and schedule revalidation.

**Exit gate:** independent review evidence, approved release decision, and no unresolved critical/major finding.
