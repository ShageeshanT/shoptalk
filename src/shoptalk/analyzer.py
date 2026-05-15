import re

from shoptalk.reply_builder import apply_tone
from shoptalk.schemas import MessageAnalysis, MessageAnalyzeRequest, OrderDetails


def _detect_quantity(text: str) -> int | None:
    match = re.search(r"\b(\d+)\b", text)
    if match:
        return int(match.group(1))
    lowered = text.lower()
    words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
    for word, value in words.items():
        if re.search(rf"\b{word}\b", lowered):
            return value
    return None


def _detect_intent(text: str) -> str:
    lowered = text.lower()
    if any(word in lowered for word in ["refund", "angry", "bad review", "complain", "wrong", "late"]):
        return "complaint"
    if any(word in lowered for word in ["pay", "payment", "paid", "deposit", "bank transfer"]):
        return "payment_question"
    if any(word in lowered for word in ["deliver", "delivery", "pickup", "where is my order"]):
        return "delivery_question"
    if any(word in lowered for word in ["order", "i want", "can i get", "can i have", "book"]):
        return "new_order"
    if any(word in lowered for word in ["available", "price", "how much", "do you have"]):
        return "product_inquiry"
    return "general"


def analyze_message(payload: MessageAnalyzeRequest) -> MessageAnalysis:
    """Rule-based placeholder analyzer.

    The production version will call an LLM and request strict JSON output.
    This deterministic version keeps the first repo commit runnable without secrets.
    """

    text = payload.text.strip()
    lowered = text.lower()
    intent = _detect_intent(text)
    urgency = "high" if any(word in lowered for word in ["urgent", "today", "asap", "bad review"]) else "normal"
    sentiment = "negative" if intent == "complaint" else "neutral"

    details = OrderDetails(quantity=_detect_quantity(text))

    if "cake" in lowered:
        details.product = "cake"
    elif "shirt" in lowered or "t-shirt" in lowered:
        details.product = "t-shirt"
    elif "dress" in lowered:
        details.product = "dress"

    size_match = re.search(r"\b(\d+(?:\.\d+)?\s?kg|small|medium|large|xl|xxl)\b", lowered)
    if size_match:
        details.size = size_match.group(1)

    if "birthday" in lowered:
        details.custom_text = "birthday message mentioned"

    if any(word in lowered for word in ["deliver", "delivery"]):
        details.delivery_required = True
    elif "pickup" in lowered:
        details.delivery_required = False

    suggested_reply = "Hi! Thanks for your message. Could you share a few more details so I can confirm this for you?"
    follow_up_needed = intent in {"new_order", "payment_question", "product_inquiry"}
    follow_up_reason = "Customer needs confirmation" if follow_up_needed else None

    if intent == "new_order":
        suggested_reply = "Hi! Yes, we can help with that. Could you confirm the date, quantity, and whether you prefer pickup or delivery?"
    elif intent == "product_inquiry":
        suggested_reply = "Hi! Yes, let me check availability for you. Which size or option are you looking for?"
    elif intent == "payment_question":
        suggested_reply = "Hi! You can complete the payment through the available payment method, and send the receipt here once done."
    elif intent == "delivery_question":
        suggested_reply = "Hi! Let me check the delivery status and update you shortly."
    elif intent == "complaint":
        suggested_reply = "Hi, sorry about that. Let me check this immediately and help sort it out for you."

    return MessageAnalysis(
        intent=intent,  # type: ignore[arg-type]
        urgency=urgency,  # type: ignore[arg-type]
        sentiment=sentiment,  # type: ignore[arg-type]
        customer_needs_reply=True,
        order_details=details,
        follow_up_needed=follow_up_needed,
        follow_up_reason=follow_up_reason,
        suggested_reply=apply_tone(suggested_reply, payload.tone),
        confidence=0.62,
    )
