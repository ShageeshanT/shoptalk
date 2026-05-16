from shoptalk.enums import OrderStatus
from shoptalk.schemas import Order

_PAYABLE_STATUSES = {
    OrderStatus.CONFIRMED,
    OrderStatus.PAYMENT_PENDING,
}


def payment_required(order: Order) -> bool:
    return order.status in _PAYABLE_STATUSES and order.total_amount is not None


def build_payment_note(order: Order) -> str:
    if not payment_required(order):
        return "No payment request is needed for this order right now."

    amount = f"Rs. {order.total_amount:,.0f}"
    return f"Please complete the payment of {amount} so we can confirm your order."
