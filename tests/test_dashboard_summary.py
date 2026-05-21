from fastapi.testclient import TestClient

from shoptalk.main import app

client = TestClient(app)


def test_dashboard_summary_includes_messages_and_approvals() -> None:
    business_response = client.post("/businesses", json={"name": "Dashboard Bakery"})
    business_id = business_response.json()["id"]
    client.post("/messages", json={"business_id": business_id, "text": "Need cake"})
    client.post("/approvals", json={"business_id": business_id, "message": "Sure"})

    response = client.get("/dashboard/summary")

    assert response.status_code == 200
    body = response.json()
    assert body["messages"] >= 1
    assert body["approval_drafts"] >= 1
