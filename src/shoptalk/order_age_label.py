from __future__ import annotations

def order_age_label(days: int) -> str:
    if days <= 0: return "New today"
    return f"{days} day old" if days == 1 else f"{days} days old"