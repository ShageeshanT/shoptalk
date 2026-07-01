"""Copy helpers for seller alert cards."""

from __future__ import annotations

from shoptalk.seller_alerts import SellerAlert


def seller_alert_cta(alert: SellerAlert | None) -> str:
    """Return the next-action copy for a seller alert card."""

    if alert is None:
        return "No urgent action needed."
    if alert.level == "danger":
        return "Reply now and resolve the risk before taking new orders."
    if alert.level == "warning":
        return "Check timing and confirm the next step with the customer."
    return "Review when the current queue is stable."
