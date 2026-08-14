# RIGOR

**Research, Investigation, Grounding, Orchestration & Revalidation**

RIGOR is a vendor-independent agentic methodology for complex, evidence-grounded investigations. It turns an ambiguous question into an explicit research plan, coordinates multiple workstreams, tests claims against sources and incentives, and produces an information-dense **dossier** from which presentations, executive briefs, or encyclopedia entries can be derived.

It starts at investigation Levels 3–5; it is deliberately not the default for routine questions.

## What RIGOR does

- maps primary sources, authorities, specialists, communities, incentives, and interests;
- scales force from structured inquiry to adversarial investigation;
- preserves claim types, citations, complete references, lineage, dissent, and revalidation;
- records competing hypotheses and turns discriminating next steps into a finite, prioritized research frontier;
- uses models as complementary lenses, never as independent evidence;
- orchestrates composable roles for discovery, verification, challenge, synthesis, and specialist audits.

## Start here

### Practical use

- In ChatGPT Work, invoke `@rigor` or select the RIGOR skill.
- In Codex, invoke `$rigor`.
- In another compatible host, install or import [`skills/rigor`](skills/rigor/SKILL.md) and use its adapter mapping.

Example: `Use $rigor to investigate whether [claim] holds. The learning or decision goal is [goal]. Scope: [scope]. Stakes if wrong: [stakes].`

The skill classifies force, creates the master plan, tests explicit hypotheses, exhausts a bounded research frontier when permitted, spawns bounded roles when the host supports subagents, records any sequential fallback, validates the Research Bundle, and returns the dense dossier first.

### Methodology reference

1. Read [Getting started](GETTING-STARTED.md), [specification](SPEC.md), and [constitution](CONSTITUTION.md).
2. Decide activation with [proportionality](docs/activation-and-proportionality.md).
3. Read the [dossier contract](docs/dossier-and-derivations.md), [citation/reference contract](docs/citation-and-reference-contract.md), and [agent architecture](docs/agent-architecture.md).
4. Follow the batch [implementation plan](docs/implementation-plan.md).

## Status

RIGOR is in active development at `0.2.0`. It has a mapped, partial self-assessment against MODA; it does not claim external certification.

## License and contributions

RIGOR is available under the [Apache License 2.0](LICENSE). Contributions follow the [contribution policy](CONTRIBUTING.md) and require Developer Certificate of Origin 1.1 sign-off.

<!-- moda:disclosure:start -->
This repository is structured and audited with [MODA](https://github.com/mklagenberg/moda).

- Artifact profile: `methodology`
- MODA compatibility: `^1.0.0`
- Manifest: [moda.yaml](moda.yaml)
- Conformance profile: [conformance/moda.yaml](conformance/moda.yaml)
<!-- moda:disclosure:end -->
