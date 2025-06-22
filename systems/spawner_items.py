import pygame, random

from constants import *
from components.items import Moneda

class GenerarItems:
    def __init__(self, jugador, items):
        self.jugador = jugador
        self.items = items

        self.spawn_end = pygame.time.get_ticks()
        self.spawn_inter = 0
        self.spawn_max = 3

    def update(self):
        self._spawn_moneda()

    def _spawn_moneda(self):
        now = pygame.time.get_ticks()
        if len(self.items) >= self.spawn_max:
            return
        
        if now - self.spawn_end > self.spawn_inter:
            self.spawn_inter = random.randint(999, 9999)
            self.spawn_end = now

            x = random.randint(50, ANCHO_VENTANA - 100)
            y = random.randint(500, Y)

            moneda = Moneda(x, y, self.jugador)
            self.items.add(moneda)