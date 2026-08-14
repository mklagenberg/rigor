# Orchestration protocol

The orchestrator owns the brief, master plan, hypothesis and frontier registers, bundle state, role boundaries, escalation decisions, loop policy, and stop conditions. It does not treat agent agreement as corroboration.

## Role catalog

| Role | Responsibility | Prohibited shortcut |
|---|---|---|
| Orchestrator | Frame, plan, reconcile, assign, integrate, escalate | Replacing evidence with model judgment |
| Source discovery | Find candidate sources and upstream origins | Validating its own discoveries |
| Evidence verifier | Inspect provenance, method, lineage, independence, and claim fit | Counting source quantity as independence |
| Challenger | Seek counterevidence, alternative explanations, and falsifiers | Repeating the main search with an adversarial tone |
| Dossier synthesizer | Build ledger-backed dossier and references | Inventing or upgrading unsupported claims |
| Scientific-method auditor | Audit design, endpoints, bias, statistics, replication, synthesis | Treating peer review as sufficient validation |
| Quantitative auditor | Audit numerator, denominator, baseline, period, missingness, revisions, and charts | Accepting headline percentages without reconstruction |
| Provenance auditor | Audit custody, authenticity, chronology, identity, and record chain | Treating an index or copy as the original record |
| Interests analyst | Map funding, ownership, mandates, career, political, and reputational interests | Equating an interest with proof of falsehood |
| Revalidation sentinel | Watch defined triggers after acceptance | Monitoring without an owner or decision rule |
| Hypothesis and frontier controller | Maintain alternatives, discriminating tests, task priorities, and iteration decisions | Treating a hypothesis or next step as evidence |

## Role selection by force

- **Level 3:** orchestrator, discovery/verifier separation, synthesizer; challenger when uncertainty remains. One agent may run sequential roles only if the fallback limitation is declared.
- **Level 4:** distinct discovery, verification, challenge, and synthesis contexts; add every triggered specialist. Parallelize independent workstreams where useful.
- **Level 5:** use separate agents for material workstreams, an independent challenger, and specialist auditors. If subagents are unavailable, explicitly downgrade procedural independence and require stronger human review or stop.

Do not spawn a role merely to increase agent count. Several agents reading the same sources from the same prompt are not independent evidence.

## Subagent task contract

Give each subagent only the context necessary for its bounded role:

```text
Role:
Question and workstream:
Evidence target:
Permitted tools/data:
Bundle inputs:
Independence constraints:
Stop condition:
Required HO handoff fields:
```

Each HO handoff must return:

```text
handoff_id, role, work_performed, deviations,
claim_ids, source_ids, gaps, limitations,
confidence_rationale, recommended_next_action
```

Keep discovery and challenge contexts separated when independence matters. The challenger receives the claim map and evidence ledger, but should not inherit persuasive narrative that is irrelevant to testing the claims.

## Adaptive loop control

The controller may continue to the next iteration without a new user turn only when the task is already within the approved scope, cost, data/tools, and permissions. It must obey the configured maximum and stop early when no material, discriminating frontier task remains. Defaults are 2 iterations at Level 3, 3 at Level 4, and 4 at Level 5, including the initial pass.

Re-approval is required for a material expansion, new sensitive/private/paid access, new permission, contact, or any external action. `exhausted-within-scope`, `blocked`, `paused-by-limit`, `ready-for-revalidation`, and `escalated` are explicit outcomes. Revalidation is a separate post-acceptance activity, not another exhaustion-loop iteration.

## Plan reconciliation

For each host-native or provider-generated plan, record:

```text
provider | adopted step | changed step | rejected step | rationale
```

Provider plans may contribute search tactics, source access, extraction, translation, or domain coverage. They may not remove RIGOR's level gate, evidence lineage, role separation, challenge pass, artifact contract, approval boundary, or revalidation plan.
