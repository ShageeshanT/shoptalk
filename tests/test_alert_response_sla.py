from shoptalk.alert_response_sla import alert_response_sla_minutes
from shoptalk.seller_alerts import SellerAlert


def test_no_alert_has_no_response_sla():
    assert alert_response_sla_minutes(None) is None


def test_danger_alert_gets_fast_response_sla():
    assert alert_response_sla_minutes(SellerAlert("danger", "Risk", "Refund")) == 10


def test_warning_alert_gets_short_response_sla():
    assert alert_response_sla_minutes(SellerAlert("warning", "Timing", "Need today")) == 30


def test_info_alert_gets_review_sla():
    assert alert_response_sla_minutes(SellerAlert("info", "FYI", "Question")) == 120
