from shoptalk.alert_escalation_label import alert_escalation_label


def test_alert_escalation_label_behavior():
    assert alert_escalation_label("danger") == "owner_review"
    assert alert_escalation_label("warning") == "seller_queue"
    assert alert_escalation_label("info") == "normal"
