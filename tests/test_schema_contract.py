from __future__ import annotations

import json
import re
import unittest
from pathlib import Path

from patchledger.core import ALLOWED_CATEGORIES, ALLOWED_VALIDATIONS, load_ledger


ROOT = Path(__file__).parents[1]
SCHEMA = ROOT / "schemas" / "ledger.schema.json"
FIXTURE = ROOT / "tests" / "fixtures" / "valid-ledger.json"


class SchemaContractTests(unittest.TestCase):
    def test_advisory_schema_accepts_published_identifiers(self) -> None:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        pattern = schema["$defs"]["record"]["properties"]["advisories"]["items"]["pattern"]
        history = json.loads((ROOT / "data" / "security-patch-history.json").read_text(encoding="utf-8"))
        identifiers = {item for record in history["records"] for item in record["advisories"]}
        for identifier in identifiers:
            for candidate in (identifier, identifier.lower()):
                with self.subTest(identifier=candidate):
                    self.assertIsNotNone(re.fullmatch(pattern, candidate))
        for malformed in ("GHSA-0000-0000-0000", "CVE-2026-nope", "CVE-2026-1234-extra"):
            self.assertIsNone(re.fullmatch(pattern, malformed))

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
