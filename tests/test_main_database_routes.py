from fastapi.testclient import TestClient

from shoptalk.main import app


def test_main_includes_database_readiness_route():
    client = TestClient(app)
    response = client.get("/database/readiness")
    assert response.status_code == 200
    assert "required_tables" in response.json()
