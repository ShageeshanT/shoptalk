from fastapi.testclient import TestClient

from shoptalk.main import app

client = TestClient(app)


def test_messages_can_be_searched_and_limited() -> None:
    business_response = client.post("/businesses", json={"name": "Search Bakery"})
    business_id = business_response.json()["id"]
    client.post("/messages", json={"business_id": business_id, "text": "Need chocolate cake"})
    client.post("/messages", json={"business_id": business_id, "text": "Need vanilla cupcakes"})

    response = client.get(f"/messages?business_id={business_id}&search=vanilla&limit=1")

    assert response.status_code == 200
    messages = response.json()
    assert len(messages) == 1
    assert messages[0]["text"] == "Need vanilla cupcakes"
