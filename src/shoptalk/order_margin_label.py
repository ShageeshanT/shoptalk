from __future__ import annotations

def order_margin_label(percent: int) -> str:
    try:
        value = int(percent)
    except (TypeError, ValueError):
        value = 0
    if value >= 50:
        return 'High margin'
    if value >= 25:
        return 'Good margin'
    if value >= 5:
        return 'Thin margin'
    return 'No margin'
