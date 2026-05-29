from __future__ import annotations

from shoptalk.schemas import MessageAnalysis


def quick_reply_chips(analysis: MessageAnalysis) -> list[str]:
    """Return short seller-selectable reply chips for a message analysis."""
    chips: list[str] = []

    if analysis.customer_needs_reply:
        chips.append("Reply to customer")
    if analysis.intent == "new_order":
        chips.append("Confirm order details")
    if analysis.intent == "product_inquiry":
        chips.append("Share product options")
    if analysis.intent == "payment_question" or analysis.payment_status == "pending":
        chips.append("Send payment instructions")
    if analysis.intent == "delivery_question" or analysis.order_details.delivery_required:
        chips.append("Confirm delivery details")
    if analysis.follow_up_needed:
        chips.append("Schedule follow-up")
    if analysis.urgency == "high":
        chips.insert(0, "Handle urgently")

    return _dedupe(chips) or ["Mark as reviewed"]


def _dedupe(items: list[str]) -> list[str]:
    seen: set[str] = set()
    unique: list[str] = []
    for item in items:
        key = item.lower()
        if key not in seen:
            seen.add(key)
            unique.append(item)
    return unique
