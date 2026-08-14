# Change proposal — Dossier and agent architecture

- **ID:** 2026-08-14-dossier-and-agent-architecture
- **Class:** normative
- **Status:** implemented
- **Owner:** Mauricio M. Klagenberg
- **Base:** 25fcb3d142de3aedd777eb5172023aba6abfd651

## Problem

RIGOR 0.1.0 describes an evidence package but does not make a dense, reusable dossier its canonical output; it also lacks a citation-to-reference contract, a reconciliation rule for vendor research plans, and an explicit architecture for composable agent roles. Its MODA component entries also omit required lifecycle metadata.

## Decision

Adopt the dossier as the canonical research artifact. Derived presentations, briefs, and encyclopedia entries are projections of it and preserve provenance for material claims. Define citation/reference, plan-reconciliation, evidence-regime, source-intelligence, and agent-role contracts. RIGOR's master plan controls the work; Gemini, ChatGPT, Claude, and other provider plans are reviewable candidates, never a silent replacement.

## Alternatives considered

- One permanent “superagent”: rejected; it hides responsibilities and applies unnecessary force.
- Treat a provider plan as canonical: rejected; it can silently lower the RIGOR level or omit a required workstream.
- Make a presentation the primary output: rejected; it loses density and auditability.

## Risks and safeguards

Role proliferation can add cost; roles are invoked only by level and evidence regime. Source profiles can turn into opaque reputational scores; profiles remain contextual, evidence-backed, and human-governed.

## Acceptance criteria

- Normative contract names the dossier, citations, references, plan reconciliation, and role controls.
- Agent roles have explicit handoffs and activation boundaries.
- MODA manifest validates against the declared immutable version.
- Local and CI validation cover the new contract surface.

## Recovery

Supersede this Change Set or revert its commit; no user data migration is required in this pre-release repository.
