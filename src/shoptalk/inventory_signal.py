from __future__ import annotations

def inventory_signal(stock: int) -> str:
    if stock <= 0: return "out"
    if stock <= 3: return "low"
    return "available"
