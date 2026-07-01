from shoptalk.alert_bulk_action import alert_bulk_action_label


def test_alert_bulk_action_label_behavior():
    assert alert_bulk_action_label(0) == "No alerts selected"
    assert alert_bulk_action_label(1) == "Resolve 1 alert"
    assert alert_bulk_action_label(3) == "Resolve 3 alerts"
