class AutocompleteModule:
    def __init__(self):
        print("Модуль автозаполнения и подсказок инициализирован.")

    def get_suggestions(self, input_text):
        suggestions = ["пример", "программирование", "проект"]
        print(f"Подсказки для '{input_text}': {suggestions}")
        return suggestions

    def correct_typos(self, input_text):
        corrected_text = input_text.replace("ошибка", "исправлено")
        print(f"Исправленный текст: {corrected_text}")
        return corrected_text

    def run(self, user_input):
        print("Обработка ввода пользователя...")
        suggestions = self.get_suggestions(user_input)
        corrected_text = self.correct_typos(user_input)
        print(f"Итоговый текст: {corrected_text}")


if __name__ == "__main__":
    autocomplete_module = AutocompleteModule()
    user_input = "ошибка в тексте"
    autocomplete_module.run(user_input)
