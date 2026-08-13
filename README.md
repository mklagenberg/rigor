# RIGOR

**Research, Investigation, Grounding, Orchestration & Revalidation**

RIGOR is a vendor-independent agentic methodology for investigations where a conventional answer, a single search, or a lightweight synthesis is not enough. It turns an ambiguous question into an explicit research plan, coordinates multiple evidence-seeking workstreams, tests claims against sources and incentives, and returns a conclusion that preserves uncertainty, dissent, and a route for revalidation.

It is designed for questions involving contested evidence, volatile facts, opaque markets, communities, institutions, significant decisions, or a high cost of being wrong. It is deliberately not the default for routine questions.

## What RIGOR does

- clarifies the decision, learning goal, boundaries, and required confidence;
- discovers primary sources, data, authorities, specialists, affected communities, and incentives;
- scales effort from a bounded Level 3 inquiry to a Level 5 adversarial investigation;
- separates source claims, observations, derived facts, inferences, opinions, and judgments;
- triangulates evidence, checks provenance, tests counterclaims, and follows material incentives;
- uses multiple research engines or models as independent investigative lenses, never as independent evidence;
- produces a traceable answer with confidence, dissent, limitations, and revalidation triggers.

## Start here

1. Read [Getting started](GETTING-STARTED.md).
2. Read the normative [specification](SPEC.md) and [constitution](CONSTITUTION.md).
3. Use [the activation and proportionality guide](docs/activation-and-proportionality.md) to decide whether RIGOR applies.
4. Use [the research process](docs/research-process.md) and [evidence model](docs/evidence-model.md) to run an investigation.

## Repository map

| Need | Authoritative location |
|---|---|
| Methodology contract | [SPEC.md](SPEC.md) |
| Non-negotiable rules | [CONSTITUTION.md](CONSTITUTION.md) |
| Agent instructions | [AGENTS.md](AGENTS.md) |
| Process and artifacts | [docs/](docs/) |
| Durable rationale | [decisions/](decisions/) |
| Change control | [changes/](changes/) and [docs/change-management.md](docs/change-management.md) |
| Deterministic checks | [scripts/validate_repository.py](scripts/validate_repository.py) |
| MODA evidence | [conformance/](conformance/) and [audits/](audits/) |

## Status

RIGOR is in active development at `0.1.0`. It has a mapped, partial self-assessment against MODA; it does not claim external certification.

<!-- moda:disclosure:start -->
This repository is structured and audited with [MODA](https://github.com/mklagenberg/moda). MODA defines an open framework for organizing, designing, auditing, packaging, and evolving agentic methodologies.

- Artifact profile: `methodology`
- MODA compatibility: `^1.0.0`
- Manifest: [`moda.yaml`](moda.yaml)
- Conformance profile: [`conformance/moda.yaml`](conformance/moda.yaml)
<!-- moda:disclosure:end -->
