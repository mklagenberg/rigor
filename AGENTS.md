<!-- moda:disclosure:start -->
This repository is structured and audited with [MODA](https://github.com/mklagenberg/moda). Before changing methodology structure, read `moda.yaml`, `conformance/moda.yaml`, and the latest audit under `audits/moda/`.
<!-- moda:disclosure:end -->

# RIGOR agent instructions

## Authority and reading order

1. Read `moda.yaml`, `SPEC.md`, and `CONSTITUTION.md`.
2. For substantive change, read the active Change Set, relevant Decision Records, and operational references.
3. For investigation work, read the dossier, citation/reference, plan-reconciliation, and agent-architecture contracts.
4. Run `python scripts/validate_repository.py .` after structural, normative, or operational changes.

## Change control

Normative and operational changes require a Change Set; durable structural choices require a Decision Record. Update `SPEC.md` before projections. Do not weaken evidence, provenance, escalation, citations, human approval, or plan reconciliation in an adapter. Preserve accepted history.

## Operating invariants

- Use RIGOR only at Levels 3–5.
- Treat the dossier as canonical and every material citation as resolvable to a complete reference.
- Preserve source identity, publication context, dates, lineage, conflicts, incentives/interests, and uncertainty.
- Treat model outputs as claims; treat model plans as candidates that need reconciliation.
- Keep discovery, verification, challenge, and synthesis separated by explicit handoffs.
- Require human approval before external, legal, medical, financial, safety-critical, reputationally harmful, or rights-affecting action.
