import pygame
import os
MAINPATH = os.path.dirname(os.path.dirname(__file__))

class Bullet():
    def __init__(self, screen, x, y, speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(os.path.join(MAINPATH, 'images/bullet.png'))
        self.image = pygame.transform.scale(self.image, (30, 10))
        self.image_rect = self.image.get_rect()
        self.rect = pygame.rect.Rect(self.x, self.y, 15, 5)
        self.image_rect.x = self.rect.x
        self.image_rect.y = self.rect.y

    def update(self):
        self.rect.x += self.speed
        self.image_rect.x = self.rect.x
        self.image_rect.y = self.rect.y
        self.screen.blit(self.image, self.image_rect)