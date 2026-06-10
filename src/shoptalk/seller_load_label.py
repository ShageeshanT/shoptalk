from __future__ import annotations

def seller_load_label(count: int) -> str:
    try:
        value = int(count)
    except (TypeError, ValueError):
        value = 0
    if value >= 50:
        return 'Heavy load'
    if value >= 20:
        return 'Busy load'
    if value >= 5:
        return 'Light load'
    return 'Clear load'
