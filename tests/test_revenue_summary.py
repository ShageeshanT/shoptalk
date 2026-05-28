from shoptalk.revenue_summary import revenue_summary


def test_revenue_summary_empty():
    assert revenue_summary([]) == {"count": 0, "total": 0, "average": 0.0}


def test_revenue_summary_values():
    assert revenue_summary([100, 200, 250]) == {"count": 3, "total": 550, "average": 183.33}
