from Jugador import Jugador
from Enemigo import Goomba
from Poderes import Hongo_rojo, Hongo_verde, Estrella
from constants import ANCHO_VENTANA, ALTO_VENTANA, Y, FONDO

import pygame

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Mario from Temu")

        self.ventana = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
        self.clock = pygame.time.Clock() # ESTABLECE EL TIEMPO desde que se inicia el juego
        self.running = True
        self.FPS = 60

#           CREAR LOS GRUPOS
        self.enemigos = pygame.sprite.Group()
        self.poderes = pygame.sprite.Group()

        goomba = Goomba(f"Goomba", 300, Y) #Instanciar a los goombas
        self.enemigos.add(goomba)
        
        self.jugador = Jugador("Mario Mosquera", 0, Y)

    def update(self):
        self.jugador.update()
        self.enemigos.update()


    def handle_events(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.running = False

    def draw(self):
        self.ventana.fill((0, 100, 200))
        self.enemigos.draw(self.ventana)
        self.ventana.blit(self.jugador.image, self.jugador.rect)

#           SUELO
        self.ventana.blit(FONDO, (0, ALTO_VENTANA - FONDO.get_height()))

#        pygame.draw.rect(self.ventana, (0,255,0), self.jugador.rect, 2) # REMARCAR LA CAJA DEL JUGADOR PARA COLISIONES
#        for enemigo in self.enemigos:
#            pygame.draw.rect(self.ventana, (255,0,0), enemigo.rect, 2) # REMARCAR LA CAJA DE LOS ENEMIGOS

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.FPS)
        
