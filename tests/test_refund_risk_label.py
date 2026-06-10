from shoptalk.refund_risk_label import refund_risk_label

def test_refund_risk_label_thresholds():
    assert refund_risk_label(80) == 'High refund risk'
    assert refund_risk_label(50) == 'Medium refund risk'
    assert refund_risk_label(20) == 'Low refund risk'

def test_refund_risk_label_invalid_value():
    assert refund_risk_label("bad") == 'No refund risk'
