def conversation_flags(text: str) -> list[str]:
    lowered = text.lower()
    flags = []
    if any(word in lowered for word in ["angry", "refund", "bad service"]):
        flags.append("needs_owner_attention")
    if any(word in lowered for word in ["urgent", "today", "asap"]):
        flags.append("time_sensitive")
    if any(word in lowered for word in ["paid", "receipt", "slip"]):
        flags.append("payment_related")
    return flags
