from shoptalk.refund_status_badge import refund_status_badge

def test_refund_status_badge_known_values():
    assert refund_status_badge('approved') == 'Refund approved'
    assert refund_status_badge('requested') == 'Refund requested'
    assert refund_status_badge('rejected') == 'Refund rejected'

def test_refund_status_badge_unknown_value():
    assert refund_status_badge("") == 'No refund'
