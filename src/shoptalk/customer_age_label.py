from __future__ import annotations

def customer_age_label(days: int) -> str:
    try:
        value = int(days)
    except (TypeError, ValueError):
        value = 0
    if value >= 365:
        return 'Long-term customer'
    if value >= 90:
        return 'Returning customer'
    if value >= 7:
        return 'New customer'
    return 'Fresh lead'
