from shoptalk.enums import OrderStatus
from shoptalk.schemas import Order, OrderRisk


def assess_order_risk(order: Order) -> OrderRisk:
    flags: list[str] = []
    score = 0

    if order.status in {OrderStatus.CONFIRMED, OrderStatus.PAYMENT_PENDING}:
        if order.total_amount and order.payment_status != "paid":
            flags.append("payment_not_confirmed")
            score += 35
        elif order.total_amount is None:
            flags.append("missing_total_amount")
            score += 20

    if order.status in {OrderStatus.PREPARING, OrderStatus.READY} and order.payment_status != "paid":
        flags.append("fulfilment_before_payment")
        score += 45

    if not order.delivery_date and order.status in {
        OrderStatus.CONFIRMED,
        OrderStatus.PAID,
        OrderStatus.PREPARING,
        OrderStatus.READY,
    }:
        flags.append("missing_delivery_date")
        score += 15

    if order.customer_id is None:
        flags.append("unlinked_customer")
        score += 10

    if score >= 60:
        level = "high"
    elif score >= 30:
        level = "medium"
    else:
        level = "low"

    return OrderRisk(order_id=order.id, level=level, score=min(score, 100), flags=flags)
