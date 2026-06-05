from __future__ import annotations

def customer_initials(name: str) -> str:
    parts=[p for p in name.strip().split() if p]
    return "".join(p[0].upper() for p in parts[:2]) or "?"