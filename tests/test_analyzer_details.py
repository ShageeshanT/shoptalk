from shoptalk.analyzer import analyze_message
from shoptalk.schemas import MessageAnalyzeRequest


def test_extracts_home_bakery_order_details() -> None:
    result = analyze_message(
        MessageAnalyzeRequest(text="Can I order two cupcakes tomorrow and write Happy 21st on them?")
    )

    assert result.intent == "new_order"
    assert result.order_details.quantity == 2
    assert result.order_details.product == "cupcakes"
    assert result.order_details.needed_by == "tomorrow"
    assert result.order_details.custom_text == "Happy 21st on them?"
