"""Small presentation helper for ShopTalk seller workflows."""


def label_payment_followup(hours: int) -> str:
    """Return a compact payment followup label for seller-facing UI."""
    return "send reminder" if hours >= 24 else "wait"
