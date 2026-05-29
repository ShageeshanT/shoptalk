from uuid import uuid4

from shoptalk.customer_risk import customer_risk_flags
from shoptalk.enums import FollowUpStatus, OrderStatus
from shoptalk.schemas import Customer, FollowUp, Order


def test_customer_risk_flags_missing_route_and_pending_work() -> None:
    business_id = uuid4()
    customer = Customer(business_id=business_id, name="Amani", channel="whatsapp")
    orders = [
        Order(business_id=business_id, title="Cupcakes", status=OrderStatus.PAYMENT_PENDING),
        Order(business_id=business_id, title="Brownies", status=OrderStatus.CONFIRMED),
    ]
    follow_ups = [
        FollowUp(business_id=business_id, title="Confirm pickup", status=FollowUpStatus.OPEN)
    ]

    flags = customer_risk_flags(customer, orders, follow_ups)

    assert flags == [
        "missing_contact_route",
        "open_follow_up",
        "payment_pending",
        "multiple_active_orders",
    ]


def test_customer_risk_flags_new_customer() -> None:
    customer = Customer(
        business_id=uuid4(),
        name="Nadi",
        channel="whatsapp",
        phone="+94700000000",
    )

    assert customer_risk_flags(customer, [], []) == ["new_customer"]
