from shoptalk.analyzer import analyze_message
from shoptalk.schemas import ConversationMessageOut, CustomerSignal, MessageAnalyzeRequest


def build_customer_signal(messages: list[ConversationMessageOut]) -> CustomerSignal | None:
    customer_messages = [message for message in messages if message.sender == "customer"]
    if not customer_messages:
        return None

    latest = max(customer_messages, key=lambda message: message.received_at)
    analysis = analyze_message(MessageAnalyzeRequest(text=latest.text))
    return CustomerSignal(
        customer_id=latest.customer_id,
        latest_message=latest.text,
        intent=analysis.intent,
        urgency=analysis.urgency,
        sentiment=analysis.sentiment,
        needs_reply=analysis.customer_needs_reply,
        suggested_reply=analysis.suggested_reply,
    )
