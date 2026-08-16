# Change proposal — Attestation, validity classes, and bundle lifecycle

- **ID:** 2026-08-16-attestation-validity-and-bundle-lifecycle
- **Class:** normative
- **Status:** proposed
- **Owner:** Mauricio M. Klagenberg
- **Base:** the commit that completes `2026-08-16-decomposition-graph-and-expansion-budget` (linear successor; rebase before implementation)

## Problem

Three gaps, one theme: a RIGOR result cannot currently travel outside its own dossier without losing what makes it trustworthy.

**No honest label.** A RIGOR output is more inspectable than an uncurated source, which invites a durable mark asserting it was audited. That inference does not survive contact with the artifact: rigor is a property of the process, truth a property of the claim. A dossier holds claims from `supported` to `insufficient`, typed from `observation` to `judgment`; a document-level correctness mark averages over all of them and lets a `judgment` travel as verified. All four Batch 4 runs passed with a named principal limitation, and `04-klagenberg-origin` passed *as a calibrated non-conclusion*. Meanwhile `docs/dossier-and-derivations.md` forbids a derivative from turning an inference into a fact — a rule with no enforcement mechanism.

**Volatility modelled at the wrong granularity.** `revalidation.triggers` is set per dossier. A market dossier holds a quarterly figure, an archival observation, and a slow statistical regularity in one artifact; one trigger set forces a choice between re-checking everything and re-checking nothing.

**Revalidation has no output.** RIGOR already states that revalidation is a post-acceptance activity rather than another exhaustion iteration, and names a sentinel role. But `scripts/validate_artifacts.py` enforces `1 <= current_iteration <= max_iterations`, so a revalidation pass cannot be recorded in `iterations` without failing validation. Nothing describes bundle versioning or supersession. A sentinel that finds a changed claim has nowhere to write the result.

## Current and proposed contract

| Surface | Current | Proposed (`0.4.0`) |
|---|---|---|
| Output label | none | top-level `attestation` recording process state only, carrying adverse states, resolving to the bundle |
| Claim volatility | not modelled | `claims[].validity_class` and `validity_trigger`, classified by decay mechanism |
| Conclusion durability | `dossier.revalidation.triggers` prose | `dossier.validity_class` derived as the weakest cited claim class, plus `validity_driver_claim_ids` |
| `judgment` criteria | required in prose | required field |
| `derived_fact` method | required in prose | required field |
| Lifecycle | acquisition only | `bundle_version` plus a `revalidations[]` register with verdicts |

## Decision

Adopt the process attestation ([0012](../../decisions/0012-process-attestation-not-verification-seal.md)), validity classes by decay mechanism ([0013](../../decisions/0013-validity-classes-by-decay-mechanism.md)), and the two-phase acquisition/revalidation lifecycle ([0014](../../decisions/0014-two-phase-acquisition-and-revalidation-lifecycle.md)).

The attestation asserts nothing about truth, carries adverse states, and must resolve. The conclusion's validity class is derived from the ledger rather than asserted, ordered `static < institutional < consensus < measured < volatile`, so the label expires on evidence rather than on arbitration. Acquisition and revalidation are the only two phases; maintenance and update are verdicts inside a revalidation, not phases of their own.

The operational contract is [docs/attestation-and-validity.md](../../docs/attestation-and-validity.md).

## Alternatives considered

Indexed with reopening conditions in [decisions/rejected-alternatives.md](../../decisions/rejected-alternatives.md): correctness seal (RJ-009), attestation only on clean runs (RJ-010), calendar TTL (RJ-011), dossier asserting its own validity (RJ-012), four lifecycle phases (RJ-013), revalidation as a loop iteration (RJ-014).

## Risks and safeguards

- **The attestation is read as endorsement anyway.** Safeguard: no field asserts truth; the claim profile and adverse states are mandatory, and the normative text forbids presenting it as certification.
- **Conservative inheritance shortens shelf life.** One volatile claim makes the whole conclusion volatile. Safeguard: `validity_driver_claim_ids` names exactly which claims are aging the conclusion, so a reader can judge materiality; the ordering is declared as a design judgement open to challenge.
- **Class assignment becomes rote.** Safeguard: `validity_trigger` is required and must name a concrete event, publication, or cadence, which is not satisfiable by a generic value.
- **Lifecycle drift.** A bundle could accumulate revalidations without version discipline. Safeguard: `bundle_version` must equal one plus the recorded revalidations, and the attestation must point at the latest entry.

## Acceptance criteria

- Every claim declares a `validity_class` from the closed vocabulary and a non-empty `validity_trigger`.
- A `judgment` claim carries explicit criteria; a `derived_fact` claim carries a reproducible method.
- `dossier.validity_class` equals the weakest class among cited claims, and `validity_driver_claim_ids` lists exactly the cited claims at that class; a stronger asserted class fails validation.
- `attestation` fields are cross-consistent with the brief, plan, dossier, and claim ledger, and `claim_profile` matches the actual support-status counts.
- `bundle_version` equals one plus the number of recorded revalidations; `latest_revalidation_id` matches the last entry, or is null when none exists.
- `0.2.0` and `0.3.0` bundles behave exactly as before.

## Compatibility

Additive and version-gated. `semver_impact: minor`. New obligations attach to `0.4.0`. This Change Set is a linear successor to the decomposition change and MUST be rebased onto its completion commit before implementation, because `0.4.0` includes the `0.3.0` contract.

## Migration

1. Preserve the `0.3.0` artifact unchanged outside an approved migration copy.
2. Set `schema_version` to `0.4.0`, add `bundle_version: 1` and an empty `revalidations` array.
3. Assign a `validity_class` and a concrete `validity_trigger` to every claim; add `criteria` to judgments and `method` to derived facts.
4. Compute `dossier.validity_class` and `validity_driver_claim_ids` from the cited claims — do not assert them.
5. Build `attestation` from the bundle's own state, including adverse states, and set `resolves_to`.
6. Run `python scripts/validate_artifacts.py BUNDLE.json` and retain the result with the artifact.

## Implementation sequence

1. `SPEC.md` — sections 4, 7, and 11 gain the attestation, validity, and lifecycle contracts.
2. `docs/attestation-and-validity.md`; update `docs/dossier-and-derivations.md` to require the attestation on derivatives and `docs/evidence-model.md` for claim-level validity.
3. `schemas/research-bundle.0.4.0.schema.json`, `templates/research-bundle.yaml`.
4. `scripts/validate_artifacts.py` — `0.4.0` branch; mirror into `skills/rigor/scripts/`.
5. Fixtures: valid `0.4.0` bundle and the `invalid-validity-inheritance` regression.
6. `skills/rigor/` and `skills/rigor-core/` — attestation emission, class assignment, and the revalidation output shape; add the revalidation sentinel handoff.
7. `moda.yaml`, `conformance/moda.yaml`, `scripts/validate_repository.py`, CI, `CHANGELOG.md`, `MIGRATIONS.md`, `ROADMAP.md`, `UPGRADE.md`.
8. Run every command in `impact.yaml`; correct causes and rerun until clean.

## Recovery

Supersede this Change Set or revert its commit. No `0.2.0` or `0.3.0` artifact is altered, and no attestation is emitted for an artifact that has not passed validation.
