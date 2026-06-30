"""Small presentation helper for ShopTalk seller workflows."""


def label_customer_trust(completed_orders: int) -> str:
    """Return a compact customer trust label for seller-facing UI."""
    return "trusted" if completed_orders >= 3 else "new"
