from shoptalk.payment_status import payment_status, remaining_balance


def test_payment_status_unpaid():
    assert payment_status(1000, 0) == "unpaid"


def test_payment_status_partial():
    assert payment_status(1000, 300) == "partial"
    assert remaining_balance(1000, 300) == 700


def test_payment_status_paid_caps_balance():
    assert payment_status(1000, 1200) == "paid"
    assert remaining_balance(1000, 1200) == 0
