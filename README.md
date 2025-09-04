FastAPI Starter Project

Day 7 – FastAPI + Token-Based Authentication

✅ Implemented endpoints for:

Health check (/healthz)

Echo (/echo)

Math operations with query params: add, subtract, multiply, divide

Unified math operation (/math/operation) using Pydantic BaseModel

✅ Refactor highlights:

Moved all math logic into app/math_utils.py as pure Python functions.

Utility functions raise ValueError for invalid input (e.g., divide by zero, unsupported operations).

FastAPI routes (main.py) catch ValueError and translate into HTTPException(status_code=400).

Separation of concerns:

math_utils.py → business logic

main.py → API layer, validation, error mapping

✅ Authentication layer:

Added authfunc in app/auth.py.

All math routes now require a static token via the Authorization header: