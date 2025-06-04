from constants import *

import pygame

class Collide:
    def __init__(self, jugador, enemigos, poderes):
        pass

def collide_jugador_poder(jugador, poderes):
    colision = pygame.sprite.spritecollideany(jugador, poderes)
    if colision:
        if colision.nombre == "New Change":
            jugador.vidas += 1
            poderes.remove(colision)
            SOUNDEFFECTS["gigante"].play()
        elif colision.nombre == "Gigante":
            jugador.crecer()
            SOUNDEFFECTS["vida"].play()
            poderes.remove(colision)
        elif colision.nombre == "Inmunidad":
            #jugador.inmunidad()
            pass

def collide_jugador_enemigo(jugador, enemigos):
    colision = pygame.sprite.spritecollideany(jugador, enemigos)
    if colision:
        if colision.nombre == "Goomba":
            jugador.vidas -= 0
            print(jugador.vidas)
        elif colision.nombre == "Turtle":
            jugador.vidas -= 0
