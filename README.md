# Security Patch Evidence Ledger

Security Patch Evidence Ledger turns a reviewed JSON list of merged security pull requests into a certification-ready evidence package. It produces Markdown, CSV, and JSON while enforcing the boundaries that make the report defensible: exact GitHub PR URLs, merge timestamps, non-duplicated records, recognized advisory identifiers, named validation evidence, and an explicit disclosure that reconstructed hours are estimates.

The tool is intentionally dependency-free at runtime and works offline after checkout.
CSV text fields beginning with spreadsheet formula characters are neutralized during export.

## What it proves

It can prove that a supplied set of merged PR records is internally consistent and that all generated totals reconcile to those records. It does **not** claim that every repository vulnerability is fixed, replace a vulnerability scanner, or turn estimated hours into a time sheet.

## Quick start

```powershell
python -m venv .venv
.venv\Scripts\python -m pip install -e .
.venv\Scripts\patch-ledger validate tests\fixtures\valid-ledger.json
.venv\Scripts\patch-ledger build tests\fixtures\valid-ledger.json --output-dir dist
```

Without installation:

```powershell
$env:PYTHONPATH = "src"
python -m patchledger.cli validate tests\fixtures\valid-ledger.json
python -m patchledger.cli build tests\fixtures\valid-ledger.json --output-dir dist
```

Generated files:

- `security-patch-evidence.md` — human-readable certification narrative and timeline.
- `security-patch-evidence.csv` — one auditable row per merged PR.
- `security-patch-summary.json` — machine-readable totals and groupings.

## Evidence format

Each record must include:

- exact `repository`, PR `number`, and canonical HTTPS GitHub `url`;
- `merged_at` with timezone;
- one of `dependency`, `manual-remediation`, or `security-hardening`;
- zero or more valid CVE/GHSA IDs;
- at least one supported validation method;
- a bounded `estimate_hours` value and an `estimate_basis` that explicitly calls it an estimate.

Supported validation values are `audit`, `build`, `ci`, `diff-review`, `integration-test`, `manual-test`, and `unit-test`.

The machine-readable contract is published at `schemas/ledger.schema.json`. Editors and ingestion pipelines can use it for completion and preliminary checks; the CLI remains the authoritative validator for cross-field rules such as matching a PR URL to its repository and number.

## Tests

```powershell
$env:PYTHONPATH = "src"
python -m unittest discover -s tests -v
```

The suite checks successful report generation and failure cases for duplicated PRs, mismatched URLs, implausible estimates, missing estimation disclosure, and malformed ledgers.

## Responsible use

Use repository evidence and honest estimates. Do not create empty pull requests to inflate activity, count a superseded PR twice, or present reconstructed hours as contemporaneous records. Certification evidence is strongest when another reviewer can reproduce the count directly from the linked pull requests.
