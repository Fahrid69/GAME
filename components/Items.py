import pygame

from constants import * 
from abc import ABC, abstractmethod


class Items(ABC, pygame.sprite.Sprite):
    def __init__(self, nombre, dx, dy):
        super().__init__()
        self.nombre = nombre
        self.dx = dx
        self.dy = dy

    @abstractmethod
    def update(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")

    @abstractmethod
    def cargar_sprites_sheet(self):
        raise NotImplementedError("Este método debe ser implementado por las subclases")


class Moneda(Items):
    def __init__(self, dx, dy, jugador):
        super().__init__("Moneda", dx, dy)

        """ATRIBUTOS DE LA MONEDA"""
        # Atributos generales
        self.jugador = jugador

        # Atributos de sprites
        self.dimension = (50, 50)
        self.sprites = self.cargar_sprites_sheet()
        self.image = self.sprites["coin"].subsurface((0, 0, 16, 16))
        self.rect = self.image.get_rect(bottomleft=(dx, dy))

        # Atributos de animación
        self.run_frame_index = 0
        self.run_frame_timer = 0
        self.run_frame_speed = 100


    def update(self):
        self._animar_movimiento()
        self._actualizar_rect()

    def _animar_movimiento(self):
        now = pygame.time.get_ticks()
        if now - self.run_frame_timer > self.run_frame_speed:
            self.run_frame_index = (self.run_frame_index + 1) % 4
            self.run_frame_timer = now


        ancho, alto = (16, 16)
            
        sheet = self.sprites["coin"]
        frame_rect = pygame.Rect(self.run_frame_index * ancho, 0, ancho, alto)
        
        frame = sheet.subsurface(frame_rect)
        frame = pygame.transform.scale(frame, self.dimension)
        
        self.image = frame


    def _actualizar_rect(self):
        self.rect = self.image.get_rect(bottomleft=(self.dx, self.dy))

    def cargar_sprites_sheet(self):
        return {
            "coin": pygame.image.load("assets/sprites/items/Moneda/coin/coin.png"),
            "bigcoin": pygame.image.load("assets/sprites/items/Moneda/bigcoin/bigcoin.png")
        }