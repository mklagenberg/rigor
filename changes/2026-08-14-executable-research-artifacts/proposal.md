# Change proposal — Executable research artifacts

- **ID:** 2026-08-14-executable-research-artifacts
- **Class:** operational
- **Status:** in-progress
- **Owner:** Mauricio M. Klagenberg
- **Base:** 1eb5da759c810b837f66cc3ced00ca48bcc7e5e8

## Problem

RIGOR's dossier and agent contracts are normative but not yet machine-readable. An implementation can therefore omit a claim lineage, leave a citation unresolved, or synthesize a dossier without a required handoff.

## Decision

Define a compact artifact bundle schema and templates for the brief, master plan, sources/references, claims/evidence, role handoffs, and dossier. Add deterministic validation with valid and deliberately invalid fixtures.

## Constraints

The contract must be vendor-neutral, readable without a runtime platform, and strict about traceability rather than a probabilistic quality score.

## Acceptance criteria

- Valid fixture passes; invalid fixtures fail for missing reference, invalid citation, and unsupported synthesis.
- Templates remain suitable for ChatGPT, Claude, Gemini, and programmatic hosts.
- Existing dossier and safety invariants are not weakened.

## Recovery

Remove or supersede the bundle contract; no user dossier migration is performed automatically.
