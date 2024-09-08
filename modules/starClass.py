import pygame
import random

class Star():
    def __init__(self,screen, x, y, width, height):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)

    def update(self, vel):
        self.x += vel
        self.rect = pygame.rect.Rect(self.x, self.y, self.width, self.height)
        pygame.draw.rect(self.screen, (255, 255, 255), self.rect)

class SpaceBCK():
    def __init__(self, screen, screen_width, screen_height, number_of_stars, vel):
        self.WIDTH = screen_width
        self.HEIGHT = screen_height
        self.num = number_of_stars
        self.vel = vel
        self.screen = screen
        self.stars = []
        for star in range(self.num):
            self.stars.append(Star(self.screen, random.randrange(0, self.WIDTH), random.randrange(0, self.HEIGHT), 2, 2))

    def draw(self):
        for star in self.stars:
            star.update(self.vel)
            if star.x < 0 or star.x > self.WIDTH:
                self.stars.remove(star)
                self.stars.append(Star(self.screen, self.WIDTH-5, random.randrange(0, self.HEIGHT), 2, 2))
            if star.y < 0 or star.y > self.WIDTH:
                self.stars.remove(star)
                self.stars.append(Star(self.screen, self.WIDTH-5, random.randrange(0, self.HEIGHT), 2, 2))