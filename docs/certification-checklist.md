# Certification evidence checklist

Use this checklist before submitting a security-certification reinstatement package.

## Evidence package

- [ ] Keep one ledger record per merged security-remediation pull request.
- [ ] Confirm every link opens the expected repository and PR number.
- [ ] Exclude open, unmerged, duplicate, and superseded PRs.
- [ ] Include advisory IDs only when the PR or linked evidence supports them.
- [ ] Record the validation that was actually performed.
- [ ] Explain every effort estimate using the published scope bands.
- [ ] Generate Markdown, CSV, and JSON from the same ledger input.
- [ ] Create SHA256SUMS and verify it before sending the package.

## Submission language

State the merged-PR count, date range, distinct advisory count, and estimated hands-on hours. Clearly label hours as reconstructed estimates. Avoid claiming that the history proves all repository alerts are closed or that estimates are time-sheet entries.

## Reviewer handoff

Provide:

1. the source ledger JSON;
2. the generated Markdown timeline;
3. the CSV detail export;
4. the JSON summary;
5. the SHA-256 manifest;
6. the repository URL and the commit used to generate the package.

Ask the reviewer to spot-check several PR links, compare row counts across formats, and run the manifest verification command.

## Suggested statement template

> I maintain a documented history of **[count]** merged security-remediation pull requests from **[start date]** through **[end date]**. The linked PR evidence identifies **[advisory count]** distinct CVE/GHSA advisories. Using the documented scope-based method, the work represents approximately **[hours] estimated hands-on hours**. These are reconstructed estimates from repository evidence, not contemporaneous time-sheet entries.
