from __future__ import annotations

def return_window_label(days: int) -> str:
    try:
        value = int(days)
    except (TypeError, ValueError):
        return 'Extended return'
    if value <= 0:
        return 'Return closed'
    if value <= 7:
        return 'Return closing soon'
    if value <= 30:
        return 'Return open'
    return 'Extended return'
