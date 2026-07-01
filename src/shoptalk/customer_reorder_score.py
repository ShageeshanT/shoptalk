from __future__ import annotations

def customer_reorder_score(past_orders: int, days_since_last: int, positive_feedback: int) -> int:
    raw_score = past_orders * 8 - days_since_last + positive_feedback * 10
    return max(0, min(100, int(raw_score)))
