"""Small presentation helper for ShopTalk seller workflows."""


def label_discount_risk(percent: float) -> str:
    """Return a compact discount risk label for seller-facing UI."""
    return "risky" if percent > 20 else "safe"
