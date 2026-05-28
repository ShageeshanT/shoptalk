from shoptalk.order_summary import summarize_order_items


def test_summarizes_empty_order():
    assert summarize_order_items([]) == "No items"


def test_summarizes_short_order():
    assert summarize_order_items(["Cake", "Brownies"]) == "Cake, Brownies"


def test_summarizes_long_order():
    assert summarize_order_items(["A", "B", "C", "D"]) == "A, B, C +1 more"
