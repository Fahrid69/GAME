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

        # Tipografia
        self.tipografia_fuente = pygame.font.Font("assets/fonts/fuente/PixelDigivolve.ttf", 30)
        
        # Manejar los tiempos de aparación de los objetos
        # Proximamente...

        # Definir los grupos de sprites
        self.enemigos = pygame.sprite.Group()
        self.poderes = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
        

        """Crear las instancias del juego"""

        # Instanciar jugador
        self.jugador = Jugador("Mario Mosquera", 0, Y)

        # Instanciar enemigos
        goomba = Goomba("Goomba", 1200, Y, self.jugador)
        turtle = Turtle("Turtle", 300, Y, self.jugador)
        self.enemigos.add(goomba, turtle)

        # Instanciar poderes
        hongo_rojo = Hongo_Rojo(500, Y)
        hongo_verde = Hongo_Verde(700, Y)
        estrella = Estrella(900, Y)
        self.poderes.add(hongo_rojo, hongo_verde, estrella)

        # Instanciar items
        # Proximamente

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

        # Dibujar la información del jugador
        self._draw_stats_info()

        # Dibujar lo demas
        self._draw_player()
        self._draw_enemies()
        self._draw_powers()

        # Dibujar la pantalla final
        self._game_over()

        self.ventana.blit(FONDO, (0, ALTO_VENTANA - FONDO.get_height()))

    def _draw_stats_info(self):
        texto_vidas = self.tipografia_fuente.render(f"vidas restantes: {self.jugador.vidas}", False, (255, 255, 255))
        texto_puntos = self.tipografia_fuente.render(f"puntos: {self.jugador.puntos}", True, (255, 255, 255))
        texto_dinero = self.tipografia_fuente.render(f"monedas: {self.jugador.puntos}", True, (255, 255, 0))
        self.ventana.blit(texto_vidas, (100, 100))
        self.ventana.blit(texto_puntos, (500, 100))
        self.ventana.blit(texto_dinero, (750, 100))

    def _draw_player(self):
        self.ventana.blit(self.jugador.image, self.jugador.rect)

    def _draw_enemies(self):
        for enemigo in self.enemigos:
            self.ventana.blit(enemigo.image, enemigo.rect)
    
    def _draw_powers(self):
        for poder in self.poderes:
            self.ventana.blit(poder.image, poder.rect)

    def _game_over(self):
        if self.jugador.vidas < 1:
            texto = self.tipografia_fuente.render(f"GAME - OVER", True, (255, 0, 0))
            rect_texto = texto.get_rect(center=(ANCHO_VENTANA//2, ALTO_VENTANA//2))
            self.ventana.blit(texto, rect_texto)

            # remover todos los sprites de enemigos y poderes
            self.jugador.kill()
            self.enemigos.empty()
            self.poderes.empty()
            
            


        """DEPURACION"""
        #recuadros(self)

    def run(self):
        while self.running:     
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(self.FPS)