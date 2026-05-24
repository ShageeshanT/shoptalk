from fastapi import FastAPI
from fastapi.testclient import TestClient

from shoptalk.db_session import create_db_engine, create_session_factory, initialize_database
from shoptalk.routes_database import router
import shoptalk.routes_database as routes_database


def test_database_routes_report_health_and_readiness(monkeypatch):
    engine = create_db_engine("sqlite+pysqlite:///:memory:")
    initialize_database(engine)
    factory = create_session_factory(engine)
    app = FastAPI(); app.include_router(router)
    def override_db_session():
        session = factory()
        try:
            yield session
        finally:
            session.close()

    app.dependency_overrides[routes_database.get_db_session] = override_db_session
    monkeypatch.setattr(routes_database, "get_engine", lambda: engine)
    client = TestClient(app)
    assert client.get("/database/health").json() == {"database": "ok"}
    assert client.get("/database/readiness").json()["ready"] is True
