# 0011 — Rejected-alternatives register with reopening conditions

- Status: proposed
- Date: 2026-08-16
- Decision owners: Mauricio M. Klagenberg
- Change Set: 2026-08-16-decomposition-graph-and-expansion-budget

## Context

Decision Records already carry an *Alternatives considered* section, and that remains the authoritative place where a rejection is argued. But a rejection is only findable if the reader knows which record argued it. Design options rejected during methodology work therefore return, are re-argued from scratch, and consume effort that produced no new information — the same waste the research frontier exists to prevent inside an investigation.

A register on its own would create the opposite failure. A list of permanent "no" answers, with no stated condition for revisiting them, is dogma; RIGOR's whole posture is calibrated and revalidatable.

## Decision

`decisions/rejected-alternatives.md` indexes rejected design alternatives under stable `RJ-` identifiers. Each entry records the rejected option, the context, the reason, the evidence relied on, the record that argued it, and — required — a **reopening condition**: the new fact, evidence, or observed failure that would make re-discussion worthwhile.

Entries are appended, never rewritten. A reopened entry is marked `reopened` and points at the record that reopened it.

## Consequences

- A settled option can be closed by citation instead of re-argued.
- Every rejection carries its own falsifier, mirroring how an accepted conclusion carries revalidation triggers.
- The register is an index, not an authority: the Decision Record's *Alternatives considered* section remains the argued source, and the register points at it.
- A rejection whose reopening condition is met becomes a candidate for a new Change Set rather than an informal reversal.

## Alternatives considered

- **Rely only on the Alternatives considered sections.** Rejected: correct but not findable, which is what causes re-litigation.
- **A rejections folder with one file per entry.** Rejected: heavier than the content warrants; a single indexed table is scannable.
- **Record rejections without reopening conditions.** Rejected: a permanent no with no falsifier is inconsistent with the rest of the methodology.

## Follow-up

Backfill `RJ-` entries for alternatives already rejected in Decision Records `0001`–`0008` when the surrounding surface is next revised.
