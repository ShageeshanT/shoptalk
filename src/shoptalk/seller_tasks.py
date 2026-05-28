"""Seller task generation helpers."""

from __future__ import annotations


def seller_tasks(needs_reply: bool, payment_pending: bool, delivery_pending: bool) -> list[str]:
    """Return seller task keys for an order or conversation."""

    tasks: list[str] = []
    if needs_reply:
        tasks.append("reply_to_customer")
    if payment_pending:
        tasks.append("collect_payment")
    if delivery_pending:
        tasks.append("confirm_delivery")
    return tasks
