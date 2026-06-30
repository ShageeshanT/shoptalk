from shoptalk.order_summary_line import order_summary_line

def test_order_summary_line():
    assert order_summary_line("Cake", 4500) == "Cake: LKR 4,500.00"
