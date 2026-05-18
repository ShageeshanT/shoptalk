from uuid import UUID

from fastapi import APIRouter, HTTPException

from shoptalk.enums import MessageDirection
from shoptalk.schemas import MessageThread, MessageThreadItem
from shoptalk.state import state

router = APIRouter(prefix="/threads", tags=["threads"])


def _display_name(direction: MessageDirection) -> str:
    if direction == MessageDirection.CUSTOMER:
        return "Customer"
    if direction == MessageDirection.ASSISTANT:
        return "ShopTalk"
    return "Seller"


@router.get("", response_model=MessageThread)
def get_thread(business_id: UUID, customer_id: UUID | None = None) -> MessageThread:
    if state.businesses.get(business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    if customer_id is not None and state.customers.get(customer_id) is None:
        raise HTTPException(status_code=404, detail="Customer not found")

    messages = [message for message in state.messages.list() if message.business_id == business_id]
    if customer_id is not None:
        messages = [message for message in messages if message.customer_id == customer_id]
    messages = sorted(messages, key=lambda message: message.received_at)

    return MessageThread(
        business_id=business_id,
        customer_id=customer_id,
        messages=[
            MessageThreadItem(
                message=message,
                direction=message.sender,
                display_name=_display_name(message.sender),
            )
            for message in messages
        ],
    )
