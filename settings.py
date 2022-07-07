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
        self.bullet_width = 500
        self.bullet_height = 15
        self.bullet_color = 100, 40, 20
        self.bullet_allowed = 3
        # Aliens
        self.fleet_drop_speed = 15
        #speedup game factor
        self.speedup_scale = 1.2
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.fleet_direction = 1  # "1" - right, "-1" left
        self.alien_points = 1

    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)