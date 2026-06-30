"""Small presentation helper for ShopTalk seller workflows."""


def label_seller_next_step(needs_payment: bool, needs_delivery: bool) -> str:
    """Return a compact seller next step label for seller-facing UI."""
    return "collect payment" if needs_payment else "confirm delivery" if needs_delivery else "reply"
