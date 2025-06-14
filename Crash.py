import pygame

from constants import *
from objects.Jugador import Jugador
from objects.Enemigo import Goomba,Turtle

class Colisiones:
    def __init__(self, jugador, enemigos, poderes, items):
        self.jugador = jugador
        self.enemigos = enemigos
        self.poderes = poderes
        self.items = items

    def detectar_colisiones(self):
        self._jugador_vs_enemigos()

    def _jugador_vs_enemigos(self):
        enemigo = pygame.sprite.spritecollideany(self.jugador, self.enemigos)
        
        # Si no hay colisión con un enemigo, o el enemigo no es un Goomba o Turtle, o el jugador no está en estado normal
        if not enemigo or not isinstance(enemigo, (Goomba, Turtle)) or self.jugador.estado != "normal":
            return

        
        for enemigo in self.enemigos:
            # Si el enemigo no está vivo, ps salta a la siguiente iteración
            if enemigo.estado != "vivo":
                continue

            # Si el jugador está en estado normal y colisiona con un enemigo
            if isinstance(enemigo, Goomba):            
                if self.jugador.rect.bottom >= enemigo.rect.top + 10 and self.jugador.impulso_salto > 0:
                    self.jugador.impulso_salto = -20
                    enemigo._procesar_muerte_aplastamiento()
                    return

            if isinstance(enemigo, Turtle):
                if self.jugador.rect.bottom >= enemigo.rect.top + 10 and self.jugador.impulso_salto > 0:
                    self.jugador.impulso_salto = -15
                    enemigo.estado = "muerto"
                    enemigo.direccion_movimiento = 0
                    enemigo.velocidad = 0
                    enemigo.image = enemigo.sprites["green"]["shell"]
                    enemigo.rect = enemigo.image.get_rect(topleft=(enemigo.rect.x, enemigo.rect.y))
                    SOUNDEFFECTS["turtle"].play()
                    return

            if self.jugador.versiones == "mm2":
                self.jugador.estado = "normal"
                self.jugador.versiones = "mm1"
                #SOUNDEFFECTS["daño2"].play()
                return

            
            if pygame.sprite.collide_rect(self.jugador, enemigo):
                self.jugador._procesar_muerte()


            if self.jugador.estado == "inmunidad":
                print("Eliminando a los enemigos")
                enemigo.kill()


    def _jugador_vs_poderes(self):
        poder = pygame.sprite.spritecollideany(self.jugador, self.poderes)
        if poder:
                if poder.nombre == "New Change":
                    self.jugador.vidas += 1
                    self.poderes.remove(poder)
                    SOUNDEFFECTS["gigante"].play()
                
                if poder.nombre == "Gigante":
                    self.jugador.crecer()
                    SOUNDEFFECTS["vida"].play()
                    self.remove(poder)
                
                if poder.colision.nombre == "Inmunidad":
                    self.jugador.inmunidad()
                    self.jugador.velocidad = 7
                    SOUNDEFFECTS["star"].play()
                    self.poderes.remove(poder)
                
"""
                if poder.nombre == "Moneda":
                    SOUNDEFFECTS["coin"].play()
                    poderes.remove(colision)


def collide_jugador_enemigo(jugador, enemigos):
    enemigo = pygame.sprite.spritecollideany(jugador, enemigos)

    # Si no hay colisión con un enemigo, o el enemigo no es un Goomba o Turtle, o el jugador no está en estado normal
    if not enemigo:
        return

    # 
    if not isinstance(enemigo, (Goomba, Turtle)):
        return
     
    if jugador.estado != "normal":
        return
    
    # Si llegamos aquí, hay colisión válida con un enemigo y el jugador está en estado normal
    if jugador.rect.bottom >= enemigo.rect.top + 10 and jugador.impulso_salto > 0:
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