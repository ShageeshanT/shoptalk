"""Small presentation helper for ShopTalk seller workflows."""


def label_catalog_match(score: float) -> str:
    """Return a compact catalog match label for seller-facing UI."""
    return "exact" if score >= 0.9 else "partial"
