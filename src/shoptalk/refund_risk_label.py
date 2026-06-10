from __future__ import annotations

def refund_risk_label(score: int) -> str:
    try:
        value = int(score)
    except (TypeError, ValueError):
        value = 0
    if value >= 80:
        return 'High refund risk'
    if value >= 50:
        return 'Medium refund risk'
    if value >= 20:
        return 'Low refund risk'
    return 'No refund risk'
