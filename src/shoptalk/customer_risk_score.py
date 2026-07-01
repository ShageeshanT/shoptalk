from __future__ import annotations

def customer_risk_score(overdue_messages: int, unpaid_orders: int, complaint_count: int) -> int:
    score = overdue_messages * 2 + unpaid_orders * 3 + complaint_count * 4
    return max(0, min(100, score * 5))
