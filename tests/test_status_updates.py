from fastapi.testclient import TestClient

from shoptalk.main import app

client = TestClient(app)


def test_can_mark_seller_task_done():
    business_response = client.post("/businesses", json={"name": "Task Bakery"})
    business_id = business_response.json()["id"]

    task_response = client.post(
        "/tasks",
        json={"business_id": business_id, "title": "Reply to cake inquiry", "priority": "high"},
    )
    task_id = task_response.json()["id"]

    update_response = client.patch(f"/tasks/{task_id}", json={"done": True})

    assert update_response.status_code == 200
    assert update_response.json()["done"] is True


def test_can_close_follow_up_status():
    business_response = client.post("/businesses", json={"name": "Follow Up Bakery"})
    business_id = business_response.json()["id"]

    follow_up_response = client.post(
        "/follow-ups",
        json={"business_id": business_id, "title": "Ask if payment was sent"},
    )
    follow_up_id = follow_up_response.json()["id"]

    update_response = client.patch(f"/follow-ups/{follow_up_id}/status", json={"status": "done"})

    assert update_response.status_code == 200
    assert update_response.json()["status"] == "done"


def test_can_update_order_status():
    business_response = client.post("/businesses", json={"name": "Order Bakery"})
    business_id = business_response.json()["id"]

    order_response = client.post(
        "/orders",
        json={"business_id": business_id, "title": "Brownies", "total_amount": 2500},
    )
    order_id = order_response.json()["id"]

    update_response = client.patch(f"/orders/{order_id}/status", json={"status": "paid"})

    assert update_response.status_code == 200
    assert update_response.json()["status"] == "paid"


def test_can_update_customer_notes():
    business_response = client.post("/businesses", json={"name": "Notes Bakery"})
    business_id = business_response.json()["id"]

    customer_response = client.post(
        "/customers",
        json={"business_id": business_id, "name": "Nila"},
    )
    customer_id = customer_response.json()["id"]

    update_response = client.patch(f"/customers/{customer_id}/notes", json={"notes": "Prefers WhatsApp updates."})

    assert update_response.status_code == 200
    assert update_response.json()["notes"] == "Prefers WhatsApp updates."
