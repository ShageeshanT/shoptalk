from shoptalk.customer_profile_depth_label import classify_customer_profile_depth


def test_classify_customer_profile_depth_labels_key_states():
    assert classify_customer_profile_depth(-1) == 'Thin'
    assert classify_customer_profile_depth(3) == 'Useful'
    assert classify_customer_profile_depth(10) == 'Rich'
