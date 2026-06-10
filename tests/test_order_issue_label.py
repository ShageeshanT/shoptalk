from shoptalk.order_issue_label import order_issue_label

def test_order_issue_label_known_values():
    assert order_issue_label('missing_item') == 'Missing item'
    assert order_issue_label('wrong_address') == 'Wrong address'
    assert order_issue_label('late_delivery') == 'Late delivery'

def test_order_issue_label_unknown_value():
    assert order_issue_label("") == 'General issue'
