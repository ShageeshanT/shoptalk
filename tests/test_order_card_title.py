from shoptalk.order_card_title import order_card_title

def test_order_card_title():
    assert order_card_title("Cake", "Nimal")=="Cake · Nimal"