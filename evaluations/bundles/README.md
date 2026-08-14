# Executable evaluation bundles

These JSON files are machine-readable projections of the four completed evaluation dossiers. They preserve the portable RIGOR links between brief, plan, sources, claims, handoffs, and conclusion.

`python scripts/validate_evaluation_corpus.py` verifies structural validity and static coverage of the ChatGPT, Claude, and Gemini adapters. It does **not** verify source truth, reproduce calculations, or prove that any provider has executed a bundle. Every bundle therefore records `runtime_state: not-executed` until a host-specific run artifact is added.
