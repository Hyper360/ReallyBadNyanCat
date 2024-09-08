import pygame

class BreathingText:
    def __init__(self, screen : pygame.Surface, x : int, y : int, size : int, text : str, colors : list):
        self.screen = screen
        self.x = x
        self.y = y
        self.text = text
        self.size = size
        self.textSurf = pygame.font.SysFont("Arial", self.size).render(self.text, True, colors[0])
        self.colors = colors

        self.colorInd = 0
        self.alpha = 255
        self.increaseFactor = 1

    def changeAlpha(self):
        if self.alpha >= 255:
            self.increaseFactor *= -1
        elif self.alpha <= 0:
            self.increaseFactor *= -1
            self.colorInd = self.colorInd+1 if self.colorInd+1 < len(self.colors) else 0
            self.textSurf = pygame.font.SysFont("Arial", self.size).render(self.text, True, self.colors[self.colorInd])
            self.textSurf.set_alpha(0)

        self.alpha += (1*self.increaseFactor)

        return self.alpha
    
    def draw(self):
        self.textSurf.set_alpha(self.changeAlpha())
        self.screen.blit(self.textSurf, (self.x, self.y))