# Threat model — CustodyProof

**Boundary:** a local teaching/validation CLI and a static dashboard. The dashboard is not connected to the CLI. No authentication, API server, account storage or production use is implemented.

| Risk | Control required |
| --- | --- |
| Input file or path abuse | Parse cautiously, enforce format/size bounds and avoid following symlinks |
| Sensitive information leaks | Redact values; do not commit real case files |
| AI output hallucination | Display grounding sources; require independent review |
| Accidental external disclosure | AI feature only opt-in and only with public queries |
| Dependency compromise | Audit versions and CI permissions before release |
| Unauthorized testing | Reject real targets; run offline synthetic exercises only |

Security claims should be verified before production.
