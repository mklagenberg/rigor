# 0013 — Validity classes by decay mechanism

- Status: proposed
- Date: 2026-08-16
- Decision owners: Mauricio M. Klagenberg
- Change Set: 2026-08-16-attestation-validity-and-bundle-lifecycle

## Context

Volatility was modelled only at dossier level, as `revalidation.triggers` with an owner. That granularity is too coarse: a market dossier holds a quarterly revenue figure, a historical archival observation, and a slow-moving statistical regularity in the same document. One trigger set for the whole artifact forces a choice between re-checking everything and re-checking nothing.

The obvious fix — a calendar time-to-live per claim — encodes the symptom instead of the cause. A claim about an officeholder does not decay on a schedule; it decays when the person leaves. A statute decays on amendment. Calendar TTLs produce two errors simultaneously: re-checking what did not change, and missing what changed early, which opens a false-confidence window between the change and the scheduled check.

## Decision

Every claim declares a `validity_class` describing its decay mechanism, plus the `validity_trigger` that requires a re-check: `static` (cannot change; only knowledge of it can), `institutional` (a discrete watchable act), `consensus` (accumulated or reversed belief), `measured` (a known publication cadence), `volatile` (live state within a declared horizon).

`dossier.validity_class` is derived, not asserted: the weakest class among the claims the conclusion cites, ordered by how long a wrong claim can survive unnoticed — `static < institutional < consensus < measured < volatile`. `dossier.validity_driver_claim_ids` names the cited claims at that class. Both are validated against the ledger.

## Consequences

- Maintenance becomes selective: a consumer re-checks the claims whose trigger fired instead of the whole dossier.
- `static` does not mean certain. What is stable is the fact, not the investigation's knowledge of it; an archival claim can still be revised by better provenance. The class governs what triggers a re-check, not confidence.
- Only `measured` legitimately uses a calendar, because its cadence is known in advance.
- One volatile claim among many static ones makes the conclusion volatile, which is deliberately conservative and will sometimes shorten a conclusion's shelf life more than a reader expects.
- The attestation gains an expiry derived from the evidence rather than arbitrated, addressing the main defect of any durable label: outliving its warrant.
- The ordering places `institutional` ahead of `consensus` because a discrete act is detectable when it happens while accumulating belief is not. This ordering is a design judgement and is a legitimate target for challenge.

## Alternatives considered

- **Calendar TTL per claim.** Rejected: encodes the symptom, and errs in both directions at once.
- **Keep volatility only at dossier level.** Rejected: too coarse for mixed-durability evidence.
- **Let the dossier assert its own validity class.** Rejected: it would permit a volatile conclusion to be presented as durable, which is the laundering this contract exists to block.
- **A numeric half-life per claim.** Rejected: false precision, and unverifiable from the ledger.

## Follow-up

Classify the corpus claims during bundle migration and check whether any class proves unassignable in practice.
