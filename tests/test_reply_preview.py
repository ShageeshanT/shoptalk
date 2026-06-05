from shoptalk.reply_preview import reply_preview

def test_reply_preview():
    assert reply_preview("a "*40,10)=="a a a a a…"