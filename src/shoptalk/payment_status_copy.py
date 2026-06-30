from __future__ import annotations

def payment_status_copy(paid: bool) -> str:
    return "Payment received" if paid else "Waiting for payment"
