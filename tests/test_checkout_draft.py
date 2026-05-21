from fastapi.testclient import TestClient

from shoptalk.main import app

client = TestClient(app)


def test_checkout_draft_includes_payment_instructions() -> None:
    business_response = client.post("/businesses", json={"name": "Checkout Bakery", "currency": "LKR"})
    business_id = business_response.json()["id"]
    order_response = client.post(
        "/orders", json={"business_id": business_id, "title": "Cake order", "total_amount": 2500}
    )

    response = client.get(f"/checkout/orders/{order_response.json()['id']}/draft")

    assert response.status_code == 200
    body = response.json()
    assert body["payment_instructions"]
    assert "LKR 2,500" in body["message"]
    assert "receipt" in body["message"].lower()
