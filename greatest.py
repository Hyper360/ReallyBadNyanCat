import pygame
import random
from modules.breathingText import BreathingText
from modules.playerClass import Player
from modules.enemyClass import Enemy
from modules.starClass import SpaceBCK

pygame.init()
song = pygame.mixer.music.load('music/Hypnotize.mp3')
display_info = pygame.display.Info()
WIDTH = display_info.current_w//2
HEIGHT = display_info.current_h//2
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags= pygame.FULLSCREEN|pygame.SCALED, vsync=1)
clock = pygame.time.Clock()
pygame.display.set_caption("Trash Nyan Cat")
pygame.display.set_icon(pygame.image.load('images/Catig.png'))
font = pygame.font.SysFont('Arial', 25)

class Game():
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.title = BreathingText(screen, 0, 0, 100, "Ghetto Nyan Cat", [(255, 0, 0), (0, 255, 0), (0, 0, 255)])
        self.songplaying = False
        self.spacebck = SpaceBCK(screen, WIDTH, HEIGHT, 700, -2)
        self.player = Player(self.screen, 300, 300, 8)
        self.enemies = []

        #SCORE TRACKING :>
        self.score = 0
        self.scoreSurface = font.render('Score :' + str(self.score),True, (200, 0, 0), None)
        self.scoreSurfaceRect = self.scoreSurface.get_rect()
        self.scoreSurfaceRect.x = 0
        self.scoreSurfaceRect.y = 0

        self.fps = clock.get_fps()
        self.fpsSurface = font.render('FPS :' + str(self.fps),True, (200, 0, 0), None)
        self.fpsSurfaceRect = self.fpsSurface.get_rect()
        self.fpsSurfaceRect.x = 0
        self.fpsSurfaceRect.y = HEIGHT - 30

        for i in range(20):
            self.enemies.append(Enemy(self.screen, WIDTH, random.randrange(0, HEIGHT), -10))


        self.state = "start"

    def start(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = "run"

        screen.fill((0, 0, 0))
        self.title.draw()

        pygame.display.flip()
        self.clock.tick(60)


    def run(self):
        curr_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.player.move(click=True)
        if self.songplaying == False:
            pygame.mixer.music.play(-1)
            self.songplaying = True
        else:
            pass
        self.screen.fill((0,0,0))
        self.spacebck.draw()

        for enemy in self.enemies:
            enemy.update()
            if enemy.x < 0:
                self.enemies.remove(enemy)
        if len(self.enemies) < 10:
            self.enemies.append(Enemy(self.screen, WIDTH, random.randrange(0, HEIGHT), -5))
        for bullet in self.player.bullets:
            bullet.update()
            if bullet.x > WIDTH:
                self.player.bullets.remove(bullet)
            for enemy in self.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    self.enemies.remove(enemy)
                    self.score += 100
                    bullet.x = WIDTH*2
        self.player.update()

        self.scoreSurface = font.render('Score :' + str(self.score),True, (200, 0, 0), None)
        self.screen.blit(self.scoreSurface, self.scoreSurfaceRect)

        self.fps = clock.get_fps()
        self.fpsSurface = font.render('FPS :' + str(round(self.fps)) + '/60',True, (200, 0, 0), None)
        self.screen.blit(self.fpsSurface, self.fpsSurfaceRect)

        pygame.display.flip()
        clock.tick(60)

    def manager(self):
        if self.state == "start":
            self.start()
        elif self.state == "run":
            self.run()

game = Game(screen, clock)

while True:
    game.manager()