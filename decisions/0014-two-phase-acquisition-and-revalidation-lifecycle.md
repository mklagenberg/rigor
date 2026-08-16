# 0014 — Two-phase acquisition and revalidation lifecycle

- Status: proposed
- Date: 2026-08-16
- Decision owners: Mauricio M. Klagenberg
- Change Set: 2026-08-16-attestation-validity-and-bundle-lifecycle

## Context

RIGOR already separates revalidation from the research loop conceptually: it is a post-acceptance activity, not another exhaustion iteration, with a sentinel role and a `ready-for-revalidation` outcome. What it lacked was an output.

The gap is structural, not editorial. `scripts/validate_artifacts.py` enforces `1 <= current_iteration <= max_iterations`, so a revalidation pass cannot be recorded in `iterations` without failing validation. Nothing in the schema describes bundle versioning, supersession, or what a fired trigger actually produces. A sentinel that finds a changed claim has nowhere to write the result.

## Decision

The bundle carries `bundle_version` and a `revalidations[]` register separate from `iterations[]`. Acquisition is bounded by the loop policy and the expansion budget and produces version 1. Each revalidation entry records its trigger, date, claims re-checked, claims changed, a verdict, and the version it produces. `bundle_version` MUST equal one plus the number of recorded revalidations, and `attestation.latest_revalidation_id` MUST point at the most recent entry.

Verdicts are `confirmed`, `amended`, `superseded`, and `withdrawn`.

## Consequences

- A fired trigger has a defined output, so revalidation stops being an intention recorded in prose.
- An attestation labels the current state of the investigation rather than its original run.
- Supersession and withdrawal are recorded rather than achieved by deleting or rewriting a dossier, consistent with preserving accepted history.
- Consumers can pin a bundle version and detect that a newer one exists.

## Alternatives considered

- **Four phases: acquisition, maintenance, update, revalidation.** Rejected: maintenance and update carry no controls distinct from revalidation. They would be the same mechanism under different names, and methodologies degrade through taxonomy inflation. They are verdicts inside a revalidation, not phases.
- **Record revalidation as another loop iteration.** Rejected: it collides with the enforced iteration limit and erases the distinction between bounded acquisition and open-ended maintenance.
- **Emit a new bundle per revalidation with no link.** Rejected: lineage between versions would be lost.

## Follow-up

Define the revalidation sentinel's handoff shape and add a regression case in which a fired trigger produces an `amended` verdict.
