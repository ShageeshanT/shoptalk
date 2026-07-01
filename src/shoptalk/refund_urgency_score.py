from __future__ import annotations

def refund_urgency_score(days_waiting: int, complaint_count: int, order_value_band: int) -> int:
    raw_score = days_waiting * 4 + complaint_count * 12 + order_value_band * 5
    return max(0, min(100, int(raw_score)))
