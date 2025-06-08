from constants import *
from Enemigo import Enemigo

import pygame, random

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
            SOUNDEFFECTS["star"].play()
            poderes.remove(colision)
            pass

def collide_jugador_enemigo(jugador, enemigos):
    colision = pygame.sprite.spritecollideany(jugador, enemigos)
    if colision:
        for enemigo in enemigos:
            if jugador.rect.colliderect(enemigo.rect):
                if jugador.rect.bottom >= enemigo.rect.top + 10 and jugador.salto > 0:
                    enemigo.fallecimiento(jugador)
                elif jugador.version == "mm2":
                    jugador.version = "mm1"
                    SOUNDEFFECTS["daño2"].play()
                else:
                    jugador.vidas -= 1
                    print(jugador.vidas)
                    SOUNDEFFECTS["daño2"].play()
                break
        """
        if jugador.rect.bottom >= enemigo.rect.bottom + 10 and jugador.salto > 0:
            jugador.vidas -= 1
            print(jugador.vidas)
            #renacer()
        elif colision.nombre == "Turtle":
            jugador.vidas -= 1"""