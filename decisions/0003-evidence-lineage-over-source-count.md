# 0003 — Evidence lineage is stronger than source count

- Status: accepted
- Date: 2026-08-13
- Decision owner: Mauricio M. Klagenberg

## Context

Many citations repeat the same press release, dataset, interview, or model output. Counting them as independent sources produces false confidence.

## Decision

RIGOR records independence groups and evaluates evidence lineage. Model agreement and secondary citation volume do not satisfy corroboration by themselves.

## Consequences

The source register and evidence ledger are required research artifacts. Level 4–5 material claims need independent corroboration or a documented exception.

## Alternatives considered

- Require a minimum citation count: rejected because it rewards duplication.
- Trust official sources without challenge: rejected because authority and evidence quality differ.

## Follow-up

Add machine-readable lineage fields to future schemas.
