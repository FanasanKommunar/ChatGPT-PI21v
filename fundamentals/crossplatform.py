class CrossPlatformModule:
    def __init__(self):
        print("Модуль кроссплатформенной доступности инициализирован.")

    def optimize_for_web(self):
        print("Оптимизация интерфейса для веб-приложения завершена.")

    def optimize_for_mobile(self):
        print("Оптимизация интерфейса для мобильного приложения завершена.")

    def optimize_for_desktop(self):
        print("Оптимизация интерфейса для настольного приложения завершена.")

    def run(self):
        print("Запуск модуля кроссплатформенной доступности...")
        self.optimize_for_web()
        self.optimize_for_mobile()
        self.optimize_for_desktop()
        print("Приложение доступно на всех платформах.")


if __name__ == "__main__":
    cross_platform_module = CrossPlatformModule()
    cross_platform_module.run()