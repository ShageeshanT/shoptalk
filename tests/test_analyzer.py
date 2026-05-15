from shoptalk.analyzer import analyze_message
from shoptalk.schemas import MessageAnalyzeRequest


def test_detects_new_order():
    result = analyze_message(MessageAnalyzeRequest(text="Hi can I order a 1kg cake for Saturday?"))

    assert result.intent == "new_order"
    assert result.order_details.product == "cake"
    assert result.order_details.size == "1kg"
    assert result.follow_up_needed is True


def test_detects_complaint():
    result = analyze_message(MessageAnalyzeRequest(text="This is late, I want a refund or I will leave a bad review"))

    assert result.intent == "complaint"
    assert result.urgency == "high"
    assert result.sentiment == "negative"
