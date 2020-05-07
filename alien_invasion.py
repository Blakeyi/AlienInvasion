import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,
                                      ai_settings.screen_height))
    #创建按钮list
    button_list = []
    button_rect = pygame.Rect(0, 0, 200, 50)
    button_rect.centerx = screen.get_rect().centerx
    button_rect.centery = screen.get_rect().centery - 180
    descrip_button = Button(screen, ai_settings, '游戏说明', button_rect)
    button_list.append(descrip_button)
    
    button_rect.centery = screen.get_rect().centery - 100
    setting_button = Button(screen, ai_settings, '游戏设置', button_rect)
    button_list.append(setting_button)

    button_rect.centery = screen.get_rect().centery - 20
    play_button = Button(screen, ai_settings, '开始游戏', button_rect)
    button_list.append(play_button)


    
    # 创建船
    ship = Ship(screen, ai_settings)
    bullets = Group()
    aliens = Group()
    # 创建外星人f
    # alien = Alien(ai_settings, screen)
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建游戏统计信息
    stats = GameStats(ai_settings, screen)
    pygame.display.set_caption("Alien Invasion")
    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件和刷新屏幕
        gf.update_screen(ai_settings, screen, ship, bullets, aliens, stats, button_list)
        gf.check_events(ai_settings, screen, ship, bullets, stats, play_button)
        

run_game()