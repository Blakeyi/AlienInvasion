import pygame


class Ship():

    def __init__(self, screen, ai_settings):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.moving_right = False  # True 一直移动
        self.moving_left = False  # True 一直移动
        self.ai_settings = ai_settings

        self.center_ship()
        self.bullet_num = ai_settings.bullets_allowed  #初始化为最大子弹数

    def blitme(self):
        """在指定的位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ 根据移动标志调整飞船的位置 """
        if self.moving_right:
            if (self.rect.centerx + self.ai_settings.ship_step_int) < (self.screen_rect.right - self.rect.width / 2) :
                self.rect.centerx += self.ai_settings.ship_step_int
            else:
                self.rect.centerx = self.screen_rect.right - self.rect.width / 2
        elif self.moving_left:
            if (self.rect.centerx - self.ai_settings.ship_step_int) > (self.screen_rect.left + self.rect.width / 2):
                self.rect.centerx -= self.ai_settings.ship_step_int
            else:
                self.rect.centerx = self.screen_rect.left + self.rect.width / 2

        self.blitme()

    def center_ship(self):
        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

