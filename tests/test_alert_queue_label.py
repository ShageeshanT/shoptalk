from shoptalk.alert_queue_label import alert_queue_label


def test_labels_empty_alert_queue_as_clear():
    assert alert_queue_label(0) == "clear"
    assert alert_queue_label(-1) == "clear"


def test_labels_small_alert_queue_as_watch():
    assert alert_queue_label(2) == "watch"


def test_labels_medium_alert_queue_as_busy():
    assert alert_queue_label(5) == "busy"


def test_labels_large_alert_queue_as_overloaded():
    assert alert_queue_label(6) == "overloaded"
