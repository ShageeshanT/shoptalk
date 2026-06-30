from __future__ import annotations

def customer_salutation(name: str) -> str:
    clean = name.strip().split()[0] if name.strip() else "there"
    return f"Hi {clean}"
