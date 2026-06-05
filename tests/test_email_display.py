from shoptalk.email_display import email_display

def test_email_display():
    assert email_display(" A@B.COM ")=="a@b.com"