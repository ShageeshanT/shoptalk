from shoptalk.alert_status_badge import alert_status_badge


def test_builds_badge_for_resolved_alert():
    assert alert_status_badge("resolved") == {
        "status": "resolved",
        "tone": "success",
        "label": "Resolved. Nice, one less gremlin in the inbox.",
    }


def test_unknown_status_defaults_to_attention_badge():
    assert alert_status_badge("strange") == {
        "status": "needs_seller_reply",
        "tone": "attention",
        "label": "Seller reply needed.",
    }
