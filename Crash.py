from constants import *
import pygame, random
from Enemigo import Goomba,Turtle

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
    
    enemigo = pygame.sprite.spritecollideany(jugador, enemigos)

    if not enemigo:
        return

    if not isinstance(enemigo, (Goomba, Turtle)):
        return

    if jugador.estado != "normal":
        return
    
    # Si llegamos aquí, hay colisión válida con un enemigo y el jugador está en estado normal
    if jugador.rect.bottom >= enemigo.rect.top + 10 and jugador.salto > 0:
        enemigo.estado = "muerto"
        jugador.salto = -15
        return

    # Si el jugador es grande (mm2) y es golpeado
    if jugador.versiones == "mm2":
        jugador.estado = "normal"
        jugador.versiones = "mm1"
        SOUNDEFFECTS["daño2"].play()
        return

    # Si el jugador es pequeño (mm1) y es golpeado
    jugador.death()
    if jugador.vidas > 0:
        SOUNDEFFECTS["daño2"].play()
                                
    elif jugador.estado == "inmunidad":
        print("eliminando a los enemigos")
        enemigo.death()
                    
"""
    Conseguir un tiempo de cooldown antes que MM vuelva a ser dañado por un enemigo
    tiempo de cooldown = 2"""