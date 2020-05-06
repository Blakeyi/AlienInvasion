class Settings():
    '''
    存储游戏设置的类
    '''
    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)      
        #飞船设置
        self.ship_step_int = 1  # 飞船移动步进距离
        self.ship_limit = 3
        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullet_step_int = 1  # 子弹移动步进距离
        self.bullets_allowed = 2000  # 为-1,即为无限子弹
        # 外星人设置
        self.alien_step_int = 1  # alien移动步进距离
        self.alien_fleet_direction = 1  #1代表右移，-1代表左移
        self.alien_drop_speed = 50

