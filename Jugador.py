from Molde import Personaje
from constants import *
from Enemigo import Animacion

import pygame

vb = "mm1"

class Jugador(Personaje):
    def __init__(self, nombre, dx, dy):
        super().__init__(nombre, dx, dy)
        self.vidas = 3
        self.puntos = 0
        self.gravedad = 1
        self.velocidad = 0
        self.poder = False
        self.estado = True
        self.ensuelo = True
        self.direccion = "der"
        self.sprites = SPRITES_JUGADOR
        self.image = self.sprites[vb]["derecha"]
        self.rect = self.image.get_rect(topleft=(dx, dy) )

        self.animacion_der = Animacion([self.sprites[vb]["der_correr1"], self.sprites[vb]["der_correr2"],self.sprites[vb]["der_correr3"]], velocidad = 7.5)
        self.animacion_izq = Animacion([self.sprites[vb]["izq_correr1"], self.sprites[vb]["izq_correr2"],self.sprites[vb]["izq_correr3"]], velocidad = 7.5)

    def update(self):
        keys = pygame.key.get_pressed()
        self.movimiento = False

#          DETECTAR CONTROLES
        if keys[pygame.K_UP] and self.ensuelo:
            self.velocidad = -20
            self.ensuelo = False
        elif keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.dx += 5
            self.direccion = "der"
            self.movimiento = True
        elif keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:
            self.dx -= 5
            self.direccion = "izq"
            self.movimiento = True

        if not self.ensuelo:
            self.velocidad +=self.gravedad
            self.dy += self.velocidad

        if self.dy >= Y:
            self.dy = Y
            self.velocidad = 0
            self.ensuelo = True

#          ACTUALIZAR LA ANIMACION
#
        if not self.ensuelo:
            self.image = SPRITES_JUGADOR[vb]["saltando_der"] if self.direccion == "der" else SPRITES_JUGADOR[vb]["saltando_izq"]
        elif self.movimiento:
            if self.direccion == "der":
                self.animacion_der.actualizar()
                self.image = self.animacion_der.get_frame()
            else:
                self.animacion_izq.actualizar()
                self.image = self.animacion_izq.get_frame()
        else:
            # Imagen estatica segun la dirección del personaje:
            if self.direccion == "der":
                self.image = self.sprites[vb]["derecha"]
            else:
                self.image = self.sprites[vb]["izquierda"]

        self.rect.bottomleft = (self.dx, self.dy)
        
    def actualizar_imgs(self, accion):
        key = f"{accion}"
        if key in self.sprites[vb]:
            self.image = self.sprites[vb][key]