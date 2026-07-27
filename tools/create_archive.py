#!/usr/bin/env python3
"""Create and verify a deterministic ZIP archive of this repository."""

from __future__ import annotations

import argparse
import hashlib
import subprocess
import tempfile
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXED_TIMESTAMP = (1980, 1, 1, 0, 0, 0)
FILE_MODE = 0o100644


def iter_files(root: Path) -> list[Path]:
    """Return only regular files tracked by Git, in a stable order.

    Release archives must not absorb ignored local runs, temporary files, or
    untracked material that could contain prompts or provider responses.
    """

    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=root, capture_output=True, check=True
    )
    files: list[Path] = []
    for name in result.stdout.decode("utf-8").split("\0"):
        if not name:
            continue
        path = root / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"tracked path is not a regular file: {name}")
        files.append(path)
    return sorted(files, key=lambda item: item.relative_to(root).as_posix())


def create_archive(output: Path, root: Path = ROOT) -> str:
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(
        output,
        "w",
        compression=zipfile.ZIP_DEFLATED,
        compresslevel=9,
    ) as archive:
        for path in iter_files(root):
            relative = path.relative_to(root).as_posix()
            info = zipfile.ZipInfo(relative, FIXED_TIMESTAMP)
            info.create_system = 3
            info.external_attr = FILE_MODE << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, path.read_bytes())
    return sha256(output)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path)
    parser.add_argument("--check-reproducible", action="store_true")
    args = parser.parse_args()
    if args.check_reproducible:
        with tempfile.TemporaryDirectory(prefix="droit-francais-archive-") as directory:
            first = Path(directory) / "first.zip"
            second = Path(directory) / "second.zip"
            first_hash = create_archive(first)
            second_hash = create_archive(second)
            print(f"first_sha256={first_hash}")
            print(f"second_sha256={second_hash}")
            if first_hash != second_hash:
                print("ERROR: deterministic archive check failed")
                return 1
            print("Deterministic archive check passed.")
            return 0
    if not args.output:
        parser.error("--output is required unless --check-reproducible is used")
    print(f"sha256={create_archive(args.output.resolve())}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
