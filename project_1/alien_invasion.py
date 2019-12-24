import pygame
from pygame.sprite import Group

from settings import Settings
from game_functions import check_events, update_screen, update_bullets, create_fleet
from ship import Ship
from alien import Alien


def run_game():
    # Initialize game and create a screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Make a ship， a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens
    create_fleet(ai_settings, screen, ship, aliens)

    while True:
        check_events(ai_settings, screen, ship, bullets)
        ship.update()
        update_bullets(bullets)

        update_screen(ai_settings, screen, ship, aliens, bullets)



if __name__ == '__main__':
    run_game()