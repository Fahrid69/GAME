from Molde import Personaje
from constants import *

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
        self.animacion = Animacion(frames, velocidad=10) # Se le pasan valores paraa animarla

        self.image = self.animacion.get_frame()
        self.rect = self.image.get_rect(bottom=500)

        self.direccion = -1

    def update(self):
        self.dx += self.direccion *2
        self.animacion.actualizar()
        self.image = self.animacion.get_frame()

        if self.dx <= 0 or self.dx >= ANCHO_VENTANA - self.rect.width:
            self.direccion *= -1
        self.rect.bottomleft = (self.dx, self.dy)

class Koopa_Troopa(Enemigo):
    def __init__(self, nombre, dx, dy):
        super().__init__(nombre, dx, dy)

class Animacion:
    def __init__(self, frames, velocidad):
        self.frames = frames
        self.velocidad = velocidad
        self.index =0
        self.contador =0
    
    def actualizar(self):
        self.contador +=1
        if self.contador >= self.velocidad:
            self.contador =0
            self.index = (self.index + 1) % len(self.frames)
    
    def get_frame(self):
        return self.frames[self.index]