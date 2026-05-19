from uuid import uuid4

from shoptalk.enums import OrderStatus
from shoptalk.order_risk import assess_order_risk
from shoptalk.schemas import Order


def test_order_risk_flags_fulfilment_before_payment() -> None:
    risk = assess_order_risk(
        Order(
            business_id=uuid4(),
            title="Birthday cake",
            status=OrderStatus.PREPARING,
            payment_status="pending",
            total_amount=6500,
        )
    )

    assert risk.level == "high"
    assert "fulfilment_before_payment" in risk.flags
    assert "missing_delivery_date" in risk.flags


def test_order_risk_stays_low_for_paid_scheduled_order() -> None:
    risk = assess_order_risk(
        Order(
            business_id=uuid4(),
            customer_id=uuid4(),
            title="Cupcake box",
            status=OrderStatus.PAID,
            payment_status="paid",
            total_amount=3500,
            delivery_date="2026-05-20",
        )
    )

    assert risk.level == "low"
    assert risk.flags == []
