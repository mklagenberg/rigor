# Executable research artifacts

RIGOR's portable interchange unit is the **Research Bundle**, defined by [the JSON Schema](../schemas/research-bundle.schema.json) and [YAML template](../templates/research-bundle.yaml).

## IDs and links

- Sources use `SR-`; claims use `CL-`; plans use `PLAN-`; handoffs use `HO-`; dossiers use `DOS-`.
- Every cited source ID must exist exactly once in `sources`.
- Every handoff claim and source ID must exist in the corresponding register.
- The dossier's plan and claim IDs must resolve within the same bundle.

The bundle validates traceability and required shape. It does not certify a source, a calculation, or a conclusion as true.

## Minimal portability

The format is data-only and has no vendor/model field. A host adapter may add fields but MUST preserve this core and MAY NOT erase required relationships. Provider-plan reconciliation is recorded under `plan.provider_reconciliation`.

## Evaluation corpus

The representative bundles live under [`evaluations/bundles/`](../evaluations/bundles/). Run `python scripts/validate_evaluation_corpus.py` to validate all four against the portable core and require a static adapter entry for ChatGPT, Claude, and Gemini.

Static coverage proves only that each adapter is mapped to the same core contract. A provider is **not executed** until a host-specific run produces an inspectable bundle and reconciliation record.
