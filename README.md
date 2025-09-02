# FastAPI Starter Project

Day 6 – FastAPI + Refactor with Utility Module

✅ Implemented endpoints for:
- Health check (`/healthz`)
- Echo (`/echo`)
- Math operations with query params: `add`, `subtract`, `multiply`, `divide`
- Unified math operation (`/math/operation`) using **Pydantic BaseModel**

✅ Refactor highlights:
- Moved all math logic into `app/math_utils.py` as pure Python functions.
- Utility functions raise `ValueError` for invalid input (e.g., divide by zero, unsupported operations).
- FastAPI routes (`main.py`) catch `ValueError` and translate into `HTTPException(status_code=400)`.
- Separation of concerns:
  - **`math_utils.py`** → business logic
  - **`main.py`** → API layer, validation, error mapping

✅ Tests cover:
- Happy paths for all operations
- Missing query params
- Division by zero
- Unsupported operations
- Validation errors (wrong types → 422 from Pydantic)

---

## Quick Start (no Docker)

```bash
# create virtual environment
python -m venv .venv

# activate it
.venv\Scripts\activate    # Windows PowerShell
# or
source .venv/bin/activate  # Mac/Linux

# install dependencies
pip install -r requirements.txt

# run the server
uvicorn app.main:app --reload
