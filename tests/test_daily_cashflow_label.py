from shoptalk.daily_cashflow_label import classify_daily_cashflow


def test_classify_daily_cashflow_labels_key_states():
    assert classify_daily_cashflow(39) == "Cashflow weak"
    assert classify_daily_cashflow(40) == "Cashflow steady"
    assert classify_daily_cashflow(75) == "Cashflow strong"
