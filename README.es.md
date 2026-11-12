# CustodyProof

[Português](README.pt-BR.md) · [English](README.en.md) · [Español](README.es.md)

> **Integridad de archivos y registro de cadena de custodia**

**Creación, concepto, dirección técnica y desarrollo: [Chris Cruz — @h4ckd4d](https://github.com/H4ckD4d)**

**Version:** v0.1.0 local starter · **License:** MIT · **Status:** synthetic demonstration, not production software.

Integridad de archivos y registro de cadena de custodia

## La mentalidad Red Team convertida en tecnología útil

Chris Cruz, conocido como @h4ckd4d, aporta experiencia en electrónica, redes, infraestructura, desarrollo y ciberseguridad. La mentalidad Red Team no es una licencia para atacar: significa plantear preguntas difíciles, examinar riesgos con autorización y construir mejores defensas. Todo proyecto comienza con una pregunta. ¿Y si un desafío práctico pudiera convertirse en una herramienta pública y verificable, creada con seguridad desde el principio?

> La visión de un hacker ético. La disciplina Red Team. Responsabilidad con personas reales.

[Storytelling PT-BR](docs/STORYTELLING.pt-BR.md) · [EN](docs/STORYTELLING.en.md) · [ES](docs/STORYTELLING.es.md)

## Quick start / Início rápido / Inicio rápido

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
custodyproof demo --lang es
python -m unittest discover -s tests -v
```

### Optional Google Search + AI

```bash
python -m pip install -e '.[ai]'
export GEMINI_API_KEY='YOUR_KEY'
custodyproof research --lang es
```

Grounded, public technical research; optional and potentially billable. [Integration documentation](docs/GOOGLE_AI.md).

### Trilingual dashboard preview

```bash
python3 -m http.server 8080 --bind 127.0.0.1 --directory dashboard
```

Open http://127.0.0.1:8080. **Only fictional UI data, no actual backend connection.**

## Collaboration

Invitación abierta: desarrolladores, estudiantes, investigadores y traductores pueden colaborar mediante issues y pull requests. Las contribuciones deben ser legales, autorizadas y verificables.

[Contribution guide](docs/CONTRIBUTING.es.md) · [Security](docs/SECURITY.es.md) · [Issues](https://github.com/H4ckD4d/custodyproof/issues)

## Ethical Red Team and support statement

Apoyamos las labores legales de protección de vidas, rescate y seguridad de profesionales y unidades de operaciones especiales legalmente constituidas en todo el mundo. No afirmamos afiliación, respaldo ni colaboración oficial con entidades militares, policiales o gubernamentales.

### More docs

[Threat model](docs/THREAT_MODEL.md) · [Red Team engineering](docs/REDTEAM_ENGINEERING.md) · [Roadmap](docs/ROADMAP.md) · [Codex instructions](AGENTS.md)

**© 2026 Chris Cruz (@h4ckd4d).**

## Siguiente mejora técnica (v0.2 candidate)

Comparación de archivos almacenados con hashes locales; no certifica procedencia.

```bash
custodyproof verify-files --ledger custody-ledger.jsonl --directory ./evidencias
```

**Chris Cruz — @h4ckd4d**.
