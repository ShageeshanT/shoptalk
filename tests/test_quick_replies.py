from shoptalk.quick_replies import quick_reply_chips
from shoptalk.schemas import MessageAnalysis


def test_quick_reply_chips_cover_order_payment_and_delivery() -> None:
    analysis = MessageAnalysis(
        intent="new_order",
        urgency="high",
        sentiment="neutral",
        customer_needs_reply=True,
        payment_status="pending",
        follow_up_needed=True,
        suggested_reply="Sure, I can help with that.",
    )
    analysis.order_details.delivery_required = True

    chips = quick_reply_chips(analysis)

    assert chips[0] == "Handle urgently"
    assert "Confirm order details" in chips
    assert "Send payment instructions" in chips
    assert "Confirm delivery details" in chips
    assert "Schedule follow-up" in chips


def test_quick_reply_chips_fallback_to_reviewed() -> None:
    analysis = MessageAnalysis(
        intent="general",
        urgency="low",
        sentiment="neutral",
        customer_needs_reply=False,
        suggested_reply="Thanks!",
    )

    assert quick_reply_chips(analysis) == ["Mark as reviewed"]
