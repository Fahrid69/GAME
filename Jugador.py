from Molde import Personaje
from constants import *
from animation import Animacion

import pygame


class Jugador(Personaje):
    def __init__(self, nombre, dx, dy):
        super().__init__(nombre, dx, dy)
        self.vidas = 3
        self.salto = 0
        self.puntos = 0
        self.gravedad = 1
        self.velocidad = 5    
        self.poder = False
        self.ensuelo = True
        self.estado = "normal"
        self.direccion = "der"
        self.versiones = "mm1"
        self.version = self.versiones
        self.sprites = SPRITES_JUGADOR
        self.tstatus = 0
        self.image = self.sprites[self.versiones]["iddle"]
        self.rect = self.image.get_rect(topleft=(dx, dy) )

        self.animacion = Animacion([self.sprites[self.versiones]["run1"], self.sprites[self.versiones]["run2"],self.sprites[self.versiones]["run3"],self.sprites[self.versiones]["run4"]], 7.5)

    def update(self):
        keys = pygame.key.get_pressed()
        self.movimiento = False

#          - DETECTAR CONTROLES -
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.ensuelo:
            self.salto = -20
            self.ensuelo = False
            SOUNDEFFECTS["salto"].play()
        elif keys[pygame.K_d] and not keys[pygame.K_a]:
            self.dx += self.velocidad
            self.direccion = "der"
            self.movimiento = True
            if self.dx > ANCHO_VENTANA - self.rect.width:
                self.dx = ANCHO_VENTANA - self.rect.width
        elif keys[pygame.K_a] and not keys[pygame.K_d]:
            self.dx -= self.velocidad
            self.direccion = "izq"
            self.movimiento = True
            if self.dx < 0:
                self.dx = 0

#           - SALTO - 
        if not self.ensuelo:
            self.salto +=self.gravedad
            self.dy += self.salto

        if self.dy >= Y:
            self.dy = Y
            self.salto = 0
            self.ensuelo = True

#          ACTUALIZAR LA ANIMACION
        if not self.ensuelo:
            self.image = SPRITES_JUGADOR[self.versiones]["jump1"] 
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
                self.image = self.sprites[self.versiones]["iddle"]
            elif self.direccion == "izq":
                self.image = pygame.transform.flip(SPRITES_JUGADOR[self.versiones]["iddle"], True, False)

#           - OPORTUNIDAD DE VIDAS - 
        if self.estado == "muerto":
            if pygame.time.get_ticks() - self.tcooldown > 3000:
                self.vidas -= 1
                self.estado = "normal"

#           - TIEMPO DE LA INMUNIDAD -
        if self.estado == "inmunidad":
            if pygame.time.get_ticks() - self.tstatus > 10000:
                self.estado = "normal"
                self.velocidad = 5

#           - IDENTIFICAR LA VERSION -
        if self.versiones != self.version:
            self.animacion = Animacion([self.sprites[self.versiones]["run1"],self.sprites[self.versiones]["run2"],self.sprites[self.versiones]["run3"],self.sprites[self.versiones]["run4"]], 7.5)
            self.version = self.versiones
        
        self.rect = self.image.get_rect(bottomleft=(self.dx, self.dy))

    def crecer(self):
        self.estado = "gigante"
        self.versiones = "mm2" # cambiar de personaje

        if self.direccion == "der":
            self.image = self.sprites[self.versiones]["iddle"] 
        else:
            self.image = pygame.transform.flip(self.sprites[self.versiones]["iddle"], True, False)

        bottomleft = self.rect.bottomleft
        self.rect = self.image.get_rect(bottomleft = bottomleft)

        self.animacion = Animacion([self.sprites[self.versiones]["run1"], self.sprites[self.versiones]["run2"], self.sprites[self.versiones]["run3"], self.sprites[self.versiones]["run4"],], 7.5)

    def inmunidad(self):
        self.estado = "inmunidad"
        self.tstatus = pygame.time.get_ticks()
    
    def death(self):
        self.estado = "muerto"
        self.tcooldown = pygame.time.get_ticks()
        print("ASJMGKLASDMGNOASLKDMGÑ")

        if self.vidas <= 0:
            self.vidas = 0
            print("GAME OVER")
            SOUNDEFFECTS["GAMEOVER"].play()

            self.image = SPRITES_JUGADOR["gameover"]
            self.rect = self.image.get_rect(bottom=Y)
  
    def actualizar_imgs(self, accion):
        key = f"{accion}"
        if key in self.sprites[self.versiones]:
            self.image = self.sprites[self.versiones][key]