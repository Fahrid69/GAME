import pygame, random

pygame.mixer.init()

## Se definen las variables que las cuales sus valores no van a modificarse

""" Relacionadas con la ventana del juego """

# Dimensiones de la ventana del juego
DIMENSION_VENTANA = (1380, 720)  # Ancho, Alto
# Importante: Modificar el tamaño de la ventana afecta las dimensiones del fondo y otros elementos del juego.


ANCHO_VENTANA = 1380
ALTO_VENTANA = 720

TITULO = ">_game_SuperMarioBros.py"

# con esta modifica el suelo real del juego a los objetos
X = random.randint(100,ANCHO_VENTANA - 50)
Y = 640                               #640

## IMGS
FONDO = pygame.transform.scale(pygame.image.load("Assets/fonts/front.png"), (ANCHO_VENTANA, 91))



