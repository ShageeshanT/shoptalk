from __future__ import annotations

def seller_close_copy(shop_name: str) -> str:
    shop = shop_name.strip() or "us"
    return f"Thanks for ordering from {shop}."
