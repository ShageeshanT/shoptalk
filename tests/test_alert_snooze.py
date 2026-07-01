from shoptalk.alert_snooze import can_snooze_alert
from shoptalk.seller_alerts import SellerAlert


def test_missing_alert_cannot_be_snoozed():
    assert can_snooze_alert(None) is False


def test_danger_alert_cannot_be_snoozed():
    assert can_snooze_alert(SellerAlert("danger", "Risk", "Refund")) is False


def test_warning_and_info_alerts_can_be_snoozed():
    assert can_snooze_alert(SellerAlert("warning", "Timing", "Need today")) is True
    assert can_snooze_alert(SellerAlert("info", "FYI", "Size")) is True
