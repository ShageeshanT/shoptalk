    from shoptalk.invoice_status_label import classify_invoice_status


    def test_classify_invoice_status_labels_key_states():
        assert classify_invoice_status(-1) == 'Paid'
assert classify_invoice_status(0) == 'Due soon'
assert classify_invoice_status(4) == 'Overdue'
