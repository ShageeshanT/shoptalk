from __future__ import annotations

def delivery_fee_label(fee: float | None) -> str:
    if fee is None: return "Delivery fee not set"
    if fee == 0: return "Free delivery"
    return f"Delivery Rs {fee:,.0f}"