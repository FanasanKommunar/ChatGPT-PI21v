class VoiceInputModule:
    def __init__(self):
        print("Модуль голосового ввода инициализирован.")

    def recognize_speech(self):
        print("Распознавание речи...")
        recognized_text = "Привет, это пример распознанного текста."
        print(f"Распознанный текст: {recognized_text}")
        return recognized_text

    def send_text_to_chat(self, text):
        print(f"Отправка текста в чат: {text}")
        print("Текст успешно отправлен.")

    def run(self):
        print("Голосовой ввод активирован. Говорите...")
        recognized_text = self.recognize_speech()
        self.send_text_to_chat(recognized_text)


if __name__ == "__main__":
    voice_module = VoiceInputModule()
    voice_module.run()