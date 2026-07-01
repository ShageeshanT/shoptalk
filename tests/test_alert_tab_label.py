from shoptalk.alert_tab_label import alert_tab_label


def test_alert_tab_label_behavior():
    assert alert_tab_label(0) == "Alerts"
    assert alert_tab_label(5) == "Alerts (5)"
