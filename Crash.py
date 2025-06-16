import pygame

from constants import *
from soundeffects import Sonidos
from objects.Jugador import Jugador
from objects.Enemigo import Goomba,Turtle

class Colisiones:
    def __init__(self, jugador, enemigos, poderes, items):
        self.jugador = jugador
        self.enemigos = enemigos
        self.poderes = poderes
        self.items = items

        self.sonidos = Sonidos()

    def detectar_colisiones(self):
        self._jugador_vs_enemigos()
        self._jugador_vs_poderes()
        self._jugador_vs_items()

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
                    print("pasapsa")
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
                    #SOUNDEFFECTS["turtle"].play()
                    return

            
            if pygame.sprite.collide_rect(self.jugador, enemigo):
                self.jugador._procesar_muerte()


            if self.jugador.estado == "inmunidad":
                print("Eliminando a los enemigos")
                enemigo.kill()


    def _jugador_vs_poderes(self):
        poder = pygame.sprite.spritecollideany(self.jugador, self.poderes)
        if poder:
            # Si colisiona con el hongo verde
            if poder.nombre == "+1HP":  
                self.jugador._incrementar_vida()
                self.poderes.remove(poder)
            
            # Si colisiona con el hongo rojo
            if poder.nombre == "Gigante":
                self.jugador._activar_gigante()
                self.poderes.remove(poder)
            
            # Si colisiona con las estrellas
            if poder.nombre == "Inmunidad":
                self.jugador._activar_inmunidad()
                self.poderes.remove(poder)

    def _jugador_vs_items(self):
        pass
            