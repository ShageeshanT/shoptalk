"""Small presentation helper for ShopTalk seller workflows."""


def label_lead_temperature(score: float) -> str:
    """Return a compact lead temperature label for seller-facing UI."""
    return "hot" if score >= 80 else "warm" if score >= 45 else "cold"
