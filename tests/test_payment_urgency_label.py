from shoptalk.payment_urgency_label import payment_urgency_label

def test_payment_urgency_label_thresholds():
    assert payment_urgency_label(0) == 'Due now'
    assert payment_urgency_label(2) == 'Due soon'
    assert payment_urgency_label(7) == 'Upcoming payment'

def test_payment_urgency_label_invalid_value():
    assert payment_urgency_label("bad") == 'Future payment'
