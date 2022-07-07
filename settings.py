class Settings():
    """Хранение настроек"""

    def __init__(self):
        """Инициализирует настройки"""
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (95, 100, 110)
        self.ship_speed_factor = 2
        self.ship_limit = 3
        self.bullet_speed_factor = 3
        self.bullet_width = 5
        self.bullet_height = 25
        self.bullet_color = 100, 40, 20
        self.bullet_allowed = 5
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 200
        self.fleet_direction = 1  # "1" - right, "-1" left
