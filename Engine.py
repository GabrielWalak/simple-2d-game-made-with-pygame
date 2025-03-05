import pygame
from copy import copy, deepcopy
from Gracz import Gracz
from Wróg import Wróg
from Pocisk import Pocisk

class Engine:
    def __init__(self):
        self.gracz = Gracz(370, 500, 60, 40, "gracz.png", 5)
        self.lista_wrogów = []
        self.lista_pocisków = []
        self.czas_ostatniego_strzału = 0
        self.opóźnienie_strzału = 500
        self.czas_ostatniego_wroga = 0
        self.opóźnienie_wroga = 4000

    def __copy__(self):
        raise TypeError("Shallow copy is not allowed for this object")

    def __deepcopy__(self, memo):
        raise TypeError("Deep copy is not allowed for this object")

    def utwórz_wrogów(self):
        for y in range(2):
            for x in range(10):
                wróg = Wróg(x * 50 + 60, y * 50 + 50, 40, 30, "wróg.png", 2, 1)
                self.lista_wrogów.append(wróg)

    def strzelaj(self):
        aktualny_czas = pygame.time.get_ticks()
        if aktualny_czas - self.czas_ostatniego_strzału > self.opóźnienie_strzału:
            pocisk = Pocisk(self.gracz.x + 22, self.gracz.y, 6, 10, "pocisk.png", 8, -1)
            self.lista_pocisków.append(pocisk)
            self.czas_ostatniego_strzału = aktualny_czas

    def aktualizuj(self):
        self.gracz.aktualizuj()
        aktualny_czas = pygame.time.get_ticks()
        if aktualny_czas - self.czas_ostatniego_wroga > self.opóźnienie_wroga:
            wróg = Wróg(370, 50, 40, 30, "wróg.png", 2, 1)
            self.lista_wrogów.append(wróg)
            self.czas_ostatniego_wroga = aktualny_czas

        for wróg in self.lista_wrogów[:]:
            wróg.aktualizuj()
            if wróg.y > self.gracz.y - self.gracz.wysokość:
                self.koniec_gry()

        for pocisk in self.lista_pocisków[:]:
            pocisk.aktualizuj()
            if pocisk.y < -10:
                self.lista_pocisków.remove(pocisk)

        self.sprawdź_kolizje()

    def sprawdź_kolizje(self):
        for wróg in self.lista_wrogów[:]:
            for pocisk in self.lista_pocisków[:]:
                if pygame.Rect(wróg.x, wróg.y, wróg.szerokość, wróg.wysokość).colliderect(
                    pygame.Rect(pocisk.x, pocisk.y, pocisk.szerokość, pocisk.wysokość)
                ):
                    self.lista_wrogów.remove(wróg)
                    self.lista_pocisków.remove(pocisk)
                    break

    def koniec_gry(self):
        pass

    def __del__(self):
        # Zwolnij zasoby i zakończ sesję Pygame
        print("Cleaning up Engine resources...")
        self.lista_wrogów.clear()
        self.lista_pocisków.clear()
        pygame.quit()
        print("Engine object is being deleted and Pygame is quit")
