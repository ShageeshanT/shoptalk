from __future__ import annotations

from shoptalk.enums import OrderStatus
from shoptalk.order_value import order_value_band
from shoptalk.schemas import Order


def order_tags(order: Order) -> list[str]:
    tags = [order.status.value, f"value_{order_value_band(order)}"]
    if order.status in {OrderStatus.NEW_INQUIRY, OrderStatus.PAYMENT_PENDING}:
        tags.append("needs_attention")
    if order.delivery_date is None:
        tags.append("delivery_unset")
    return tags
