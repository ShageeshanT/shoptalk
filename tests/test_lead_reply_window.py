from shoptalk.lead_reply_window import lead_reply_window


def test_lead_reply_window():
    assert lead_reply_window(180) == "today"
