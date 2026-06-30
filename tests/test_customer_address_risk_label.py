from shoptalk.customer_address_risk_label import classify_customer_address_risk


def test_classify_customer_address_risk_labels_key_states():
    assert classify_customer_address_risk(0) == "Address ready"
    assert classify_customer_address_risk(1) == "Needs detail"
    assert classify_customer_address_risk(3) == "Address risky"
