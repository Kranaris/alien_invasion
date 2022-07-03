class Settings():
    """Хранение настроек"""
    def __init__(self):
        """Инициализирует настройки"""
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (95, 100, 110)
        self.ship_speed_factor = 0.5
        self.bullet_speed_factor = 0.5
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = 100, 40, 0