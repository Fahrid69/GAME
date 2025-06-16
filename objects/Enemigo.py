import pygame

from constants import *
from objects.Jugador import Jugador
from soundeffects import Sonidos
from abc import ABC, abstractmethod


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
    def _moverse(self):
        pass

    @abstractmethod
    def _animar(self):
        pass
    """
    @abstractmethod
    def _procesar_muerte_aplastamiento(self):
        pass

class Goomba(Enemigo):
    def __init__(self, nombre, dx, dy):
        super().__init__(nombre, dx, dy)

        """ATRIBUTOS GENERALES DEL ENEMIGO"""

        # Atributos del enemigo
        self.vidas = 1
        self.estado = "vivo"
        self.direccion = "izq"
        self.velocidad = 3
        self.direccion_movimiento = 1

        # Atributos de movimiento
        self.dimension = (50,50)
        self.sprites = self.cargar_sprites()
        self.image = self.sprites["brown"]["run"].subsurface((0, 0, 16, 16))
        self.image = pygame.transform.scale(self.image, self.dimension)
        self.rect = self.image.get_rect(topleft=(dx, dy))

        # Atributos de animación
        self.run_frame_timer = 0
        self.run_frame_index = 0        
        self.run_frame_speed = 200
        self.run_total_frames = self.sprites["brown"]["run"].get_width() // 16

        # Definir la variable para los sonidos del enemigo
        self.sonidos = Sonidos()

        # Temporizadores
        self.tiempo_desaparicion = 0

    def update(self):
        if self.estado == "vivo":
            self._moverse()
            self._animar()
            self._actualizar_posicion()
        elif self.estado == "muerto":
            self._correr_tiempo_muerte()

    
    def _moverse(self):
        # Verifica la dirección de movimiento del enemigo (goomba).
        if self.direccion == "izq":
            self.direccion_movimiento = -1
        elif self.direccion == "der":
            self.direccion_movimiento = 1

        self.dx += self.direccion_movimiento * self.velocidad

        # Cambiar la dirección si toca alguno de los bordes
        if self.dx < 0 or  self.dx >= ANCHO_VENTANA  - self.rect.width:
            self.direccion_movimiento *= -1
            self.direccion = "izq" if self.direccion_movimiento < 0 else "der"


    def _actualizar_posicion(self):
        # Actualiza la posición del sprite del goomba.
        self.rect.bottomleft = (self.dx, self.dy)

    def _animar(self):
        # Animar el sprite del goomba en movimiento.
        now = pygame.time.get_ticks()
        if now - self.run_frame_timer > self.run_frame_speed:
            self.run_frame_index = (self.run_frame_index + 1) % self.run_total_frames
            self.run_frame_timer = now

        sheet = self.sprites["brown"]["run"]
        frame_rect = pygame.Rect(self.run_frame_index * 16, 0, 16, 16)
        frame = sheet.subsurface(frame_rect)
        frame = pygame.transform.scale(frame, self.dimension)

        if self.direccion == "izq":
            frame = pygame.transform.flip(frame, True, False)
        self.image = frame

    def _procesar_muerte_aplastamiento(self):
        self.estado = "muerto"
        self.sonidos._reproducir_sonido_goomba()
        self.image = self.sprites["brown"]["crushed"]
        self.tiempo_desaparicion = pygame.time.get_ticks()

    def _correr_tiempo_muerte(self):
        tiempo = pygame.time.get_ticks() - self.tiempo_desaparicion
        if tiempo > 1000:
            self.jugador.puntos += 100
            self.kill()


    def cargar_sprites(self):
        return {
            "brown": {
                "run": pygame.image.load("assets/sprites/enemies/Goomba/g1/run.png"),
                "crushed": pygame.transform.scale(pygame.image.load("assets/sprites/enemies/Goomba/g1/dead.png"),self.dimension),
            }
        }


class Turtle(Enemigo):
    def __init__(self, nombre, dx, dy):
        pass

    def update(self):
        self.mover() 

    def _procesar_muerte_aplastamiento(self):
        return super()._morir()