import pygame
from copy import copy, deepcopy
from Engine import Engine
class Game(Engine):
    def __init__(self):
        super().__init__()

    def __copy__(self):
        raise TypeError("Shallow copy is not allowed for this object")

    def __deepcopy__(self, memo):
        raise TypeError("Deep copy is not allowed for this object")

    def run(self):
        pygame.init()
        self.utwórz_wrogów()

        zegar = pygame.time.Clock()
        while True:
            self.obsługa_inputu()
            self.aktualizuj()
            self.rysuj()
            zegar.tick(90)

        self.koniec_gry()


