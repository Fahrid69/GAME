from constants import *

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
            jugador.inmunidad()
            jugador.velocidad = 7
            SOUNDEFFECTS["star"].play()
            poderes.remove(colision)
        elif colision.nombre == "Moneda":
            SOUNDEFFECTS["coin"].play()
            poderes.remove(colision)

def collide_jugador_enemigo(jugador, enemigos):
    colision = pygame.sprite.spritecollideany(jugador, enemigos)
    if colision:
        if jugador.estado == "normal":
            for enemigo in enemigos:
                if jugador.rect.colliderect(enemigo.rect):
                    if jugador.rect.bottom >= enemigo.rect.top + 10 and jugador.salto > 0:
                        enemigo.death(jugador)
                    elif jugador.versiones == "mm2":
                        jugador.estado = "normal"
                        jugador.versiones = "mm1"
                        SOUNDEFFECTS["daño2"].play()
                    else:
                        jugador.death()
                        if jugador.vidas > 0:
                            SOUNDEFFECTS["daño2"].play()

                            
        elif jugador.estado == "inmunidad":
            print("eliminando a los enemigos")
            #enemigos.remove(colision)
            pass
                
"""
    Conseguir un tiempo de cooldown antes que MM vuelva a ser dañado por un enemigo
    tiempo de cooldown = 2"""