from shoptalk.alert_export_row import alert_export_row


def test_alert_export_row_behavior():
    assert alert_export_row("warning", "Timing") == {"level": "warning", "title": "Timing"}
