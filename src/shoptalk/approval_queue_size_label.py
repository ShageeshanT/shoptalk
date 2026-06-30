"""Small presentation helper for ShopTalk seller workflows."""


def label_approval_queue_size(count: int) -> str:
    """Return a compact approval queue size label for seller-facing UI."""
    return "busy" if count >= 10 else "light"
