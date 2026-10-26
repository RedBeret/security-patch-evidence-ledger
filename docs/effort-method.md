# Effort estimate method

This project reports reconstructed effort when contemporaneous time sheets are unavailable. Every published total must call the result an estimate.

## Inputs

Use evidence that another reviewer can inspect:

- merged pull-request URL and merge time;
- changed-file and line scope;
- advisory or security rationale in the PR;
- recorded test, build, audit, or CI result;
- review notes for unusual remediation work.

Do not count open, closed-unmerged, duplicate, or superseded pull requests.

## Scope bands

| Estimate | Typical scope |
|---:|---|
| 0.50 hour | One-file, very small dependency or lock update |
| 0.75 hour | Up to two files and about 100 changed lines |
| 1.00 hour | Moderate change up to about 500 lines or a focused manual fix |
| 1.50 hours | Large grouped refresh, multiple lockfiles, or substantial validation |

The bands estimate hands-on triage, change review, and validation. They do not represent elapsed CI time or prove billable labor.

## Required disclosure

Each ledger record includes an estimate_basis field. It should name the band or evidence used and explicitly say that the value is estimated. The generated report also states that totals are reconstructed estimates rather than time-sheet entries.

## Review rule

Prefer the lower reasonable band when evidence is incomplete. Raise an estimate only when the PR shows additional change or validation scope. Keep a note explaining exceptions so another reviewer can reproduce the decision.
