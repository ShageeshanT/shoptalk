from shoptalk.inbox_pressure_label import inbox_pressure_label

def test_inbox_pressure_label_thresholds():
    assert inbox_pressure_label(100) == 'Inbox overloaded'
    assert inbox_pressure_label(30) == 'Inbox busy'
    assert inbox_pressure_label(1) == 'Inbox active'

def test_inbox_pressure_label_invalid_value():
    assert inbox_pressure_label("bad") == 'Inbox clear'
