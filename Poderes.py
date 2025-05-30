from constants import *

import pygame

class Poder(pygame.sprite.Sprite):
    def __init__(self, nombre, image, dx, dy):
        super().__init__()
        self.nombre = nombre
        self.image = image
        self.rect = self.image.get_rect(topleft=(dx, dy))
        
class Hongo_rojo(Poder):
    def __init__(self, dx, dy):
        imagen = SPRITES_PODERES["hongo rojo"]
        super().__init__("Gigante", imagen, dx, dy)


class Hongo_verde(Poder):
    def __init__(self, dx, dy):
        imagen = SPRITES_PODERES["hongo verde"]
        super().__init__("New Change", imagen, dx, dy)

class Estrella(Poder):
    def __init__(self, dx, dy):
        imagen = SPRITES_PODERES["star"]
        super().__init__("Inmunidad", imagen, dx, dy)