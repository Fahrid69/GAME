import pygame
## Se definen las variables que las cuales sus valores no van a modificarse

# VALORES DEL TAMAÑO DE LA VENTANA
ANCHO_VENTANA = 1100
ALTO_VENTANA = 600

# SE DEFINE EL SUELO REAL
Y = 553

## IMGS
FONDO = pygame.transform.scale(pygame.image.load("Assets/font/Layer_0001_8.png"), (1100, 600))

# DIRECTORIOS
D_JUGADOR = "Assets/"
D_GOOMBA = "Assets/enemy/Goomba/"
D_PODERES = "Assets/powers/"

# ESCALAS CORRESPONDIENTES A:
E_JUGADOR = (80,80)

# ALMACENAR LOS SPRITES:
SPRITES_JUGADOR = {
    "mm1": {
        "derecha": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/DERECHA.png"),E_JUGADOR),
        "izquierda": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/IZQUIERDA.png"),E_JUGADOR),
        "der_correr1": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/CORRIENDO_DERECHA_1.png"),E_JUGADOR),
        "der_correr2": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/CORRIENDO_DERECHA_2.png"),E_JUGADOR),
        "der_correr3": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/CORRIENDO_DERECHA_3.png"),E_JUGADOR),
        "izq_correr1": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/CORRIENDO_IZQUIERDA_1.png"),E_JUGADOR),
        "izq_correr2": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/CORRIENDO_IZQUIERDA_2.png"),E_JUGADOR),
        "izq_correr3": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/CORRIENDO_IZQUIERDA_3.png"),E_JUGADOR),
        "saltando_der": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/SALTAR_DERECHA.png"),E_JUGADOR),
        "saltando_izq": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/SALTAR_IZQUIERDA.png"),E_JUGADOR)
    },
    "mm2": {
        "derecha": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/DERECHA.png"),E_JUGADOR),
        "izquierda": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/IZQUIERDA.png"),E_JUGADOR),
        "der_correr1": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/00_DERECHA_GRANDE.png"),E_JUGADOR),
        "der_correr2": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/01_DERECHA_GRANDE.png"),E_JUGADOR),
        "der_correr3": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/02_DERECHA_GRANDE.png"),E_JUGADOR),
        "izq_correr1": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/00_IZQUIERDA_GRANDE.png"),E_JUGADOR),
        "izq_correr2": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/01_IZQUIERDA_GRANDE.png"),E_JUGADOR),
        "izq_correr3": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/02_IZQUIERDA_GRANDE.png"),E_JUGADOR),
        "saltando_der": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/SALTAR_DERECHA_GRANDE.png"),E_JUGADOR),
        "saltando_izq": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/SALTAR_IZQUIERDA_GRANDE.png"),E_JUGADOR),
    }
}

SPRITES_GOOMBA = {
    "brown": {
        "caminar1": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}cafe/01_goomba.png"), (50,50)),
        "caminar2": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}cafe/02_goomba.png"), (50,50)),
        "muerto": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}cafe/00_goomba.png"), (50,50))
    },
    "black": {
        "caminar1": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}negro/01_goomba.png"), (50,50)),
        "caminar2": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}negro/02_goomba.png"), (50,50)),
        "muerto": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}negro/00_goomba.png"), (50,50))
    }
}

SPRITES_PODERES = {
    "hongo rojo": {
        "1hr": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/Hongo Rojo/01_hr.png"), (30,30)),
        "2hr": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/Hongo Rojo/02_hr.png"), (30,30)),
        "3hr": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/Hongo Rojo/03_hr.png"), (30,30))
    },
    "hongo verde": {
        "1hv": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/Hongo Verde/01_hv.png"), (30,30)),
        "2hv": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/Hongo Verde/02_hv.png"), (30,30)),
        "3hv": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/Hongo Verde/03_hv.png"), (30,30))
    },
    "star": {
        "01s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrellas/starr_1.png"), (30,30)),
        "02s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrellas/starr_3.png"), (30,30)),
        "03s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrellas/starr_4.png"), (30,30)),
        "04s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrellas/starr_5.png"), (30,30)),
        "05s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrellas/starr_6.png"), (30,30))
    }
}