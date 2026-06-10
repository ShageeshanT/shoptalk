from __future__ import annotations

def order_size_label(amount: int) -> str:
    try:
        value = int(amount)
    except (TypeError, ValueError):
        value = 0
    if value >= 50000:
        return 'Large order'
    if value >= 15000:
        return 'Medium order'
    if value >= 1000:
        return 'Small order'
    return 'Tiny order'
