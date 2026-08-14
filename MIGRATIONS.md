# Migrations

## Development 0.1.0 → 0.2.0

The Bundle adds a required `plan.research_loop`, top-level `hypotheses`, `research_frontier`, and `iterations` registers.

1. Preserve the historical `0.1.0` artifact unchanged outside an approved migration copy.
2. Set `schema_version` to `0.2.0` and add the finite loop policy: maximum/current iteration, status, stop conditions, and re-approval triggers.
3. Add empty registers when no hypothesis or task was used, but add an initial iteration journal entry explaining the completed pass.
4. When a next step is material, capture it as a frontier task rather than only prose; preserve blocked and deferred tasks.
5. Run `python scripts/validate_artifacts.py BUNDLE.json` and retain the validation result with the artifact.

This is a backward-compatible capability at methodology level, but consumers MUST NOT represent an unmigrated `0.1.0` Bundle as conformant with the `0.2.0` contract.

Future migrations must state affected versions, prerequisites, exact steps, validation, recovery, and whether historical evidence needs reinterpretation.
