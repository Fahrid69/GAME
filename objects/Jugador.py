import pygame

from constants import *
from soundeffects import Sonidos
from abc import ABC, abstractmethod


class Personaje(ABC, pygame.sprite.Sprite):
    def __init__(self, nombre, dx, dy):
        super().__init__()
        self.nombre = nombre
        self.dx = dx
        self.dy = dy
        
    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def cargar_sprites(self):
        pass

    @abstractmethod
    def _manejar_controles(self):
        pass


class Jugador(Personaje):
    def __init__(self, nombre, dx, dy):
        super().__init__(nombre, dx, dy)
    
        self.vidas = 3
        self.puntos = 0
        self.gravedad = 1
        self.velocidad = 5
        self.impulso_salto = 0
        
        self.estado = "normal"
        self.direccion = "der"
        self.poder_activo = "normal"
        self.versiones = "mm1"

        self.is_powered_up = False
        self.is_dead = False
        self.is_jumping = False
        self.is_grounded = True
        self.is_moving = False

        self.sprites_size = (64, 64)  # Tamaño de los sprites del jugador
        self.sprites = self.cargar_sprites()
        self.image = self.sprites["normal"]["idle"]
        self.rect = self.image.get_rect(topleft=(dx, dy))

        self.run_frame_index = 0
        self.run_frame_timer = 0
        self.run_frame_speed = 100
        self.run_total_frames = self.sprites["normal"]["run"].get_width() // 18 

        # Definir la varriable para los sonidos del juego
        self.sonidos = Sonidos()


        # Temporizadores para estados especiales
        self.tiempo_moribundo = 0
        self.tiempo_inmunidad = 0


    def update(self):
        self._manejar_controles()
        self._aplicar_gravedad()
        self._actualizar_animacion()
        #self._manejar_estados_especiales()
        #self._verificar_cambio_version()
        self._actualizar_rect()

    def _manejar_controles(self):
        keys = pygame.key.get_pressed()

        # Reseteo de movimiento, y salto.
        self.is_moving = False
        self.is_jumping = False

        # Movimiento vertical (+)
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]):
            self._realizar_salto()

        # Movimiento horizontal (+)
        if keys[pygame.K_d] and not keys[pygame.K_a]:
            self._mover_derecha()
        
        # Movimiento Horizontal (-)
        elif keys[pygame.K_a] and not keys[pygame.K_d]:
            self._mover_izquierda()

    def _realizar_salto(self):
        if self.is_grounded and not self.is_jumping:
            self.impulso_salto = -20
            self.is_grounded = False
            self.is_jumping = True
            self.sonidos._reproducir_sonido_salto() 

    def _mover_derecha(self):
        self.dx += self.velocidad
        self.direccion = "der"
        self.is_moving = True
        if self.dx > ANCHO_VENTANA - self.rect.width:
            self.dx = ANCHO_VENTANA - self.rect.width

    def _mover_izquierda(self):
        self.dx -= self.velocidad
        self.direccion = "izq"
        self.is_moving = True
        if self.dx < 0:
            self.dx = 0

    def _aplicar_gravedad(self):
        if not self.is_grounded:
            self.impulso_salto += self.gravedad
            self.dy += self.impulso_salto

        if self.dy >= Y:
            self.dy = Y
            self.impulso_salto = 0
            self.is_jumping = False
            self.is_grounded = True

    def _actualizar_animacion(self):
        if not self.is_grounded:
            self._animar_salto()
        elif self.is_moving:
            self._animar_correr()
        else:
            self._animar_inactivo()

    def _animar_salto(self):
        self.image = self.sprites["normal"]["jump"] 
        if self.direccion == "izq":
            self.image = pygame.transform.flip(self.image, True, False)

    def _animar_correr(self):
        now = pygame.time.get_ticks()
        if now - self.run_frame_timer > self.run_frame_speed:
            self.run_frame_index = (self.run_frame_index + 1) % self.run_total_frames
            self.run_frame_timer = now

        sheet = self.sprites["normal"]["run"]
        frame_rect = pygame.Rect(self.run_frame_index * 18, 0, 18, 18)
        frame = sheet.subsurface(frame_rect)
        frame = pygame.transform.scale(frame, self.sprites_size)

        if self.direccion == "izq":
            frame = pygame.transform.flip(frame, True, False)
        self.image = frame

    def _animar_inactivo(self):
        self.image = self.sprites["normal"]["idle"]
        if self.direccion == "izq":
            self.image = pygame.transform.flip(self.image, True, False)


    def _procesar_muerte(self):
        self.tiempo_moribundo = pygame.time.get_ticks()
        if pygame.time.get_ticks() - self.tiempo_moribundo > 2000:
            self.vidas -= 1
            print(f"vidas: {self.vidas}")
            self.estado = "normal"
            if self.vidas <= 0:
                self.vidas = 0
                self.is_dead = True
                self.image = self.sprites["muerto"]["dead"]
                self.rect = self.image.get_rect(topleft=(self.dx, self.dy))
                print("GAMEOVER")
                #["GAMEOVER"].play()

    def _actualizar_rect(self):
        self.rect = self.image.get_rect(bottomleft=(self.dx, self.dy))

    def cargar_sprites(self, ):
        return {
            "normal": {
                "idle": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm1/idle/idle.png"), (self.sprites_size)),
                "run": pygame.image.load("assets/sprites/player/Jugador/mm1/run/run.png"),
                "jump": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm1/jump/jump.png"), (self.sprites_size))
            },
            "gigante": {
                "idle": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm2/idle/idle.png"), (self.sprites_size)),
                "run": pygame.image.load("assets/sprites/player/Jugador/mm2/run/run.png"),
                "jump": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm2/jump/jump.png"), (self.sprites_size)),
                "crouch": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm2/crouch/crouch.png"), (self.sprites_size))
            },
            "muerto": {
                "dead": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/death/dead.png"), (self.sprites_size))
            }
        }
