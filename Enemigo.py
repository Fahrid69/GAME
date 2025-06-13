from constants import *
from abc import ABC, abstractmethod
from soundeffects import Animacion

import pygame, random

class Enemigo(ABC, pygame.sprite.Sprite):
    def __init__(self, nombre, dx, dy):
        super().__init__()
        self.nombre = nombre
        self.dx = dx
        self.dy = dy
    """    
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def cargar_sprites(self):
        pass

    @abstractmethod
    def mover(self):
        pass

    @abstractmethod
    def animar(self):
        pass

    @abstractmethod
    def morir(self):
        pass"""

class Goomba(Enemigo):
    def __init__(self, nombre, dx, dy):
        super().__init__(nombre, dx, dy)

        """ ATRIBUTOS """
        self.estado = "vivo"
        self.direccion = "izq"
        self.velocidad = 4

        self.image = SPRITES_GOOMBA["brown"]["caminar1"]
        self.rect = self.image.get_rect(topleft=(dx, dy))

    def cargar_sprites(numero, dimension, personaje, path):
        sprites = {}
        for i in range(numero):
            dir = f"{path}1{i}_{personaje}.png"

            try:
                # Cargar las imagenes.
                sprite = pygame.transform.scale(pygame.image.load(dir), dimension).convert_alpha()
                sprites.append(sprite)
            except Exception as e:
                print(f"no se pudo cargar {dir}: {e}")
        return sprites
    
    def mover(self):
        if self.estado == "vivo":
            # Define la dirección del objeto.
            if self.direccion == "izq":
                self.movimiento = -1
            elif self.direccion == "der":
                self.movimiento = 1

            self.dx += self.movimiento * self.velocidad

            # Invertir la imagen del objeto.
            if self.movimiento > 0:
                self.image = pygame.transform.flip(self.image, True, False)

            self.rect.x = self.dx

            # Cambiar la dirección si toca alguno de los bordes
            if self.dx < 0 or  self.dx >= ANCHO_VENTANA  - self.rect.width:
                self.movimiento *= -1
                self.direccion = "izq" if self.movimiento < 0 else "der"

            # Actualiza lla posición
            self.rect.bottomleft = (self.dx, self.dy)

    def animar(self):
        pass
    def morir(self):
        if self.estado == "muerto":
            self.kill()
            
    def update(self):
        if self.estado == "vivo":
            self.mover()
            self.animar()
        elif self.estado == "muerto":
            self.morir()


class Turtle(Enemigo):
    def __init__(self, nombre, dx, dy):
        pass

    def update(self):
        self.mover() 
