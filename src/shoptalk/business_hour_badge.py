from __future__ import annotations

def business_hour_badge(open_flag: int) -> str:
    try:
        value = int(open_flag)
    except (TypeError, ValueError):
        value = 0
    if value >= 1:
        return 'Open now'
    if value >= 0:
        return 'Closed now'
    if value >= 2:
        return 'Special hours'
    return 'Hours unknown'
