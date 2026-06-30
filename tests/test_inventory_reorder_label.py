from shoptalk.inventory_reorder_label import classify_inventory_reorder


def test_classify_inventory_reorder_labels_key_states():
    assert classify_inventory_reorder(2) == "Reorder now"
    assert classify_inventory_reorder(7) == "Reorder soon"
    assert classify_inventory_reorder(17) == "Stock safe"
