from shoptalk.customer_trust_label import customer_trust_label

def test_customer_trust_label_thresholds():
    assert customer_trust_label(80) == 'Trusted customer'
    assert customer_trust_label(50) == 'Normal trust'
    assert customer_trust_label(20) == 'Low trust'

def test_customer_trust_label_invalid_value():
    assert customer_trust_label("bad") == 'Unknown trust'
