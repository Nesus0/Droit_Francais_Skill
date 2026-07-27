#!/usr/bin/env python3
"""Validate public repository content without claiming to scrub Git history."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ALLOWED_EMAILS = {"Nesus0@users.noreply.github.com"}
EMAIL_PATTERN = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
FORBIDDEN_PATTERNS = {
    "local path": re.compile("/" + "Users/|/" + "home/|C:" + "\\\\" + "Users" + "\\\\"),
    "private key": re.compile(r"BEGIN (?:RSA|OPENSSH|EC) PRIVATE KEY"),
    "GitHub token": re.compile(r"(?:ghp_|github_pat_)[A-Za-z0-9_]{20,}"),
    "OpenAI-style key": re.compile(r"sk-[A-Za-z0-9]{20,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
}
REQUIRED_FILES = {
    "GOVERNANCE.md",
    "OPEN_SOURCE_READINESS.md",
    "GITHUB_PUBLIC_SURFACE_AUDIT.md",
    "LICENSE_AND_REUSE_AUDIT.md",
    "DESIGN_AND_USABILITY_AUDIT.md",
    ".github/ISSUE_TEMPLATE/legal-error.yml",
    ".github/ISSUE_TEMPLATE/feature-request.yml",
    ".github/pull_request_template.md",
}


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True
    )
    return [ROOT / item for item in result.stdout.decode().split("\0") if item]


def validate_links(path: Path, text: str, errors: list[str]) -> None:
    for target in re.findall(r"\[[^]]+\]\(([^)]+)\)", text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        destination = target.split("#", 1)[0]
        if destination and not (path.parent / destination).exists():
            errors.append(f"{path.relative_to(ROOT)}: broken relative link {destination}")


def validate(include_history: bool) -> list[str]:
    errors: list[str] = []
    for required in REQUIRED_FILES:
        if not (ROOT / required).is_file():
            errors.append(f"missing public governance file: {required}")
    for path in tracked_files():
        if path.is_symlink():
            errors.append(f"tracked symbolic link: {path.relative_to(ROOT)}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for email in EMAIL_PATTERN.findall(text):
            if email not in ALLOWED_EMAILS:
                errors.append(f"{path.relative_to(ROOT)}: non-allowed email address")
        for label, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(text):
                errors.append(f"{path.relative_to(ROOT)}: possible {label}")
        if path.suffix == ".md":
            validate_links(path, text, errors)
        if path.suffix in {".yml", ".yaml"}:
            for action in re.findall(r"^\s*-\s*uses:\s*[^@\s]+@([^\s#]+)", text, re.MULTILINE):
                if not re.fullmatch(r"[0-9a-f]{40}", action):
                    errors.append(f"{path.relative_to(ROOT)}: action is not pinned to a full SHA")
    if include_history:
        result = subprocess.run(
            [
                "git",
                "log",
                "--branches",
                "--tags",
                "--format=%an%x00%ae%x00%cn%x00%ce",
            ],
            cwd=ROOT,
            capture_output=True,
            check=True,
        )
        for record in result.stdout.decode().splitlines():
            fields = record.split("\0")
            if len(fields) == 4 and (fields[0] != "Nesus0" or fields[2] != "Nesus0" or fields[1] not in ALLOWED_EMAILS or fields[3] not in ALLOWED_EMAILS):
                errors.append("Git history contains non-allowed author or committer metadata")
                break
        tags = subprocess.run(
            [
                "git",
                "for-each-ref",
                "--format=%(taggername)%00%(taggeremail:trim)",
                "refs/tags",
            ],
            cwd=ROOT,
            capture_output=True,
            check=True,
        )
        for record in tags.stdout.decode().splitlines():
            name, _, email = record.partition("\0")
            if name and (name != "Nesus0" or email not in ALLOWED_EMAILS):
                errors.append("Git tags contain non-allowed tagger metadata")
                break
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--include-history", action="store_true")
    args = parser.parse_args()
    errors = validate(args.include_history)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Public repository content is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
