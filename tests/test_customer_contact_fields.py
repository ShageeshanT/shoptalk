from fastapi.testclient import TestClient

from shoptalk.main import app

client = TestClient(app)


def test_customer_contact_fields_are_saved() -> None:
    business_response = client.post("/businesses", json={"name": "Contact Bakery"})
    business_id = business_response.json()["id"]

    response = client.post(
        "/customers",
        json={
            "business_id": business_id,
            "name": "Amani",
            "channel": "whatsapp",
            "phone": "+94770000000",
            "email": "amani@example.com",
            "tags": ["regular", "birthday"],
        },
    )

    assert response.status_code == 201
    body = response.json()
    assert body["phone"] == "+94770000000"
    assert body["email"] == "amani@example.com"
    assert body["tags"] == ["regular", "birthday"]
