class GameStats():

    def __init__(self, ai_settings):
        with open("high_score.txt", "r") as hs:
            file_high_score = int(hs.read())
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False
        self.high_score = file_high_score

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
