from shoptalk.adapters import InboundMessage
from shoptalk.schemas import ConversationMessageOut
from shoptalk.state import state


def ingest_inbound_message(payload: InboundMessage) -> ConversationMessageOut:
    existing = next(
        (
            message
            for message in state.messages.list()
            if message.channel == payload.channel and message.external_message_id == payload.conversation_id
        ),
        None,
    )
    if existing is not None:
        return existing

    message = ConversationMessageOut(
        business_id=payload.business_id,
        customer_id=payload.customer_id,
        text=payload.text,
        channel=payload.channel,
        external_message_id=payload.conversation_id,
    )
    return state.messages.add(message)
