from __future__ import annotations

def customer_phone_mask(phone: str) -> str:
    digits = "".join(ch for ch in phone if ch.isdigit())
    return "***" + digits[-4:] if len(digits) >= 4 else "***"
