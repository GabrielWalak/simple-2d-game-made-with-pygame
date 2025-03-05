import pygame
from copy import copy, deepcopy
from Game import Game

class Graphics(Game):
    def __init__(self):
        super().__init__()
        self.szerokość_okna = 800
        self.wysokość_okna = 600
        self.okno = pygame.display.set_mode((self.szerokość_okna, self.wysokość_okna))
        pygame.display.set_caption("Space Invaders")

    def __copy__(self):
        raise TypeError("Shallow copy is not allowed for this object")

    def __deepcopy__(self, memo):
        raise TypeError("Deep copy is not allowed for this object")

    def koniec_gry(self):
        czcionka = pygame.font.SysFont(None, 100)
        tekst = czcionka.render("GAME OVER", True, (255, 0, 0))
        tekst_rect = tekst.get_rect(center=(self.szerokość_okna // 2, self.wysokość_okna // 2))

        self.okno.blit(tekst, tekst_rect)
        pygame.display.flip()

        pygame.time.delay(3000)
        pygame.quit()

    def rysuj(self):
        self.okno.fill((0, 0, 0))
        self.blituj(self.gracz)
        for wróg in self.lista_wrogów:
            self.blituj(wróg)
        for pocisk in self.lista_pocisków:
            self.blituj(pocisk)
        pygame.display.flip()

    def blituj(self, obiekt):
        self.okno.blit(obiekt.obraz, (obiekt.x, obiekt.y))

    def obsługa_inputu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.strzelaj()

        klawisze = pygame.key.get_pressed()
        if klawisze[pygame.K_LEFT]:
            self.gracz.x -= self.gracz.prędkość
        if klawisze[pygame.K_RIGHT]:
            self.gracz.x += self.gracz.prędkość
        if self.gracz.x < 0:
            self.gracz.x = 0
        elif self.gracz.x > self.szerokość_okna - self.gracz.szerokość:
            self.gracz.x = self.szerokość_okna - self.gracz.szerokość
