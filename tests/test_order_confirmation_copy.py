from shoptalk.order_confirmation_copy import order_confirmation_copy


def test_order_confirmation_copy_without_total():
    assert order_confirmation_copy("Nimal", "brownie box") == "Hi Nimal, confirming brownie box. We'll update you soon."


def test_order_confirmation_copy_with_total():
    assert "Rs 2,500.00" in order_confirmation_copy("Nimal", "brownie box", 2500)
