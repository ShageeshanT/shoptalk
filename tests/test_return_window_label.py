from shoptalk.return_window_label import return_window_label

def test_return_window_label_thresholds():
    assert return_window_label(0) == 'Return closed'
    assert return_window_label(7) == 'Return closing soon'
    assert return_window_label(30) == 'Return open'

def test_return_window_label_invalid_value():
    assert return_window_label("bad") == 'Extended return'
