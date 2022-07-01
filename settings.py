class Settings():
    """Хранение настроек"""
    def __init__(self):
        """Инициализирует настройки"""
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (100, 100, 110)
        self.ship_speed_factor = 5