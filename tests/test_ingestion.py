from fastapi.testclient import TestClient

from shoptalk.main import app

client = TestClient(app)


def test_ingestion_endpoint_stores_channel_message_metadata():
    business_response = client.post("/businesses", json={"name": "Ingest Bakery"})
    business_id = business_response.json()["id"]

    response = client.post(
        "/ingestion/messages",
        json={
            "business_id": business_id,
            "channel": "whatsapp",
            "conversation_id": "wa-thread-1",
            "sender_id": "customer-1",
            "text": "Hi, can I order cupcakes tomorrow?",
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["channel"] == "whatsapp"
    assert body["external_message_id"] == "wa-thread-1"
    assert body["sender"] == "customer"
