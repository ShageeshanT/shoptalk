from shoptalk.seller_capacity_risk_label import classify_seller_capacity_risk


def test_classify_seller_capacity_risk_labels_key_states():
    assert classify_seller_capacity_risk(4) == "Capacity fine"
    assert classify_seller_capacity_risk(5) == "Capacity tight"
    assert classify_seller_capacity_risk(12) == "Over capacity"
