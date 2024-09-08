import pygame
import os
from modules.bulletClass import Bullet
MAINPATH = os.path.dirname(os.path.dirname(__file__))

class TrailOBJ(pygame.Rect):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height)
        self.color = color

class Player():
    def __init__(self, screen, x, y, speed):
        self.screen = screen
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(os.path.join(MAINPATH, 'images/Catig.png'))
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.set_colorkey((255,255,255))
        self.rect = self.image.get_rect()

        self.gun_image = pygame.image.load(os.path.join(MAINPATH, 'images/glock.png'))
        self.gun_image = pygame.transform.scale(self.gun_image, (25, 25))
        self.gun_image = pygame.transform.flip(self.gun_image, True, False)
        self.gun_image_rect = self.gun_image.get_rect()
        self.gun_image_rect.center = self.rect.midright

        self.trail = pygame.rect.Rect(self.rect.centerx - 50, self.rect.y, self.rect.width, self.rect.height)
        self.bullets = []
        self.trails = []
        self.curColor = [255, 0, 0]
        self.incIndex = [1, "O"]
        self.decIndex = [0, "X"]

        self.reloadtime = pygame.time.get_ticks()
        self.reload = 150
        self.shot = pygame.mixer.Sound(os.path.join(MAINPATH, "music/Gunshot.mp3"))

    def colorGen(self):
        if self.incIndex[1] != "X":
            ind = self.incIndex[0]
            if self.curColor[ind] < 255:
                self.curColor[ind] += 5
            else:
                self.incIndex[0] = self.incIndex[0]+1 if self.incIndex[0]+1 <= 2 else 0
                self.incIndex[1] = "X"
                self.decIndex[1] = "O"


        if self.decIndex[1] != "X":
            ind = self.decIndex[0]
            if self.curColor[ind] > 0:
                self.curColor[ind] -= 5
            else:
                self.decIndex[0] = self.decIndex[0]+1 if self.decIndex[0]+1 <= 2 else 0
                self.decIndex[1] = "X"
                self.incIndex[1] = "O"


        return (self.curColor[0], self.curColor[1], self.curColor[2])

    def trail_update(self):
         for trail in self.trails:
            trail.x -= self.speed
            pygame.draw.rect(self.screen, trail.color, trail)
            if trail.x < 0:
                self.trails.remove(trail)

    def move(self, click = False):
        curr_time = pygame.time.get_ticks()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x -= (self.speed * 2)
        if keys[pygame.K_RIGHT]:
            self.x += self.speed
        if keys[pygame.K_DOWN]:
            self.y += self.speed
        if keys[pygame.K_UP]:
            self.y -= self.speed
        if keys[pygame.K_SPACE] or click == True:
            if curr_time - self.reloadtime >= self.reload:
                self.bullets.append(Bullet(self.screen, self.gun_image_rect.midright[0], self.gun_image_rect.midright[1] - 10, 10))
                self.reloadtime = curr_time
                self.shot.play(maxtime=1000)

        self.rect.x = self.x
        self.rect.y = self.y
        self.rect.center = (self.x, self.y)
        self.gun_image_rect.centerx = self.rect.midright[0] + 15
        self.gun_image_rect.centery = self.rect.midright[1]
        self.trail = TrailOBJ(self.rect.x - 30, self.rect.y, self.rect.width, self.rect.height, self.colorGen())
        self.trails.append(self.trail)

    def update(self):
        self.trail_update()
        self.move()
        self.screen.blit(self.image, (self.rect))
        self.screen.blit(self.gun_image, self.gun_image_rect)