import pygame

class Personaje(pygame.sprite.Sprite):
    def __init__(self, nombre, dx, dy):
        self.nombre = nombre
        self.dx = dx
        self.dy = dy

