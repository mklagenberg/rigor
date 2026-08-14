# Host capability mapping

RIGOR is host-neutral. The portable controls remain fixed; tool names, agent APIs, storage, authentication, and interaction mechanics belong to the adapter layer.

## Capability detection

Before execution, identify whether the current host provides:

- web or database retrieval;
- document/PDF inspection;
- code or deterministic calculation;
- persistent files or structured artifacts;
- subagents, parallel tasks, or isolated contexts;
- user approval and external-action controls.

Use only capabilities actually exposed in the current session. Never claim that an agent, provider, source, or validator ran when it did not.

## Host patterns

| Host | Invocation | Agent pattern | Important constraint |
|---|---|---|---|
| ChatGPT Work | `@rigor` or skill picker | Spawn bounded subagents when available | Tool and connector access varies by workspace |
| Codex | `$rigor` | Delegate independent workstreams with subagents | Preserve filesystem and approval boundaries |
| Claude | Installed/project skill invocation | Map roles to available agent/task features | Record any missing structured-artifact support |
| Gemini | Gem/instruction or agent workflow | Reconcile Deep Research plan to RIGOR | Gemini's plan is a provider plan, not the master plan |
| Generic host | Explicit skill/prompt import | Use exposed agent primitives | Fall back transparently when a primitive is absent |

## Sequential fallback

When subagents or isolated contexts are unavailable:

1. freeze the master plan before discovery;
2. run discovery and store only its HO handoff;
3. begin verification from source records, not discovery rhetoric;
4. reset assumptions before the challenge pass and list plausible falsifiers first;
5. synthesize only after the challenge result is recorded;
6. mark `procedural_independence: limited` in the brief and limitations;
7. at Level 5, require independent human review or stop if the missing separation can materially affect safety or validity.

Sequential separation reduces contamination but does not create true independence. State that limitation plainly.

