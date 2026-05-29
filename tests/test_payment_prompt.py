from uuid import uuid4

from shoptalk.payment_prompt import payment_prompt
from shoptalk.schemas import Order


def test_payment_prompt_includes_amount_and_method() -> None:
    order = Order(business_id=uuid4(), title="cupcake box", total_amount=4500)

    assert payment_prompt(order, payment_method="bank transfer") == (
        "Your cupcake box is confirmed. Please complete Rs 4,500 via bank transfer."
    )


def test_payment_prompt_handles_missing_amount() -> None:
    order = Order(business_id=uuid4(), title="brownie tray", total_amount=None)

    assert payment_prompt(order, payment_method="cash on pickup") == (
        "Your brownie tray is confirmed. Please complete payment via cash on pickup."
    )
