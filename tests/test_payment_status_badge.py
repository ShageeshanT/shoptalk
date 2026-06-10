from shoptalk.payment_status_badge import payment_status_badge

def test_payment_status_badge_known_states():
    assert payment_status_badge("paid") == "Paid"
    assert payment_status_badge("partial") == "Partial payment"
    assert payment_status_badge("overdue") == "Payment overdue"

def test_payment_status_badge_defaults_to_pending():
    assert payment_status_badge("") == "Payment pending"
