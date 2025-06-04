import pygame
pygame.mixer.init()
## Se definen las variables que las cuales sus valores no van a modificarse

# VALORES DEL TAMAÑO DE LA VENTANA
ANCHO_VENTANA = 1380
ALTO_VENTANA = 720

# con esta modifica el suelo real del juego a los objetos
Y = 400

## IMGS
FONDO = pygame.transform.scale(pygame.image.load("Assets/font/4.Ground.png"), (1200, 720))

# DIRECTORIOS FIJOS
D_JUGADOR = "Assets/player/"
D_GOOMBA = "Assets/enemy/Goomba/"
D_TURTLE = "Assets/enemy/Turtle/"
D_PODERES = "Assets/powers/"

# ESCALAS CORRESPONDIENTES A:
E_JUGADOR = (60,60)

# ALMACENAR LOS SPRITES:
SPRITES_JUGADOR = {
    "mm1": {
        "iddle": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/DERECHA.png"),E_JUGADOR),
        "run1": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/CORRIENDO_DERECHA_1.png"),E_JUGADOR),
        "run2": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/CORRIENDO_DERECHA_2.png"),E_JUGADOR),
        "run3": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/CORRIENDO_DERECHA_3.png"),E_JUGADOR),
        "run4": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/CORRIENDO_DERECHA_4.png"),E_JUGADOR),
        "jump1": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm1/SALTAR_DERECHA.png"),E_JUGADOR)
    },
    "mm2": {
        "iddle": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/DERECHA.png"),(60,80)),
        "run1": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/00_DERECHA_GRANDE.png"),(60,80)),
        "run2": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/01_DERECHA_GRANDE.png"),(60,80)),
        "run3": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/02_DERECHA_GRANDE.png"),(60,80)),
        "run4": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/03_DERECHA_GRANDE.png"),(60,80)),
        "jump1": pygame.transform.scale(pygame.image.load(f"{D_JUGADOR}mm2/SALTAR_DERECHA_GRANDE.png"),(60,80))
    }
}

SPRITES_GOOMBA = {
    "brown": {
        "caminar1": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}g1/10_goomba.png"), (50,50)),
        "caminar2": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}g1/20_goomba.png"), (50,50)),
        "muerto": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}g1/30_goomba.png"), (50,50))
    },
    "black": {
        "caminar1": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}g2/10_goomba.png"), (50,50)),
        "caminar2": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}g2/20_goomba.png"), (50,50)),
        "muerto": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}g2/30_goomba.png"), (50,50))
    }
}

SPRITES_TURTLE = {
    "turtle": {
        "01t": pygame.transform.scale(pygame.image.load(f"{D_TURTLE}10_turtle.png"),(50,50)),
        "02t": pygame.transform.scale(pygame.image.load(f"{D_TURTLE}20_turtle.png"),(50,50)),
        "03t": pygame.transform.scale(pygame.image.load(f"{D_TURTLE}30_turtle.png"),(50,50)),
        "04t": pygame.transform.scale(pygame.image.load(f"{D_TURTLE}40_turtle.png"),(50,50)),
        "00t": pygame.transform.scale(pygame.image.load(f"{D_TURTLE}50_turtle.png"),(50,50))
    }
}

SPRITES_PODERES = {
    "hongo rojo": {
        "1hr": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/Hongo Rojo/10_hr.png"), (50,50)),
        "2hr": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/Hongo Rojo/20_hr.png"), (50,50)),
        "3hr": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/Hongo Rojo/30_hr.png"), (50,50)),
        "4hr": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/Hongo Rojo/40_hr.png"), (50,50))
    },
    "hongo verde": {
        "1hv": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/Hongo Verde/10_hv.png"), (50,50)),
        "2hv": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/Hongo Verde/20_hv.png"), (50,50)),
        "3hv": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/Hongo Verde/30_hv.png"), (50,50)),
        "4hv": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/Hongo Verde/40_hv.png"), (50,50))    
    },
    "estrella": {
        "1s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrella/10_starman.png"), (40,40)),
        "2s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrella/20_starman.png"), (40,40)),
        "3s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrella/30_starman.png"), (40,40)),
        "4s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrella/40_starman.png"), (40,40)),
        "5s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrella/50_starman.png"), (40,40))
    }
}

SOUNDEFFECTS = {
    "salto": pygame.mixer.Sound("Assets/soundeffects/soundjump/jump.wav"),
    "vida": pygame.mixer.Sound("Assets/soundeffects/soundpower/hv/518306__mrthenoronha__extra-life-8-bit.wav"),
    "gigante": pygame.mixer.Sound("Assets/soundeffects/soundpower/hr/647977__cloud-10__8-bit-coin-or-power-up-fx-for-retro-video-games.mp3")
}