from shoptalk.alert_followup_window import alert_followup_window_minutes
from shoptalk.seller_alerts import SellerAlert


def test_missing_alert_has_no_followup_window():
    assert alert_followup_window_minutes(None) is None


def test_danger_alert_has_one_hour_followup_window():
    assert alert_followup_window_minutes(SellerAlert("danger", "Risk", "Refund")) == 60


def test_warning_alert_has_three_hour_followup_window():
    assert alert_followup_window_minutes(SellerAlert("warning", "Timing", "Need today")) == 180


def test_info_alert_has_next_day_followup_window():
    assert alert_followup_window_minutes(SellerAlert("info", "FYI", "Size")) == 1440
