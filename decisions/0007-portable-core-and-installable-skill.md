# 0007 — Portable core and installable orchestration skill

- Status: accepted
- Date: 2026-08-14
- Owner: Mauricio M. Klagenberg
- Change Set: 2026-08-14-installable-rigor-skill

## Decision

Keep `skills/rigor-core` as the small, host-neutral embedded protocol and publish `skills/rigor` as the user-facing installable orchestration skill. The installable package may map RIGOR roles to host-provided subagents, tools, files, and approvals, but it cannot change the activation levels, evidence lineage, role separation, challenge, artifact, human-decision, or revalidation contracts.

When isolated subagents are unavailable, the skill uses a declared sequential fallback. That fallback preserves role order and handoffs but must not be presented as independent review. Level 5 work requires stronger human review or a stop when missing separation is material.

MODA remains the methodology lifecycle and packaging framework. It is not a RIGOR research role and must never be instantiated inside an investigation.

## Rationale

A compact core supports portability and embedding. A richer installable skill gives users a practical invocation surface, host detection, agent orchestration, progressive reference loading, deterministic bundle validation, and a dense dossier contract. Keeping these layers separate prevents host mechanics from redefining the methodology.

## Consequences

- Users can invoke RIGOR directly through supported skill interfaces.
- ChatGPT, Codex, Claude, Gemini, and generic hosts can map the same role contract to different execution primitives.
- Agent count is not treated as evidence independence; source lineage remains the unit of corroboration.
- Runtime adapter compatibility and independent review remain pre-release gates.
- Package updates are explicit and version-aware; installed skills do not silently update themselves.
