from __future__ import annotations

def daily_sales_label(amount: int) -> str:
    try:
        value = int(amount)
    except (TypeError, ValueError):
        value = 0
    if value >= 100000:
        return 'Strong sales day'
    if value >= 25000:
        return 'Good sales day'
    if value >= 1:
        return 'Sales recorded'
    return 'No sales'
