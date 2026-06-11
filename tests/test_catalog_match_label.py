    from shoptalk.catalog_match_label import classify_catalog_match


    def test_classify_catalog_match_labels_key_states():
        assert classify_catalog_match(-1) == 'None'
assert classify_catalog_match(1) == 'Possible'
assert classify_catalog_match(2) == 'Multiple'
