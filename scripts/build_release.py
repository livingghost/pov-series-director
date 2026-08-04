#!/usr/bin/env python3
"""Build and verify a deterministic release ZIP."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import subprocess
import sys
import tempfile
import tomllib
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_manifest() -> dict:
    with (ROOT / "package-manifest.toml").open("rb") as handle:
        return tomllib.load(handle)


def included_files(manifest: dict) -> list[Path]:
    excluded_names = set(manifest["release"].get("exclude_names", []))
    files: set[Path] = set()
    for rel in manifest["release"]["include"]:
        path = ROOT / rel
        if path.is_file():
            files.add(path)
        elif path.is_dir():
            for child in path.rglob("*"):
                if child.is_file() and not any(part in excluded_names for part in child.parts):
                    files.add(child)
        else:
            raise FileNotFoundError(path)
    output = ROOT / manifest["release"]["output"]
    files.discard(output)
    files.discard(output.with_suffix(output.suffix + ".sha256"))
    return sorted(files, key=lambda p: p.relative_to(ROOT).as_posix())


def write_zip(output: Path, manifest: dict) -> None:
    version = manifest["package"]["version"]
    prefix = f"pov-series-director-{version}"
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for path in included_files(manifest):
            rel = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(f"{prefix}/{rel}", date_time=(1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = (0o755 if path.suffix == ".py" else 0o644) << 16
            archive.writestr(info, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_zip(output: Path, manifest: dict) -> None:
    version = manifest["package"]["version"]
    prefix = f"pov-series-director-{version}"
    with tempfile.TemporaryDirectory() as tmp:
        tmp_path = Path(tmp)
        with zipfile.ZipFile(output) as archive:
            bad = archive.testzip()
            if bad:
                raise RuntimeError(f"corrupt ZIP member: {bad}")
            archive.extractall(tmp_path)
        extracted = tmp_path / prefix
        subprocess.run([sys.executable, "scripts/validate_skill.py"], cwd=extracted, check=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--skip-extracted-validation", action="store_true")
    args = parser.parse_args(argv)

    manifest = load_manifest()
    subprocess.run([sys.executable, "scripts/build_demo.py", "--check"], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "scripts/build_flat.py"], cwd=ROOT, check=True)
    subprocess.run([sys.executable, "scripts/validate_skill.py"], cwd=ROOT, check=True)

    output = ROOT / manifest["release"]["output"]
    write_zip(output, manifest)
    if not args.skip_extracted_validation:
        verify_zip(output, manifest)

    checksum = sha256(output)
    checksum_path = output.with_suffix(output.suffix + ".sha256")
    checksum_path.write_text(f"{checksum}  {output.name}\n", encoding="utf-8")
    print(f"wrote {output.relative_to(ROOT)} ({output.stat().st_size:,} bytes)")
    print(f"sha256 {checksum}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
