    from shoptalk.bulk_order_label import classify_bulk_order


    def test_classify_bulk_order_labels_key_states():
        assert classify_bulk_order(-1) == 'Retail'
assert classify_bulk_order(10) == 'Bulk'
assert classify_bulk_order(50) == 'Wholesale'
