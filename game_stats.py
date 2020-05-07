import pygame.font


class GameStats:
    """Track statistics for Alien Invasion."""
 
    def __init__(self, ai_settings, screen):
        """Initialize statistics."""
        self.settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image_list = []
        self.msg_list = ['历史最高分: ', '当前总得分: ', '当前杀敌数: ', '剩余生命数: ']
        # Start Alien Invasion in an active state.
      
        self.game_active = False
        self.history_score = 999  # 历史最高分
        self.current_score = 0  # 当前得分
        self.kill_num = 0       # 当前杀敌数
        self.ships_left = self.settings.ship_limit  # 当前剩余飞船数

        # 设置状态栏的尺寸和其他属性
        self.font = pygame.font.SysFont('方正粗黑宋简体', 24)
        self.width, self.height = 200, 130
        self.bg_color = ai_settings.bg_color
        self.text_color = (163, 85, 104)  # 酒红色
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.centerx = self.screen_rect.width-self.width / 2
        self.rect.centery = self.height / 2

    def update_msg(self):
        str1 = ''
        msg1 = ''
        self.image_list = []
        for i in range(4):
            if i == 0:
                str1 = str(self.history_score)
            elif i == 1:
                str1 = str(self.current_score)
            elif i == 2:
                str1 = str(self.kill_num)
            elif i == 3:
                str1 = str(self.ships_left)
            msg1 = self.msg_list[i] + str1
            self.image_list.append(self.prep_msg(msg1))


    def prep_msg(self, msg):
        """ 将 msg 渲染为图像，并使其在按钮上居中 """
        # print(pygame.font.get_fonts())
        msg_image = self.font.render(msg, True, self.text_color, self.bg_color)
        return msg_image

    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.settings.ship_limit
        self.kill_num = 0
        self.current_score = 0

    def draw(self):
        #  绘制一个用颜色填充的按钮，再绘制文本
        self.update_msg()
        self.screen.fill(self.bg_color, self.rect)
        for i in range(len(self.image_list)):
            imag_rect = self.image_list[i].get_rect()
            imag_rect.left = self.rect.left
            imag_rect.top = self.font.get_height() * (0.5 + i)
            self.screen.blit(self.image_list[i], imag_rect)
