import pygame

from constants import *
from systems.crash import *
from components.debug import *
from components.items import Moneda
from components.player import Jugador
from components.enemies import Goomba, Turtle
from components.powers import Hongo_Rojo, Hongo_Verde, Estrella
from systems.spawner_enemies import GenerarEnemigos
from systems.spawner_powers import GenerarPoderes
from systems.spawner_items import GenerarItems


class Game:
    def __init__(self):
        # Inicializar Pygame y crear la ventana del juego
        pygame.init()
        pygame.display.set_caption(TITULO)
        self.ventana = pygame.display.set_mode((DIMENSION_VENTANA))
        self.clock = pygame.time.Clock()
        self.time = pygame.time.get_ticks()
        self.running = True

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
        self.generar_enemigo = GenerarEnemigos(self.jugador, self.enemigos)

        # Instanciar poderes
        self.generar_poder = GenerarPoderes(self.jugador, self.poderes)

        # Instanciar items
        self.generar_item = GenerarItems(self.jugador, self.items)

        # Colisiones
        self.colisiones = Colisiones(self.jugador, self.enemigos, self.poderes, self.items)

        
    def update(self):
        self.jugador.update()
        self.enemigos.update()
        self.generar_enemigo.update()
        self.poderes.update()
        self.generar_poder.update()
        self.items.update()
        self.generar_item.update()
        self.colisiones.detectar_colisiones()

    def handle_events(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.running = False


    def draw(self):
        self.ventana.fill((150, 200, 255))

        # Dibujar la información del jugador
        self._draw_stats_info()

        self.ventana.blit(FONDO, (0, ALTO_VENTANA - FONDO.get_height()))

        # Dibujar lo demas
        self._draw_enemies()
        self._draw_powers()
        self._draw_items()
        self._draw_player()

        #recuadros(self)

        # Dibujar la pantalla final
        self._vistar_game_over()


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
    
    def _draw_items(self):
        for item in self.items:
            self.ventana.blit(item.image, item.rect)

    def _vistar_game_over(self):
        if self.jugador.is_dead:
            self.ventana.fill((0,0,0))

            self.heart = pygame.transform.scale(pygame.image.load("assets/fonts/pixels/heart-broken.png"), (50,50))
            self.ventana.blit(self.heart, (ANCHO_VENTANA//2, ALTO_VENTANA//2))

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
            self.clock.tick(60)