#!/usr/bin/env python3
"""Validate the source registry without third-party dependencies."""

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
REGISTRY = ROOT / "references" / "sources.json"
SCHEMA = ROOT / "schemas" / "source-registry.schema.json"
REQUIRED_FIELDS = {
    "id": str,
    "authority_level": str,
    "domains": list,
    "nature_normative": str,
    "opposability": str,
    "access_mode": str,
    "citation_template": str,
    "refresh_policy": str,
    "privacy_level": str,
    "tool_adapter": str,
    "fallback_strategy": str,
    "url": str,
}
ID_PATTERN = re.compile(r"^[a-z0-9-]+$")
REQUIRED_SOURCE_IDS = {
    "legifrance",
    "jorf",
    "judilibre",
    "justice-administrative",
    "conseil-constitutionnel",
    "kali",
    "eurlex",
    "curia",
    "hudoc",
    "boss",
    "bofip",
    "cnil",
    "amf",
    "acpr",
    "autorite-concurrence",
    "inpi",
    "daj-commande-publique",
}


def load_json(path: Path, errors: list[str]):
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        errors.append(f"missing file: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    return None


def validate() -> list[str]:
    errors: list[str] = []
    schema = load_json(SCHEMA, errors)
    registry = load_json(REGISTRY, errors)
    if schema is not None and not isinstance(schema, dict):
        errors.append("source schema must contain a JSON object")
    if registry is None:
        return errors
    if not isinstance(registry, dict):
        return errors + ["registry root must be an object"]
    if not isinstance(registry.get("registry_version"), str) or not registry["registry_version"].strip():
        errors.append("registry_version must be a non-empty string")
    sources = registry.get("sources")
    if not isinstance(sources, list) or not sources:
        return errors + ["sources must be a non-empty array"]

    seen_ids: set[str] = set()
    for index, source in enumerate(sources, start=1):
        label = f"sources[{index}]"
        if not isinstance(source, dict):
            errors.append(f"{label} must be an object")
            continue
        missing = set(REQUIRED_FIELDS) - set(source)
        extra = set(source) - set(REQUIRED_FIELDS)
        if missing:
            errors.append(f"{label} missing fields: {', '.join(sorted(missing))}")
        if extra:
            errors.append(f"{label} unsupported fields: {', '.join(sorted(extra))}")
        for field, expected_type in REQUIRED_FIELDS.items():
            value = source.get(field)
            if not isinstance(value, expected_type):
                errors.append(f"{label}.{field} must be {expected_type.__name__}")
            elif expected_type is str and not value.strip():
                errors.append(f"{label}.{field} must not be empty")
        source_id = source.get("id")
        if isinstance(source_id, str):
            if not ID_PATTERN.fullmatch(source_id):
                errors.append(f"{label}.id must use lowercase ASCII letters, digits, and hyphens")
            if source_id in seen_ids:
                errors.append(f"duplicate source id: {source_id}")
            seen_ids.add(source_id)
        domains = source.get("domains")
        if isinstance(domains, list) and (
            not domains or any(not isinstance(domain, str) or not domain.strip() for domain in domains)
        ):
            errors.append(f"{label}.domains must be a non-empty array of non-empty strings")
        url = source.get("url")
        if isinstance(url, str):
            parsed = urlparse(url)
            if parsed.scheme != "https" or not parsed.netloc:
                errors.append(f"{label}.url must be an absolute HTTPS URL")
    missing_required_ids = REQUIRED_SOURCE_IDS - seen_ids
    if missing_required_ids:
        errors.append(f"missing required source ids: {', '.join(sorted(missing_required_ids))}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        for problem in problems:
            print(f"ERROR: {problem}", file=sys.stderr)
        raise SystemExit(1)
    print("Source registry is valid.")
