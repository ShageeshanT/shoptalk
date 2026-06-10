from __future__ import annotations

def inbox_pressure_label(count: int) -> str:
    try:
        value = int(count)
    except (TypeError, ValueError):
        value = 0
    if value >= 100:
        return 'Inbox overloaded'
    if value >= 30:
        return 'Inbox busy'
    if value >= 1:
        return 'Inbox active'
    return 'Inbox clear'
