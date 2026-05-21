from fastapi.testclient import TestClient

from shoptalk.main import app

client = TestClient(app)


def test_customer_timeline_combines_messages_orders_and_followups() -> None:
    business_response = client.post("/businesses", json={"name": "Timeline Bakery"})
    business_id = business_response.json()["id"]
    customer_response = client.post("/customers", json={"business_id": business_id, "name": "Navi"})
    customer_id = customer_response.json()["id"]

    client.post("/messages", json={"business_id": business_id, "customer_id": customer_id, "text": "Need cake"})
    order_response = client.post(
        "/orders", json={"business_id": business_id, "customer_id": customer_id, "title": "Chocolate cake"}
    )
    client.post(
        "/follow-ups",
        json={
            "business_id": business_id,
            "customer_id": customer_id,
            "order_id": order_response.json()["id"],
            "title": "Confirm pickup",
        },
    )

    response = client.get(f"/timelines/customers/{customer_id}")

    assert response.status_code == 200
    event_types = {event["event_type"] for event in response.json()["events"]}
    assert {"message", "order", "follow_up"}.issubset(event_types)
