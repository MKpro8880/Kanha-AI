def handle_command(text):
    text = text.lower()

    if "time" in text:
        return "I will tell you the time soon."
    if "date" in text:
        return "I will tell you the date soon."

    return None