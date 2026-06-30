"""Small presentation helper for ShopTalk seller workflows."""


def label_pickup_window(hours: int) -> str:
    """Return a compact pickup window label for seller-facing UI."""
    return "today" if hours <= 24 else "later"
