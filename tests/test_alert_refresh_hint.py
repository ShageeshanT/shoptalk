from shoptalk.alert_refresh_hint import alert_refresh_hint


def test_alert_refresh_hint_behavior():
    assert alert_refresh_hint(True) == "New customer alerts available. Refresh the queue."
    assert alert_refresh_hint(False) == "Alert queue is up to date."
