# app/db.py
from __future__ import annotations

import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# --- 1) Connection URL ---
# Prefer env var so you don't hardcode secrets.
# Format: postgresql+psycopg2://USER:PASSWORD@HOST:PORT/DBNAME
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg2://fastapi_user:superSecretPass@localhost:5432/my_fastapi_db",
)

# --- 2) Engine (one per app) ---
# echo=False (quiet), pool_pre_ping=True prevents stale-connection errors
engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    # future-proof defaults; SQLAlchemy 2.0 style
)

# --- 3) Session factory (creates new Session objects) ---
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
)

# --- 4) Declarative Base for models ---
class Base(DeclarativeBase):
    pass

# --- 5) FastAPI dependency: yields a Session per-request ---
def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
