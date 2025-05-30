import pygame
import os

pygame.init()

ANCHO, ALTO = 1100, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("pruebita")

# Carpeta de imágenes
carpeta = "Assets/font/"

# Ordenar nombres de archivo primero
nombres_ordenados = sorted([archivo for archivo in os.listdir(carpeta) if archivo.endswith(".png")])
nombres_ordenados.reverse()  

capas = [pygame.image.load(os.path.join(carpeta, archivo)).convert_alpha() for archivo in nombres_ordenados]

# Dibujar las capas
ventana.fill((0, 0, 0))
fondo= pygame.image.load("Assets/font/4.Ground.png")
ventana.blit(fondo, (100, 100))

pygame.display.flip()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

pygame.quit()
