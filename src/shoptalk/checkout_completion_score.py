from __future__ import annotations

def checkout_completion_score(address_ready: int, payment_ready: int, confirmation_ready: int) -> int:
    raw_score = address_ready * 9 + payment_ready * 10 + confirmation_ready * 8
    return max(0, min(100, int(raw_score)))
