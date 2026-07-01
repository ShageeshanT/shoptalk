from shoptalk.alert_priority_score import alert_priority_score
from shoptalk.seller_alerts import SellerAlert


def test_missing_alert_has_zero_priority():
    assert alert_priority_score(None, minutes_waiting=90) == 0


def test_scores_danger_above_warning():
    danger = SellerAlert("danger", "Risk", "Refund")
    warning = SellerAlert("warning", "Timing", "Need today")
    assert alert_priority_score(danger) > alert_priority_score(warning)


def test_wait_time_increases_priority_without_exceeding_cap():
    alert = SellerAlert("danger", "Risk", "Refund")
    assert alert_priority_score(alert, minutes_waiting=300) == 100


def test_negative_wait_time_is_ignored():
    alert = SellerAlert("info", "FYI", "Question")
    assert alert_priority_score(alert, minutes_waiting=-10) == 20
