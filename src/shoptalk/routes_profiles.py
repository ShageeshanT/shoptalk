from uuid import UUID

from fastapi import APIRouter, HTTPException

from shoptalk.customer_profile import build_customer_profile
from shoptalk.schemas import CustomerProfile

router = APIRouter(prefix="/profiles", tags=["profiles"])


@router.get("/customers/{customer_id}", response_model=CustomerProfile)
def get_customer_profile(customer_id: UUID) -> CustomerProfile:
    profile = build_customer_profile(customer_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return profile
