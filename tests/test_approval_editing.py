from fastapi.testclient import TestClient

from shoptalk.main import app

client = TestClient(app)


def test_approval_draft_can_be_edited_before_approval() -> None:
    draft_response = client.post("/approvals", json={"message": "Hi, pickup is okay"})
    draft_id = draft_response.json()["id"]

    edit_response = client.patch(f"/approvals/{draft_id}", json={"message": "Hi, pickup tomorrow is okay"})
    approve_response = client.post(f"/approvals/{draft_id}/approve")

    assert edit_response.status_code == 200
    assert edit_response.json()["edited_message"] == "Hi, pickup tomorrow is okay"
    assert approve_response.json()["status"] == "approved"
    assert approve_response.json()["edited_message"] == "Hi, pickup tomorrow is okay"
