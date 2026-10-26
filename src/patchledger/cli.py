"""Command-line interface for the Security Patch Evidence Ledger."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .core import EvidenceError, build_reports, load_ledger, summarize


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="patch-ledger", description="Validate security-patch evidence and build certification-ready reports.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    validate = subparsers.add_parser("validate", help="Validate a ledger and print its summary.")
    validate.add_argument("input", type=Path)

    build = subparsers.add_parser("build", help="Validate a ledger and write Markdown, CSV, and JSON reports.")
    build.add_argument("input", type=Path)
    build.add_argument("--output-dir", type=Path, default=Path("dist"))
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        ledger = load_ledger(args.input)
        if args.command == "validate":
            print(json.dumps(summarize(ledger), indent=2, sort_keys=True))
        else:
            paths = build_reports(ledger, args.output_dir)
            for path in paths:
                print(path)
        return 0
    except EvidenceError as exc:
        print(f"evidence error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
