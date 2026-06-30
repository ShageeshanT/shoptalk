def reply_queue_label(count):
    return "clear" if count == 0 else "busy" if count < 10 else "overloaded"
