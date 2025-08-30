# FastAPI Starter Project

Day 5 – FastAPI + Tests + Pydantic Models + Validation

✅ Implemented endpoints for:
- Health check (`/healthz`)
- Echo (`/echo`)
- Math operations: `add`, `subtract`, `multiply`, `divide`
- Unified math operation (`/math/operation`) using **Pydantic BaseModel**

✅ Tests cover:
- Happy paths for all operations
- Error handling for missing query params
- Division by zero
- Unsupported operations
- Validation errors (wrong types → Pydantic 422 response)
- JSON decode errors (invalid JSON payloads)

### How to run locally

```bash
# create virtual environment
python -m venv .venv
# activate it
.venv\Scripts\activate  # Windows PowerShell
# or
source .venv/bin/activate  # Mac/Linux

# install dependencies
pip install -r requirements.txt

# run the server
uvicorn app.main:app --reload
