#!/usr/bin/env python3
"""Validate the complete executable RIGOR evaluation corpus."""
from __future__ import annotations

import json
import sys
from pathlib import Path

from validate_artifacts import validate

ROOT = Path(__file__).resolve().parents[1]
BUNDLES = ROOT / "evaluations" / "bundles"
EXPECTED = {
    "01-chloroquine-covid.json",
    "02-ai-market-bubble.json",
    "03-us-brazil-dictatorship.json",
    "04-klagenberg-origin.json",
}
PROVIDERS = {"chatgpt", "claude", "gemini"}


def main() -> int:
    found = {path.name for path in BUNDLES.glob("*.json")}
    if found != EXPECTED:
        print(f"RIGOR evaluation corpus validation: FAILED\\n- expected {sorted(EXPECTED)}, found {sorted(found)}")
        return 1
    try:
        for path in sorted(BUNDLES.glob("*.json")):
            bundle = json.loads(path.read_text(encoding="utf-8"))
            validate(bundle)
            reconciliations = bundle["plan"].get("provider_reconciliation", [])
            providers = {item.get("provider") for item in reconciliations}
            if providers != PROVIDERS:
                raise ValueError(f"{path.name}: expected provider coverage {sorted(PROVIDERS)}")
            for item in reconciliations:
                if item.get("structural_state") != "compatible" or item.get("runtime_state") != "not-executed":
                    raise ValueError(f"{path.name}: provider state must be structural-only until a host run exists")
            if path.name == "04-klagenberg-origin.json":
                if not bundle["hypotheses"] or not bundle["research_frontier"] or not bundle["iterations"]:
                    raise ValueError("04-klagenberg-origin.json: must exercise hypothesis, frontier, and iteration contracts")
                if not any(task.get("status") == "ready" for task in bundle["research_frontier"]):
                    raise ValueError("04-klagenberg-origin.json: must preserve a ready next-record task")
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print(f"RIGOR evaluation corpus validation: FAILED\\n- {error}")
        return 1
    print("RIGOR evaluation corpus validation: PASSED")
    print("Static adapter coverage passed; no provider runtime execution is claimed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
