import pygame, random

from components.enemies import Goomba, Turtle
from constants import *

class GenerarEnemigos:
    def __init__(self, jugador, enemigos):
        self.jugador = jugador
        self.enemigos = enemigos

        self.spawn_end = pygame.time.get_ticks()
        self.spawn_inter = 3000
        self.spawn_max = 2

    def update(self):
        self._spawnear()
        self._dificultad_agregada()

    def _spawnear(self):
        if len(self.enemigos) >= self.spawn_max:
            return
        
        now = pygame.time.get_ticks()
        if now - self.spawn_end > self.spawn_inter:
            self.spawn_inter = random.randint(999, 9999)
            
            self.spawn_end = now

            tipo = random.choice([1, 2])

            x = ANCHO_VENTANA - 50
            y = Y

            if tipo == 1:
                enemigo = Goomba("Goomba", x, y, self.jugador)
            else:
                enemigo = Turtle("Tortuga", random.randint(self.jugador.dx - 199, self.jugador.dx + 199), 0, self.jugador)
            self.enemigos.add(enemigo)

    def _dificultad_agregada(self):
        puntos = self.jugador.puntos

        # YES
        if puntos > 1900:
            self.spawn_max = 3
            self.spawn_inter = random.randint(999,6999)
        if puntos > 4900:
            self.spawn_max = 5
            self.spawn_inter = random.randint(999,4999)
        if puntos > 9900:
            self.spawn_max = 7
            self.spawn_inter = random.randint(999,1999)
        if puntos > 14900:
            self.spawn_max = 11
            self.spawn_inter = random.randint(499,999)
        if puntos > 18900:
            self.spawn_max = 13
            self.spawn_inter = 100