from constants import *
from animation import Animacion

import pygame, random

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, nombre, dx, dy):
        super().__init__()
        self.nombre = nombre
        self.dx = dx
        self.dy = dy
        self.velocidad = -2

class Goomba(Enemigo):
    def __init__(self, nombre, dx, dy):
        super().__init__(nombre, dx, dy)
        self.variante = random.choice(("black", "brown"))
        self.sprites = SPRITES_GOOMBA[self.variante]
        self.estado = "vivo"

        frames =[self.sprites["caminar1"], self.sprites["caminar2"]] #   Cargar las imagenes para la animacion
        self.animacion = Animacion(frames, 10) #se le pasan valores paraa animarla

        self.image = self.animacion.get_frame()
        self.rect = self.image.get_rect(bottom=Y)

        self.movimiento = -1.5

    def death(self, jugador):
        """Goomba al ser pisado desde arriba por MM, se cargara la imagen de muerte y MM rebotara sobre el. La imagen cargada de muerte de goomba, 
        debera desaparecer 1 segundo despues sumando 100 puntos a los puntos del jugador"""
        self.movimiento = 0
        self.estado = "muerto"
        self.tiempo = pygame.time.get_ticks()
        SOUNDEFFECTS["daño"].play()

        jugador.puntos += 100
        jugador.salto = -16


    def update(self):
        self.dx += self.movimiento *2
        self.animacion.actualizar()

        if self.dx <= 0 or self.dx >= ANCHO_VENTANA - self.rect.width:
            self.movimiento *= -1
        self.rect.bottomleft = (self.dx, self.dy)

        if self.estado == "vivo":
            self.image = self.animacion.get_frame()
        elif self.estado == "muerto":
            self.image = SPRITES_GOOMBA[self.variante]["muerto"]
            if pygame.time.get_ticks() - self.tiempo >= 1000:
                self.kill()
                return  # No se sigue moviendo ni animando

class Turtle(Enemigo):
    def __init__(self, nombre, dx, dy):
        super().__init__(nombre, dx, dy)
        self.sprites = SPRITES_TURTLE["turtle"]

#           CARGAAMOS LAS IMAGENES PARA LUEGO ANIMARLAS CON ANIMATION.PY
        frames = [self.sprites["01t"], self.sprites["02t"], self.sprites["03t"], self.sprites["04t"]]
        self.animacion = Animacion(frames, 10)

#           Conseguimos la animación y la otorgamos como imagen
        self.image = self.animacion.get_frame()
        self.rect = self.image.get_rect(bottom=Y)

        self.movimiento = -1
        self.estado = "vivo"
        self.direccion = "izq"

    def death(self, jugador):
        self.falltime = pygame.time.get_ticks()
        self.estado = "muerto"

        self.movimiento = 0
        jugador.puntos += 100
        jugador.salto = -16
        SOUNDEFFECTS["daño1"].play()


    def update(self):
        if self.estado == "vivo":
            self.dx += self.movimiento *2
            self.animacion.actualizar()
            self.image = self.animacion.get_frame()
        elif self.estado == "muerto":
            if self.direccion == "der": self.image = pygame.transform.flip(SPRITES_TURTLE["turtle"]["00t"], True, False)
            else: self.image = SPRITES_TURTLE["turtle"]["00t"]

            if pygame.time.get_ticks() - self.falltime > 7000:
                self.estado = "vivo"
                if self.direccion == "izq":
                    self.movimiento = -1
                elif self.direccion == "der":
                    self.movimiento = 1
        self.rect.x = self.dx

#           CHOCA CON LOS LIMITES DE LA VENTANAS
#           Y SE DEVUELVE        
        if self.dx < 0 or self.dx >= ANCHO_VENTANA - self.rect.width:
            self.movimiento *= -1
            self.direccion = "izq"
        self.rect.bottomleft = (self.dx, self.dy)

#           SE DA LA VUELTA
        if self.movimiento > 0 :
            self.direccion = "der"
            self.image = pygame.transform.flip(self.animacion.get_frame(), True, False)


#
