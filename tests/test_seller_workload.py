from shoptalk.seller_workload import should_show_workload_warning, workload_label


def test_workload_label_buckets_tasks():
    assert workload_label(2) == "clear"
    assert workload_label(8) == "busy"
    assert workload_label(1, overdue_tasks=1) == "overloaded"


def test_workload_warning_for_busy_sellers():
    assert should_show_workload_warning(7) is True
