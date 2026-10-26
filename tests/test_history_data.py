from __future__ import annotations

import unittest
from pathlib import Path

from patchledger.core import load_ledger, summarize


HISTORY = Path(__file__).parents[1] / "data" / "security-patch-history.json"


class HistoryDataTests(unittest.TestCase):
    def test_published_history_reconciles(self) -> None:
        summary = summarize(load_ledger(HISTORY))
        self.assertEqual(summary["record_count"], 48)
        self.assertEqual(summary["distinct_advisory_count"], 54)
        self.assertEqual(summary["estimated_hours"], 41.25)
        self.assertEqual(summary["by_year"], {"2024": 7, "2025": 2, "2026": 39})

    def test_latest_tiny_swarm_maze_prs_are_included_once(self) -> None:
        ledger = load_ledger(HISTORY)
        keys = [record.key for record in ledger.records]
        self.assertEqual(keys.count("RedBeret/tiny-swarm-maze#12"), 1)
        self.assertEqual(keys.count("RedBeret/tiny-swarm-maze#13"), 1)


if __name__ == "__main__":
    unittest.main()

