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
    response = client.post("/draft-reply", json={"text": "Can I order two cupcakes today?"})
    assert response.status_code == 200
    body = response.json()
    assert body["requires_human_approval"] is True
    assert body["suggested_reply"]


def test_conversation_summary_returns_latest_signal() -> None:
    business_response = client.post("/businesses", json={"name": "Signal Bakery"})
    business_id = business_response.json()["id"]
    customer_response = client.post(
        "/customers",
        json={"business_id": business_id, "name": "Nadi", "channel": "whatsapp"},
    )
    customer_id = customer_response.json()["id"]

    message_response = client.post(
        "/messages",
        json={
            "business_id": business_id,
            "customer_id": customer_id,
            "sender": "customer",
            "text": "Can I order two cakes today?",
        },
    )
    assert message_response.status_code == 201

    summary_response = client.get(
        "/conversations/summary",
        params={"business_id": business_id, "customer_id": customer_id},
    )

    assert summary_response.status_code == 200
    body = summary_response.json()
    assert body["messages"] == 1
    assert body["customer_messages"] == 1
    assert body["signal"]["intent"] == "new_order"
    assert body["signal"]["needs_reply"] is True


def test_order_next_action_explains_seller_step() -> None:
    business_response = client.post("/businesses", json={"name": "Action Bakery"})
    business_id = business_response.json()["id"]
    order_response = client.post(
        "/orders",
        json={"business_id": business_id, "title": "Ribbon cake", "status": "payment_pending"},
    )
    order_id = order_response.json()["id"]

    action_response = client.get(f"/orders/{order_id}/next-action")

    assert action_response.status_code == 200
    body = action_response.json()
    assert body["active"] is True
    assert "payment" in body["next_step"].lower()


def test_order_payment_request_draft_includes_amount() -> None:
    business_response = client.post("/businesses", json={"name": "Pay Bakery"})
    business_id = business_response.json()["id"]
    order_response = client.post(
        "/orders",
        json={
            "business_id": business_id,
            "title": "Cupcake box",
            "total_amount": 2500,
            "status": "payment_pending",
        },
    )
    order_id = order_response.json()["id"]

    payment_response = client.get(f"/orders/{order_id}/payment-request")

    assert payment_response.status_code == 200
    body = payment_response.json()
    assert body["required"] is True
    assert "2,500" in body["message"]


def test_catalog_match_endpoint_returns_best_items() -> None:
    response = client.post(
        "/catalog/match",
        json={
            "message": "Do you have chocolate cake?",
            "catalog": [
                {"name": "Chocolate Cake", "price": 3500, "tags": ["cake", "birthday"]},
                {"name": "Vanilla Cupcakes", "price": 1200, "tags": ["cupcake"]},
            ],
        },
    )

    assert response.status_code == 200
    body = response.json()
    assert body[0]["item"]["name"] == "Chocolate Cake"


def test_thread_endpoint_returns_messages_in_order() -> None:
    business_response = client.post("/businesses", json={"name": "Thread Bakery"})
    business_id = business_response.json()["id"]
    customer_response = client.post(
        "/customers",
        json={"business_id": business_id, "name": "Savi", "channel": "whatsapp"},
    )
    customer_id = customer_response.json()["id"]
    client.post(
        "/messages",
        json={
            "business_id": business_id,
            "customer_id": customer_id,
            "sender": "customer",
            "text": "Hi, do you have cupcakes?",
        },
    )
    client.post(
        "/messages",
        json={
            "business_id": business_id,
            "customer_id": customer_id,
            "sender": "assistant",
            "text": "Yes, what quantity do you need?",
        },
    )

    response = client.get("/threads", params={"business_id": business_id, "customer_id": customer_id})

    assert response.status_code == 200
    body = response.json()
    assert len(body["messages"]) == 2
    assert body["messages"][0]["direction"] == "customer"
    assert body["messages"][1]["display_name"] == "ShopTalk"


def test_catalog_items_can_be_created_and_listed() -> None:
    business_response = client.post("/businesses", json={"name": "Catalog Bakery"})
    business_id = business_response.json()["id"]

    create_response = client.post(
        "/catalog-items",
        json={
            "business_id": business_id,
            "name": "Mini Brownie Box",
            "price": 1800,
            "tags": ["brownie", "box"],
        },
    )

    assert create_response.status_code == 201
    list_response = client.get("/catalog-items", params={"business_id": business_id})
    assert list_response.status_code == 200
    items = list_response.json()
    assert any(item["name"] == "Mini Brownie Box" for item in items)


def test_checkout_draft_includes_order_total() -> None:
    business_response = client.post("/businesses", json={"name": "Checkout Bakery", "currency": "LKR"})
    business_id = business_response.json()["id"]
    order_response = client.post(
        "/orders",
        json={"business_id": business_id, "title": "Birthday Cake", "total_amount": 5200},
    )
    order_id = order_response.json()["id"]

    response = client.get(f"/checkout/orders/{order_id}/draft")

    assert response.status_code == 200
    body = response.json()
    assert body["currency"] == "LKR"
    assert "5,200" in body["message"]


def test_customer_profile_groups_related_records() -> None:
    business_response = client.post("/businesses", json={"name": "Profile Bakery"})
    business_id = business_response.json()["id"]
    customer_response = client.post(
        "/customers",
        json={"business_id": business_id, "name": "Nishi", "channel": "whatsapp"},
    )
    customer_id = customer_response.json()["id"]
    client.post("/orders", json={"business_id": business_id, "customer_id": customer_id, "title": "Cake"})
    client.post(
        "/messages",
        json={"business_id": business_id, "customer_id": customer_id, "text": "Need a cake"},
    )

    response = client.get(f"/profiles/customers/{customer_id}")

    assert response.status_code == 200
    body = response.json()
    assert body["customer"]["name"] == "Nishi"
    assert len(body["orders"]) >= 1
    assert len(body["messages"]) >= 1


def test_sales_funnel_counts_order_statuses() -> None:
    business_response = client.post("/businesses", json={"name": "Funnel Bakery"})
    business_id = business_response.json()["id"]
    client.post("/orders", json={"business_id": business_id, "title": "Cake", "status": "new_inquiry"})
    client.post("/orders", json={"business_id": business_id, "title": "Brownies", "status": "paid"})

    response = client.get("/sales/funnel")

    assert response.status_code == 200
    body = response.json()
    assert body["new_inquiries"] >= 1
    assert body["paid"] >= 1
