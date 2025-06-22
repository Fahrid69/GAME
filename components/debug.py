import pygame


"""__Esta es la sección para depurar el código__"""


# CREA UN CUADRO AL REDEDOR DE LA CAJA DEL JUGADOR
# PARA IDENTIFICAR COLISIONES 
def recuadros(self):
    pygame.draw.rect(self.ventana, (0,255,0), self.jugador.rect, 1) # REMARCAR LA CAJA DEL JUGADOR PARA COLISIONES
    for enemigo in self.enemigos:
        pygame.draw.rect(self.ventana, (255,0,0), enemigo.rect, 1) #REMARCAR LA CAJA DE LOS ENEMIGOS
    for poder in self.poderes:
        pygame.draw.rect(self.ventana, (0,0,255), poder.rect, 1) #REMARCAR AMBAS 
    for item in self.items:
        pygame.draw.rect(self.ventana, (0,0,255), item.rect, 1)

def comandos(Self):
    pass