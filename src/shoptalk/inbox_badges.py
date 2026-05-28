"""Inbox badge helpers for customer chat cards."""

from __future__ import annotations


def inbox_badges(has_order: bool, has_payment: bool, needs_reply: bool) -> list[str]:
    """Return badge labels for a chat list row."""

    badges: list[str] = []
    if needs_reply:
        badges.append("needs_reply")
    if has_order:
        badges.append("order")
    if has_payment:
        badges.append("payment")
    return badges
