from shoptalk.alert_search_text import alert_search_text


def test_alert_search_text_behavior():
    assert alert_search_text("Timing", "Need Today") == "timing need today"
