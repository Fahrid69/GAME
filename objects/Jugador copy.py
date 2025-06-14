import pygame

from constants import *
from abc import ABC, abstractmethod


class Personaje(ABC, pygame.sprite.Sprite):
    def __init__(self, nombre, dx, dy):
        super().__init__()
        self.nombre = nombre
        self.dx = dx
        self.dy = dy


class Jugador(Personaje):
    def __init__(self, nombre, dx, dy):
        super().__init__(nombre, dx, dy)
    
        self.vidas = 3
        self.salto = 0
        self.puntos = 0
        self.gravedad = 1
        self.velocidad = 5
        
        self.estado = "normal"
        self.direccion = "der"
        self.poder_activo = "normal"
        self.versiones = "mm1"

        self.poder = False
        self.is_moving = False

        self.sprites = self.cargar_sprites()
        self.run_frames = self.cargar_frames_run(4, 20, 28)

        self.version = self.versiones
        self.tstatus = 0
        self.image = self.sprites["normal"]["iddle"]
        self.rect = self.image.get_rect(topleft=(dx, dy))




    def update(self):
        self._manejar_controles()
        self._aplicar_gravedad()
        self._actualizar_animacion()
        self._manejar_estados_especiales()
        self._verificar_cambio_version()
        self._actualizar_rect()

    def _manejar_controles(self):
        keys = pygame.key.get_pressed()
        self.is_moving = False

        # Movimiento vertical (+)
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.is_moving:
            self._realizar_salto()

        # Movimiento horizontal (+)
        if keys[pygame.K_d] and not keys[pygame.K_a]:
            self._mover_derecha()
        
        # Movimiento Horizontal (-)
        elif keys[pygame.K_a] and not keys[pygame.K_d]:
            self._mover_izquierda()

    def _realizar_salto(self):
        self.salto = -20
        self.is_moving = False
        SOUNDEFFECTS["salto"].play()

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
        if not self.is_moving:
            self.salto += self.gravedad
            self.dy += self.salto

        if self.dy >= Y:
            self.dy = Y
            self.salto = 0
            self.is_moving = True

    def _actualizar_animacion(self):
        if not self.is_moving:
            self._animar_salto()
        elif self.movimiento:
            self._animar_correr()
        else:
            self._animar_quieto()

    def _animar_salto(self):
        self.image = SPRITES_JUGADOR[self.poder_activo]["jump1"] 
        if self.direccion == "izq":
            self.image = pygame.transform.flip(self.image, True, False)

    def _animar_correr(self):
        self.animacion.actualizar()
        frame = self.animacion.get_frame()
        if self.direccion == "izq":
            frame = pygame.transform.flip(frame, True, False)
        self.image = frame

    def _animar_quieto(self):
        if self.direccion == "der":
            self.image = self.sprites[self.poder_activo]["iddle"]
        elif self.direccion == "izq":
            self.image = pygame.transform.flip(SPRITES_JUGADOR[self.poder_activo]["iddle"], True, False)

    def _manejar_estados_especiales(self):
        if self.estado == "muerto":
            self._procesar_muerte()
        elif self.estado == "inmunidad":
            self._procesar_inmunidad()

    def _procesar_muerte(self):
        if pygame.time.get_ticks() - self.tcooldown > 2000:
            self.vidas -= 1
            print(f"vidas: {self.vidas}")
            self.estado = "normal"
            if self.vidas <= 0:
                self.vidas = 0
                print("GAMEOVER")
                SOUNDEFFECTS["GAMEOVER"].play()

    def _procesar_inmunidad(self):
        if pygame.time.get_ticks() - self.tstatus > 10000:
            self.velocidad = 5
            self.estado = "normal"
            print("termino la inmunidad")

    def _verificar_cambio_version(self):
        if self.versiones != self.version:
            self.animacion = Animacion([self.sprites[self.versiones]["run1"],
                                        self.sprites[self.versiones]["run2"],
                                        self.sprites[self.versiones]["run3"],
                                        self.sprites[self.versiones]["run4"]], 7.5)
            self.version = self.versiones

    def _actualizar_rect(self):
        self.rect = self.image.get_rect(bottomleft=(self.dx, self.dy))

    # Las siguientes funciones se mantienen exactamente igual que en el original
    def crecer(self):
        self.estado = "gigante"
        self.versiones = "mm2" # cambiar de personaje

        if self.direccion == "der":
            self.image = self.sprites[self.versiones]["iddle"] 
        else:
            self.image = pygame.transform.flip(self.sprites[self.versiones]["iddle"], True, False)

        bottomleft = self.rect.bottomleft
        self.rect = self.image.get_rect(bottomleft = bottomleft)

        self.animacion = Animacion([self.sprites[self.versiones]["run1"], 
                                    self.sprites[self.versiones]["run2"], 
                                    self.sprites[self.versiones]["run3"], 
                                    self.sprites[self.versiones]["run4"],], 7.5)

    def inmunidad(self):
        self.estado = "inmunidad"
        self.tstatus = pygame.time.get_ticks()
    
    def death(self):
        self.estado = "muerto"
        self.tcooldown = pygame.time.get_ticks()

        if self.vidas < 0:
            self.image = SPRITES_JUGADOR["gameover"]
            self.rect = self.image.get_rect(bottom=Y)
  
    def actualizar_imgs(self, accion):
        key = f"{accion}"
        if key in self.sprites[self.versiones]:
            self.image = self.sprites[self.versiones][key]

    def cargar_frames_run(self, num_frames, frame_width, frame_height):
        sheet = self.sprites["normal"]["run"]
        frames = []
        for i in range(num_frames):
            frame = sheet.subsurface(pygame.Rect(i * frame_width, 0, frame_width, frame_height))
            frames.append(frame)
        return frames

    def _animar_correr(self):
        now = pygame.time.get_ticks()
        if now - self.run_frame_timer > self.run_frame_speed:
            self.run_frame_index = (self.run_frame_index + 1) % len(self.run_frames)
            self.run_frame_timer = now
        frame = self.run_frames[self.run_frame_index]
        if self.direccion == "izq":
            frame = pygame.transform.flip(frame, True, False)
        self.image = frame

    def cargar_sprites(self):
        return {
            "normal": {
                "idle": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm1/idle/10_idle_mm1.png"), (50,50)),
                "run": pygame.image.load("assets/sprites/player/Jugador/mm1/run/run.png"),
                "jump": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm1/jump/10_jump_mm1.png"), (50,50))
            },
            "gigante": {
                "idle": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm2/idle/20_idle_mm2.png"), (50,80)),
                "run": pygame.image.load("assets/sprites/player/Jugador/mm2/run/run.png"),
                "jump": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm2/jump/20_jump_mm2.png"), (50,80)),
                "crouch": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm2/crouch/20_crouch_mm2.png"), (50,80))
            },
            "muerto": {
                "dead": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/death/dead.png"), (50,50))
            }
        }
