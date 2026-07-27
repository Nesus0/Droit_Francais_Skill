#!/usr/bin/env python3
"""Validate JSONL evaluation cases without third-party dependencies."""

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "evaluations" / "cases.jsonl"
REQUIRED_FIELDS = {"id": str, "prompt": str, "expected": list, "forbidden": list, "tags": list}
ID_PATTERN = re.compile(r"^[a-z0-9-]+$")
MINIMUM_CASES = 28
REQUIRED_COVERAGE_TAGS = {
    "source-honesty",
    "vigour",
    "temporal",
    "safety",
    "privacy",
    "prompt-injection",
    "source-hierarchy",
    "citation-fidelity",
    "jurisdiction",
    "insufficient-facts",
}


def validate_string_list(value: object, field: str, line_number: int, errors: list[str]) -> None:
    if not isinstance(value, list) or not value:
        errors.append(f"line {line_number}: {field} must be a non-empty array")
        return
    if any(not isinstance(item, str) or not item.strip() for item in value):
        errors.append(f"line {line_number}: {field} must contain only non-empty strings")


def validate() -> list[str]:
    errors: list[str] = []
    try:
        lines = CASES.read_text(encoding="utf-8").splitlines()
    except FileNotFoundError:
        return [f"missing file: {CASES.relative_to(ROOT)}"]
    seen_ids: set[str] = set()
    seen_tags: set[str] = set()
    valid_case_count = 0
    for line_number, raw_line in enumerate(lines, start=1):
        if not raw_line.strip():
            errors.append(f"line {line_number}: blank lines are not allowed")
            continue
        try:
            case = json.loads(raw_line)
        except json.JSONDecodeError as exc:
            errors.append(f"line {line_number}: invalid JSON: {exc}")
            continue
        if not isinstance(case, dict):
            errors.append(f"line {line_number}: case must be an object")
            continue
        missing = REQUIRED_FIELDS.keys() - case.keys()
        extra = case.keys() - REQUIRED_FIELDS.keys()
        if missing:
            errors.append(f"line {line_number}: missing fields: {', '.join(sorted(missing))}")
        if extra:
            errors.append(f"line {line_number}: unsupported fields: {', '.join(sorted(extra))}")
        for field, expected_type in REQUIRED_FIELDS.items():
            value = case.get(field)
            if not isinstance(value, expected_type):
                errors.append(f"line {line_number}: {field} must be {expected_type.__name__}")
            elif expected_type is str and not value.strip():
                errors.append(f"line {line_number}: {field} must not be empty")
        case_id = case.get("id")
        if isinstance(case_id, str):
            if not ID_PATTERN.fullmatch(case_id):
                errors.append(f"line {line_number}: id must use lowercase ASCII letters, digits, and hyphens")
            if case_id in seen_ids:
                errors.append(f"line {line_number}: duplicate id: {case_id}")
            seen_ids.add(case_id)
        for field in ("expected", "forbidden", "tags"):
            validate_string_list(case.get(field), field, line_number, errors)
        tags = case.get("tags")
        if isinstance(tags, list):
            seen_tags.update(tag for tag in tags if isinstance(tag, str))
        valid_case_count += 1
    if valid_case_count < MINIMUM_CASES:
        errors.append(f"at least {MINIMUM_CASES} cases are required; found {valid_case_count}")
    missing_tags = REQUIRED_COVERAGE_TAGS - seen_tags
    if missing_tags:
        errors.append(f"missing required evaluation coverage tags: {', '.join(sorted(missing_tags))}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}", file=sys.stderr)
        raise SystemExit(1)
    print("Evaluation cases are valid.")
