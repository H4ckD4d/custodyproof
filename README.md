# CustodyProof

[Português](README.pt-BR.md) · [English](README.en.md) · [Español](README.es.md)

> **Verificação de integridade e registro de cadeia de custódia**

**Criação, concepção, direção técnica e desenvolvimento: [Chris Cruz — @h4ckd4d](https://github.com/H4ckD4d)**

**Version:** v0.1.0 local starter · **License:** MIT · **Status:** synthetic demonstration, not production software.

CustodyProof registra hashes SHA-256 e eventos encadeados para análise de integridade.

## O olhar de um hacker Red Team transformado em produto

A jornada de Chris Cruz, conhecido como @h4ckd4d, percorre eletrônica, redes, infraestrutura, desenvolvimento e segurança cibernética. A mentalidade Red Team não é invadir: é fazer perguntas difíceis, examinar riscos de forma autorizada e desenvolver soluções melhores. Todo projeto nasce de uma pergunta. E se pudéssemos transformar uma dificuldade real em uma ferramenta pública, verificável, útil para comunidades técnicas e construída com segurança desde o início?

> O olhar de um hacker ético. A disciplina do Red Team. A responsabilidade de construir para pessoas reais.

[Storytelling PT-BR](docs/STORYTELLING.pt-BR.md) · [EN](docs/STORYTELLING.en.md) · [ES](docs/STORYTELLING.es.md)

## Quick start / Início rápido / Inicio rápido

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e .
custodyproof demo --lang pt
python -m unittest discover -s tests -v
```

### Optional Google Search + AI

```bash
python -m pip install -e '.[ai]'
export GEMINI_API_KEY='YOUR_KEY'
custodyproof research --lang pt
```

Grounded, public technical research; optional and potentially billable. [Integration documentation](docs/GOOGLE_AI.md).

### Trilingual dashboard preview

```bash
python3 -m http.server 8080 --bind 127.0.0.1 --directory dashboard
```

Open http://127.0.0.1:8080. **Only fictional UI data, no actual backend connection.**

## Collaboration

Convite aberto: profissionais, estudantes, pesquisadores e tradutores podem colaborar por issues e pull requests. Contribuições devem ser legais, autorizadas e verificáveis.

[Contribution guide](docs/CONTRIBUTING.pt-BR.md) · [Security](docs/SECURITY.pt-BR.md) · [Issues](https://github.com/H4ckD4d/custodyproof/issues)

## Ethical Red Team and support statement

Declaramos apoio ao trabalho lícito de proteção de vidas, salvamento e defesa realizado por profissionais de segurança e forças especiais legalmente constituídas no mundo. Não possuímos vínculo, endosso ou parceria oficial com organizações militares, policiais ou governamentais.

### More docs

[Threat model](docs/THREAT_MODEL.md) · [Red Team engineering](docs/REDTEAM_ENGINEERING.md) · [Roadmap](docs/ROADMAP.md) · [Codex instructions](AGENTS.md)

**© 2026 Chris Cruz (@h4ckd4d).**
