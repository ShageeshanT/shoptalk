"""Small presentation helper for ShopTalk seller workflows."""


def label_payment_receipt(has_receipt: bool) -> str:
    """Return a compact payment receipt label for seller-facing UI."""
    return "received" if has_receipt else "missing"
