import pygame

from crash import *
from constants import *
from objects.debug import *
from objects.Items import Moneda
from objects.Jugador import Jugador
from objects.Enemigo import Goomba, Turtle
from objects.Poderes import Hongo_Rojo, Hongo_Verde, Estrella


class Game:
    def __init__(self):
        # Inicializar Pygame y crear la ventana del juego
        pygame.init()
        pygame.display.set_caption(f"{TITULO}")
        self.ventana = pygame.display.set_mode((DIMENSION_VENTANA))
        self.clock = pygame.time.Clock()
        self.running = True
        self.FPS = 60
        
        # Manejar los tiempos de aparación de los objetos


        # Definir los grupos de sprites
        self.enemigos = pygame.sprite.Group()
        self.poderes = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        

        """Crear los objetos del juego"""

        # Instanciar jugador
        self.jugador = Jugador("Mario Mosquera", 0, Y)

        # Instanciar enemigos
        goomba = Goomba("Goomba", 1200, Y)
        turtle = Turtle("Turtle", 300, Y)
        self.enemigos.add(goomba)

        # Instanciar poderes
        hongo_rojo = Hongo_Rojo(500, Y)
        hongo_verde = Hongo_Verde(700, Y)
        estrella = Estrella(900, Y)
        self.poderes.add(estrella)

        # Colisiones
        self.colisiones = Colisiones(self.jugador, self.enemigos, self.poderes, None)

        
    def update(self):
        self.jugador.update()
        self.enemigos.update()
        self.poderes.update()
        self.colisiones.detectar_colisiones()

    def handle_events(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.running = False


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

        """DEPURACION"""
        #recuadros(self)

    def run(self):
        while self.running:     
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.FPS)