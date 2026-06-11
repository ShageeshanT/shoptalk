from shoptalk.seller_energy_label import classify_seller_energy


def test_classify_seller_energy_labels_key_states():
    assert classify_seller_energy(-1) == 'Calm'
    assert classify_seller_energy(4) == 'Focused'
    assert classify_seller_energy(10) == 'Stretched'
