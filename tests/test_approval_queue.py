from fastapi.testclient import TestClient

from shoptalk.main import app

client = TestClient(app)


def test_approval_queue_can_filter_drafts_by_status_and_business() -> None:
    business_response = client.post("/businesses", json={"name": "Approval Queue Bakery"})
    business_id = business_response.json()["id"]
    draft_response = client.post("/approvals", json={"business_id": business_id, "message": "First reply"})
    client.post("/approvals", json={"message": "Other reply"})
    client.post(f"/approvals/{draft_response.json()['id']}/approve")

    response = client.get(f"/approvals?business_id={business_id}&status=approved")

    assert response.status_code == 200
    drafts = response.json()
    assert len(drafts) == 1
    assert drafts[0]["message"] == "First reply"
    assert drafts[0]["status"] == "approved"
