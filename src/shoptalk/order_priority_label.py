from __future__ import annotations

def order_priority_label(hours_until_due: float) -> str:
    if hours_until_due <= 2: return "urgent"
    if hours_until_due <= 24: return "today"
    return "normal"
