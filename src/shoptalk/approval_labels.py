"""Approval queue label helpers."""

from __future__ import annotations


def approval_label(kind: str) -> str:
    """Return a friendly label for approval queue item kind."""

    labels = {
        "reply": "Reply draft",
        "order": "Order draft",
        "followup": "Follow-up",
    }
    return labels.get(kind, "Review item")
