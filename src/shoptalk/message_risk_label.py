from __future__ import annotations

def message_risk_label(score: int) -> str:
    try:
        value = int(score)
    except (TypeError, ValueError):
        value = 0
    if value >= 80:
        return 'High risk'
    if value >= 50:
        return 'Medium risk'
    if value >= 20:
        return 'Low risk'
    return 'Safe'
