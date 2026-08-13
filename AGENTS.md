<!-- moda:disclosure:start -->
This repository is structured and audited with [MODA](https://github.com/mklagenberg/moda). MODA defines an open framework for organizing, designing, auditing, packaging, and evolving agentic methodologies.

Before changing methodology structure, read `moda.yaml`, `conformance/moda.yaml`, and the latest audit under `audits/moda/`. Do not claim conformance without evidence produced against the declared MODA version. Do not silently migrate user-authored content.
<!-- moda:disclosure:end -->

# RIGOR agent instructions

## Authority and reading order

1. Read `moda.yaml`, `SPEC.md`, and `CONSTITUTION.md`.
2. For a substantive change, read the active Change Set under `changes/`, the relevant Decision Records, and the affected operational references.
3. Run `python scripts/validate_repository.py .` after any structural, normative, or operational change. Interpret failures, correct the cause, and rerun it before handoff.
4. Never claim a release, external certification, source verification, or behavioral result without the corresponding evidence.

## Change control

- Classify changes as editorial, operational, or normative. Normative and operational changes require a Change Set in `changes/`; durable structural choices require a Decision Record.
- Update the authoritative source before projections. `SPEC.md` is normative; operational detail belongs in `docs/`.
- Do not silently weaken evidence, provenance, escalation, or human-approval requirements in a host adapter, prompt, or implementation.
- Preserve history. Do not delete accepted audits, decisions, or Change Sets; supersede them through a later artifact.

## RIGOR operating invariants

- Use RIGOR only when its activation gate is met; it is intentionally not the default for simple lookups or low-consequence explanations.
- Separate observations, source claims, derived facts, inferences, judgments, and unresolved questions.
- Preserve source identity, publication date, access date, primary evidence, conflicts, material incentives, and uncertainty.
- Match investigation depth and autonomy to consequence, reversibility, stakes, and evidence volatility.
- Human approval is mandatory before legal, medical, financial, safety-critical, reputationally harmful, or externally consequential conclusions are acted on.
- Treat model outputs as claims requiring evidence; multiple models are independent lenses, not independent evidence.

## Repository map

- `SPEC.md` — normative methodology contract.
- `docs/` — operational references, evidence model, evaluation, and governance.
- `examples/` — representative cases; illustrative rather than authoritative.
- `scripts/` — deterministic repository checks.
- `conformance/` and `audits/` — MODA mapping and audit evidence.
- `decisions/` — durable rationale.
