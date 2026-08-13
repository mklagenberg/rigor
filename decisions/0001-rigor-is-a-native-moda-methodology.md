# 0001 — RIGOR is a native MODA methodology

- Status: accepted
- Date: 2026-08-13
- Decision owner: Mauricio M. Klagenberg

## Context

RIGOR needs to coordinate multiple research processes, methods, evidence models, and future agent implementations. A prompt or a single workflow would not capture its end-to-end contracts and governance.

## Decision

RIGOR is a `methodology` profile designed natively with MODA `^1.0.0`. It declares a mapped, partial conformance state until audit evidence supports a stronger claim.

## Consequences

The repository maintains a normative specification, agent entry point, manifest, Change Sets, Decision Records, deterministic validation, and audit evidence.

## Alternatives considered

- A prompt collection: rejected because it cannot govern proportionality, evidence lineage, or evolution.
- A framework only: rejected because RIGOR prescribes an end-to-end outcome path.

## Follow-up

Build portable skills and evaluation cases before a stable release.
