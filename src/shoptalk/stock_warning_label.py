"""Small presentation helper for ShopTalk seller workflows."""


def label_stock_warning(available: int) -> str:
    """Return a compact stock warning label for seller-facing UI."""
    return "low stock" if available <= 3 else "available"
