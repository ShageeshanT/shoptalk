from uuid import UUID

from fastapi import APIRouter, HTTPException

from shoptalk.schemas import CustomerTimeline
from shoptalk.state import state
from shoptalk.timeline import build_customer_timeline

router = APIRouter(prefix="/timelines", tags=["timelines"])


@router.get("/customers/{customer_id}", response_model=CustomerTimeline)
def get_customer_timeline(customer_id: UUID) -> CustomerTimeline:
    if state.customers.get(customer_id) is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return build_customer_timeline(customer_id)
