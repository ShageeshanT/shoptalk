from shoptalk.seller_note_quality import seller_note_quality


def test_seller_note_quality():
    assert seller_note_quality("call before delivery") == "useful"
