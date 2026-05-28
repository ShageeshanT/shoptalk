from __future__ import annotations


def customer_segment_label(order_count: int, total_spend: float) -> str:
    if order_count >= 10 or total_spend >= 250_000:
        return "vip"
    if order_count >= 3 or total_spend >= 50_000:
        return "repeat"
    if order_count == 1 or total_spend > 0:
        return "new"
    return "prospect"


def customer_segment_priority(segment: str) -> int:
    priorities = {
        "vip": 100,
        "repeat": 70,
        "new": 40,
        "prospect": 10,
    }
    return priorities.get(segment, 0)
