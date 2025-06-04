from Molde import Personaje
from constants import *
from animation import Animacion

import pygame


class Jugador(Personaje):
    def __init__(self, nombre, dx, dy):
        super().__init__(nombre, dx, dy)
        self.vidas = 3
        self.salto = 0
        self.vel = 5    
        self.puntos = 0
        self.gravedad = 1
        self.poder = False
        self.estado = True
        self.ensuelo = True
        self.direccion = "der"
        self.version = "mm1"
        self.sprites = SPRITES_JUGADOR
        self.image = self.sprites[self.version]["iddle"]
        self.rect = self.image.get_rect(topleft=(dx, dy) )

        self.animacion = Animacion([self.sprites[self.version]["run1"], self.sprites[self.version]["run2"],self.sprites[self.version]["run3"],self.sprites[self.version]["run4"]], 7.5)

    def update(self):
        keys = pygame.key.get_pressed()
        self.movimiento = False

#          DETECTAR CONTROLES
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.ensuelo:
            self.salto = -20
            self.ensuelo = False
            SOUNDEFFECTS["salto"].play()
        elif keys[pygame.K_d] and not keys[pygame.K_a]:
            self.dx += self.vel
            self.direccion = "der"
            self.movimiento = True
            #no salirse de la ventana
            if self.dx > ANCHO_VENTANA - self.rect.width:
                self.dx = ANCHO_VENTANA - self.rect.width
        elif keys[pygame.K_a] and not keys[pygame.K_d]:
            self.dx -= self.vel
            self.direccion = "izq"
            self.movimiento = True
            #no salirse d ela ventana
            if self.dx < 0:
                self.dx = 0

        if not self.ensuelo:
            self.salto +=self.gravedad
            self.dy += self.salto

        if self.dy >= Y:
            self.dy = Y
            self.salto = 0
            self.ensuelo = True

#          ACTUALIZAR LA ANIMACION
#
        if not self.ensuelo:
            self.image = SPRITES_JUGADOR[self.version]["jump1"] 
            if self.direccion == "izq":
                self.image = pygame.transform.flip(self.image, True, False)
        elif self.movimiento:
            self.animacion.actualizar()
            frame = self.animacion.get_frame()
            if self.direccion == "izq":
                frame = pygame.transform.flip(frame, True, False)
            self.image =frame
            
        else:
            # Imagen estatica segun la dirección del personaje:
            if self.direccion == "der":
                self.image = self.sprites[self.version]["iddle"]
            elif self.direccion == "izq":
                self.image = pygame.transform.flip(SPRITES_JUGADOR[self.version]["iddle"], True, False)

        self.rect.bottomleft = (self.dx, self.dy)

#           LIMITAR ESPACIO
        if self.dx <= 0 or self.dx >= ANCHO_VENTANA:
            self.vel = 0
            if self.direccion == "der":
                self.vel = 5
        else:
            self.vel = 5

    def crecer(self):
        if self.version == "mm2":
            return
        
        self.version = "mm2" # cambiar de personaje

        if self.direccion == "der":
            self.image = self.sprites[self.version]["iddle"] 
        else:
            self.image = pygame.transform.flip(self.sprites[self.version]["iddle"], True, False)

        self.vel = 6

        bottomleft = self.rect.bottomleft
        self.rect = self.image.get_rect(bottomleft = bottomleft)

        self.animacion = Animacion([self.sprites[self.version]["run1"], self.sprites[self.version]["run2"], self.sprites[self.version]["run3"], self.sprites[self.version]["run4"],], 7.5)
  
    def actualizar_imgs(self, accion):
        key = f"{accion}"
        if key in self.sprites[self.version]:
            self.image = self.sprites[self.version][key]