from uuid import UUID

from fastapi import APIRouter, HTTPException

from shoptalk.schemas import CheckoutDraft
from shoptalk.state import state

router = APIRouter(prefix="/checkout", tags=["checkout"])


@router.get("/orders/{order_id}/draft", response_model=CheckoutDraft)
def draft_checkout(order_id: UUID) -> CheckoutDraft:
    order = state.orders.get(order_id)
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")

    business = state.businesses.get(order.business_id)
    currency = business.currency if business is not None else "LKR"
    amount = order.total_amount
    amount_text = f"{currency} {amount:,.0f}" if amount is not None else f"the final {currency} total"
    instructions = "Bank transfer, cash on pickup, or seller-confirmed payment link"
    message = (
        f"Your order '{order.title}' is ready for payment. "
        f"Please pay {amount_text} via {instructions} and send the receipt here so we can confirm it."
    )
    return CheckoutDraft(
        order_id=order.id,
        amount=amount,
        currency=currency,
        payment_instructions=instructions,
        message=message,
    )
