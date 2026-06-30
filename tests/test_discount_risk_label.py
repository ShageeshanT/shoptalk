from shoptalk.discount_risk_label import label_discount_risk


def test_discount_risk_label():
    assert label_discount_risk(25) == "risky"
