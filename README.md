FastAPI Starter Project

Final README – Database + Users + Auth + Tests

✅ Implemented endpoints

Health check: GET /healthz

Echo: GET /echo?msg=...

Math (Bearer token required):

GET /math/add|subtract|multiply|divide?a=&b=

POST /math/operation ({"op":"add|subtract|multiply|divide","a":...,"b":...})

Users:

POST /users/ – create user

GET /users/ – list users

GET /users/{id} – get by id

GET /users/by_email?email=... – get by email

✅ Database integration (PostgreSQL + SQLAlchemy)

SQLAlchemy engine + session factory + get_db() dependency

Tables auto-created on startup (learning phase; migrations later with Alembic)

User model: id, name, email (UNIQUE), created_at

✅ Behavior & validation (Users)

Normalization:

Email: trim + lowercase (stored normalized)

Name: trim (casing preserved)

Policy:

Only .com or .ca emails accepted → otherwise 422

Uniqueness:

Duplicate email → 409

Status codes:

201 create, 200 read, 404 not found, 409 conflict, 422 validation

✅ Separation of concerns

app/db.py → engine, session, Base, get_db() (connection pooling)

app/models.py → ORM tables (e.g., User)

app/schemas.py → request/response models (Pydantic, EmailStr, from_attributes=True)

app/auth.py → Bearer-token check (used by math endpoints)

app/main.py → routes, validation/error mapping, startup table creation

app/math_utils.py → pure business logic for math endpoints

✅ Tests & CI

Pytest suite covering math routes, auth, and users (create, by-email happy path, not found, invalid TLD, empty fields)

GitHub Actions workflow runs tests using SQLite via DATABASE_URL=sqlite:///./test.db

requirements.txt checked into repo for CI install



Quick start

Reqs: Python 3.11+, Postgres 14+ (local)

Install

python -m pip install -U pip
pip install -r requirements.txt

# (optional) DATABASE_URL env; else default in code is used
# DATABASE_URL=postgresql+psycopg2://fastapi_user:PASS@localhost:5432/my_fastapi_db
uvicorn app.main:app --reload
# http://127.0.0.1:8000  |  /docs

Project structure (key files)
app/
  main.py        # routes, startup
  auth.py        # Bearer token check (math)
  math_utils.py  # pure math functions
  db.py          # engine, Session, Base, get_db()
  models.py      # User model
  schemas.py     # Pydantic models (EmailStr, from_attributes)
tests/
  test_app.py
.github/workflows/ci.yml

Endpoints

Health/Echo

GET /healthz

GET /echo?msg=...

Math (requires Authorization: Bearer superSecret123)

GET /math/add|subtract|multiply|divide?a=&b=

POST /math/operation → {result}

Users

POST /users/ → 201 (create)

GET /users/ → 200 (list)

GET /users/{id} → 200/404 (by id)

GET /users/by_email?email=... → 200/404/422 (by email)

Users: behavior & validation

Normalization: email = trim + lowercase (stored normalized); name = trim (casing preserved)

Policy: only .com / .ca emails accepted → 422 otherwise

Uniqueness: duplicate email → 409

Status codes: 201 create, 200 read, 404 not found, 409 conflict, 422 validation

Database

SQLAlchemy engine + session dependency (get_db()), tables auto-created on startup (learning phase; migrations later with Alembic).

Local Postgres URL example:
postgresql+psycopg2://fastapi_user:PASS@localhost:5432/my_fastapi_db

Testing & CI

Tests: pytest -q

CI (GitHub Actions): installs requirements.txt, sets DATABASE_URL=sqlite:///./test.db, runs tests.
