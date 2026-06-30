"""Small presentation helper for ShopTalk seller workflows."""


def label_customer_reply_gap(minutes: int) -> str:
    """Return a compact customer reply gap label for seller-facing UI."""
    return "urgent" if minutes >= 120 else "watch" if minutes >= 45 else "fresh"
