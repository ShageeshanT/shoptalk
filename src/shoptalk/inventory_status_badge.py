from __future__ import annotations

def inventory_status_badge(quantity: int) -> str:
    try:
        value = int(quantity)
    except (TypeError, ValueError):
        value = 0
    if value <= 0:
        return "Out of stock"
    if value <= 5:
        return "Low stock"
    if value <= 50:
        return "Healthy stock"
    return "Overstock"
