from shoptalk.export_names import safe_export_name


def test_safe_export_name():
    assert safe_export_name("May Orders.csv") == "may_orders_csv"


def test_safe_export_name_default():
    assert safe_export_name(" !!! ") == "export"
