from fastapi.testclient import TestClient

from shoptalk.main import app

client = TestClient(app)


def test_health_check_covers_operational_stores() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    checks = {check["name"]: check for check in response.json()["checks"]}
    assert response.json()["status"] == "ok"
    assert checks["approvals"]["ok"] is True
    assert checks["follow_ups"]["ok"] is True
