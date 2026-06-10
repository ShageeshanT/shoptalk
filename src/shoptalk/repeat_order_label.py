from __future__ import annotations

def repeat_order_label(count: int) -> str:
    try:
        value = int(count)
    except (TypeError, ValueError):
        value = 0
    if value >= 10:
        return 'Loyal buyer'
    if value >= 3:
        return 'Repeat buyer'
    if value >= 1:
        return 'Second order'
    return 'First order'
