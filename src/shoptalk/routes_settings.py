from uuid import UUID

from fastapi import APIRouter, HTTPException

from shoptalk.schemas import Business, BusinessSettingsUpdate
from shoptalk.state import state

router = APIRouter(prefix="/settings", tags=["settings"])


@router.patch("/businesses/{business_id}", response_model=Business)
def update_business_settings(business_id: UUID, payload: BusinessSettingsUpdate) -> Business:
    business = state.businesses.get(business_id)
    if business is None:
        raise HTTPException(status_code=404, detail="Business not found")

    updates = payload.model_dump(exclude_none=True)
    updated = business.model_copy(update=updates)
    state.businesses.add(updated)
    return updated
