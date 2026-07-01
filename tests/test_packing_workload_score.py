from shoptalk.packing_workload_score import packing_workload_score


def test_packing_workload_score_bounds():
    assert 0 <= packing_workload_score(1) <= 100


def test_packing_workload_score_counts_rush_and_fragile_orders():
    assert packing_workload_score(5, fragile_orders=2, rush_orders=2) > packing_workload_score(5)
