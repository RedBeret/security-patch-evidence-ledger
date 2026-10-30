from __future__ import annotations

import csv
import json
import tempfile
import unittest
from pathlib import Path

from patchledger.cli import main
from patchledger.core import EvidenceError, build_reports, load_ledger, summarize


FIXTURE = Path(__file__).parent / "fixtures" / "valid-ledger.json"


class LedgerTests(unittest.TestCase):
    def test_summary_reconciles_counts_and_hours(self) -> None:
        summary = summarize(load_ledger(FIXTURE))
        self.assertEqual(summary["record_count"], 3)
        self.assertEqual(summary["distinct_advisory_count"], 2)
        self.assertEqual(summary["estimated_hours"], 1.75)
        self.assertEqual(summary["by_year"], {"2026": 3})

    def test_build_writes_all_formats_with_matching_row_counts(self) -> None:
        ledger = load_ledger(FIXTURE)
        with tempfile.TemporaryDirectory() as temp_dir:
            markdown_path, csv_path, json_path = build_reports(ledger, temp_dir)
            self.assertIn("Merged security-remediation PRs: **3**", markdown_path.read_text(encoding="utf-8"))
            with csv_path.open(encoding="utf-8", newline="") as handle:
                self.assertEqual(len(list(csv.DictReader(handle))), 3)
            self.assertEqual(json.loads(json_path.read_text(encoding="utf-8"))["estimated_hours"], 1.75)
            self.assertNotIn(b"\r\n", markdown_path.read_bytes())
            self.assertNotIn(b"\r\n", json_path.read_bytes())

    def test_duplicate_pull_request_is_rejected(self) -> None:
        raw = json.loads(FIXTURE.read_text(encoding="utf-8"))
        raw["records"].append(dict(raw["records"][0]))
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "duplicate.json"
            path.write_text(json.dumps(raw), encoding="utf-8")
            with self.assertRaisesRegex(EvidenceError, "duplicate pull requests"):
                load_ledger(path)

    def test_mismatched_pull_request_url_is_rejected(self) -> None:
        raw = json.loads(FIXTURE.read_text(encoding="utf-8"))
        raw["records"][0]["url"] = "https://github.com/RedBeret/other/pull/6"
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "bad-url.json"
            path.write_text(json.dumps(raw), encoding="utf-8")
            with self.assertRaisesRegex(EvidenceError, "must equal"):
                load_ledger(path)

    def test_unbounded_estimate_is_rejected(self) -> None:
        raw = json.loads(FIXTURE.read_text(encoding="utf-8"))
        raw["records"][0]["estimate_hours"] = 80
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "bad-hours.json"
            path.write_text(json.dumps(raw), encoding="utf-8")
            with self.assertRaisesRegex(EvidenceError, "at most 24"):
                load_ledger(path)

    def test_estimate_disclosure_is_required(self) -> None:
        raw = json.loads(FIXTURE.read_text(encoding="utf-8"))
        raw["records"][0]["estimate_basis"] = "Actual work completed."
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "bad-disclosure.json"
            path.write_text(json.dumps(raw), encoding="utf-8")
            with self.assertRaisesRegex(EvidenceError, "must disclose"):
                load_ledger(path)

    def test_cli_returns_nonzero_for_invalid_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            path = Path(temp_dir) / "invalid.json"
            path.write_text("{}", encoding="utf-8")
            self.assertEqual(main(["validate", str(path)]), 2)

    def test_csv_formula_prefix_is_neutralized(self) -> None:
        raw = json.loads(FIXTURE.read_text(encoding="utf-8"))
        raw["records"][0]["title"] = "=HYPERLINK(\"https://example.invalid\")"
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "formula.json"
            source.write_text(json.dumps(raw), encoding="utf-8")
            _, csv_path, _ = build_reports(load_ledger(source), Path(temp_dir) / "out")
            with csv_path.open(encoding="utf-8", newline="") as handle:
                row = next(csv.DictReader(handle))
            self.assertTrue(row["title"].startswith("'="))


if __name__ == "__main__":
    unittest.main()
