from shoptalk.enums import OrderStatus
from shoptalk.schemas import Order

_ACTIVE_STATUSES = {
    OrderStatus.NEW_INQUIRY,
    OrderStatus.CONFIRMED,
    OrderStatus.PAYMENT_PENDING,
    OrderStatus.PAID,
    OrderStatus.PREPARING,
    OrderStatus.READY,
}


def is_active_order(order: Order) -> bool:
    return order.status in _ACTIVE_STATUSES


def seller_next_step(order: Order) -> str:
    if order.status == OrderStatus.NEW_INQUIRY:
        return "Confirm item, date, delivery details, and price before accepting the order."
    if order.status == OrderStatus.PAYMENT_PENDING:
        return "Send payment instructions and hold fulfilment until payment is confirmed."
    if order.status == OrderStatus.PAID:
        return "Move the order into preparation and confirm the delivery or pickup window."
    if order.status == OrderStatus.PREPARING:
        return "Prepare the order and update the customer when it is ready."
    if order.status == OrderStatus.READY:
        return "Tell the customer the order is ready for pickup or delivery."
    if order.status == OrderStatus.CONFIRMED:
        return "Collect payment or mark payment status before fulfilment."
    if order.status == OrderStatus.DELIVERED:
        return "Order is complete. Ask for feedback only if appropriate."
    return "Order is cancelled. No seller action needed."
