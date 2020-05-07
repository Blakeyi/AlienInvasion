import pygame.font


class Button():

    def __init__(self, screen, ai_settings, msg, rect):
        """初始化按钮的属性"""
        # 设置按钮的尺寸和其他属性
        self.screen = screen
        self.bg_color = (0, 255, 0)
        self.text_color = (255, 255, 255)  # 黑色
        self.font = pygame.font.SysFont('方正粗黑宋简体', 48)
        self.rect = rect
        self.prep_msg(msg)
    
    def prep_msg(self, msg):
        """ 将 msg 渲染为图像，并使其在按钮上居中 """
        self.msg_image = self.font.render(msg, True, self.text_color, self.bg_color)
        self.text_rect = self.msg_image.get_rect()
        self.text_rect.centery = self.rect.centery
        self.text_rect.centerx = self.rect.centerx

    def draw(self):
        #  绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.bg_color, self.rect)
        self.screen.blit(self.msg_image, self.text_rect)