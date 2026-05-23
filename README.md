# InferPilot

InferPilot is a local AI gateway that reduces LLM costs automatically using routing, caching, and usage analytics.

> Reduce AI costs by 60% automatically.

## MVP Features

- OpenAI-compatible `/v1/chat/completions` endpoint
- `model: auto` smart routing
- Exact + semantic cache
- Usage, cache, model, request, and savings analytics
- Local benchmark and terminal dashboard scripts
- FastAPI backend with SQLite for local development
- Next.js dashboard UI
- Docker-ready setup

## Backend Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
make run
```

Open API docs:

```text
http://localhost:8000/docs
```

## Frontend Setup

```bash
cd web
npm install
cp .env.local.example .env.local
npm run dev
```

Open dashboard:

```text
http://localhost:3000
```

## Benchmark

With backend running:

```bash
python scripts/benchmark_savings.py
python scripts/dashboard.py
```

## V1 Philosophy

Keep V1 focused. Do not add billing, teams, RBAC, enterprise auth, agents, RAG, custom models, or fine-tuning until savings are validated with real users.
