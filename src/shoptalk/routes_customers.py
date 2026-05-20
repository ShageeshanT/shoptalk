from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from shoptalk.schemas import Customer, CustomerCreate
from shoptalk.status_updates import CustomerNoteUpdate
from shoptalk.state import state

router = APIRouter(prefix="/customers", tags=["customers"])


def _ensure_business_exists(business_id: UUID) -> None:
    if state.businesses.get(business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")


@router.post("", response_model=Customer, status_code=status.HTTP_201_CREATED)
def create_customer(payload: CustomerCreate) -> Customer:
    _ensure_business_exists(payload.business_id)
    customer = Customer(**payload.model_dump())
    return state.customers.add(customer)


@router.get("", response_model=list[Customer])
def list_customers(business_id: UUID | None = None) -> list[Customer]:
    if business_id is None:
        return state.customers.list()
    _ensure_business_exists(business_id)
    return state.customers.list_for_business(business_id)


@router.get("/{customer_id}", response_model=Customer)
def get_customer(customer_id: UUID) -> Customer:
    customer = state.customers.get(customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    return customer


@router.patch("/{customer_id}/notes", response_model=Customer)
def update_customer_notes(customer_id: UUID, payload: CustomerNoteUpdate) -> Customer:
    customer = state.customers.get(customer_id)
    if customer is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    updated = customer.model_copy(update={"notes": payload.notes})
    state.customers.add(updated)
    return updated
