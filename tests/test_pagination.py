from shoptalk.pagination import paginate


def test_paginate_clamps_limit_and_offset() -> None:
    page = paginate([1, 2, 3], limit=500, offset=-2)
    assert page.items == [1, 2, 3]
    assert page.limit == 100
    assert page.offset == 0
