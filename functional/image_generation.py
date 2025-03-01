class ImageGenerationModule:
    def __init__(self):
        print("Модуль генерации изображений инициализирован.")

    def process_request(self, text_description):
        print(f"Обработка запроса: {text_description}")
        return text_description

    def generate_image(self, description):
        print("Генерация изображения на основе описания...")
        image = "Изображение: " + description
        print(f"Сгенерированное изображение: {image}")
        return image

    def run(self, text_description):
        print("Запуск модуля генерации изображений...")
        processed_description = self.process_request(text_description)
        generated_image = self.generate_image(processed_description)
        print("Изображение успешно сгенерировано.")


if __name__ == "__main__":
    image_gen_module = ImageGenerationModule()
    text_description = "Красивый закат над морем"
    image_gen_module.run(text_description)