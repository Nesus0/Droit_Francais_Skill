#!/usr/bin/env python3
"""Run the repository-local, non-provider adapter compatibility matrix."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "evaluations" / "adapter-matrix.json"


def validate() -> list[str]:
    errors: list[str] = []
    try:
        matrix = json.loads(MATRIX.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        return [f"cannot load matrix: {exc}"]
    if not isinstance(matrix, dict) or not isinstance(matrix.get("adapters"), list):
        return ["matrix.adapters must be an array"]
    seen: set[str] = set()
    for entry in matrix["adapters"]:
        if not isinstance(entry, dict):
            errors.append("adapter entry must be an object")
            continue
        adapter_id = entry.get("id")
        if not isinstance(adapter_id, str) or not adapter_id:
            errors.append("adapter id must be a non-empty string")
            continue
        if adapter_id in seen:
            errors.append(f"duplicate adapter id: {adapter_id}")
        seen.add(adapter_id)
        base = ROOT / str(entry.get("path", ""))
        for relative in entry.get("required_files", []):
            path = ROOT / relative
            if not path.is_file():
                errors.append(f"{adapter_id}: missing required file {relative}")
        prompt = entry.get("canonical_prompt")
        if not isinstance(prompt, str) or not (ROOT / prompt).is_file():
            errors.append(f"{adapter_id}: canonical prompt is missing")
        status = entry.get("expected_status")
        if status != "PRESENT_NOT_EXECUTED":
            errors.append(f"{adapter_id}: unexpected status {status!r}")
        if not base.is_dir():
            errors.append(f"{adapter_id}: adapter directory is missing")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args()
    errors = validate()
    if args.json_output:
        print(json.dumps({"ok": not errors, "errors": errors}, ensure_ascii=True))
    else:
        if errors:
            for error in errors:
                print(f"ERROR: {error}")
        else:
            print("Adapter matrix is valid; provider behavior was not executed.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
