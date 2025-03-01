class LanguageDetectionModule:
    def __init__(self):
        print("Модуль определения языка инициализирован.")

    def detect_language(self, text):
        print(f"Определение языка для текста: {text}")
        detected_language = "русский"
        print(f"Определенный язык: {detected_language}")
        return detected_language

    def set_language(self, language):
        print(f"Выбран язык: {language}")
        return language

    def run(self, text, user_language=None):
        print("Запуск модуля определения языка...")
        detected_language = self.detect_language(text)
        if user_language:
            selected_language = self.set_language(user_language)
        else:
            selected_language = detected_language
        print(f"Используемый язык: {selected_language}")


if __name__ == "__main__":
    language_module = LanguageDetectionModule()
    text = "Привет, как дела?"
    language_module.run(text, user_language="русский")