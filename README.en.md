# CustodyProof

[Português](README.pt-BR.md) · [English](README.en.md) · [Español](README.es.md)

> **File integrity and chain of custody records**

**Creator, concept, technical direction and development: [Chris Cruz — @h4ckd4d](https://github.com/H4ckD4d)**

**Version:** v0.1.0 local starter · **License:** MIT · **Status:** synthetic demonstration, not production software.

File integrity and chain of custody records

## A Red Team hacker mindset, turned into useful technology

Chris Cruz, known as @h4ckd4d, brings experience across electronics, networks, infrastructure, software development, and cybersecurity. A Red Team mindset is not a license to attack: it is about asking difficult questions, examining risks with authorization, and building stronger solutions. Every project starts with a question. What if a practical challenge could become a public, verifiable tool for technical communities, designed with security from the beginning?

> An ethical hacker perspective. Red Team discipline. Responsibility to real people.

[Storytelling PT-BR](docs/STORYTELLING.pt-BR.md) · [EN](docs/STORYTELLING.en.md) · [ES](docs/STORYTELLING.es.md)

## Quick start / Início rápido / Inicio rápido

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
custodyproof demo --lang en
python -m unittest discover -s tests -v
```

### Optional Google Search + AI

```bash
python -m pip install -e '.[ai]'
export GEMINI_API_KEY='YOUR_KEY'
custodyproof research --lang en
```

Grounded, public technical research; optional and potentially billable. [Integration documentation](docs/GOOGLE_AI.md).

### Trilingual dashboard preview

```bash
python3 -m http.server 8080 --bind 127.0.0.1 --directory dashboard
```

Open http://127.0.0.1:8080. **Only fictional UI data, no actual backend connection.**

## Collaboration

Open invitation: developers, students, researchers and translators can contribute through issues and pull requests. Contributions must be legal, authorized and verifiable.

[Contribution guide](docs/CONTRIBUTING.en.md) · [Security](docs/SECURITY.en.md) · [Issues](https://github.com/H4ckD4d/custodyproof/issues)

## Ethical Red Team and support statement

We support lawful efforts to protect lives, conduct rescues and provide responsible security by legally constituted special operations and public safety professionals worldwide. No official military, police, government or institutional affiliation, endorsement or partnership is claimed.

### More docs

[Threat model](docs/THREAT_MODEL.md) · [Red Team engineering](docs/REDTEAM_ENGINEERING.md) · [Roadmap](docs/ROADMAP.md) · [Codex instructions](AGENTS.md)

**© 2026 Chris Cruz (@h4ckd4d).**

## Next technical increment (v0.2 candidate)

Compare stored files against local ledger hashes; this does not certify provenance.

```bash
custodyproof verify-files --ledger custody-ledger.jsonl --directory ./evidencias
```

**Chris Cruz — @h4ckd4d**.

## v0.3 candidate enhancement

Local custody manifest report (not a certification):

```bash
custodyproof manifest --ledger ledger.jsonl --directory ./evidencias
```

[Commercial roadmap](docs/COMMERCIAL.md) · Chris Cruz — @h4ckd4d.
