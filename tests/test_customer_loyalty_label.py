from shoptalk.customer_loyalty_label import classify_customer_loyalty


def test_classify_customer_loyalty_labels_key_states():
    assert classify_customer_loyalty(1) == "New buyer"
    assert classify_customer_loyalty(2) == "Returning buyer"
    assert classify_customer_loyalty(6) == "Loyal buyer"
