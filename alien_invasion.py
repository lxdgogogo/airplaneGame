import game_functions as gf
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from GameStats import GameStats
from botton import Button
from scoreboard import Scoreboard


def run_game():  # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # 创建play按钮
    play_button = Button(ai_settings, screen, "PLAY")
    # 创建一个用于存储游戏统计信息的实例并创建记分牌
    stats = GameStats(ai_settings)
    scoreboard = Scoreboard(ai_settings, screen, stats)

    # 创建一个飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets, scoreboard)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets, stats, scoreboard)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, scoreboard)
        gf.update_screen(ai_settings, screen, stats, ship, bullets, aliens, play_button, scoreboard)


run_game()
