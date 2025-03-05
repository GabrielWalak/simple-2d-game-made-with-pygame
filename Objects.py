import pygame
from copy import copy, deepcopy
class Objects:
    def __init__(self, x, y, szerokość, wysokość, obraz):
        self.x = x
        self.y = y
        self.szerokość = szerokość
        self.wysokość = wysokość
        self.obraz = pygame.image.load(obraz)  # Załadowanie obrazu

    def __copy__(self):
        raise TypeError("Shallow copy is not allowed for this object")

    def __deepcopy__(self, memo):
        raise TypeError("Deep copy is not allowed for this object")

    def aktualizuj(self):
        pass

