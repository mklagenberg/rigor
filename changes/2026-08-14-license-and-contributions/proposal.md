# Change proposal — License and contribution policy

- **ID:** 2026-08-14-license-and-contributions
- **Class:** normative
- **Status:** implemented
- **Base:** 303b46954d43b85b39b5b154bd2cf3026d3d217c

## Problem

RIGOR declared `NOASSERTION` and had no contribution contract. Use, redistribution, patent rights, and contributor authority were therefore unresolved pre-release gates.

## Decision and contract

Adopt Apache License 2.0 and require DCO 1.1 sign-off for contributions. Document contributor workflow, rights, evidence expectations, privacy boundaries, and validation gates in `CONTRIBUTING.md`.

## Alternatives

- MIT: simpler, but lacks Apache-2.0's explicit patent grant and termination provision.
- Reciprocal/copyleft license: stronger downstream sharing obligation, but unnecessarily restricts adoption for the current project goals.
- Project-specific CLA: higher administrative burden without a demonstrated need.

## Risks

- Contributors may submit material they do not control: mitigated by DCO, review, and explicit provenance rules.
- Users may infer trademark or certification rights: Apache-2.0 does not grant them, and RIGOR continues to reject unsupported certification claims.
- Legal text may drift: the `LICENSE` file uses the unmodified Apache-2.0 text.

## Acceptance criteria

- [x] Root `LICENSE` contains Apache License 2.0.
- [x] `CONTRIBUTING.md` defines DCO sign-off and quality gates.
- [x] Manifest, README, roadmap, changelog, conformance map, validator, and Decision Record are synchronized.
- [x] Repository, artifact, corpus, and MODA validation pass.

## Compatibility, migration, and recovery

This is the first asserted repository license; no earlier licensed release is being relicensed. Existing unpublished adopters must review Apache-2.0 before redistribution. Recovery requires a new owner decision and explicit legal review; published release licenses cannot be silently withdrawn.
