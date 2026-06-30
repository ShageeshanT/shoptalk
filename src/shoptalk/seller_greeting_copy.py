from __future__ import annotations

def seller_greeting_copy(shop_name: str) -> str:
    shop = shop_name.strip() or "ShopTalk"
    return f"Hi, welcome to {shop}. How can we help with your order today?"
