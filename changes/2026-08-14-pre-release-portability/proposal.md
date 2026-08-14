# Change proposal — Executable evaluation corpus and portability evidence

- **ID:** 2026-08-14-pre-release-portability
- **Class:** operational
- **Status:** implemented except for provider runtime execution and licensing
- **Base:** 7519f9d0d60152baf8a4b2172abeb39c47fbcbf6

## Problem

Batch 4 demonstrated RIGOR through narrative dossiers, but did not prove that their source, claim, handoff, plan, and dossier relationships can move as portable data. The adapters also existed only as guidance, not as a testable compatibility boundary.

## Proposed contract

Each completed evaluation has a JSON Research Bundle under `evaluations/bundles/`. A deterministic corpus validator validates every bundle and checks that each records the three supported host adapters as **structurally compatible, runtime not executed**. This is deliberately weaker than a provider-run claim.

## Alternatives

- Treat the Markdown dossiers as sufficient: rejected; narrative does not prove machine-readable linkage.
- Claim cross-provider execution from adapter prose: rejected; no run occurred in Claude or Gemini.
- Delay all work until license selection: rejected; data portability and license policy are separable.

## Risks and controls

- Bundle drift from the dossier: each bundle links to its run and the corpus validator requires the full case set.
- False portability claim: runtime state is required to remain `not-executed` until evidence of a real host run exists.
- Source truth mistaken for schema validity: validator states it checks shape and links only.

## Acceptance criteria

- [x] Four evaluation bundles validate against the Research Bundle contract.
- [x] Deterministic corpus validation checks all four cases and static adapter coverage.
- [x] Documentation distinguishes structural compatibility from executed provider evidence.
- [ ] Run a bounded bundle in ChatGPT, Claude, and Gemini and record resulting artifacts.
- [ ] Decide license and contribution policy before pre-release.

## Compatibility, migration, and recovery

The existing `0.1.0` bundle schema is unchanged. No adopter migration is required. Remove an incorrect bundle and restore the affected run to narrative-only status; do not alter accepted run history.
