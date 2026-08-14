# Change proposal — Agent protocol and adapters

- **ID:** 2026-08-14-agent-protocol-and-adapters
- **Class:** operational
- **Status:** implemented
- **Owner:** Mauricio M. Klagenberg
- **Base:** 8f0c517e62919f1f6619c69b2033ddf3b6b19624

## Decision

Package a portable RIGOR core protocol and thin adapters for ChatGPT, Claude, and Gemini. The core produces the Research Bundle; adapters only map host capabilities and must not weaken evidence, plan-reconciliation, or human-approval gates.

## Acceptance criteria

- A role protocol declares activation, inputs, permitted actions, and standard handoff.
- Every adapter declares host limitations and preserves the bundle contract.
- No adapter authorizes external action or treats model output as evidence.
