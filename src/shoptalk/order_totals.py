"""Order total calculation helpers."""

from __future__ import annotations


def order_subtotal(prices: list[float]) -> float:
    """Return the subtotal for order line prices."""

    return round(sum(prices), 2)


def order_total(prices: list[float], delivery_fee: float = 0.0, discount: float = 0.0) -> float:
    """Return a non-negative final order total."""

    return max(round(order_subtotal(prices) + delivery_fee - discount, 2), 0.0)
