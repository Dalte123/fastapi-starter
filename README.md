FastAPI Starter Project

Day 9 – Database Integration (PostgreSQL + SQLAlchemy)

✅ Implemented endpoints for:

Health check (/healthz)

Echo (/echo)

Users: create/list/get-by-id

POST /users/

GET /users/

GET /users/{id}

(Math endpoints from earlier remain available.)

✅ Database integration:

Added PostgreSQL connection via SQLAlchemy engine + session factory.

Tables are created on app startup for learning (Alembic migrations planned later).

User model enforces unique email and stores created_at timestamp.

✅ Refactor highlights:

Introduced app/db.py with Engine, SessionLocal, Base, and request-scoped get_db() dependency.

Added app/models.py with User (id, name, email UNIQUE, created_at).

Added app/schemas.py with UserCreate (Pydantic EmailStr) and UserRead (from_attributes enabled).

✅ Separation of concerns:

db.py → connection pool, sessions, Base, FastAPI dependency

models.py → database tables (ORM models)

schemas.py → API request/response validation (Pydantic)

main.py → routes, validation, error mapping, startup create_all()

✅ Authentication layer:

Existing Bearer token auth in app/auth.py continues to protect math routes.

To call math routes, include the header:
Authorization: Bearer superSecret123