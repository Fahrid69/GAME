import pygame

from constants import *
from soundeffects import Sonidos
from components.Jugador import Jugador
from components.Enemigo import Goomba,Turtle

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
        # Si el jugador no está en estado vivo realmente, ignora las colisiones con enemigos vivos por si acaso
        if self.jugador.current_status_life != "vivo":
            return

        # Detectar colisión con cualquier enemigo vivo
        enemigo = pygame.sprite.spritecollideany(self.jugador,
            [enemigo for enemigo in self.enemigos if enemigo.current_status == "vivo"])

        # Si no hay colisiones se va
        if not enemigo:
            return


        # Verificar si el jugador cae sobre el enemigo (colisión desde arriba)
        if self.jugador.rect.bottom >= enemigo.rect.top + 10 and self.jugador.is_jumping:
            self.jugador.impulso_salto = -20

            # Llamamos al método especifico de muerte por aplastamiento
            if isinstance(enemigo, (Goomba, Turtle)): 
                enemigo._procesar_muerte_aplastamiento()
                return

        # Si verificar colisión lateral o frontal
        if pygame.sprite.collide_rect(self.jugador, enemigo):
            # Primero verificar si el jugador está en estado de inmunidad (tiene prioridad)
            if self.jugador.current_status_temporal == "inmunidad":
                enemigo.kill() 
                return  # se devuelve
            
            # Si no es inmune, verificar si está en estado gigante
            if self.jugador.current_status_size == "gigante":
                self.jugador._desactivar_gigante()  # Reduce de tamaño sin perder vida
                return
                        
            # Si no es inmune ni gigante, procesa daño normal
            self.jugador._procesar_muerte()                        


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
            