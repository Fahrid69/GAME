from Molde import Personaje
from constants import *
from animation import Animacion

import pygame
import random

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, nombre, dx, dy):
        super().__init__()
        self.nombre = nombre
        self.dx = dx
        self.dy = dy
        self.velocidad = -2

class Goomba(Enemigo):
    def __init__(self, nombre, dx, dy):
        super().__init__(nombre, dx, dy)
        self.variante = random.choice(("black", "brown"))
        self.sprites = SPRITES_GOOMBA[self.variante]

        frames =[self.sprites["caminar1"], self.sprites["caminar2"]] #  Cargar las imagenes para la animacion
        self.animacion = Animacion(frames, 10) # Se le pasan valores paraa animarla

        self.image = self.animacion.get_frame()
        self.rect = self.image.get_rect(bottom=Y)

        self.direccion = -1.5

    def update(self):
        self.dx += self.direccion *2
        self.animacion.actualizar()
        self.image = self.animacion.get_frame()

        if self.dx <= 0 or self.dx >= ANCHO_VENTANA - self.rect.width:
            self.direccion *= -1
        self.rect.bottomleft = (self.dx, self.dy)

class Turtle(Enemigo):
    def __init__(self, nombre, dx, dy):
        super().__init__(nombre, dx, dy)
        self.sprites = SPRITES_TURTLE["turtle"]

#           CARGAAMOS LAS IMAGENES PARA LUEGO ANIMARLAS CON ANIMATION.PY
        frames = [self.sprites["01t"], self.sprites["02t"], self.sprites["03t"], self.sprites["04t"]]
        self.animacion = Animacion(frames, 10)

#           Conseguimos la animación y la otorgamos como imagen
        self.image = self.animacion.get_frame()
        self.rect = self.image.get_rect(bottom=Y)

        self.direccion = -1

    def update(self):
        self.dx += self.direccion *2
        self.animacion.actualizar()
        self.image = self.animacion.get_frame()

        self.rect.x = self.dx

#           CHOCA CON LOS LIMITES DE LA VENTANAS
#           Y SE DEVUELVE        
        if self.dx <= 0 or self.dx >= ANCHO_VENTANA - self.rect.width:
            self.direccion *= -1
        self.rect.bottomleft = (self.dx, self.dy)

#           SE DA LA VUELTA
        if self.direccion > 0 :
            self.image = pygame.transform.flip(self.animacion.get_frame(), True, False)

#
