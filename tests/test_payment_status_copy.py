from shoptalk.payment_status_copy import payment_status_copy

def test_payment_status_copy():
    assert payment_status_copy(True) == "Payment received"
