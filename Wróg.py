import pygame
from Objects import Objects

class Wróg(Objects):
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
        # Zwalnianie zasobów, jeśli to konieczne
        if self.obraz_załadowany:
            del self.obraz
            self.obraz_załadowany = False
        print(f"Wróg został usunięty: ({self.x}, {self.y})")

    def aktualizuj(self):
        self.x += self.prędkość * self.kierunek
        # Zmiana kierunku ruchu, jeśli wróg dotknie krawędzi ekranu
        if self.x <= 0 or self.x >= 800 - self.szerokość:
            self.kierunek *= -1
            self.y += 30  # Przesunięcie wroga w dół

        # Możesz dodać dodatkowe warunki do usuwania wroga, jeśli chcesz
        if self.y > 600:  # Załóżmy, że wysokość okna gry to 600 pikseli
            print("Wróg opuścił obszar gry")
            del self  # Wywołanie destruktora
