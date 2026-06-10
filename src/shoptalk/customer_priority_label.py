from __future__ import annotations

def customer_priority_label(score: int) -> str:
    try:
        value = int(score)
    except (TypeError, ValueError):
        value = 0
    if value >= 80:
        return "High priority"
    if value >= 50:
        return "Medium priority"
    if value >= 20:
        return "Low priority"
    return "Watch"
