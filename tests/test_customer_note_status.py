from shoptalk.customer_note_status import customer_note_status

def test_customer_note_status_thresholds():
    assert customer_note_status(5) == 'Rich notes'
    assert customer_note_status(1) == 'Has notes'
    assert customer_note_status(0) == 'No notes'

def test_customer_note_status_invalid_value():
    assert customer_note_status("bad") == 'No notes'
