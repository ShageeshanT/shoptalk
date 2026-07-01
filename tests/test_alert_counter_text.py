from shoptalk.alert_counter_text import alert_counter_text


def test_alert_counter_text_behavior():
    assert alert_counter_text(0) == "No active alerts"
    assert alert_counter_text(1) == "1 active alert"
    assert alert_counter_text(2) == "2 active alerts"
