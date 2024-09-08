import pygame
import os
MAINPATH = os.path.dirname(os.path.dirname(__file__))

class Enemy():
    def __init__(self, screen, x, y, speed):
        self.x = x
        self.y = y
        self.speed = speed
        self.screen = screen
        self.rect = pygame.rect.Rect(self.x, self.y, 50, 50)
        self.image = pygame.transform.scale2x(pygame.image.load(os.path.join(MAINPATH, "images/astroid.png")))

    def update(self):
        self.x += self.speed
        self.rect = pygame.rect.Rect(self.x, self.y, 50, 50)
        self.screen.blit(self.image, self.rect)