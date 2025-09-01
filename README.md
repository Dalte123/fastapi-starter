# FastAPI Starter Project

Day 6 – FastAPI + Tests + Pydantic Models + Validation

---

## 📂 Features Implemented

✅ Endpoints:
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

---

## 📂 Project Structure
