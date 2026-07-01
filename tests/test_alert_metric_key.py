from shoptalk.alert_metric_key import alert_metric_key


def test_alert_metric_key_behavior():
    assert alert_metric_key("danger") == "seller_alerts.danger"
    assert alert_metric_key("weird") == "seller_alerts.unknown"
