from __future__ import annotations

def discount_label(percent: float | None) -> str:
    if not percent: return "No discount"
    return f"{percent:g}% discount"