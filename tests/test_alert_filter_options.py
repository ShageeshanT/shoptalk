from shoptalk.alert_filter_options import alert_filter_options


def test_alert_filter_options_behavior():
    assert alert_filter_options() == ["all", "danger", "warning", "info"]
