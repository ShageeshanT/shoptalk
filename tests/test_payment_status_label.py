from shoptalk.payment_status_label import payment_status_label

def test_payment_status_label():
    assert payment_status_label("partially_paid") == "Partially Paid"
    assert payment_status_label("") == "Unknown"