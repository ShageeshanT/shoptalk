from __future__ import annotations

def payment_nudge_copy(customer_name: str) -> str:
    name = customer_name.strip() or "there"
    return f"Hi {name}, your order is confirmed. Please send the payment slip when ready."
