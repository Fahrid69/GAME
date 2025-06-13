from Jugador import Jugador
from Enemigo import Goomba, Turtle
from Poderes import Hongo_rojo, Hongo_verde, Estrella, Moneda
from Crash import *
from constants import ANCHO_VENTANA, ALTO_VENTANA, X, Y
from debug import recuadros

import pygame

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("SMMC")
        self.ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        self.clock = pygame.time.Clock()
        self.running = True
        self.FPS = 60
        
        self.spawn = 4000
        self.tspawn = pygame.time.get_ticks()

#           CREAR LOS GRUPOS:
        self.enemigos = pygame.sprite.Group()
        self.poderes = pygame.sprite.Group()
        
#           - INSTANCIAMIENTO: -
        self.jugador = Jugador("Mario Mosquera", 0, Y)
#           - 
        goomba = Goomba("Goomba", 1200, Y) #Instanciar a los goombas
        turtle = Turtle("Turtle", 300, Y)
        self.enemigos.add(goomba)

        estrella = Estrella(900, Y)
        hongo_verde = Hongo_verde(700, Y)
        hongo_rojo = Hongo_rojo(500, Y)

        moneda = Moneda(X, random.randint(400, Y))

        self.poderes.add()
        
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
        """
        if self.jugador.vidas <= 0:
            self.running = False"""

    def draw(self):
        self.ventana.fill((150, 200, 255))
        self.ventana.blit(self.jugador.image, self.jugador.rect)
        self.enemigos.draw(self.ventana)
        self.poderes.draw(self.ventana)
        self.ventana.blit(FONDO, (0, ALTO_VENTANA - FONDO.get_height()))

        if self.jugador.vidas == 0:
            fuente = pygame.font.SysFont("Times New Roman", 50, bold=True)
            texto = fuente.render("GAME OVER", True, (255, 0, 0))
            rect_texto = texto.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA//2))
            self.ventana.blit(texto, rect_texto)



#           DEPURAR
        #recuadros(self)

#           SUELO

    def run(self):
        while self.running:     
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.FPS)