from uuid import UUID

from fastapi import APIRouter, HTTPException, Query

from shoptalk.schemas import ConversationMessageOut
from shoptalk.search import search_messages
from shoptalk.state import state

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/messages", response_model=list[ConversationMessageOut])
def search_customer_messages(q: str = Query(..., min_length=1), business_id: UUID | None = None) -> list[ConversationMessageOut]:
    if business_id is not None and state.businesses.get(business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return search_messages(q, business_id=business_id)
