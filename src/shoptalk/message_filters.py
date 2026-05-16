from uuid import UUID

from shoptalk.schemas import ConversationMessageOut


def messages_for_customer(
    messages: list[ConversationMessageOut],
    customer_id: UUID,
) -> list[ConversationMessageOut]:
    return [message for message in messages if message.customer_id == customer_id]


def unread_customer_messages(messages: list[ConversationMessageOut]) -> list[ConversationMessageOut]:
    return [message for message in messages if message.sender == "customer"]


def latest_message(messages: list[ConversationMessageOut]) -> ConversationMessageOut | None:
    if not messages:
        return None
    return max(messages, key=lambda message: message.received_at)
