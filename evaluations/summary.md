# Evaluation corpus summary

- **Batch:** 4 — evaluation corpus
- **Run date:** 2026-08-14
- **Cases:** 4
- **Result:** 4 passes; no dimension scored zero
- **Mean score:** 14/16

## Results

| Case | Evidence regime | Score | Result | Principal limitation |
|---|---|---:|---|---|
| [01 — Chloroquine and COVID-19](runs/01-chloroquine-covid.md) | scientific and medical | 13/16 | pass | machine-readable handoff and full reproducibility package pending |
| [02 — AI market bubble](runs/02-ai-market-bubble.md) | quantitative market analysis | 14/16 | pass | uneven private-company data and no machine-readable run bundle |
| [03 — U.S. responsibility in Brazil’s dictatorship](runs/03-us-brazil-dictatorship.md) | historical provenance and responsibility | 15/16 | pass | later periods and actor-specific responsibility require separate workstreams |
| [04 — Klagenberg family origin](runs/04-klagenberg-origin.md) | genealogy, onomastics, and provenance | 14/16 | pass by calibrated non-conclusion | original record images and a continuous kinship chain remain pending |

## What the corpus validated

1. **Claim decomposition changes the answer.** Treatment efficacy, market bubbles, historical responsibility, and family origin each contained multiple distinct claims that required different evidence.
2. **Authority is not evidence lineage.** Official, scientific, corporate, archival, and community sources were useful only after identifying what they could directly establish, their custody, method, incentives, and dependence.
3. **Source count is not independence.** Repeated claims in articles, reports, databases, or genealogy trees may descend from one original source.
4. **Counterevidence must be planned.** Each run tested credible alternatives and overbroad framings instead of collecting only confirming material.
5. **A qualified or negative conclusion can pass.** The genealogy case correctly stopped before inventing a family origin; the market case rejected a single categorical answer for a heterogeneous market.
6. **Conclusions require revalidation triggers.** Every passing run stated what new evidence, time change, or scope expansion could alter the result.

## Recurring weakness

All four runs preserve plans, limitations, and remediation in narrative form, but none emits the complete machine-readable research bundle defined by the Batch 2 schema. This explains every score of 1 in **Handoffs/plan control** and prevents the corpus from yet proving end-to-end artifact portability across ChatGPT, Claude, and Gemini.

## Required remediation before release

- Create at least one complete machine-readable bundle for each evidence regime represented in the corpus.
- Validate every bundle against `schemas/research-bundle.schema.json` and cross-reference rules.
- Add regression fixtures for source-copy dependence, missing counterevidence, overbroad quantitative denominators, and unsupported genealogical links.
- Execute the same bounded case through each provider adapter and compare artifact compatibility, not prose similarity.
- Preserve failed or downgraded runs as regression evidence instead of rewriting history.
- Obtain independent review of scores and conclusion calibration before a pre-release decision.

## Batch decision

**Batch 4 exit gate: passed with remediation carried into Batch 5.**

The corpus demonstrates that RIGOR’s core controls behave across four materially different evidence regimes. It does not yet demonstrate provider portability or complete machine-readable execution. Those are explicit pre-release gates, not reasons to discard the evaluation results.
