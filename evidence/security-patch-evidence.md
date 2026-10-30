# Security Patch Evidence Ledger

Owner: **RedBeret**  
Generated: **2026-10-26T04:30:00Z**

## Summary

- Merged security-related PRs (remediation and hardening): **48**
- Distinct CVE/GHSA identifiers: **54**
- Estimated hands-on hours: **41.25**
- Disclosure: hours are reconstructed estimates from repository evidence, not contemporaneous time-sheet entries.
- CVE and GHSA identifiers may refer to the same vulnerability; this is an identifier count.

## Timeline

| Merged | Repository / PR | Category | Advisories | Validation | Est. hours |
|---|---|---|---|---|---:|
| 2024-02-02 | [RedBeret/AIChatPoweredEcommerce#2](https://github.com/RedBeret/AIChatPoweredEcommerce/pull/2) — Bump the pip group across 1 directories with 4 updates | dependency | CVE-2023-30861, GHSA-G4MX-Q9VG-27P4, GHSA-M2QF-HXJV-5GPQ | build, ci, diff-review | 0.5 |
| 2024-04-16 | [RedBeret/reactresolve#5](https://github.com/RedBeret/reactresolve/pull/5) — Bump idna from 3.6 to 3.7 | dependency | CVE-2024-3651 | ci, diff-review | 0.5 |
| 2024-04-16 | [RedBeret/TryOpenAIChatCompletions#2](https://github.com/RedBeret/TryOpenAIChatCompletions/pull/2) — Bump idna from 3.6 to 3.7 | dependency | CVE-2024-3651 | ci, diff-review | 0.5 |
| 2024-04-18 | [RedBeret/AIChatPoweredEcommerce#49](https://github.com/RedBeret/AIChatPoweredEcommerce/pull/49) — Bump the pip group across 1 directory with 3 updates | dependency | CVE-2024-1135, CVE-2024-21503, CVE-2024-3651 | ci, diff-review | 0.75 |
| 2024-07-21 | [RedBeret/AIChatPoweredEcommerce#56](https://github.com/RedBeret/AIChatPoweredEcommerce/pull/56) — Bump the pip group across 1 directory with 5 updates | dependency | CVE-2024-1135, CVE-2024-34062, CVE-2024-3651, GHSA-G7VV-2V7X-GJ9P | build, ci, diff-review | 1 |
| 2024-07-30 | [RedBeret/AIChatPoweredEcommerce#60](https://github.com/RedBeret/AIChatPoweredEcommerce/pull/60) — Bump the pip group across 1 directory with 4 updates | dependency | CVE-2024-1135, CVE-2024-3651 | ci, diff-review | 0.75 |
| 2024-07-31 | [RedBeret/AIChatPoweredEcommerce#61](https://github.com/RedBeret/AIChatPoweredEcommerce/pull/61) — Bump the pip group across 1 directory with 2 updates | dependency | CVE-2024-34062, GHSA-G7VV-2V7X-GJ9P | ci, diff-review | 0.5 |
| 2025-05-31 | [RedBeret/neon-grid-hacker#2](https://github.com/RedBeret/neon-grid-hacker/pull/2) — Bump the npm\_and\_yarn group across 1 directory with 3 updates | dependency | GHSA-VG6X-RCGG-RJX6 | ci, diff-review | 0.75 |
| 2025-06-02 | [RedBeret/AI-Chess-Mentor-for-Beginners#2](https://github.com/RedBeret/AI-Chess-Mentor-for-Beginners/pull/2) — Bump the npm\_and\_yarn group across 1 directory with 5 updates | dependency | GHSA-VG6X-RCGG-RJX6 | build, ci, diff-review | 1.5 |
| 2026-03-03 | [RedBeret/AI-Chess-Mentor-for-Beginners#3](https://github.com/RedBeret/AI-Chess-Mentor-for-Beginners/pull/3) — Bump the npm\_and\_yarn group across 1 directory with 2 updates | dependency | Security remediation documented without embedded ID | ci, diff-review | 0.75 |
| 2026-03-03 | [RedBeret/AI-Chess-Mentor-for-Beginners#4](https://github.com/RedBeret/AI-Chess-Mentor-for-Beginners/pull/4) — build\(deps\): bump the npm\_and\_yarn group across 1 directory with 7 updates | dependency | Security remediation documented without embedded ID | audit, build, ci, diff-review | 1 |
| 2026-03-12 | [RedBeret/intent-config-workbench#2](https://github.com/RedBeret/intent-config-workbench/pull/2) — Bump actions/setup-python from 5 to 6 | dependency | Security remediation documented without embedded ID | diff-review | 0.5 |
| 2026-03-23 | [RedBeret/reactresolve#12](https://github.com/RedBeret/reactresolve/pull/12) — Bump the pip group across 1 directory with 3 updates | dependency | CVE-2024-34062, GHSA-G7VV-2V7X-GJ9P | ci, diff-review | 0.75 |
| 2026-03-23 | [RedBeret/TryOpenAIChatCompletions#4](https://github.com/RedBeret/TryOpenAIChatCompletions/pull/4) — Bump the pip group across 1 directory with 2 updates | dependency | CVE-2024-34062, GHSA-G7VV-2V7X-GJ9P | ci, diff-review | 0.75 |
| 2026-03-24 | [RedBeret/reactresolve#20](https://github.com/RedBeret/reactresolve/pull/20) — Bump the npm\_and\_yarn group across 1 directory with 6 updates | dependency | Security remediation documented without embedded ID | build, ci, diff-review, unit-test | 1.5 |
| 2026-03-24 | [RedBeret/dev-portfolio#10](https://github.com/RedBeret/dev-portfolio/pull/10) — Bump the npm\_and\_yarn group across 1 directory with 22 updates | dependency | CVE-2025-12816, CVE-2025-66030, CVE-2025-66031, CVE-2025-7339, GHSA-554W-WPV2-VW27, GHSA-5GFM-WPXJ-WJGQ, GHSA-65CH-62R8-G69G, GHSA-76C9-3JPH-RJ3Q | build, ci, diff-review, unit-test | 1.5 |
| 2026-04-04 | [RedBeret/tiny-swarm-maze#2](https://github.com/RedBeret/tiny-swarm-maze/pull/2) — Bump picomatch from 4.0.3 to 4.0.4 in /frontend in the npm\_and\_yarn group across 1 directory | dependency | CVE-2026-33671, CVE-2026-33672, GHSA-3V7F-55P6-F55P, GHSA-C2C7-RCM5-VVQJ | diff-review | 0.5 |
| 2026-04-05 | [RedBeret/dune-awakening-transfer-prep#7](https://github.com/RedBeret/dune-awakening-transfer-prep/pull/7) — Bump the npm\_and\_yarn group across 1 directory with 1 update | dependency | CVE-2026-33671, CVE-2026-33672, GHSA-3V7F-55P6-F55P, GHSA-C2C7-RCM5-VVQJ | diff-review | 0.75 |
| 2026-04-05 | [RedBeret/AI-Chess-Mentor-for-Beginners#9](https://github.com/RedBeret/AI-Chess-Mentor-for-Beginners/pull/9) — build\(deps\): bump the npm\_and\_yarn group across 1 directory with 1 update | dependency | CVE-2026-33671, CVE-2026-33672, GHSA-3V7F-55P6-F55P, GHSA-C2C7-RCM5-VVQJ | build, diff-review | 0.75 |
| 2026-04-05 | [RedBeret/dev-portfolio#11](https://github.com/RedBeret/dev-portfolio/pull/11) — Bump micromatch from 4.0.5 to 4.0.8 in the npm\_and\_yarn group across 1 directory | dependency | CVE-2024-4067, CVE-2024-4068 | diff-review | 1 |
| 2026-04-05 | [RedBeret/reactresolve#24](https://github.com/RedBeret/reactresolve/pull/24) — Bump the npm\_and\_yarn group across 1 directory with 1 update | dependency | CVE-2026-33671, CVE-2026-33672, GHSA-3V7F-55P6-F55P, GHSA-C2C7-RCM5-VVQJ | diff-review | 0.75 |
| 2026-04-05 | [RedBeret/AI-Chess-Mentor-for-Beginners#12](https://github.com/RedBeret/AI-Chess-Mentor-for-Beginners/pull/12) — build\(deps\): bump the npm\_and\_yarn group across 1 directory with 3 updates | dependency | CVE-2021-23337, CVE-2026-4800, GHSA-F23M-R3PF-42RH, GHSA-F886-M6HF-6M8V, GHSA-R5FR-RJXR-66JC | build, ci, diff-review | 0.75 |
| 2026-04-05 | [RedBeret/dune-awakening-transfer-prep#8](https://github.com/RedBeret/dune-awakening-transfer-prep/pull/8) — Bump lodash from 4.17.23 to 4.18.1 in the npm\_and\_yarn group across 1 directory | dependency | CVE-2021-23337, CVE-2026-4800, GHSA-F23M-R3PF-42RH, GHSA-R5FR-RJXR-66JC | build, ci, diff-review | 0.5 |
| 2026-04-12 | [RedBeret/dev-portfolio#15](https://github.com/RedBeret/dev-portfolio/pull/15) — Bump the npm\_and\_yarn group across 1 directory with 6 updates | dependency | CVE-2021-23337, CVE-2022-24771, CVE-2022-35961, CVE-2026-25793, CVE-2026-33671, CVE-2026-33672, CVE-2026-33891, CVE-2026-33894, CVE-2026-33895, CVE-2026-33896, CVE-2026-4800, CVE-2026-4867, GHSA-2328-F5F3-GJ25, GHSA-37CH-88JC-XWX2, GHSA-3V7F-55P6-F55P, GHSA-5GFM-WPXJ-WJGQ, GHSA-5M6Q-G25R-MVWX, GHSA-C2C7-RCM5-VVQJ, GHSA-F23M-R3PF-42RH, GHSA-F886-M6HF-6M8V, GHSA-PPP5-5V6C-4JWP, GHSA-Q67F-28XG-22RW, GHSA-R5FR-RJXR-66JC | build, ci, diff-review, unit-test | 1 |
| 2026-07-26 | [RedBeret/airgap-patch#2](https://github.com/RedBeret/airgap-patch/pull/2) — Bump pytest from 8.4.1 to 9.0.3 in the pip group across 1 directory | dependency | CVE-2025-71176 | ci, diff-review, unit-test | 0.5 |
| 2026-07-26 | [RedBeret/airgap-patch#6](https://github.com/RedBeret/airgap-patch/pull/6) — Bump ansible-core to 2.18.18 for CVE-2026-11332 | dependency | CVE-2026-11332 | build, diff-review, unit-test | 0.5 |
| 2026-08-28 | [RedBeret/saas-launch-pad-kit#9](https://github.com/RedBeret/saas-launch-pad-kit/pull/9) — build\(deps\): bump the npm\_and\_yarn group across 1 directory with 2 updates | dependency | Security remediation documented without embedded ID | build, ci, diff-review | 1.5 |
| 2026-08-28 | [RedBeret/saas-launch-pad-kit#10](https://github.com/RedBeret/saas-launch-pad-kit/pull/10) — build\(deps\): bump the npm\_and\_yarn group across 1 directory with 8 updates | dependency | CVE-2026-13149, GHSA-MH99-V99M-4GVG | build, ci, diff-review | 1.5 |
| 2026-08-28 | [RedBeret/AI-Chess-Mentor-for-Beginners#16](https://github.com/RedBeret/AI-Chess-Mentor-for-Beginners/pull/16) — build\(deps\): bump the npm\_and\_yarn group across 1 directory with 7 updates | dependency | CVE-2026-13149, GHSA-MH99-V99M-4GVG | build, ci, diff-review | 1.5 |
| 2026-08-30 | [RedBeret/restore-verify#11](https://github.com/RedBeret/restore-verify/pull/11) — Bump the python-dependencies group across 1 directory with 6 updates | dependency | CVE-2026-11332 | ci, diff-review, unit-test | 0.75 |
| 2026-08-30 | [RedBeret/AIChatPoweredEcommerce#85](https://github.com/RedBeret/AIChatPoweredEcommerce/pull/85) — Bump pyjwt from 2.12.1 to 2.13.0 in the pip group across 1 directory | dependency | GHSA-993G-76C3-P5M4, GHSA-FHV5-28VV-H8M8, GHSA-JQ35-7PRP-9V3F, GHSA-W7VC-732C-9M39, GHSA-XGMM-8J9V-C9WX | ci, diff-review | 0.5 |
| 2026-08-30 | [RedBeret/reactresolve#32](https://github.com/RedBeret/reactresolve/pull/32) — Update React Router security release | dependency | Security remediation documented without embedded ID | audit, build, ci, diff-review | 0.75 |
| 2026-08-30 | [RedBeret/reactresolve#33](https://github.com/RedBeret/reactresolve/pull/33) — Update UUID security release | dependency | Security remediation documented without embedded ID | audit, build, ci, diff-review | 0.75 |
| 2026-08-30 | [RedBeret/field-sync-notebook#6](https://github.com/RedBeret/field-sync-notebook/pull/6) — Bump pytest from 8.3.4 to 9.0.3 in /backend in the pip group across 1 directory | dependency | CVE-2025-71176 | ci, diff-review, unit-test | 0.5 |
| 2026-08-30 | [RedBeret/dev-portfolio#28](https://github.com/RedBeret/dev-portfolio/pull/28) — deps: bump the npm group across 1 directory with 12 updates | dependency | Security remediation documented without embedded ID | ci, diff-review, unit-test | 1.5 |
| 2026-10-15 | [RedBeret/Web-Dev-Bootcamp-Angela-Yu#2](https://github.com/RedBeret/Web-Dev-Bootcamp-Angela-Yu/pull/2) — fix\(security\): refresh all example dependencies and check routes in CI | dependency | Security remediation documented without embedded ID | audit, ci, diff-review | 1.5 |
| 2026-10-15 | [RedBeret/restore-verify#17](https://github.com/RedBeret/restore-verify/pull/17) — Bump the python-dependencies group across 1 directory with 7 updates | dependency | CVE-2026-32274 | ci, diff-review | 1 |
| 2026-10-15 | [RedBeret/rag-eval-bench#3](https://github.com/RedBeret/rag-eval-bench/pull/3) — fix\(security\): patch local model loading and keep remote code disabled | security-hardening | GHSA-JHR6-GM9C-RQJV | build, ci, diff-review, unit-test | 1 |
| 2026-10-15 | [RedBeret/tiny-swarm-maze#10](https://github.com/RedBeret/tiny-swarm-maze/pull/10) — fix\(security\): use patched pytest for backend tests | dependency | GHSA-6W46-J5RX-G56G | ci, diff-review, unit-test | 0.5 |
| 2026-10-15 | [RedBeret/field-sync-notebook#10](https://github.com/RedBeret/field-sync-notebook/pull/10) — fix\(security\): refresh compatible frontend dependency resolutions | dependency | Security remediation documented without embedded ID | audit, ci, diff-review | 1 |
| 2026-10-15 | [RedBeret/saas-launch-pad-kit#15](https://github.com/RedBeret/saas-launch-pad-kit/pull/15) — fix\(security\): refresh dependencies and patch selector parser | dependency | Security remediation documented without embedded ID | audit, build, diff-review | 1.5 |
| 2026-10-15 | [RedBeret/AI-Chess-Mentor-for-Beginners#20](https://github.com/RedBeret/AI-Chess-Mentor-for-Beginners/pull/20) — fix\(security\): patch frontend tooling and preserve local publishing | dependency | Security remediation documented without embedded ID | audit, build, diff-review | 1.5 |
| 2026-10-26 | [RedBeret/reactresolve#34](https://github.com/RedBeret/reactresolve/pull/34) — Bump browserslist from 4.28.1 to 4.28.9 in /client in the npm\_and\_yarn group across 1 directory | dependency | Security remediation documented without embedded ID | ci, diff-review | 0.5 |
| 2026-10-26 | [RedBeret/edge-lab-console#8](https://github.com/RedBeret/edge-lab-console/pull/8) — build\(deps\): bump source-map-js from 1.2.1 to 1.2.2 in /frontend in the npm\_and\_yarn group across 1 directory | dependency | CVE-2026-93749 | build, ci, diff-review | 0.5 |
| 2026-10-26 | [RedBeret/repo-flight-deck#8](https://github.com/RedBeret/repo-flight-deck/pull/8) — Bump source-map-js from 1.2.1 to 1.2.2 in /frontend in the npm\_and\_yarn group across 1 directory | dependency | CVE-2026-93749 | ci, diff-review | 0.5 |
| 2026-10-26 | [RedBeret/telemetry-replay-studio#7](https://github.com/RedBeret/telemetry-replay-studio/pull/7) — Bump source-map-js from 1.2.1 to 1.2.2 in /frontend in the npm\_and\_yarn group across 1 directory | dependency | CVE-2026-93749 | ci, diff-review | 0.5 |
| 2026-10-26 | [RedBeret/tiny-swarm-maze#12](https://github.com/RedBeret/tiny-swarm-maze/pull/12) — ci: add frontend security validation | security-hardening | Security remediation documented without embedded ID | audit, build, ci, diff-review | 0.75 |
| 2026-10-26 | [RedBeret/tiny-swarm-maze#13](https://github.com/RedBeret/tiny-swarm-maze/pull/13) — fix\(security\): update Vite and patch source-map DoS | dependency | CVE-2026-93749 | audit, build, ci, diff-review | 0.75 |

## Attestation boundary

Merge status and security relevance must be checked against GitHub before records are supplied. The offline validator checks record structure, PR URL consistency, duplicates, timestamps, and estimates; it does not contact GitHub or independently confirm that a PR was merged.

SHA-256 checksums detect changes relative to a trusted manifest. They do not authenticate the author or establish the truth of source records.
