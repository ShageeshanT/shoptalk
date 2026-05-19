from uuid import UUID

from fastapi import APIRouter, HTTPException

from shoptalk.customer_insights import build_customer_insight
from shoptalk.customer_profile import build_customer_profile
from shoptalk.schemas import CustomerInsight, CustomerProfile
from shoptalk.state import state

router = APIRouter(prefix="/profiles", tags=["profiles"])


@router.get("/customers/{customer_id}", response_model=CustomerProfile)
def get_customer_profile(customer_id: UUID) -> CustomerProfile:
    profile = build_customer_profile(customer_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return profile


@router.get("/customers/{customer_id}/insights", response_model=CustomerInsight)
def get_customer_insight(customer_id: UUID) -> CustomerInsight:
    if state.customers.get(customer_id) is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return build_customer_insight(
        customer_id=customer_id,
        orders=state.orders.list(),
        messages=state.messages.list(),
        follow_ups=state.follow_ups.list(),
    )
