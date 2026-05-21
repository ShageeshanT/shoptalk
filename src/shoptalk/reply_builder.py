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
    if analysis.order_details.size:
        parts.append(f"Size: {analysis.order_details.size}")
    if analysis.order_details.needed_by:
        parts.append(f"Needed by: {analysis.order_details.needed_by}")
    if analysis.order_details.delivery_required is not None:
        parts.append("Delivery: yes" if analysis.order_details.delivery_required else "Delivery: pickup")
    if analysis.order_details.custom_text:
        parts.append(f"Custom text: {analysis.order_details.custom_text}")
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
