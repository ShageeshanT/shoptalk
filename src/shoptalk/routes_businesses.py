from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from shoptalk.schemas import Business, BusinessCreate
from shoptalk.state import state

router = APIRouter(prefix="/businesses", tags=["businesses"])


@router.post("", response_model=Business, status_code=status.HTTP_201_CREATED)
def create_business(payload: BusinessCreate) -> Business:
    business = Business(**payload.model_dump())
    return state.businesses.add(business)


@router.get("", response_model=list[Business])
def list_businesses() -> list[Business]:
    return state.businesses.list()


@router.get("/{business_id}", response_model=Business)
def get_business(business_id: UUID) -> Business:
    business = state.businesses.get(business_id)
    if business is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return business
