    from shoptalk.inventory_coverage_label import classify_inventory_coverage


    def test_classify_inventory_coverage_labels_key_states():
        assert classify_inventory_coverage(-1) == 'Critical'
assert classify_inventory_coverage(2) == 'Low'
assert classify_inventory_coverage(10) == 'Covered'
