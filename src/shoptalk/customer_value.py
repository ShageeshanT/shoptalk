"""Customer value labels for dashboard summaries."""

from __future__ import annotations


def customer_value_label(order_count: int, total_spend: float) -> str:
    """Return a compact customer value label."""

    if order_count >= 10 or total_spend >= 100_000:
        return "vip"
    if order_count >= 3 or total_spend >= 25_000:
        return "repeat"
    if order_count == 1:
        return "new_buyer"
    return "prospect"
