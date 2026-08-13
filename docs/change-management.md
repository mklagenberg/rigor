# Change management

Operational and normative changes require a Change Set under `changes/<id>/` with `proposal.md` and `impact.yaml`.

Classify the change before implementation:

- **editorial:** clarifies wording without changing required behavior;
- **operational:** changes how RIGOR is executed;
- **normative:** changes a mandatory contract, invariant, profile, or compatibility expectation.

For operational or normative work, record problem, current and proposed contract, alternatives, risks, acceptance criteria, compatibility, migration, and recovery. Every affected surface is marked `updated`, `reviewed`, or `not-applicable` with rationale.

A Change Set does not replace a Decision Record. Run deterministic validation and the relevant representative evaluation before marking a Change Set implemented.
