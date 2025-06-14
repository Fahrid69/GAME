import pygame

from constants import * 
from abc import ABC, abstractmethod


class Items(ABC, pygame.sprite.Sprite):
    def __init__(self, nombre, image, dx, dy):
        super().__init__()
        self.nombre = nombre
        self.image = image
        self.rect = self.image.get_rect(topleft=(dx, dy))
        self.dx = dx
        self.dy = dy

    @abstractmethod
    def update(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    @abstractmethod
    def cargar_sprites_sheet(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")


class Moneda(Items):
    def __init__(self, dx, dy):
        super().__init__("Moneda", dx, dy)

        """ATRIBUTOS DE LA MONEDA"""

        # Atributos de sprites
        self.dimension = (32, 32)
        self.sprites = self.cargar_sprites_sheet()
        self.image = self.sprites["coin"]
        self.rect = self.image.get_rect(topleft=(dx, dy))

        # Atributos de animación
        self.run_frame_index = 0
        self.run_frame_timer = 0
        self.run_frame_speed = 100
        self.run_total_frames = self.sprites["coin"].get_width() // 16  

    def update(self):
        self._animar_movimiento()

    def _animar_movimiento(self):
        pass

    def cargar_sprites_sheet(self):
        return {
            "coin": pygame.image.load("assets/sprites/powers/Moneda/coin.png"),
            "bigcoin": pygame.image.load("assets/sprites/powers/Moneda/bigcoin.png")
        }