"""Small presentation helper for ShopTalk seller workflows."""


def label_fulfillment_delay(days: int) -> str:
    """Return a compact fulfillment delay label for seller-facing UI."""
    return "delayed" if days > 2 else "on track"
