from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from patchledger.attest import verify_manifest, write_manifest
from patchledger.core import EvidenceError


class ManifestTests(unittest.TestCase):
    def test_manifest_round_trip_and_tamper_detection(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            first = root / "report.md"
            second = root / "summary.json"
            first.write_text("evidence", encoding="utf-8")
            second.write_text('{"count": 1}', encoding="utf-8")
            manifest = write_manifest([second, first], root / "SHA256SUMS")
            self.assertEqual([path.name for path in verify_manifest(manifest)], ["report.md", "summary.json"])
            first.write_text("changed", encoding="utf-8")
            with self.assertRaisesRegex(EvidenceError, "checksum mismatch"):
                verify_manifest(manifest)

    def test_manifest_rejects_parent_directory_paths(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            manifest = Path(temp_dir) / "SHA256SUMS"
            manifest.write_text(f"{'0' * 64}  ../outside.txt\n", encoding="utf-8")
            with self.assertRaisesRegex(EvidenceError, "plain file names"):
                verify_manifest(manifest)


if __name__ == "__main__":
    unittest.main()
