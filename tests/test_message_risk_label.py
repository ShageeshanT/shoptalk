from shoptalk.message_risk_label import message_risk_label

def test_message_risk_label_thresholds():
    assert message_risk_label(80) == 'High risk'
    assert message_risk_label(50) == 'Medium risk'
    assert message_risk_label(20) == 'Low risk'

def test_message_risk_label_invalid_value():
    assert message_risk_label("bad") == 'Safe'
