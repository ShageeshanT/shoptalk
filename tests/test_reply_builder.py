from shoptalk.reply_builder import build_seller_summary
from shoptalk.schemas import MessageAnalysis, OrderDetails


def test_seller_summary_includes_order_context() -> None:
    analysis = MessageAnalysis(
        intent="new_order",
        urgency="normal",
        sentiment="neutral",
        customer_needs_reply=True,
        order_details=OrderDetails(
            product="cupcakes",
            quantity=12,
            size="box of 12",
            needed_by="tomorrow",
            delivery_required=True,
            custom_text="Happy birthday",
        ),
        suggested_reply="Sure",
    )

    summary = build_seller_summary(analysis)

    assert "Product: cupcakes" in summary
    assert "Needed by: tomorrow" in summary
    assert "Delivery: yes" in summary
    assert "Custom text: Happy birthday" in summary
