from Game import Game
import pygame


class Keyboard(Game):
    def __init__(self, x, prędkość):
        super().__init__()
        self.x = x
        self.prędkość = prędkość

    def qq(self):
        klawisze = pygame.key.get_pressed()
        if klawisze[pygame.K_LEFT]:
            self.x -= self.prędkość
        if klawisze[pygame.K_RIGHT]:
            self.x += self.prędkość



