from __future__ import annotations

def delivery_fee_badge(fee: int) -> str:
    try:
        value = int(fee)
    except (TypeError, ValueError):
        return "Custom delivery fee"
    if value <= 0:
        return "Free delivery"
    if value <= 500:
        return "Standard delivery fee"
    if value <= 1500:
        return "High delivery fee"
    return "Custom delivery fee"
