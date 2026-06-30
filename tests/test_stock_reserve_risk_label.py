from shoptalk.stock_reserve_risk_label import classify_stock_reserve_risk


def test_classify_stock_reserve_risk_labels_key_states():
    assert classify_stock_reserve_risk(4) == "Low reserve"
    assert classify_stock_reserve_risk(5) == "Reserve watch"
    assert classify_stock_reserve_risk(15) == "Reserve risk"
