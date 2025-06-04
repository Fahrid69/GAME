from constants import *
from animation import Animacion

import pygame

class Poder(pygame.sprite.Sprite):
    def __init__(self, nombre, image, dx, dy):
        super().__init__()
        self.nombre = nombre
        self.image = image
        self.rect = self.image.get_rect(bottomleft=(dx,Y))
        
class Hongo_rojo(Poder):
    def __init__(self, dx, dy):
        imagen = SPRITES_PODERES["hongo rojo"]["1hr"]
        super().__init__("Gigante", imagen, dx, dy)

        frames =[SPRITES_PODERES["hongo rojo"]["1hr"],SPRITES_PODERES["hongo rojo"]["2hr"],SPRITES_PODERES["hongo rojo"]["3hr"],SPRITES_PODERES["hongo rojo"]["4hr"]]
        self.animacion = Animacion(frames, 7.5)
    
    def update(self):
        self.animacion.actualizar()
        self.image = self.animacion.get_frame()



class Hongo_verde(Poder):
    def __init__(self, dx, dy):
        imagen = SPRITES_PODERES["hongo verde"]["1hv"]
        super().__init__("New Change", imagen, dx, dy)

        frames =[SPRITES_PODERES["hongo verde"]["1hv"],SPRITES_PODERES["hongo verde"]["2hv"],SPRITES_PODERES["hongo verde"]["3hv"],SPRITES_PODERES["hongo verde"]["4hv"]]
        self.animacion = Animacion(frames, 10)
    
    def update(self):
        self.animacion.actualizar()
        self.image = self.animacion.get_frame()

class Estrella(Poder):
    def __init__(self, dx, dy):
        imagen = SPRITES_PODERES["estrella"]["1s"]
        super().__init__("Inmunidad", imagen, dx, dy)

#           Animar:
        frames = [SPRITES_PODERES["estrella"]["1s"],SPRITES_PODERES["estrella"]["2s"],SPRITES_PODERES["estrella"]["3s"],SPRITES_PODERES["estrella"]["4s"],SPRITES_PODERES["estrella"]["5s"]]
        self.animacion = Animacion(frames, 12.5)

#        

        self.velocidad = 5
        self.salto = 10
        self.gravedad = 0.25
        self.direccion = -1
        self.suelo = Y

    def update(self):
#           ANIMACION:
        self.animacion.actualizar()
        self.image = self.animacion.get_frame()

#           REBOTAR:
        if self.rect.left <= 0 or self.rect.right >= ANCHO_VENTANA:
            self.direccion *=-1

        self.rect.x += self.velocidad * self.direccion


        self.salto += self.gravedad
        self.rect.y += self.salto

        if self.rect.bottom >= self.suelo:
            self.rect.bottom = self.suelo
            self.salto =-10