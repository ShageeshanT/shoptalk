from __future__ import annotations

def quantity_label(quantity: int | None) -> str:
    if quantity is None: return "Quantity not set"
    return f"{quantity} item" if quantity == 1 else f"{quantity} items"