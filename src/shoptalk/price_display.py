from __future__ import annotations

def price_display(amount: float, currency: str = "LKR") -> str:
    return f"{currency} {amount:,.2f}"
