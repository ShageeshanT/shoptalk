"""Small presentation helper for ShopTalk seller workflows."""


def label_order_packaging(fragile: bool) -> str:
    """Return a compact order packaging label for seller-facing UI."""
    return "fragile" if fragile else "standard"
