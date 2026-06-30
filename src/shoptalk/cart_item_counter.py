from __future__ import annotations

def cart_item_counter(items: list[str]) -> int:
    return len([item for item in items if item.strip()])
