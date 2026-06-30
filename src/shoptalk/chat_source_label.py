"""Small presentation helper for ShopTalk seller workflows."""


def label_chat_source(channel: str) -> str:
    """Return a compact chat source label for seller-facing UI."""
    return "whatsapp" if channel.lower().startswith("wa") else channel.lower()
