from shoptalk.sentiment_badge import sentiment_badge

def test_sentiment_badge():
    assert sentiment_badge("negative")=="⚠️ Negative"