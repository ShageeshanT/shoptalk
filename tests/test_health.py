"""Tests for the /health endpoint."""

from fastapi.testclient import TestClient

from shoptalk.main import app


client = TestClient(app)


def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


def test_health_includes_version():
    response = client.get("/health")
    data = response.json()
    assert "version" in data
    assert data["version"] != ""


def test_health_includes_uptime():
    response = client.get("/health")
    data = response.json()
    assert "uptime_seconds" in data
    assert data["uptime_seconds"] >= 0
