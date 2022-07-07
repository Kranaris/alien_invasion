class Settings():
    """Хранение настроек"""

    def __init__(self):
        """Инициализирует настройки"""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (95, 100, 110)
        # Ship
        self.ship_limit = 3
        # Bullets
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 100, 40, 20
        self.bullet_allowed = 3
        # Aliens
        self.fleet_drop_speed = 15
        #speedup game factor
        self.speedup_scale = 1.2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1  # "1" - right, "-1" left

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale