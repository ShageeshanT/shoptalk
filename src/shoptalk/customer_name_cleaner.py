from __future__ import annotations

def customer_name_cleaner(name: str) -> str:
    return " ".join(name.strip().title().split())
