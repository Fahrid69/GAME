from Jugador import Jugador
from Enemigo import Goomba, Turtle
from Poderes import Hongo_rojo, Hongo_verde, Estrella
from Crash import *
from constants import ANCHO_VENTANA, ALTO_VENTANA, Y, SOUNDEFFECTS
from debug import recuadros

import pygame

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("SMMG")

        self.ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        self.clock = pygame.time.Clock() # ESTABLECE EL TIEMPO desde que se inicia el juego
        self.running = True
        self.FPS = 60

#           CREAR LOS GRUPOS
        self.enemigos = pygame.sprite.Group()
        self.poderes = pygame.sprite.Group()
        
        self.jugador = Jugador("Mario Mosquera", 0, Y)

        goomba = Goomba("Goomba", 900, Y) #Instanciar a los goombas
        turtle = Turtle("Turtle", 200, Y)
        self.enemigos.add(goomba, turtle)

        estrella = Estrella(900, Y)
        hongo_verde = Hongo_verde(700, Y)
        hongo_rojo = Hongo_rojo(500, Y)
        self.poderes.add(hongo_rojo, hongo_verde) # agg la estrella

    def update(self):
        self.jugador.update()
        self.enemigos.update()
        self.poderes.update()

        collide_jugador_poder(self.jugador, self.poderes)
        collide_jugador_enemigo(self.jugador, self.enemigos)


    def handle_events(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.ventana.fill((50, 175, 250))
        self.ventana.blit(self.jugador.image, self.jugador.rect)
        self.enemigos.draw(self.ventana)
        self.poderes.draw(self.ventana)
        self.ventana.blit(FONDO, (0, ALTO_VENTANA - FONDO.get_height()))


#           DEPURAR
        recuadros(self)

#           SUELO

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.FPS)