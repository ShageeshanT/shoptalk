from __future__ import annotations

def order_value_band(amount: float) -> str:
    if amount < 0:
        raise ValueError("amount cannot be negative")
    if amount < 2500:
        return "starter"
    if amount < 10000:
        return "standard"
    return "premium"
