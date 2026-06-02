from shoptalk.enums import OrderStatus


def order_priority(status: OrderStatus, overdue: bool = False, paid: bool = False) -> str:
    if overdue:
        return "urgent"
    if status == OrderStatus.PAYMENT_PENDING:
        return "payment"
    if paid and status in {OrderStatus.CONFIRMED, OrderStatus.PREPARING}:
        return "fulfillment"
    if status == OrderStatus.NEW_INQUIRY:
        return "reply"
    return "normal"
