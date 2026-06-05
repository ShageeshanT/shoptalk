from __future__ import annotations

def customer_value_label(value: float) -> str:
    if value >= 50000: return "VIP customer"
    if value >= 10000: return "Growing customer"
    return "New customer"