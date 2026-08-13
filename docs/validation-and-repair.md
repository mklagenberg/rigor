# Validation and repair

## Deterministic first

Structural validation is deterministic whenever practical. Run:

```bash
python scripts/validate_repository.py .
```

The script checks required repository interfaces, mandatory MODA markers, references, and basic manifest consistency. It does not determine whether a conclusion is true or whether an investigation is sufficiently skeptical.

## Repair loop

1. run the relevant deterministic check;
2. interpret the output and identify the cause;
3. correct the authoritative artifact;
4. rerun the same check;
5. record any remaining blocker and its owner.

Do not declare a check passed from a previous run after changing an affected file.

## Human evaluation

Human review decides whether activation, level, source independence, confidence, and residual risk are justified. The reviewer must inspect evidence, not merely a model summary.
