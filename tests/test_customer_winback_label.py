from shoptalk.customer_winback_label import classify_customer_winback


def test_classify_customer_winback_labels_key_states():
    assert classify_customer_winback(-1) == 'Active'
    assert classify_customer_winback(30) == 'Nudge'
    assert classify_customer_winback(50) == 'Winback'
