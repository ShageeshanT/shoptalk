from fastapi.testclient import TestClient

from shoptalk.main import app

client = TestClient(app)


def test_ingestion_reuses_existing_external_message() -> None:
    business_response = client.post("/businesses", json={"name": "Idempotent Bakery"})
    business_id = business_response.json()["id"]
    payload = {
        "business_id": business_id,
        "channel": "whatsapp",
        "conversation_id": "wa-message-1",
        "sender_id": "customer-1",
        "text": "Need cupcakes",
    }

    first = client.post("/ingestion/messages", json=payload)
    second = client.post("/ingestion/messages", json=payload)

    assert first.status_code == 201
    assert second.status_code == 201
    assert second.json()["id"] == first.json()["id"]
