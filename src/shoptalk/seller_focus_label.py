"""Small presentation helper for ShopTalk seller workflows."""


def label_seller_focus(overdue: int) -> str:
    """Return a compact seller focus label for seller-facing UI."""
    return "overdue" if overdue > 0 else "clean"
