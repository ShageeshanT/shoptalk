from shoptalk.business_hours import availability_label, is_business_hour


def test_business_hour_inside_window():
    assert is_business_hour(10)


def test_business_hour_outside_window():
    assert not is_business_hour(20)


def test_availability_label():
    assert availability_label(11) == "open"
    assert availability_label(22) == "after_hours"
