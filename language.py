# language.py
def detect_language(text):
    # Пример простого определения языка
    if text.isascii():
        return "English"
    else:
        return "Unknown Language"
