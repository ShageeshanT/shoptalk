from __future__ import annotations

def stock_turnover_label(days: int) -> str:
    try:
        value = int(days)
    except (TypeError, ValueError):
        return 'Stale stock'
    if value <= 7:
        return 'Fast moving'
    if value <= 30:
        return 'Normal moving'
    if value <= 90:
        return 'Slow moving'
    return 'Stale stock'
