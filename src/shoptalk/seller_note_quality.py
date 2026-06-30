def seller_note_quality(note):
    return "empty" if not note.strip() else "short" if len(note.strip()) < 12 else "useful"
