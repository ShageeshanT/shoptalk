from shoptalk.seller_notes import normalize_seller_note, note_preview


def test_normalize_seller_note_collapses_spaces():
    assert normalize_seller_note("  call   after   lunch ") == "call after lunch"


def test_note_preview_shortens_long_note():
    assert note_preview("a" * 80, 10) == "aaaaaaaaa…"
