import pytest
from app.db import Base, engine

@pytest.fixture(scope="session", autouse=True)
def _create_db():
    # Ensure tables exist for the DATABASE_URL used by tests (SQLite in CI)
    Base.metadata.create_all(bind=engine)
    yield
    # Optional cleanup:
    Base.metadata.drop_all(bind=engine)
