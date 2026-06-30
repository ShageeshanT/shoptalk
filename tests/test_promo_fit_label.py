from shoptalk.promo_fit_label import classify_promo_fit


def test_classify_promo_fit_labels_key_states():
    assert classify_promo_fit(14) == "Skip promo"
    assert classify_promo_fit(15) == "Light promo"
    assert classify_promo_fit(35) == "Strong promo"
