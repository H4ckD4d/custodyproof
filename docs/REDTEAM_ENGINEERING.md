# Red Team-driven secure engineering: custodyproof

**Owner:** Chris Cruz (@h4ckd4d). This is a **defensive design guide**, not proof that a product has undergone penetration testing.

## Scope
Chain integrity, SHA-256 verification, tamper resistance vs. true immutability, evidence retention and lawful handling.

## Secure engineering gates

1. **Scope and authorization** — work only with synthetic, owned or explicitly approved information.
2. **Threat modeling** — map assets, data boundaries, misuse scenarios and safe mitigation.
3. **Least privilege** — restrict access, GitHub Actions permissions, API tokens and external services.
4. **Privacy minimization** — avoid logging credentials, personal details or authentic evidence in public repositories.
5. **Verification** — write unit and integration tests with fictional inputs; document what is not covered.
6. **Supply chain** — review third-party packages, license notices, updates and CI runner trust.
7. **Incident readiness** — define private vulnerability reporting, versioned fixes and recovery procedures.
8. **AI safety** — disclose that grounding involves Google queries, require human source review and never submit private data.

## Release criteria (future)
- Threat model reviewed and updated.
- Secrets scanning and dependency audits enabled.
- No public exploitable test targets or sensitive telemetry.
- Validation, data privacy and access controls tested.
- Documentation readable in Portuguese, English and Spanish.

## Public safety support
The project supports **lawful service, protecting lives and rescue efforts** by professional public safety and special operations personnel globally. It does **not** claim formal endorsement or partnership with any public agency or military unit.
