from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from shoptalk.schemas import Order, OrderCreate
from shoptalk.state import state

router = APIRouter(prefix="/orders", tags=["orders"])


def _validate_order_links(payload: OrderCreate) -> None:
    if state.businesses.get(payload.business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    if payload.customer_id is not None and state.customers.get(payload.customer_id) is None:
        raise HTTPException(status_code=404, detail="Customer not found")


@router.post("", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(payload: OrderCreate) -> Order:
    _validate_order_links(payload)
    order = Order(**payload.model_dump())
    return state.orders.add(order)


@router.get("", response_model=list[Order])
def list_orders(business_id: UUID | None = None) -> list[Order]:
    if business_id is None:
        return state.orders.list()
    if state.businesses.get(business_id) is None:
        raise HTTPException(status_code=404, detail="Business not found")
    return state.orders.list_for_business(business_id)


@router.get("/{order_id}", response_model=Order)
def get_order(order_id: UUID) -> Order:
    order = state.orders.get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return order
