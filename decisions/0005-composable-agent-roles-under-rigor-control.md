# 0005 — Composable agent roles under RIGOR control

- Status: accepted
- Date: 2026-08-14
- Owner: Mauricio M. Klagenberg
- Change Set: 2026-08-14-dossier-and-agent-architecture

## Decision

RIGOR uses named, composable methodological roles rather than a permanent monolithic agent. The RIGOR master plan is the control plane. A provider-native plan from Gemini, ChatGPT, Claude, or another system is a candidate input that must be reconciled and recorded before execution.

No role may treat another model's output as evidence, lower the investigation level, or take an external action without the controls required by RIGOR.

## Consequences

Roles can be activated only where their distinct review reduces risk. Their handoffs remain auditable and replaceable across providers.
