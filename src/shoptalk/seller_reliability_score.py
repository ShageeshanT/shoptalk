from __future__ import annotations

def seller_reliability_score(completed_orders: int, late_orders: int, missed_replies: int) -> int:
    raw_score = completed_orders * 6 - late_orders * 8 - missed_replies * 5
    return max(0, min(100, int(raw_score)))
