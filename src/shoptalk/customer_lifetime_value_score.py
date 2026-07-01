from __future__ import annotations

def customer_lifetime_value_score(average_order_value: float, repeat_orders: int, loyalty_months: int) -> int:
    raw_score = average_order_value * 0.4 + repeat_orders * 8 + loyalty_months * 2
    return max(0, min(100, int(raw_score)))
