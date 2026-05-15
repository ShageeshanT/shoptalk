from shoptalk.schemas import MessageAnalysis


def build_suggested_reply(analysis: MessageAnalysis) -> str:
    if analysis.intent == "order_request":
        return "Thanks! I can help with that. Could you confirm the quantity and pickup or delivery time?"
    if analysis.intent == "price_question":
        return "Sure, I can check the price for you. Which item and quantity are you looking for?"
    if analysis.intent == "complaint":
        return "Sorry about that. Please send the order details so we can sort it out quickly."
    return "Thanks for the message. I’ll check and get back to you shortly."
