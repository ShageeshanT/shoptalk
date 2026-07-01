from shoptalk.alert_safe_title import alert_safe_title


def test_alert_safe_title_behavior():
    assert alert_safe_title("  Refund ") == "Refund"
    assert alert_safe_title("  ") == "Untitled alert"
