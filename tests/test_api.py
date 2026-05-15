from fastapi.testclient import TestClient

from shoptalk.main import app

client = TestClient(app)


def test_business_customer_order_followup_flow() -> None:
    business_response = client.post("/businesses", json={"name": "Cake Desk"})
    assert business_response.status_code == 201
    business_id = business_response.json()["id"]

    customer_response = client.post(
        "/customers",
        json={"business_id": business_id, "name": "Amani", "channel": "whatsapp"},
    )
    assert customer_response.status_code == 201
    customer_id = customer_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={
            "business_id": business_id,
            "customer_id": customer_id,
            "title": "2 cupcakes",
            "total_amount": 1200,
        },
    )
    assert order_response.status_code == 201
    order_id = order_response.json()["id"]

    follow_up_response = client.post(
        "/follow-ups",
        json={
            "business_id": business_id,
            "customer_id": customer_id,
            "order_id": order_id,
            "title": "Confirm pickup time",
        },
    )
    assert follow_up_response.status_code == 201

    summary_response = client.get("/dashboard/summary")
    assert summary_response.status_code == 200
    assert summary_response.json()["businesses"] >= 1
    assert summary_response.json()["open_follow_ups"] >= 1


def test_missing_business_rejected_for_customer() -> None:
    response = client.post(
        "/customers",
        json={"business_id": "00000000-0000-0000-0000-000000000000", "name": "Ghost"},
    )
    assert response.status_code == 404


def test_draft_reply_endpoint_returns_human_approved_reply():
    response = client.post("/draft-reply", json={"message": "Can I order two cupcakes today?"})
    assert response.status_code == 200
    body = response.json()
    assert body["requires_human_approval"] is True
    assert body["suggested_reply"]
