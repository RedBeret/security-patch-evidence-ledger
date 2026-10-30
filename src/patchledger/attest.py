"""SHA-256 manifests for generated evidence packages."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path
from typing import Iterable

from .core import EvidenceError


LINE_RE = re.compile(r"^([0-9a-f]{64})  ([^\r\n]+)$")


def _digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def write_manifest(files: Iterable[Path], destination: Path) -> Path:
    items = sorted((Path(path) for path in files), key=lambda path: path.name.casefold())
    if not items:
        raise EvidenceError("manifest: at least one file is required")
    names = [path.name for path in items]
    if len(set(name.casefold() for name in names)) != len(names):
        raise EvidenceError("manifest: duplicate file names are not allowed")
    if any(not path.is_file() for path in items):
        raise EvidenceError("manifest: every input must be an existing file")
    destination.write_text("".join(f"{_digest(path)}  {path.name}\n" for path in items), encoding="utf-8", newline="\n")
    return destination


def verify_manifest(manifest: Path) -> tuple[Path, ...]:
    root = manifest.resolve().parent
    verified: list[Path] = []
    seen: set[str] = set()
    for line_number, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        match = LINE_RE.fullmatch(line)
        if not match:
            raise EvidenceError(f"manifest line {line_number}: expected '<sha256>  <file>'")
        expected, name = match.groups()
        candidate = Path(name)
        if candidate.is_absolute() or len(candidate.parts) != 1 or name in {".", ".."}:
            raise EvidenceError(f"manifest line {line_number}: paths must be plain file names")
        folded = name.casefold()
        if folded in seen:
            raise EvidenceError(f"manifest line {line_number}: duplicate file name")
        seen.add(folded)
        path = root / name
        if not path.is_file() or _digest(path) != expected:
            raise EvidenceError(f"manifest line {line_number}: checksum mismatch for {name}")
        verified.append(path)
    if not verified:
        raise EvidenceError("manifest: at least one entry is required")
    return tuple(verified)
