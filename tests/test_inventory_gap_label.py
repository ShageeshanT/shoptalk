from shoptalk.inventory_gap_label import inventory_gap_label


def test_inventory_gap_label():
    assert inventory_gap_label(5, 2) == "partial"
