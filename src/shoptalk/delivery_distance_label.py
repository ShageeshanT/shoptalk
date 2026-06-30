"""Small presentation helper for ShopTalk seller workflows."""


def label_delivery_distance(km: float) -> str:
    """Return a compact delivery distance label for seller-facing UI."""
    return "far" if km >= 15 else "near" if km <= 3 else "standard"
