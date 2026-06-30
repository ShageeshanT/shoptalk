"""Small presentation helper for ShopTalk seller workflows."""


def label_cart_size(quantity: int) -> str:
    """Return a compact cart size label for seller-facing UI."""
    return "bulk" if quantity >= 12 else "multi" if quantity >= 2 else "single"
