# 0012 — Process attestation, not a verification seal

- Status: proposed
- Date: 2026-08-16
- Decision owners: Mauricio M. Klagenberg
- Change Set: 2026-08-16-attestation-validity-and-bundle-lifecycle

## Context

A RIGOR output is more inspectable than an uncurated source, which invites a durable mark asserting that its content was audited and is therefore reliable. That inference does not survive contact with the artifact.

Rigor is a property of the process; truth is a property of the claim. A dossier holds claims from `supported` to `insufficient`, typed from `observation` to `judgment`. A document-level mark of correctness averages over all of them, and a `judgment` quoted out of a marked dossier would travel as verified — the exact laundering the typed claim ledger exists to prevent.

The corpus makes it concrete. All four Batch 4 runs passed with a named principal limitation, and `04-klagenberg-origin` passed *as a calibrated non-conclusion*. A binary mark cannot describe an outcome the rubric measures as a gradient. RIGOR also instructs that official publication and peer review are evidence inputs with distinct failure modes rather than automatic truth; a correctness seal would manufacture one more such input.

Separately, `docs/dossier-and-derivations.md` already forbids a derivative from turning an inference into a fact or hiding a material qualification. That rule had no enforcement mechanism.

## Decision

The bundle carries a top-level `attestation` that records only what was run: methodology and version, schema version, bundle ID, level, validator status, procedural independence, loop status, the claim profile by support status, the derived validity class, the latest revalidation, and a locator.

Three constraints are normative. The attestation asserts nothing about truth. It carries adverse states — `paused-by-limit`, `procedural_independence: limited`, and non-zero `insufficient` counts appear in it. And it MUST resolve to the bundle it labels, under the rule that already requires every citation to resolve to a complete reference.

## Consequences

- The label is falsifiable and machine-checkable; its fields are cross-validated against the ledger they summarize.
- An attestation that appears only on clean runs would be a marketing badge; carrying the adverse states makes it a nutrition label instead.
- Derivative integrity becomes checkable, which is the attestation's real purpose: preventing decontextualized reuse rather than signalling trust.
- The attestation does not raise any claim's support status and MUST NOT be presented as certification.

## Alternatives considered

- **A correctness seal ("audited by RIGOR vX").** Rejected: wrong granularity, defeats the claim ledger, and is contradicted by passing non-conclusions.
- **A seal emitted only on clean runs.** Rejected: it becomes a badge, and RIGOR does not erase `blocked` or `paused-by-limit` states.
- **A score or grade.** Rejected: it recreates a single-number authority over heterogeneous claims.
- **No label at all.** Rejected: the existing derivative rule has no other enforcement path.

## Follow-up

Define the human-readable rendering of the attestation for derived formats, and add a regression case in which a derivative quotes a `judgment` as fact.
