    from shoptalk.customer_tag_density_label import classify_customer_tag_density


    def test_classify_customer_tag_density_labels_key_states():
        assert classify_customer_tag_density(-1) == 'Untagged'
assert classify_customer_tag_density(1) == 'Tagged'
assert classify_customer_tag_density(6) == 'Crowded'
