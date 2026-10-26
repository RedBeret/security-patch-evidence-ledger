# Security Policy

## Supported version

The latest release on the default branch receives security fixes.

## Reporting a vulnerability

Please use GitHub private vulnerability reporting when available. Otherwise, contact the repository owner privately and do not include exploit details in a public issue.

Include the affected version, a minimal reproduction, realistic impact, and any proposed mitigation. Reports will be acknowledged within seven days when operationally possible.

## Security boundaries

- Input files are treated as untrusted and validated before report generation.
- The tool performs no network requests and does not execute content from evidence records.
- Output paths are chosen by the local operator.
- The CLI does not accept GitHub tokens or other credentials.
