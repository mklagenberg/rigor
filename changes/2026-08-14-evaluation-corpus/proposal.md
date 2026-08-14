# Change proposal — Evaluation corpus

- **ID:** 2026-08-14-evaluation-corpus
- **Class:** operational
- **Status:** implemented and evaluated
- **Owner:** Mauricio M. Klagenberg
- **Base:** fcceed5ef6a35bf52af78f1a638d161468d549e2

## Decision

Create and execute four adversarial evaluation cases based on RIGOR's founding scenarios. They test methodology behavior, not a pre-approved substantive answer. Each case defines force, evidence regime, required controls, failure modes, scoring, and remediation.

## Acceptance criteria

- Cases cover scientific-method, quantitative, historical-responsibility, and genealogical-provenance regimes.
- A case cannot pass by citing authority, model consensus, or volume of links alone.
- Evaluation records preserve limitations, failures, revalidation triggers, and remediation.
- No Level 5 run passes with a zero in any dimension or a total below 12/16.

## Result

All four cases passed with scores from 13/16 to 15/16 and no zero dimensions. The aggregate record is [evaluations/summary.md](../../evaluations/summary.md).

The evaluation also exposed a recurring limitation: runs did not emit complete machine-readable research bundles. Provider portability and bundle generation therefore remain explicit Batch 5 pre-release gates rather than assumed capabilities.
