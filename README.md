# Day 4 – FastAPI + Tests + Math Operations (add, multiply, divide)

![CI](https://github.com/Dalte123/fastapi-starter/actions/workflows/ci.yml/badge.svg)

A tiny, production-style starter to get you moving step by step with FastAPI, testing, and CI.

---

## Quick start (no Docker)

```bash
python -m venv .venv
# PowerShell: .venv\Scripts\Activate.ps1
# Bash: source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
# http://127.0.0.1:8000/healthz
