from __future__ import annotations

def product_visibility_label(views: int) -> str:
    try:
        value = int(views)
    except (TypeError, ValueError):
        value = 0
    if value >= 1000:
        return 'Hot product'
    if value >= 100:
        return 'Visible product'
    if value >= 1:
        return 'Low visibility'
    return 'Unseen product'
