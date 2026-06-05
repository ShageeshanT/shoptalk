from __future__ import annotations

def order_amount_label(amount: float | None, currency: str="LKR") -> str:
    if amount is None:
        return "Amount not set"
    prefix = "Rs" if currency.upper()=="LKR" else currency.upper()
    return f"{prefix} {amount:,.2f}"