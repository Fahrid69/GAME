import pygame

from constants import *
from soundeffects import Sonidos
from abc import ABC, abstractmethod


class Poder(ABC, pygame.sprite.Sprite):
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
        

class Hongo_Rojo(Poder):
    def __init__(self, dx, dy):
        super().__init__("Gigante", dx, dy)

        """ATRIBUTOS DEL HONGO ROJO"""
        # Atributos generales
        self.velocidad = 2
        self.direccion = -1

        # Atributos de sprites
        self.dimension = (45, 45)
        self.sprites = self.cargar_sprites_sheet()
        self.image = self.sprites["mushroom"].subsurface((0, 0, 18, 18))
        self.image = pygame.transform.scale(self.image, self.dimension)
        self.rect = self.image.get_rect(bottomleft=(dx, dy))
        
        # Atributos de animación
        self.run_frame_index = 0
        self.run_frame_timer = 0
        self.run_frame_speed = 125
        self.run_total_frames = self.sprites["mushroom"].get_width() // 18

    def update(self):
        self._moverse()
        self._actualizar_rect()
        self._animar_movimiento()


    def _moverse(self):
        self.dx += self.direccion * self.velocidad

        # Chocarse con los limites visibles
        if self.dx < 0 or self.dx >= ANCHO_VENTANA - self.rect.width:
            self.direccion *= -1

    def _animar_movimiento(self):
        now = pygame.time.get_ticks()
        if now - self.run_frame_timer > self.run_frame_speed:
            self.run_frame_index = (self.run_frame_index + 1) % self.run_total_frames
            self.run_frame_timer = now

        sheet = self.sprites["mushroom"]
        frame_rect = pygame.Rect(self.run_frame_index * 18, 0, 18, 18)
        frame = sheet.subsurface(frame_rect)
        frame = pygame.transform.scale(frame, self.dimension)
        self.image = frame


    def _actualizar_rect(self):
        self.rect.bottomleft = (self.dx, self.dy)


    def cargar_sprites_sheet(self):
        return {
            "mushroom": pygame.image.load("assets/sprites/powers/Hongos/hr/mushroom.png")
        }


class Hongo_Verde(Poder):
    def __init__(self, dx, dy):
        super().__init__("+1HP", dx, dy)

        """ATRIBUTOS DEL HONGO VERDE"""
        # Atributos generales
        self.velocidad = 3
        self.direccion = 1

        # Atributos de sprites
        self.dimension = (45, 45)
        self.sprites = self.cargar_sprites_sheet()  
        self.image = self.sprites["mushroom"].subsurface((0, 0, 18, 18))
        self.image = pygame.transform.scale(self.image, self.dimension)
        self.rect = self.image.get_rect(bottomleft=(dx, dy))

        # Atributos de animación
        self.run_frame_index = 0
        self.run_frame_timer = 0
        self.run_frame_speed = 100
        self.run_total_frames = self.sprites["mushroom"].get_width() // 18

    def update(self):
        self._moverse()
        self._actualizar_rect()
        self._animar_movimiento()


    def _moverse(self):
        self.dx += self.direccion * self.velocidad

        # Chocarse con los limites:
        if self.dx < 0 or self.dx >= ANCHO_VENTANA - self.rect.width:
            self.direccion *= -1

    def _animar_movimiento(self):
        now = pygame.time.get_ticks()
        if now - self.run_frame_timer > self.run_frame_speed:
            self.run_frame_index = (self.run_frame_index + 1) % self.run_total_frames
            self.run_frame_timer = now

        sheet = self.sprites["mushroom"]
        frame_rect = pygame.Rect(self.run_frame_index * 18, 0, 18, 18)
        frame = sheet.subsurface(frame_rect)
        frame = pygame.transform.scale(frame, self.dimension)
        self.image = frame


    def _actualizar_rect(self):
        self.rect.bottomleft = (self.dx, self.dy)

    def cargar_sprites_sheet(self):
        return {
            "mushroom": pygame.image.load("assets/sprites/powers/Hongos/hv/mushroom.png")
        }
    

class Estrella(Poder):
    def __init__(self, dx, dy):
        super().__init__("Inmunidad", dx, dy)
        self.velocidad = 4
        self.salto = 5
        self.gravedad = 0.625
        self.direccion = -1
        self.suelo = Y

        # Atributos de sprites
        self.dimension = (50, 50)
        self.sprites = self.cargar_sprites_sheet()
        self.image = self.sprites["estrella"].subsurface((0, 0, 16, 16))
        self.image = pygame.transform.scale(self.image, self.dimension)
        self.rect = self.image.get_rect(bottomleft=(dx, dy))

        # Atributos de animación
        self.run_frame_index = 0
        self.run_frame_timer = 0
        self.run_frame_speed = 150
        self.run_total_frames = self.sprites["estrella"].get_width() // 16

    def update(self):
        self._moverse()
        self._animar_movimiento()


    def _moverse(self):
        if self.rect.left <= 0 or self.rect.right >= ANCHO_VENTANA:
            self.direccion *=-1

        self.rect.x += self.velocidad * self.direccion


        self.salto += self.gravedad
        self.rect.y += self.salto

        if self.rect.bottom >= self.suelo:
            self.rect.bottom = self.suelo
            self.salto =-10
    
    def _animar_movimiento(self):
        now = pygame.time.get_ticks()
        if now - self.run_frame_timer > self.run_frame_speed:
            self.run_frame_index = (self.run_frame_index + 1) % self.run_total_frames
            self.run_frame_timer = now

        sheet = self.sprites["estrella"]
        frame_rect = pygame.Rect(self.run_frame_index * 16, 0, 16, 16)
        frame = sheet.subsurface(frame_rect)
        frame = pygame.transform.scale(frame, self.dimension)
        self.image = frame

    def cargar_sprites_sheet(self):
        return {
            "estrella": pygame.image.load("assets/sprites/powers/Estrella/starman.png")
        }

