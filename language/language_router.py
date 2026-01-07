def detect_language(text):
    if any(char in text for char in ["હ", "છ", "ક"]):
        return "gujarati"
    elif any(char in text for char in ["ह", "क", "म"]):
        return "hindi"
    else:
        return "english"