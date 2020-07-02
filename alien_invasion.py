import game_functions as gf
import pygame
import random
from settings import Settings
from ship import Ship
def run_game():
    # 游戏初始化方法,并创建对象
    pygame.init()
    ai_settings=Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("外星人入侵")
    bg_color = (ai_settings.bg_color)
    ship = Ship(ai_settings,screen)
    while True:
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()
