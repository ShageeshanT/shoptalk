from shoptalk.payment_delay_reason import payment_delay_reason


def test_payment_delay_reason():
    assert payment_delay_reason(3) == "overdue"
