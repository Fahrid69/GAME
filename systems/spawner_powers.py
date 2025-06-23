import pygame, random

from constants import *
from components.powers import Hongo_Rojo, Hongo_Verde, Estrella

class GenerarPoderes:
    def __init__(self, jugador, poderes):
        self.jugador = jugador
        self.poderes = poderes

        self.spawn_end = pygame.time.get_ticks()
        self.spawn_inter = random.randint(8000, 12000) 
        self.spawn_max = 1 # Entre 8 y 12 segundos

    def update(self):
        self._generar_poder()


    def _generar_poder(self):
        if len(self.poderes) == self.spawn_max:
            return
        
        now = pygame.time.get_ticks()
        if now - self.spawn_end >= self.spawn_inter:
            self.spawn_end = now
            self.spawn_inter = random.randint(8000, 12000)

            prob = random.randint(1, 100)


            if prob <= 60 and self.jugador.vidas < 3:
                poder = Hongo_Verde( self._posicion_segura() , Y)
            elif prob <= 90 and not self.jugador.current_status_size == "gigante":
                poder = Hongo_Rojo( self._posicion_segura() , Y)
            elif prob <= 20 and not self.jugador.current_status_temporal == "inmunidad" and self.jugador.puntos > 4900:
                poder = Estrella( self._posicion_segura() , Y)
            else:
                return

            self.poderes.add(poder) 

    def _posicion_segura(self):
        # Asegura que no aparezca demasiado cerca del jugador
        while True:
            x = random.randint(100, ANCHO_VENTANA - 100)
            if abs(x - self.jugador.rect.x) > 150:
                return x