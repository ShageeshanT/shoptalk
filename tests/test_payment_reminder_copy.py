from shoptalk.payment_reminder_copy import payment_reminder_copy


def test_payment_reminder_copy_empty():
    assert payment_reminder_copy(0) == "No payment is due right now."


def test_payment_reminder_copy_formats_amount():
    assert payment_reminder_copy(1500, "tomorrow") == "Gentle reminder: Rs 1,500.00 is due tomorrow."
