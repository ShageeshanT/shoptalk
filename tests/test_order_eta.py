from shoptalk.order_eta import eta_label


def test_eta_label_buckets_delivery_dates():
    assert eta_label(None) == "unscheduled"
    assert eta_label(-1) == "overdue"
    assert eta_label(0) == "today"
    assert eta_label(2) == "soon"
    assert eta_label(5) == "scheduled"
