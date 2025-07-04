import pygame, random

from constants import *
from components.player import Jugador
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
    def __init__(self, nombre, dx, dy, jugador):
        super().__init__(nombre, dx, dy)

        """ATRIBUTOS GENERALES DE <<GOOMBA>>"""

        # Atributos del enemigo
        self.vidas = 1
        self.current_status = "vivo"
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

        # Definir la variable para los sonidos del enemigo
        self.sonidos = Sonidos()

        # Temporizadores
        self.tiempo_desaparicion = 0

        self.jugador = jugador


    def update(self):
        if self.current_status == "vivo":
            self._moverse()
            self._animar()
            self._actualizar_rect()
        elif self.current_status == "muerto":
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

    def _animar(self):
        # Animar el sprite del goomba en movimiento.
        now = pygame.time.get_ticks()
        if now - self.run_frame_timer > self.run_frame_speed:
            self.run_frame_index = (self.run_frame_index + 1) % 2
            self.run_frame_timer = now

        sheet = self.sprites["brown"]["run"]
        frame_rect = pygame.Rect(self.run_frame_index * 16, 0, 16, 16)
        frame = sheet.subsurface(frame_rect)
        frame = pygame.transform.scale(frame, self.dimension)

        if self.direccion == "der":
            frame = pygame.transform.flip(frame, True, False)
        self.image = frame


    def _procesar_muerte_aplastamiento(self):
        self.vidas -= 1
        if self.vidas >= 0:
            self.current_status = "muerto"
            self.tiempo_desaparicion = pygame.time.get_ticks()

        self.sonidos._reproducir_sonido_goomba()
        self.image = self.sprites["brown"]["crushed"]

    def _correr_tiempo_muerte(self):
        tiempo = pygame.time.get_ticks() - self.tiempo_desaparicion
        if tiempo > 1000:
            if self.vidas == 0:
                self.jugador._incrementar_puntos()
                self.kill()


    def _actualizar_rect(self):
        # Actualiza la posición del sprite del goomba.
        self.rect.bottomleft = (self.dx, self.dy)

    def cargar_sprites(self):
        return {
            "brown": {
                "run": pygame.image.load("assets/sprites/enemies/Goomba/slow goomba/run/run.png"),
                "crushed": pygame.transform.scale(pygame.image.load("assets/sprites/enemies/Goomba/slow goomba/death/dead.png"),self.dimension),
            },
            "black": {
                "run": pygame.image.load("assets/sprites/enemies/Goomba/fast goomba/run/run.png"),
                "crushed": pygame.transform.scale(pygame.image.load("assets/sprites/enemies/Goomba/fast goomba/death/dead.png"), self.dimension)
            }
        }


class Turtle(Enemigo):
    def __init__(self, nombre, dx, dy, jugador):
        super().__init__(nombre, dx, dy)
        
        """ATRIBUTOS GENERALES DE LA <<TORTUGA>>"""

        # Atributos del enemigo
        self.vidas = 2
        self.current_status = "vivo"
        self.direccion = random.choice(["izq", "der"])
        self.velocidad = 2.9
        self.movimiento = 1

        self.descenso = True

        self.jugador = jugador


        # Atributos de movimiento
        self.dimension = (50,50)
        self.sprites = self.cargar_sprites()
        self.image = self.sprites["best turtle"]["run"].subsurface((0, 0, 16, 16))
        self.image = pygame.transform.scale(self.image, self.dimension)
        self.rect = self.image.get_rect(bottomleft=(dx,dy))

        # Atributos de animación
        self.run_frame_timer = 0
        self.run_frame_index = 0        
        self.run_frame_speed = 75

        # Definir la variable para los sonidos del enemigo
        self.sonidos = Sonidos()

        # Temporizadores
        self.tiempo_desaparicion = 0
        self.tiempo_revivir = 0


    def update(self):
        self._actualizar_rect()
        self._controlar_aparicion()


    def _controlar_aparicion(self):
        if self.descenso == True:
            self._animar_aparicion()
        else:
            self._controlar_estados()

    def _controlar_estados(self):
        if self.current_status == "vivo":
            self._moverse()
            self._animar()
        elif self.current_status == "derribado":
            self._revivir()
        else:
            self._correr_tiempo_muerte()

    
    def _moverse(self):
        # Verifica la dirección de movimiento del enemigo <<Goomba>>
        if self.direccion == "izq":
            self.movimiento = -1
        elif self.direccion == "der":
            self.movimiento = 1

        self.dx += self.movimiento * self.velocidad

        # Cambiar la dirección si toca alguno de los limites visibles
        if self.dx < 0:
            self.movimiento *= -1
            self._tratar_limites()
            self.direccion = "der"
        elif self.dx >= ANCHO_VENTANA  - self.rect.width:
            self.movimiento *= -1
            self._tratar_limites()
            self.direccion = "izq"

    def _animar_aparicion(self):
        if self.descenso == True:
            self.dy += 10
            self.image = self.sprites["best turtle"]["shell"]
            self._tratar_limites()
            # PIENSO AGREGAR SONIDO LUEGO AQUÍ
            if self.dy >= Y:
                self.dy = Y
                self.descenso = False
            return True
        return False
        
    def _tratar_limites(self):
        if self.dx < 0:
            self.dx = 0
        elif self.dx > ANCHO_VENTANA - self.rect.width:
            self.dx = ANCHO_VENTANA - self.rect.width

    def _animar(self):
        # Animar el sprite en movimiento.
        now = pygame.time.get_ticks()
        if now - self.run_frame_timer > self.run_frame_speed:
            self.run_frame_index = (self.run_frame_index + 1) % 4
            self.run_frame_timer = now

        sheet = self.sprites["best turtle"]["run"]
        frame_rect = pygame.Rect(self.run_frame_index * 16, 0, 16, 16)
        frame = sheet.subsurface(frame_rect)
        frame = pygame.transform.scale(frame, self.dimension)

        if self.direccion == "der":
            frame = pygame.transform.flip(frame, True, False)
        self.image = frame


    def _procesar_muerte_aplastamiento(self):
        self.vidas -= 1
        self.sonidos._reproducir_sonido_turtle()
        self.image = self.sprites["best turtle"]["dead"]
        if self.direccion == "der":
            self.image = pygame.transform.flip(self.image, True, False)
        self.current_status = "derribado"

        if self.vidas > 0:
            self.tiempo_revivir = pygame.time.get_ticks()

        # Empieza el proceso para eliminar al enemigo del campo
        if self.vidas <= 0:
            self.current_status = "muerto"
            self.image = self.sprites["best turtle"]["shell"]
            self.tiempo_desaparicion = pygame.time.get_ticks()

    def _revivir(self):
        tiempo = pygame.time.get_ticks() - self.tiempo_revivir
        if tiempo > random.randint(999, 9999):
            self.current_status = "vivo"
            # RECORDAR AGREGAR EL EFECTO DE SONIDO AQUÍ

    def _correr_tiempo_muerte(self):
        tiempo = pygame.time.get_ticks() - self.tiempo_desaparicion
        if tiempo > 1000 and self.current_status == "muerto":
            if self.vidas == 0:
                # Compensa al jugador con +100 puntos
                self.jugador._incrementar_puntos()
                self.kill()


    def _actualizar_rect(self):
        # Actualiza la posición del sprite de la tortuga
        self.rect.bottomleft = (self.dx, self.dy)

    def cargar_sprites(self):
        return {
            "best turtle": {
                "run": pygame.image.load("assets/sprites/enemies/Turtle/good turtle/run/run.png"),
                "shell": pygame.transform.scale(pygame.image.load("assets/sprites/enemies/Turtle/good turtle/shell/shell.png"), self.dimension),
                "dead": pygame.transform.scale(pygame.image.load("assets/sprites/enemies/Turtle/good turtle/death/dead.png"), self.dimension)
            }
        }