# Attestation and validity

A RIGOR output is not automatically more accurate than an uncurated source. It is more *inspectable*. The label RIGOR emits must say the second thing, because saying the first would manufacture exactly the authority-without-lineage that RIGOR exists to refuse.

## Attestation is a process label, not a verification seal

Rigor is a property of the process; truth is a property of the claim. A dossier holds claims ranging from `supported` to `insufficient` and typed from `observation` to `judgment`. A document-level mark of correctness averages over all of them, and a `judgment` quoted out of a marked dossier would travel as verified. That defeats the typed claim ledger, which exists precisely to stop that move.

The evaluation corpus makes the point concretely: all four runs passed with a named principal limitation, and the genealogy run passed *as a calibrated non-conclusion*. A binary mark of correctness cannot describe an outcome the rubric deliberately measures as a gradient.

`attestation` therefore records only what was run:

```text
methodology, methodology_version, schema_version, bundle_id, level,
validator_status, procedural_independence, loop_status,
claim_profile {supported, contested, insufficient, other},
validity_class, latest_revalidation_id, resolves_to
```

Three rules keep it honest:

1. **It attests nothing about truth.** No field asserts that a claim is correct.
2. **It carries adverse states.** `paused-by-limit`, `procedural_independence: limited`, and a claim profile with `insufficient` counts appear in the attestation. An attestation that only exists on clean runs is a marketing badge; one that reports the bad states is a nutrition label.
3. **It must resolve.** `resolves_to` points at the bundle it labels, under the same rule that already requires every immediate citation to resolve to one complete reference. An unresolvable attestation is worthless.

Its practical value is not trust signalling. [Derived formats](dossier-and-derivations.md) MUST NOT turn an inference into a fact or hide a material qualification — a rule that existed only in prose, with nothing able to check it. The attestation is what makes that rule enforceable across a derivative.

## Validity classes decay by mechanism, not by clock

"Goes stale quickly" is a symptom; the cause is what would have to change in the world. A claim about an officeholder does not decay on a calendar, it decays when the person leaves. A claim about a statute decays on amendment. Calendar TTLs produce two errors at once: re-checking what did not change, and missing what changed early — the false-confidence window between the change and the scheduled check.

Every claim declares a `validity_class` and the `validity_trigger` that requires a re-check:

| Class | Decays when | Example trigger |
|---|---|---|
| `static` | Cannot change; only knowledge of it can | A newly inspected primary record contradicts the reading |
| `institutional` | A discrete, watchable act occurs | Amendment, appointment, merger, standard revision, archive opening |
| `consensus` | Belief accumulates or reverses | New trial, replication failure, retraction, revised guideline |
| `measured` | A known publication cadence advances | Next quarterly filing, index release, census round |
| `volatile` | Live state moves within a declared horizon | Price, position, or availability at a stated instant |

`static` does not mean "true forever". What is stable is the fact, not the investigation's knowledge of it; an archival claim can still be revised by better provenance. The class governs **what triggers a re-check**, not how much confidence the claim carries.

Only `measured` legitimately uses a calendar, because its cadence is known in advance.

## The conclusion inherits the weakest class

A conclusion is no more durable than the least durable claim it rests on. One `volatile` claim among twenty `static` ones makes the conclusion volatile. `dossier.validity_class` is therefore **derived, not asserted**: the weakest class among the claims in `dossier.claim_ids`, ordered by how long a wrong claim can survive unnoticed —

```text
static < institutional < consensus < measured < volatile
```

`institutional` sits ahead of `consensus` because a discrete act is detectable when it happens, while accumulating belief is not. `dossier.validity_driver_claim_ids` names the cited claims sitting at that weakest class, so the reader can see what is aging the conclusion.

This is computed from the ledger, so it is deterministic and validated. It also gives the attestation an expiry derived from the evidence rather than arbitrated, which addresses the main defect of any durable label: outliving its own warrant.

## Acquisition and revalidation are the only two phases

RIGOR already separates revalidation from the research loop: it is a post-acceptance activity, not another exhaustion iteration. What was missing was an output. The loop validator enforces `current_iteration <= max_iterations`, so a revalidation pass literally could not be recorded as an iteration, and nothing described bundle versioning or supersession.

Two phases carry distinct controls and are therefore modelled:

- **Acquisition** — bounded by the loop policy and the expansion budget; produces `bundle_version: 1`.
- **Revalidation** — driven by a fired trigger; appends to `revalidations[]` and produces the next `bundle_version`.

"Maintenance" and "update" are not separate phases. They would run the same mechanism under different names, and a methodology gains nothing from taxonomy inflation. They are verdicts inside a revalidation entry: `confirmed`, `amended`, `superseded`, `withdrawn`.

`bundle_version` MUST equal one plus the number of recorded revalidations, and `attestation.latest_revalidation_id` MUST point at the most recent entry, so an attestation always labels the current state rather than the original run.
