class InteractionHistoryModule:
    def __init__(self):
        print("Модуль истории взаимодействий инициализирован.")
        self.history = []

    def save_interaction(self, user_message, bot_response):
        interaction = {"user": user_message, "bot": bot_response}
        self.history.append(interaction)
        print("Взаимодействие сохранено.")

    def search_history(self, keyword):
        print(f"Поиск по истории для ключевого слова: {keyword}")
        results = [interaction for interaction in self.history if keyword in interaction["user"] or keyword in interaction["bot"]]
        print(f"Результаты поиска: {results}")
        return results

    def filter_history(self, filter_func):
        print("Фильтрация истории...")
        filtered_results = list(filter(filter_func, self.history))
        print(f"Отфильтрованные результаты: {filtered_results}")
        return filtered_results

    def run(self):
        print("Демонстрация работы модуля истории взаимодействий...")
        self.save_interaction("Привет", "Привет! Как я могу помочь?")
        self.save_interaction("Как дела?", "Все отлично, спасибо!")
        self.search_history("дела")
        self.filter_history(lambda x: "Привет" in x["user"])


if __name__ == "__main__":
    history_module = InteractionHistoryModule()
    history_module.run()