from __future__ import annotations

import json
import unittest
from pathlib import Path

from patchledger.core import ALLOWED_CATEGORIES, ALLOWED_VALIDATIONS, load_ledger


ROOT = Path(__file__).parents[1]
SCHEMA = ROOT / "schemas" / "ledger.schema.json"
FIXTURE = ROOT / "tests" / "fixtures" / "valid-ledger.json"


class SchemaContractTests(unittest.TestCase):
    def test_schema_and_runtime_categories_match(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        record = schema["$defs"]["record"]
        self.assertEqual(set(record["properties"]["category"]["enum"]), ALLOWED_CATEGORIES)
        self.assertEqual(set(record["properties"]["validations"]["items"]["enum"]), ALLOWED_VALIDATIONS)

    def test_fixture_contains_every_schema_required_field(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        raw = json.loads(FIXTURE.read_text(encoding="utf-8"))
        required = set(schema["$defs"]["record"]["required"])
        self.assertTrue(all(required <= set(record) for record in raw["records"]))
        self.assertEqual(len(load_ledger(FIXTURE).records), len(raw["records"]))


if __name__ == "__main__":
    unittest.main()
