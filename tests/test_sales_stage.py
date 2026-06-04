from shoptalk.sales_stage import sales_stage


def test_sales_stage_new():
    assert sales_stage(False, False, False, False) == "new"


def test_sales_stage_ready():
    assert sales_stage(True, True, True, False) == "ready_to_confirm"
