# Day 3 – FastAPI + Tests (Add & Multiply)

![CI](https://github.com/Dalte123/fastapi-starter/actions/workflows/ci.yml/badge.svg)

A tiny, production-style starter that evolves step by step.

---

## Quick start (no Docker)
```bash
python -m venv .venv
# PowerShell: .venv\Scripts\Activate.ps1
# Bash: source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
# http://127.0.0.1:8000/healthz
