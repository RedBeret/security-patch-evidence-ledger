"""Validation and reporting primitives for security-patch evidence."""

from __future__ import annotations

import csv
import json
import re
from collections import Counter
from dataclasses import dataclass
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlparse


ADVISORY_RE = re.compile(r"^(?:CVE-\d{4}-\d{4,}|GHSA-[23456789cfghjmpqrvwx]{4}-[23456789cfghjmpqrvwx]{4}-[23456789cfghjmpqrvwx]{4})$", re.IGNORECASE)
REPOSITORY_RE = re.compile(r"^[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+$")
ALLOWED_CATEGORIES = {"dependency", "manual-remediation", "security-hardening"}
ALLOWED_VALIDATIONS = {"audit", "build", "ci", "diff-review", "integration-test", "manual-test", "unit-test"}


class EvidenceError(ValueError):
    """Raised when evidence cannot be treated as a defensible record."""


@dataclass(frozen=True)
class PatchRecord:
    repository: str
    number: int
    url: str
    title: str
    merged_at: datetime
    category: str
    advisories: tuple[str, ...]
    validations: tuple[str, ...]
    estimate_hours: Decimal
    estimate_basis: str
    notes: str

    @property
    def key(self) -> str:
        return f"{self.repository}#{self.number}"


@dataclass(frozen=True)
class Ledger:
    owner: str
    generated_at: datetime
    records: tuple[PatchRecord, ...]


def _required(mapping: dict[str, Any], name: str, location: str) -> Any:
    if name not in mapping:
        raise EvidenceError(f"{location}: missing required field '{name}'")
    return mapping[name]


def _text(value: Any, name: str, location: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise EvidenceError(f"{location}.{name}: expected a non-empty string")
    return value.strip()


def _parse_timestamp(value: Any, name: str, location: str) -> datetime:
    text = _text(value, name, location)
    normalized = text[:-1] + "+00:00" if text.endswith("Z") else text
    try:
        result = datetime.fromisoformat(normalized)
    except ValueError as exc:
        raise EvidenceError(f"{location}.{name}: invalid ISO-8601 timestamp") from exc
    if result.tzinfo is None:
        raise EvidenceError(f"{location}.{name}: timezone is required")
    return result.astimezone(timezone.utc)


def _parse_estimate(value: Any, location: str) -> Decimal:
    try:
        estimate = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise EvidenceError(f"{location}.estimate_hours: expected a number") from exc
    if not estimate.is_finite() or estimate <= 0 or estimate > Decimal("24"):
        raise EvidenceError(f"{location}.estimate_hours: must be greater than 0 and at most 24")
    if estimate.as_tuple().exponent < -2:
        raise EvidenceError(f"{location}.estimate_hours: use no more than two decimal places")
    return estimate


def _validate_url(url: str, repository: str, number: int, location: str) -> None:
    parsed = urlparse(url)
    expected_path = f"/{repository}/pull/{number}"
    if parsed.scheme != "https" or parsed.netloc.lower() != "github.com" or parsed.path.rstrip("/") != expected_path:
        raise EvidenceError(f"{location}.url: must equal https://github.com/{repository}/pull/{number}")
    if parsed.query or parsed.fragment or parsed.username or parsed.password:
        raise EvidenceError(f"{location}.url: query strings, fragments, and credentials are not allowed")


def _string_list(value: Any, name: str, location: str) -> tuple[str, ...]:
    if not isinstance(value, list):
        raise EvidenceError(f"{location}.{name}: expected a list")
    result = tuple(_text(item, name, location) for item in value)
    if len(set(item.casefold() for item in result)) != len(result):
        raise EvidenceError(f"{location}.{name}: duplicate values are not allowed")
    return result


def _parse_record(raw: Any, index: int) -> PatchRecord:
    location = f"records[{index}]"
    if not isinstance(raw, dict):
        raise EvidenceError(f"{location}: expected an object")

    repository = _text(_required(raw, "repository", location), "repository", location)
    if not REPOSITORY_RE.fullmatch(repository):
        raise EvidenceError(f"{location}.repository: expected owner/name")

    number = _required(raw, "number", location)
    if isinstance(number, bool) or not isinstance(number, int) or number <= 0:
        raise EvidenceError(f"{location}.number: expected a positive integer")

    url = _text(_required(raw, "url", location), "url", location)
    _validate_url(url, repository, number, location)

    category = _text(_required(raw, "category", location), "category", location)
    if category not in ALLOWED_CATEGORIES:
        raise EvidenceError(f"{location}.category: must be one of {sorted(ALLOWED_CATEGORIES)}")

    advisories = tuple(item.upper() for item in _string_list(raw.get("advisories", []), "advisories", location))
    for advisory in advisories:
        if not ADVISORY_RE.fullmatch(advisory):
            raise EvidenceError(f"{location}.advisories: invalid advisory identifier '{advisory}'")

    validations = tuple(item.casefold() for item in _string_list(_required(raw, "validations", location), "validations", location))
    if not validations:
        raise EvidenceError(f"{location}.validations: at least one validation is required")
    unknown = sorted(set(validations) - ALLOWED_VALIDATIONS)
    if unknown:
        raise EvidenceError(f"{location}.validations: unsupported values {unknown}")

    estimate_basis = _text(_required(raw, "estimate_basis", location), "estimate_basis", location)
    if "estimate" not in estimate_basis.casefold():
        raise EvidenceError(f"{location}.estimate_basis: must disclose that the hours are estimated")

    return PatchRecord(
        repository=repository,
        number=number,
        url=url,
        title=_text(_required(raw, "title", location), "title", location),
        merged_at=_parse_timestamp(_required(raw, "merged_at", location), "merged_at", location),
        category=category,
        advisories=advisories,
        validations=validations,
        estimate_hours=_parse_estimate(_required(raw, "estimate_hours", location), location),
        estimate_basis=estimate_basis,
        notes=_text(raw.get("notes", "No additional notes."), "notes", location),
    )


def load_ledger(path: str | Path) -> Ledger:
    source = Path(path)
    try:
        raw = json.loads(source.read_text(encoding="utf-8"))
    except OSError as exc:
        raise EvidenceError(f"cannot read {source}: {exc}") from exc
    except json.JSONDecodeError as exc:
        raise EvidenceError(f"{source}: invalid JSON at line {exc.lineno}, column {exc.colno}") from exc

    if not isinstance(raw, dict):
        raise EvidenceError("ledger root: expected an object")
    records_raw = _required(raw, "records", "ledger")
    if not isinstance(records_raw, list):
        raise EvidenceError("ledger.records: expected a list")

    records = tuple(_parse_record(item, index) for index, item in enumerate(records_raw))
    if not records:
        raise EvidenceError("ledger.records: at least one merged patch record is required")

    keys = [record.key.casefold() for record in records]
    duplicates = sorted(key for key, count in Counter(keys).items() if count > 1)
    if duplicates:
        raise EvidenceError(f"ledger.records: duplicate pull requests {duplicates}")

    return Ledger(
        owner=_text(_required(raw, "owner", "ledger"), "owner", "ledger"),
        generated_at=_parse_timestamp(_required(raw, "generated_at", "ledger"), "generated_at", "ledger"),
        records=tuple(sorted(records, key=lambda record: (record.merged_at, record.repository.casefold(), record.number))),
    )


def summarize(ledger: Ledger) -> dict[str, Any]:
    advisory_ids = sorted({item for record in ledger.records for item in record.advisories})
    by_year = Counter(str(record.merged_at.year) for record in ledger.records)
    by_repository = Counter(record.repository for record in ledger.records)
    by_category = Counter(record.category for record in ledger.records)
    total = sum((record.estimate_hours for record in ledger.records), Decimal("0"))
    return {
        "owner": ledger.owner,
        "generated_at": ledger.generated_at.isoformat().replace("+00:00", "Z"),
        "record_count": len(ledger.records),
        "distinct_advisory_count": len(advisory_ids),
        "advisory_ids": advisory_ids,
        "estimated_hours": float(total),
        "by_year": dict(sorted(by_year.items())),
        "by_repository": dict(sorted(by_repository.items())),
        "by_category": dict(sorted(by_category.items())),
    }


def write_json(ledger: Ledger, destination: Path) -> None:
    destination.write_text(json.dumps(summarize(ledger), indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")


def _csv_safe(value: Any) -> Any:
    """Neutralize formula prefixes when a CSV is opened in a spreadsheet."""
    if not isinstance(value, str):
        return value
    if value.startswith(("=", "+", "-", "@", "\t", "\r")):
        return "'" + value
    return value


def write_csv(ledger: Ledger, destination: Path) -> None:
    with destination.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["repository", "pr_number", "title", "merged_at", "category", "advisories", "validations", "estimated_hours", "estimate_basis", "url", "notes"])
        for record in ledger.records:
            writer.writerow([_csv_safe(value) for value in [
                record.repository,
                record.number,
                record.title,
                record.merged_at.isoformat().replace("+00:00", "Z"),
                record.category,
                ";".join(record.advisories),
                ";".join(record.validations),
                str(record.estimate_hours),
                record.estimate_basis,
                record.url,
                record.notes,
            ]])


def write_markdown(ledger: Ledger, destination: Path) -> None:
    summary = summarize(ledger)
    lines = [
        "# Security Patch Evidence Ledger",
        "",
        f"Owner: **{ledger.owner}**  ",
        f"Generated: **{summary['generated_at']}**",
        "",
        "## Summary",
        "",
        f"- Merged security-remediation PRs: **{summary['record_count']}**",
        f"- Distinct CVE/GHSA identifiers: **{summary['distinct_advisory_count']}**",
        f"- Estimated hands-on hours: **{summary['estimated_hours']:.2f}**",
        "- Disclosure: hours are reconstructed estimates from repository evidence, not contemporaneous time-sheet entries.",
        "",
        "## Timeline",
        "",
        "| Merged | Repository / PR | Category | Advisories | Validation | Est. hours |",
        "|---|---|---|---|---|---:|",
    ]
    for record in ledger.records:
        advisories = ", ".join(record.advisories) or "Security remediation documented without embedded ID"
        validations = ", ".join(record.validations)
        title = " ".join(record.title.split()).replace("|", "\\|")
        lines.append(
            f"| {record.merged_at.date().isoformat()} | [{record.repository}#{record.number}]({record.url}) — {title} | "
            f"{record.category} | {advisories} | {validations} | {record.estimate_hours} |"
        )
    lines.extend([
        "",
        "## Attestation boundary",
        "",
        "This report counts only merged pull requests supplied in the validated ledger. Open, closed-unmerged, duplicated, or malformed records are rejected or excluded before report generation.",
        "",
    ])
    destination.write_text("\n".join(lines), encoding="utf-8", newline="\n")


def build_reports(ledger: Ledger, output_dir: str | Path) -> tuple[Path, Path, Path]:
    target = Path(output_dir)
    target.mkdir(parents=True, exist_ok=True)
    markdown_path = target / "security-patch-evidence.md"
    csv_path = target / "security-patch-evidence.csv"
    json_path = target / "security-patch-summary.json"
    write_markdown(ledger, markdown_path)
    write_csv(ledger, csv_path)
    write_json(ledger, json_path)
    return markdown_path, csv_path, json_path
