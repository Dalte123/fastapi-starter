# Day 1–2 — FastAPI + Tests + Docker + CI (Starter)

![CI](https://github.com/Dalte123/fastapi-starter/actions/workflows/ci.yml/badge.svg)

A tiny, production-style FastAPI starter with:
- Day 1: health check + echo endpoints, tests, CI
- Day 2: `/math/add` endpoint with validation + tests

---

## Quick start (no Docker)

```bash
python -m venv .venv
# PowerShell: .venv\Scripts\Activate.ps1
# Bash: source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
# http://127.0.0.1:8000/docs
