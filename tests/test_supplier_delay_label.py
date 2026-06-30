from shoptalk.supplier_delay_label import classify_supplier_delay


def test_classify_supplier_delay_labels_key_states():
    assert classify_supplier_delay(1) == "Supplier on time"
    assert classify_supplier_delay(2) == "Supplier watch"
    assert classify_supplier_delay(12) == "Supplier late"
