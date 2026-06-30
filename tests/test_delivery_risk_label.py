from shoptalk.delivery_risk_label import delivery_risk_label

def test_delivery_risk_label():
    assert delivery_risk_label(6, True) == "high"
    assert delivery_risk_label(2) == "low"
