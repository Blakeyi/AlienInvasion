import pygame
import os
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像，设置属性
        filename = ai_settings.resource_path(os.path.join("images", "alien.bmp"))
        # self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.image.load(filename)
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        self.count = 0  # 用于控制外星人移动
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ 移动外星人 """
        self.x += (self.ai_settings.alien_step_int *
                   self.ai_settings.alien_fleet_direction)
        self.rect.x = self.x
    
    def check_edges(self):
        """ 如果外星人位于屏幕边缘，就返回 True"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def draw(self):
        self.blitme()
