from shoptalk.order_profit import summarize_profit


def test_summarize_profit_returns_profit_and_margin():
    summary = summarize_profit(revenue=10000, cost=6500)

    assert summary.revenue == 10000
    assert summary.cost == 6500
    assert summary.profit == 3500
    assert summary.margin_percent == 35
    assert summary.label == "healthy_margin"


def test_summarize_profit_labels_losses():
    summary = summarize_profit(revenue=3000, cost=4500)

    assert summary.profit == -1500
    assert summary.margin_percent == -50
    assert summary.label == "loss"


def test_summarize_profit_handles_zero_revenue():
    summary = summarize_profit(revenue=0, cost=0)

    assert summary.profit == 0
    assert summary.margin_percent == 0
    assert summary.label == "break_even"


def test_summarize_profit_clamps_negative_inputs():
    summary = summarize_profit(revenue=-50, cost=-10)

    assert summary.revenue == 0
    assert summary.cost == 0
    assert summary.profit == 0
    assert summary.label == "break_even"
