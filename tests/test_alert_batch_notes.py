from shoptalk.alert_batch_notes import alert_batch_notes
from shoptalk.seller_alerts import SellerAlert


def test_returns_owner_notes_for_each_alert():
    notes = alert_batch_notes(
        [
            SellerAlert("warning", "Timing", "Need today"),
            SellerAlert("danger", "Risk", "Refund"),
        ]
    )

    assert notes == ["WARNING: Timing - Need today", "DANGER: Risk - Refund"]


def test_returns_empty_list_without_alerts():
    assert alert_batch_notes([]) == []
