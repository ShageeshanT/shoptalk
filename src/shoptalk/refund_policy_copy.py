def refund_policy_copy(order_status: str) -> str:
    if order_status in {"cancelled", "new_inquiry"}:
        return "Refund or cancellation can be handled before preparation starts."
    if order_status in {"preparing", "ready"}:
        return "Refund options may be limited because the order is already in progress."
    return "Refund handling depends on the seller policy for this order."
