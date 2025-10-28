# Research Rabbit Hole Explorer + Agent Cloud

A multi‑agent literature explorer that debates, cites, and renders an interactive mind‑map; extended with a hyper‑personal Agent Cloud (memory, code/dataset vetting, lightweight experiment runner).

## Highlights
- Socratic **multi‑agent debate** (Scout → Critic → Synthesiser) with **LangGraph** orchestration.
- **Semantic Scholar / arXiv / Papers With Code** fetchers with **dedup (cosine ≥ 0.92)**.
- **pgvector** memory, **LiteLLM** cost/latency‑aware routing, **server‑side DOT→SVG**.
<<<<<<< HEAD
- **Strict typing**, **ruff+black+isort+mypy** via pre‑commit.
=======
- **Strict typing**, **ruff+black+isort+mypy** via pre‑commit. 
>>>>>>> 0dd2eb4 (retrieval embeddings)
- Makefile targets you actually use (`make up`, `make check`, `make fmt`, etc.).
- Minimal React UI that streams run status and renders the SVG.

## Quickstart
```bash
make bootstrap
cp infra/.env.example .env
$EDITOR .env
make up
open http://localhost:5173
```

## Layout
```
backend/        # FastAPI + LangGraph + pgvector + LiteLLM
frontend/       # Vite/React minimal UI
infra/          # docker-compose, migrations, .env.example
.github/        # CI
scripts/        # helpers
```

## License
MIT
