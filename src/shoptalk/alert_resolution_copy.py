"""Resolution copy for seller alert states."""

from __future__ import annotations


def alert_resolution_copy(status: str) -> str:
    """Return seller-facing copy for an alert resolution status."""

    if status == "resolved":
        return "Resolved. Nice, one less gremlin in the inbox."
    if status == "waiting_on_customer":
        return "Waiting for the customer to reply."
    return "Seller reply needed."
