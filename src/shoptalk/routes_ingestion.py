from fastapi import APIRouter, HTTPException, status

from shoptalk.adapters import InboundMessage
from shoptalk.message_ingestion import ingest_inbound_message
from shoptalk.schemas import ConversationMessageOut
from shoptalk.state import state

router = APIRouter(prefix="/ingestion", tags=["ingestion"])


@router.post("/messages", response_model=ConversationMessageOut, status_code=status.HTTP_201_CREATED)
def ingest_message(payload: InboundMessage) -> ConversationMessageOut:
    if payload.business_id is not None and state.businesses.get(payload.business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    if payload.customer_id is not None and state.customers.get(payload.customer_id) is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return ingest_inbound_message(payload)
