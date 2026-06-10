from shoptalk.approval_status_label import approval_status_label

def test_approval_status_label_known_values():
    assert approval_status_label('approved') == 'Approved'
    assert approval_status_label('pending') == 'Pending approval'
    assert approval_status_label('rejected') == 'Rejected'

def test_approval_status_label_unknown_value():
    assert approval_status_label("") == 'Draft'
