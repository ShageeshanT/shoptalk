from shoptalk.alert_owner_note import alert_owner_note
from shoptalk.seller_alerts import SellerAlert


def test_returns_note_for_missing_alert():
    assert alert_owner_note(None) == "No alert to review."


def test_returns_compact_owner_note_for_alert():
    assert alert_owner_note(SellerAlert("warning", "Timing", "Need today")) == "WARNING: Timing - Need today"
