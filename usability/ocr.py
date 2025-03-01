class OCRModule:
    def __init__(self):
        print("Модуль распознавания текста по изображению инициализирован.")

    def upload_image(self, image_path):
        print(f"Изображение загружено: {image_path}")
        return image_path

    def extract_text(self, image_path):
        print("Обработка изображения для извлечения текста...")
        extracted_text = "Пример извлеченного текста."
        print(f"Извлеченный текст: {extracted_text}")
        return extracted_text

    def run(self, image_path):
        print("Запуск модуля распознавания текста...")
        uploaded_image = self.upload_image(image_path)
        extracted_text = self.extract_text(uploaded_image)
        print("Текст успешно извлечен.")


if __name__ == "__main__":
    ocr_module = OCRModule()
    image_path = "example_image.png"
    ocr_module.run(image_path)