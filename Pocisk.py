import pygame
from Objects import Objects
from copy import copy, deepcopy
class Pocisk(Objects):
    def __init__(self, x, y, szerokość, wysokość, obraz, prędkość, kierunek):
        super().__init__(x, y, szerokość, wysokość, obraz)
        self.prędkość = prędkość
        self.kierunek = kierunek
        self.obraz_załadowany = True

    def __copy__(self):
        raise TypeError("Shallow copy is not allowed for this object")

    def __deepcopy__(self, memo):
        raise TypeError("Deep copy is not allowed for this object")

    def __del__(self):
        if self.obraz_załadowany:
            del self.obraz
            self.obraz_załadowany = False
        print(f"Pocisk został usunięty: ({self.x}, {self.y})")

    def aktualizuj(self):
        self.y += self.prędkość * self.kierunek
        # Usunięcie pocisku, jeśli opuści obszar gry
        if self.y < 0 or self.y > 600:  # Załóżmy, że wysokość okna gry to 600 pikseli
            print("Pocisk opuścił obszar gry")
            del self  # Wywołanie destruktora


