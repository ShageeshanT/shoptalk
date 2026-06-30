"""Small presentation helper for ShopTalk seller workflows."""


def build_seller_dashboard_hint(open_orders: int, pending_replies: int) -> str:
    """Return a compact seller dashboard hint label for seller-facing UI."""
    return f"{open_orders} open orders, {pending_replies} pending replies"
