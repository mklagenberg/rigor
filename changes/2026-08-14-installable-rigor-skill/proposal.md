# Change proposal — Installable RIGOR orchestration skill

- **ID:** 2026-08-14-installable-rigor-skill
- **Class:** operational
- **Status:** implemented
- **Base:** 6886a0c5412811db261c43fde794546c22117ebd

## Problem

RIGOR had a portable protocol seed and host adapters, but no installable, user-facing skill that could classify force, build and reconcile the master plan, orchestrate bounded roles, preserve fallbacks, validate artifacts, and return the canonical dossier.

## Decision and contract

Add `skills/rigor` as a development package beside `skills/rigor-core`. The package contains the concise skill entrypoint, host UI metadata, activation, orchestration, artifact, and host-capability references, a Research Bundle template, and a dependency-free validator.

The skill may spawn agents only when the current host exposes that capability and the separation materially improves the investigation. It must otherwise declare the sequential fallback and its reduced procedural independence. MODA governs this change but is excluded from runtime research plans.

## Acceptance criteria

- [x] Skill initializes and validates under the platform skill contract.
- [x] Level 0–2 exclusion and Level 3–5 force controls are explicit.
- [x] Role selection, handoffs, challenge independence, and sequential fallback are explicit.
- [x] Research Bundle plus dense dossier remain canonical outputs.
- [x] Immediate citations resolve to complete references with author, title, type, venue, dates, lineage, interests, and limitations.
- [x] Portable bundle validation passes all four executable evaluation bundles.
- [x] MODA manifest, decision record, conformance profile, documentation, roadmap, changelog, and CI are synchronized.

## Compatibility, migration, and recovery

This is an additive `0.1.0` development package. Existing consumers of `rigor-core` do not need to migrate. Hosts without subagents use the declared sequential fallback. Recovery consists of removing the `rigor-skill` package mapping and installable directory while retaining the portable core and normative methodology.
