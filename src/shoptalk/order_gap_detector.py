REQUIRED_FIELDS = ("customer", "items", "delivery", "payment")


def order_gaps(order: dict) -> list[str]:
    return [field for field in REQUIRED_FIELDS if not order.get(field)]
