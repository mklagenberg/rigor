# Change proposal — Hypothesis-driven adaptive exhaustion

- **ID:** 2026-08-14-hypothesis-and-adaptive-exhaustion
- **Class:** normative
- **Status:** implemented
- **Base:** ca6ad95a20821128e93fd3ffed153de323f912d1

## Problem

RIGOR could record open questions and recommend next steps, but it had no contract that turned these recommendations into a bounded next iteration. It also described future forecasting separately from incomplete historical inference despite both relying on explicit, testable hypotheses.

## Decision and contract

Introduce a general hypothesis contract, research frontier, iteration journal, and adaptive exhaustion loop. Prospecting/futures becomes an application of the hypothesis mechanism. The Bundle schema advances to `0.2.0` and adds `hypotheses`, `research_frontier`, `iterations`, and a required loop policy in the plan.

## Risks and mitigations

- **Runaway loops:** finite defaults, explicit override, diminishing-return stop, WIP priority, and re-approval triggers.
- **Hypothesis laundering:** hypothesis records remain distinct from typed claims; expected traces never count as evidence.
- **Absence overreach:** coverage assessment is mandatory before a missing record weakens a hypothesis.
- **Schema breakage:** migration guidance and deterministic validation accompany the `0.2.0` bundle shape.

## Acceptance criteria

- [x] Normative process, evidence, dossier, agency, and completion contracts define the mechanism.
- [x] Schema, template, validators, and RIGOR skill carry the same fields and boundaries.
- [x] Evaluation corpus includes a hypothesis/frontier/iteration regression case and rejects an invalid frontier reference.
- [x] Existing evaluation bundles migrate to schema `0.2.0`.
- [x] Repository, skill, artifact, corpus, and MODA validation pass.

## Compatibility, migration, and recovery

`0.1.0` bundles require migration before `0.2.0` validation: add the loop policy, empty or populated registers, and at least one iteration journal entry. Consumers may preserve a legacy reader, but MUST NOT label a `0.1.0` bundle as fully conformant with this contract. Recovery is a new Change Set that retains the historical `0.2.0` decision while adjusting the future contract; published investigation artifacts are not rewritten silently.
