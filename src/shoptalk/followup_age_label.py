from __future__ import annotations

def followup_age_label(days: int) -> str:
    try:
        value = int(days)
    except (TypeError, ValueError):
        return 'Very overdue'
    if value <= 0:
        return 'Due today'
    if value <= 2:
        return 'Recently due'
    if value <= 7:
        return 'Overdue'
    return 'Very overdue'
