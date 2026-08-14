---
name: rigor
description: Plan, execute, challenge, and revalidate Level 3–5 investigations as traceable Research Bundles and dense dossiers. Use for contested, consequential, multi-source, incentive-laden, scientific, quantitative, historical, genealogical, market, or community questions where ordinary retrieval is insufficient; for research-plan reconciliation across ChatGPT, Gemini, Claude, or other research engines; and when claims need typed evidence, source lineage, counterevidence, interest mapping, specialist audits, or independent agent roles. Do not use for simple Level 0–2 lookup, explanation, or bounded synthesis.
---

# RIGOR

Run evidence-grounded investigations without confusing source volume, authority, or model agreement with proof. Produce a machine-readable Research Bundle and a dense dossier as the canonical outputs; derive lighter formats only afterward.

## Load the operating references

Read these files before execution:

1. `references/activation.md` to classify force and escalation.
2. `references/orchestration.md` before creating workstreams or subagents.
3. `references/artifacts.md` before writing claims, citations, references, or the dossier.
4. `references/host-capabilities.md` when mapping the plan to a host, provider, or sequential fallback.

Read `manifest.yaml` on first activation in a session. Report an update or security warning if one is known. Never silently change the installed methodology. If version status cannot be checked, continue with the installed version and record `version_status: unknown` or `offline` in the brief.

## Execute the investigation

1. Frame the question, intended learning or decision, scope, exclusions, time/jurisdiction, stakes, permissions, and decision owner. Ask only for missing choices that materially alter the work.
2. Classify Level 0–5. Exit RIGOR at Levels 0–2 and answer proportionately. Do not lower an assigned Level 3–5 without a recorded rationale.
3. Identify applicable evidence regimes: general, scientific-critical, quantitative-audit, historical-provenance, genealogy/identity-resolution, interests-and-disclosure, community-practice, or another explicitly defined regime.
4. Create one RIGOR master plan with bounded workstreams, evidence targets, role owners, tool/data permissions, stop conditions, challenge routes, and revalidation triggers.
5. Reconcile any ChatGPT, Gemini, Claude, or other host-native deep-research plan against the master plan. Adopt useful retrieval tactics, but do not allow a provider plan to replace RIGOR's controls.
6. Select the smallest role set that preserves independence. Spawn subagents only when the host exposes that capability and separate context or parallel work materially reduces shared blind spots. Otherwise use the documented sequential fallback and mark independence as limited.
7. Require every role to return an HO handoff containing work performed, deviations, claim IDs, source IDs, gaps, limitations, confidence rationale, and recommended next action.
8. Verify source identity, provenance, method, incentives/interests, dependencies, and claim support. Search deliberately for counterevidence and credible alternative explanations. No role validates its own discovery.
9. Synthesize only ledger-backed claims. Distinguish observation, source claim, derived fact, inference, judgment, and open question. Preserve conflicts and non-conclusions.
10. Emit the Research Bundle JSON and dense dossier. Run `python scripts/validate_bundle.py BUNDLE.json` and repair traceability failures before declaring completion.
11. State conclusion, confidence rationale, limitations, unresolved questions, and revalidation owner/triggers. Stop for human direction before consequential external use.

## Maintain control boundaries

- User approval covers the agreed scope, force, cost, permissions, and output. Do not request approval for every internal role handoff.
- Re-approval is required for material scope/cost expansion, new sensitive data, new permissions, external actions, or high-stakes application.
- Do not publish, contact, accuse, purchase, trade, diagnose, prescribe, or make a binding decision on the user's behalf.
- Treat model output, community consensus, official publication, peer review, and corporate disclosure as evidence inputs with different failure modes—not automatic truth.
- Map economic incentives and less explicit interests. Separate an organization's investor filing, technical documentation, marketing page, commissioned report, and employee/community statement.
- Count independent evidence lineages, not repeated links or copied claims.
- MODA governs the design and evolution of this skill. Never instantiate MODA as a research role or include it in an investigation plan.

## Deliverables

Return, in this order unless the user asks otherwise:

1. scope and force decision;
2. concise execution summary and important plan deviations;
3. dense dossier with claim labels and immediate citations;
4. complete references with author/organization, title, source type, venue/place, publication date, locator/URL, access date, status, lineage, incentives, and limitations;
5. Research Bundle file or embedded JSON;
6. limitations, open questions, and revalidation triggers;
7. optional derived formats linked back to the dossier.

If the evidence does not justify an answer, deliver a calibrated non-conclusion and the next-record plan. That is a successful RIGOR outcome.

