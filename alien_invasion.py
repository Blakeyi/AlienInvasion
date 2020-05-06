import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from alien import Alien
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    #创建按钮
    play_button = Button(ai_settings, screen, 'PLAY')
    # 创建船
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    # 创建外星人f
    # alien = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建游戏统计信息
    stats = GameStats(ai_settings)

    pygame.display.set_caption("Alien Invasion")
    print('开始游戏')
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件和刷新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stats, play_button)
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button)
        

run_game()