from shoptalk.schemas import MessageAnalysis


def build_seller_summary(analysis: MessageAnalysis) -> str:
    parts = [
        f"Intent: {analysis.intent}",
        f"Urgency: {analysis.urgency}",
        f"Sentiment: {analysis.sentiment}",
    ]
    if analysis.order_details.product:
        parts.append(f"Product: {analysis.order_details.product}")
    if analysis.order_details.quantity:
        parts.append(f"Quantity: {analysis.order_details.quantity}")
    if analysis.follow_up_needed and analysis.follow_up_reason:
        parts.append(f"Follow-up: {analysis.follow_up_reason}")
    return " | ".join(parts)


def apply_tone(reply: str, tone: str) -> str:
    normalized_tone = tone.lower().strip()
    if normalized_tone == "warm":
        return f"Hi! {reply}"
    if normalized_tone == "short":
        return reply.replace("Thanks for your message. ", "")
    if normalized_tone == "professional":
        return reply.replace("Hi", "Hello")
    return reply
