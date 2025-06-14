import pygame
class Sonidos:
    def __init__(self):
        pygame.mixer.init()
        # Cargar la musica de fondo
        self.sonido_fondo = pygame.mixer.Sound("assets/soundeffects/soundtrack/soundtrack.mp3")
        self.sonido_fondo.set_volume(0.5)
        self.sonido_fondo.play(-1) 

        # Cargar los efectos de sonido del juego
        #self.sonido_salir = pygame.mixer.Sound()
        #self.sonido_moneda = pygame.mixer.Sound("assets/soundeffects/soundcoins/get_coin.wav")
        self.sonido_saltar = pygame.mixer.Sound("assets/soundeffects/soundjump/jump.wav")
        self.sonido_goomba = pygame.mixer.Sound("assets/soundeffects/soundamage/goomba/goomba.ogg")
        #self.sonido_muerte = pygame.mixer.Sound()
        #self.sonido_poder = pygame.mixer.Sound()
    

    def _reproducir_sonido_salto(self):
        self.sonido_saltar.play()

    def _reproducir_sonido_goomba(self):
        self.sonido_goomba.play()

"""
    def _reproducir_daño_jugador(self):
        self.sonido_daño.play()

    def _reproducir_sonido_muerte(self):
        self.sonido_muerte.play()"""