from __future__ import annotations

def catalog_price_label(price: float | None, currency: str="LKR") -> str:
    return "Price not set" if price is None else f"{currency.upper()} {price:,.0f}"