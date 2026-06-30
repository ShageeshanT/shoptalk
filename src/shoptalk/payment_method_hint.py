def payment_method_hint(text):
    lower = text.lower(); return "bank" if "bank" in lower else "cash" if "cash" in lower else "unknown"
