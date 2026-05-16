from uuid import UUID

from shoptalk.analyzer import analyze_message
from shoptalk.message_filters import latest_message, messages_for_customer, unread_customer_messages
from shoptalk.schemas import ConversationMessageOut, CustomerSignal, MessageAnalyzeRequest


def build_customer_inbox_item(
    customer_id: UUID,
    messages: list[ConversationMessageOut],
) -> CustomerSignal | None:
    customer_messages = unread_customer_messages(messages_for_customer(messages, customer_id))
    latest = latest_message(customer_messages)
    if latest is None:
        return None

    analysis = analyze_message(MessageAnalyzeRequest(text=latest.text))
    return CustomerSignal(
        customer_id=customer_id,
        latest_message=latest.text,
        intent=analysis.intent,
        urgency=analysis.urgency,
        sentiment=analysis.sentiment,
        needs_reply=analysis.customer_needs_reply,
        suggested_reply=analysis.suggested_reply,
    )
