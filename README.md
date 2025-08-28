# Day 4 — FastAPI + Tests + Math Ops (add, multiply, divide, subtract)

![CI](https://github.com/Dalte123/fastapi-starter/actions/workflows/ci.yml/badge.svg)

A tiny, production-style starter: FastAPI app with tests and CI. No Docker required.

---

## Quick start (no Docker)

```bash
python -m venv .venv
# Windows PowerShell:
#   .\.venv\Scripts\Activate.ps1
# If PowerShell blocks it:
#   .\.venv\Scripts\activate.bat
# macOS/Linux:
#   source .venv/bin/activate

pip install -r requirements.txt
uvicorn app.main:app --reload
# App:     http://127.0.0.1:8000
# Health:  http://127.0.0.1:8000/healthz
# Docs:    http://127.0.0.1:8000/docs
