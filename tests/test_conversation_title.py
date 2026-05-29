from uuid import uuid4

from shoptalk.conversation_title import conversation_title, truncate_conversation_title
from shoptalk.schemas import Customer, Order


def test_conversation_title_prefers_latest_order() -> None:
    business_id = uuid4()
    customer = Customer(business_id=business_id, name="Amani", channel="whatsapp")
    order = Order(business_id=business_id, title="Chocolate cake")

    assert conversation_title(customer, order) == "Amani · Chocolate cake"


def test_conversation_title_falls_back_to_channel_or_unknown() -> None:
    customer = Customer(business_id=uuid4(), name="Nadi", channel="instagram")

    assert conversation_title(customer) == "Nadi · instagram"
    assert conversation_title(None) == "Unknown customer"


def test_truncate_conversation_title() -> None:
    assert truncate_conversation_title("Short", limit=8) == "Short"
    assert truncate_conversation_title("Chocolate cupcake order", limit=10) == "Chocolate…"
