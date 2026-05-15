from shoptalk.analyzer import analyze_message
from shoptalk.reply import build_suggested_reply
from shoptalk.schemas import AnalyzeMessageRequest


def test_order_reply_asks_for_quantity_and_time():
    analysis = analyze_message(AnalyzeMessageRequest(message="Can I order a cake today?"))
    reply = build_suggested_reply(analysis)
    assert "quantity" in reply.lower()
    assert "time" in reply.lower()
