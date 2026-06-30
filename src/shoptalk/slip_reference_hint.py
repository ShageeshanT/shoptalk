from __future__ import annotations

def slip_reference_hint(order_code: str) -> str:
    code = order_code.strip().upper()
    return f"Use {code} as the payment reference." if code else "Ask the seller for the payment reference."
