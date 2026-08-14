# Contributing to RIGOR

RIGOR accepts corrections, evidence-model improvements, evaluation cases, validators, adapters, and documentation contributions that preserve its traceability and safety invariants.

## Before contributing

1. Read [AGENTS.md](AGENTS.md), [SPEC.md](SPEC.md), and [CONSTITUTION.md](CONSTITUTION.md).
2. Open or reference an issue for changes that alter behavior, public contracts, schemas, adapters, packaging, or governance.
3. Add a Change Set under `changes/<id>/` for operational or normative work. Add a Decision Record for a durable structural choice.
4. Do not include secrets, private personal data, confidential sources, or material you do not have the right to contribute.

## Pull-request expectations

- Keep the change focused and explain its problem, evidence, trade-offs, and remaining limitations.
- Preserve source lineage, claim typing, citation-to-reference resolution, uncertainty, challenge passes, and human approval gates.
- Update the authoritative contract before derived adapters or examples.
- Add deterministic validation or regression evidence whenever the property is mechanically testable.
- Run the repository, artifact, evaluation-corpus, and affected MODA checks.
- Do not present a self-audit, model judgment, or passing schema check as proof that a substantive conclusion is true.

## Developer Certificate of Origin

RIGOR uses the [Developer Certificate of Origin 1.1](https://developercertificate.org/) instead of a contributor license agreement. By signing off a contribution, you certify that you have the right to submit it under this repository's [Apache License 2.0](LICENSE).

Add this line to every commit message, using your real name and an email address you control:

```text
Signed-off-by: Your Name <your.email@example.com>
```

Git can add the sign-off with `git commit -s`. A maintainer may ask for a corrected commit when the sign-off is absent; sign-off does not replace authorship, review, or repository validation.

## Review and acceptance

Maintainers may request changes for scope, evidence quality, compatibility, privacy, safety, provenance, or maintainability. Submission does not guarantee acceptance. Accepted contributions are licensed under Apache-2.0 as described in the repository license.
