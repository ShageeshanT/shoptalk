from __future__ import annotations

def payment_urgency_label(days: int) -> str:
    try:
        value = int(days)
    except (TypeError, ValueError):
        return 'Future payment'
    if value <= 0:
        return 'Due now'
    if value <= 2:
        return 'Due soon'
    if value <= 7:
        return 'Upcoming payment'
    return 'Future payment'
