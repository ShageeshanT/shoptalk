"""Small presentation helper for ShopTalk seller workflows."""


def label_reply_tone(is_complaint: bool) -> str:
    """Return a compact reply tone label for seller-facing UI."""
    return "soft" if is_complaint else "clear"
