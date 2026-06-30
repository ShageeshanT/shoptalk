"""Small presentation helper for ShopTalk seller workflows."""


def label_customer_language(text: str) -> str:
    """Return a compact customer language label for seller-facing UI."""
    return "sinhala" if text.startswith("ayubowan") else "english"
