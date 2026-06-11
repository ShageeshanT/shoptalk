from shoptalk.order_risk_label import classify_order_risk


def test_classify_order_risk_labels_key_states():
    assert classify_order_risk(-1) == 'Low'
    assert classify_order_risk(30) == 'Medium'
    assert classify_order_risk(70) == 'High'
