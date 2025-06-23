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
    
        # Lógica de atributos de numero:
        self.vidas = 3
        self.puntos = 0
        self.gravedad = 1
        self.velocidad = 5
        self.salto = 20
        self.impulso_salto = 0
        
        # Lógica de atributos en cadena:
        self.current_status_size = "normal" # Estados pósible de tamaño: "Normal", "Gigante"
        self.current_status_temporal = "ninguno" # Estados posible temporádicos: "Ninguno", "Inmunidad"
        self.current_status_life = "vivo" # Estados posibles de vida: "Vivo", "Moribundo", "muerto".
        self.current_side = "der"

        # Lógica de atributos en bool:
        self.is_dead = False
        self.is_jumping = False
        self.is_grounded = True
        self.is_moving = False

        # Atributos de sprites: cargue, tamaño, imágen
        self.dimension = (64, 64)  # Tamaño normal de los sprites del jugador
        self.sprites = self.cargar_sprites()
        self.image = self.sprites[self.current_status_size]["idle"]
        self.rect = self.image.get_rect(topleft=(dx, dy))
        # Atributos de sprites: animación 
        self.run_frame_index = 0
        self.run_frame_timer = 0
        self.run_frame_speed = 100


        # Definir la varriable para los sonidos del juego
        self.sonidos = Sonidos()


        # Temporizadores para estados especiales
        self.tiempo_moribundo = 0
        self.tiempo_inmunidad = 0


    def update(self):
        if self.current_status_life != "moribundo":
            self._manejar_controles()
            self._actualizar_animacion()
            self._manejar_estados_especiales()
        
        if self.current_status_life == "moribundo":
            self._correr_tiempo_moribundeo()
            self._moribundeo()
            
        self._aplicar_gravedad()
        self._actualizar_rect()


    def _manejar_controles(self):
        keys = pygame.key.get_pressed()

        # Reseteo de movimiento, y salto.
        self.is_moving = False

        # Movimiento vertical (+)
        if (keys[pygame.K_SPACE] or keys[pygame.K_w] or keys[pygame.K_UP]):
            self._realizar_salto()

        # Movimiento horizontal (+)
        if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and not (keys[pygame.K_a] or keys[pygame.K_LEFT]):
            self._mover_derecha()
        
        # Movimiento Horizontal (-)
        if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and not (keys[pygame.K_d] or keys[pygame.K_RIGHT]):
            self._mover_izquierda()

        # Movimiento exclusivo
        if self.current_status_size == "gigante":
            if (keys[pygame.K_s] or keys[pygame.K_DOWN]) and not (self.is_moving and self.is_grounded):
                self._animar_agacharse_grande()


    def _realizar_salto(self):
        if self.is_grounded and not self.is_jumping:
            self.impulso_salto = self.salto * -1
            self.is_grounded = False
            self.is_jumping = True
            self.sonidos._reproducir_sonido_salto() 

    def _mover_derecha(self):
        self.dx += self.velocidad
        self.current_side = "der"
        self.is_moving = True
        if self.dx > ANCHO_VENTANA - self.rect.width:
            self.dx = ANCHO_VENTANA - self.rect.width

    def _mover_izquierda(self):
        self.dx -= self.velocidad
        self.current_side = "izq"
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
            self.is_grounded = True
            self.is_jumping = False


    def _actualizar_animacion(self):
        if self.is_jumping:
            self._animar_salto()
        elif self.is_moving:
            self._animar_correr()
        else:
            self._animar_inactivo()

    def _animar_salto(self):
        self.image = self.sprites[self.current_status_size]["jump"] 
        if self.current_side == "izq":
            self.image = pygame.transform.flip(self.image, True, False)

    def _animar_correr(self):
        now = pygame.time.get_ticks()
        if now - self.run_frame_timer > self.run_frame_speed:
            self.run_frame_index = (self.run_frame_index + 1) % 4
            self.run_frame_timer = now


        ancho, alto = (18, 18) if self.current_status_size == "normal" else (20, 28)
            
        sheet = self.sprites[self.current_status_size]["run"]
        frame_rect = pygame.Rect(self.run_frame_index * ancho, 0, ancho, alto)
        frame = sheet.subsurface(frame_rect)
        frame = pygame.transform.scale(frame, self.dimension)

        if self.current_side == "izq":
            frame = pygame.transform.flip(frame, True, False)
        self.image = frame

    def _animar_inactivo(self):
        self.image = self.sprites[self.current_status_size]["idle"]
        if self.current_side == "izq":
            self.image = pygame.transform.flip(self.image, True, False)

    def _animar_agacharse_grande(self):
        self.image = self.sprites["gigante"]["crouch"]
        if self.current_side == "izq":
            self.image = pygame.transform.flip(self.image, True, False)

    
    def _manejar_estados_especiales(self):
        # Estados especiales como: "inmune".
        if self.current_status_temporal == "inmunidad":
            self._desactivar_inmunidad()

    def _incrementar_puntos(self, cantidad=100):
        self.sonidos._reproducir_sonido_moneda()
        self.puntos += cantidad

    def _incrementar_vida(self):
        self.vidas += 1
        self.sonidos._reproducir_sonido_hv()

    def _activar_gigante(self):
        self.dimension = (64, 80)
        self.current_status_size = "gigante"
        self.sprites = self.cargar_sprites()
        self.sonidos._reproducir_sonido_hr()

    def _desactivar_gigante(self):
        self.dimension = (64, 64)
        self.sprites = self.cargar_sprites()
        self.current_status_size = "normal"

    def _activar_inmunidad(self):
        self.current_status_temporal = "inmunidad"
        self.velocidad = 6
        self.tiempo_inmunidad = pygame.time.get_ticks()
        self.sonidos._reproducir_sonido_inmunidad()

    def _desactivar_inmunidad(self):
        tiempo = pygame.time.get_ticks() - self.tiempo_inmunidad
        #print(tiempo)
        if tiempo >= 9000:
            self.current_status_temporal = "ninguno"
            self.velocidad = 5

    def _recibir_golpe(self):
        if self.estado_tamano == "gigante":
            self._desactivar_gigante()
        else:
            self._procesar_muerte()

    def _procesar_muerte(self):
        self.current_status_life = "moribundo"
        self.tiempo_moribundo = pygame.time.get_ticks()

        # NO RESTAR LA VIDA AQUÍ
        if self.vidas == 1:
            self.is_dead = True
            self.current_status_life = "muerto"
            self.sonidos._reproducir_sonido_gameover()
            print(f"Puntos total: {self.puntos}")

        else:
            self.sonidos._reproducir_sonido_moribundo()

    def _correr_tiempo_moribundeo(self):
        tiempo = pygame.time.get_ticks() - self.tiempo_moribundo
        if tiempo > 2000:
            if self.current_status_size == "gigante":
                self._desactivar_gigante()
            else:
                self.vidas -= 1
            self.current_status_life = "vivo"
            self.impulso_salto = 0
            self.is_grounded = False
            self.is_jumping = True

    def _moribundeo(self):
        if self.is_grounded and not self.is_jumping:
            self.impulso_salto = -25
            self.is_grounded = False
            self.is_jumping = True
        self.image = self.sprites["muerto"]["dead"]
            

    def _actualizar_rect(self):
        self.rect = self.image.get_rect(bottomleft=(self.dx, self.dy))

    def cargar_sprites(self):
        return {
            "normal": {
                "idle": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm1/idle/idle.png"), (self.dimension)),
                "run": pygame.image.load("assets/sprites/player/Jugador/mm1/run/run.png"),
                "jump": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm1/jump/jump.png"), (self.dimension))
            },
            "gigante": {
                "idle": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm2/idle/idle.png"), (self.dimension)),
                "run": pygame.image.load("assets/sprites/player/Jugador/mm2/run/run.png"),
                "jump": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm2/jump/jump.png"), (self.dimension)),
                "crouch": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/mm2/crouch/crouch.png"), (self.dimension))
            },
            "muerto": {
                "dead": pygame.transform.scale(pygame.image.load("assets/sprites/player/Jugador/death/dead.png"), (self.dimension))
            }
        }
