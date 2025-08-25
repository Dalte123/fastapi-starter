# Day 1 – FastAPI + Tests + Docker + CI (Starter)

A tiny, production-style starter to get you moving on Day 1.

## Quick start (no Docker)
```bash
python -m venv .venv
# PowerShell: .venv\Scripts\Activate.ps1
# Bash: source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
# http://127.0.0.1:8000/healthz
```

## Run tests
```bash
pytest -q
```

## With Docker
```bash
docker build -t day1-fastapi .
docker run -p 8000:8000 day1-fastapi
# http://127.0.0.1:8000/healthz
```
