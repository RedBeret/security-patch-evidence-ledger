"""Command-line interface for the Security Patch Evidence Ledger."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .attest import verify_manifest, write_manifest
from .core import EvidenceError, build_reports, load_ledger, summarize


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="patch-ledger", description="Validate security-patch evidence and build certification-ready reports.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="Validate a ledger and print its summary.")
    validate.add_argument("input", type=Path)

    build = subparsers.add_parser("build", help="Validate a ledger and write Markdown, CSV, and JSON reports.")
    build.add_argument("input", type=Path)
    build.add_argument("--output-dir", type=Path, default=Path("dist"))

    attest = subparsers.add_parser("attest", help="Write SHA-256 checksums for a generated report directory.")
    attest.add_argument("report_dir", type=Path)

    verify = subparsers.add_parser("verify-manifest", help="Verify a report directory against its SHA-256 manifest.")
    verify.add_argument("manifest", type=Path)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        if args.command == "validate":
            ledger = load_ledger(args.input)
            print(json.dumps(summarize(ledger), indent=2, sort_keys=True))
        elif args.command == "build":
            ledger = load_ledger(args.input)
            paths = build_reports(ledger, args.output_dir)
            for path in paths:
                print(path)
        elif args.command == "attest":
            names = ["security-patch-evidence.md", "security-patch-evidence.csv", "security-patch-summary.json"]
            path = write_manifest((args.report_dir / name for name in names), args.report_dir / "SHA256SUMS")
            print(path)
        else:
            for path in verify_manifest(args.manifest):
                print(path)
        return 0
    except EvidenceError as exc:
        print(f"evidence error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
