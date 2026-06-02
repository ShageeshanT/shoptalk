def is_repeat_customer(order_count: int) -> bool:
    return order_count >= 2


def repeat_customer_label(order_count: int) -> str:
    if order_count >= 5:
        return "loyal"
    if order_count >= 2:
        return "repeat"
    return "new"
