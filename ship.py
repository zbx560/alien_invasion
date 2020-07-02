import pygame
class Ship():
    def __init__(self,ai_settings,screen):
        self.screen = screen
        self.ai_settings = ai_settings

        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # 将每艘船初始位置设为屏幕底端中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)
        # 移动标志
        self.moving_right = False
        self.moving_left = False

    def blitem(self):
        self.screen.blit(self.image,self.rect)
    def update(self):
        if self.moving_left and self.rect.left > 0 :
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.screen.get_rect().right :
            self.center += self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center

