from uuid import UUID

from fastapi import APIRouter, HTTPException, status

from shoptalk.order_risk import assess_order_risk
from shoptalk.orders import is_active_order, seller_next_step
from shoptalk.payments import build_payment_note, payment_required
from shoptalk.schemas import Order, OrderAction, OrderCreate, OrderRisk, PaymentRequestDraft
from shoptalk.status_updates import OrderStatusUpdate
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


@router.get("/{order_id}/next-action", response_model=OrderAction)
def get_order_next_action(order_id: UUID) -> OrderAction:
    order = state.orders.get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return OrderAction(
        order_id=order.id,
        status=order.status,
        active=is_active_order(order),
        next_step=seller_next_step(order),
    )


@router.get("/{order_id}/payment-request", response_model=PaymentRequestDraft)
def get_payment_request(order_id: UUID) -> PaymentRequestDraft:
    order = state.orders.get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return PaymentRequestDraft(
        order_id=order.id,
        required=payment_required(order),
        message=build_payment_note(order),
    )


@router.get("/{order_id}/risk", response_model=OrderRisk)
def get_order_risk(order_id: UUID) -> OrderRisk:
    order = state.orders.get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return assess_order_risk(order)


@router.patch("/{order_id}/status", response_model=Order)
def update_order_status(order_id: UUID, payload: OrderStatusUpdate) -> Order:
    order = state.orders.get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    updated = order.model_copy(update={"status": payload.status})
    state.orders.add(updated)
    return updated
