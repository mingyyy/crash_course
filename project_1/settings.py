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
        self.bullet_speed_factor = 5
        self.bullet_width = 3
        self.bullet_height = 12
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        # alien settings
        self.alien_speed_factor = 2
        self.fleet_drop_speed = 3

        # fleet_direction of 1 represents right; -1 left
        self.fleet_direction = 1
        self.ship_limit = 3


