from __future__ import annotations

def stock_level_label(count: int | None) -> str:
    if count is None: return "Stock unknown"
    if count <= 0: return "Out of stock"
    if count < 5: return "Low stock"
    return "In stock"