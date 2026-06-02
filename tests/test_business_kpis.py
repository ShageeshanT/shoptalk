from shoptalk.business_kpis import average_order_value, conversion_rate


def test_conversion_rate_handles_zero_inquiries():
    assert conversion_rate(3, 0) == 0


def test_business_kpis_calculate_values():
    assert conversion_rate(5, 20) == 25
    assert average_order_value(10000, 4) == 2500
