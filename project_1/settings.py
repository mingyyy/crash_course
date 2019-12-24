import sys
import pygame


class Settings():
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (220, 220, 220)

        # ship settings
        self.ship_speed_factor = 1.5

        # Bullet settings
        self.bullet_speed_factor = 2
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5
