from uuid import UUID

from shoptalk.schemas import ConversationMessageOut
from shoptalk.state import state


def search_messages(query: str, business_id: UUID | None = None) -> list[ConversationMessageOut]:
    needle = query.strip().lower()
    if not needle:
        return []

    messages = state.messages.list()
    if business_id is not None:
        messages = [message for message in messages if message.business_id == business_id]
    return [message for message in messages if needle in message.text.lower()]
