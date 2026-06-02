from shoptalk.payment_copy import payment_confirmation_copy, payment_reminder_copy


def test_payment_confirmation_copy_uses_customer_name():
    assert "Nimal" in payment_confirmation_copy("Nimal")


def test_payment_reminder_copy_formats_amount():
    assert "LKR 2,500" in payment_reminder_copy(2500)
