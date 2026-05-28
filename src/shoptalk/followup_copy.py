"""Follow-up copy helpers."""

from __future__ import annotations


def followup_copy(reason: str) -> str:
    """Return a seller-facing follow-up prompt."""

    normalized = reason.lower().strip()
    if normalized == "payment":
        return "Ask the customer to confirm the payment or receipt."
    if normalized == "delivery":
        return "Confirm delivery or pickup details with the customer."
    return "Send a polite follow-up to keep the conversation moving."
