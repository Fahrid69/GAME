import pygame, random
pygame.mixer.init()
## Se definen las variables que las cuales sus valores no van a modificarse

# VALORES DEL TAMAÑO DE LA VENTANA
ANCHO_VENTANA = 1380
ALTO_VENTANA = 720

# con esta modifica el suelo real del juego a los objetos
X = random.randint(100,ANCHO_VENTANA - 50)
Y = 640                               #640

## IMGS
FONDO = pygame.transform.scale(pygame.image.load("Assets/font/front.png"), (ANCHO_VENTANA, 91))

# DIRECTORIOS FIJOS
D_JUGADOR = "assets/sprites/player/Jugador/"
D_GOOMBA = "assets/sprites/enemy/Goomba/"
D_TURTLE = "assets/sprites/enemy/Turtle/"
D_PODERES = "assets/sprites/powers/"

# ESCALAS CORRESPONDIENTES A:
E_JUGADOR = (60,60)

# ALMACENAR LOS SPRITES:

SPRITES_GOOMBA = {
    "brown": {
        "caminar1": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}g1/10_goomba.png"), (50,50)),
        "caminar2": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}g1/11_goomba.png"), (50,50)),
        "muerto": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}g1/30_goomba.png"), (50,50))
    },
    "black": {
        "caminar1": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}g2/20_goomba.png"), (50,50)),
        "caminar2": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}g2/21_goomba.png"), (50,50)),
        "muerto": pygame.transform.scale(pygame.image.load(f"{D_GOOMBA}g2/30_goomba.png"), (50,50))
    }
}

SPRITES_TURTLE = {
    "turtle": {
        "01t": pygame.transform.scale(pygame.image.load(f"{D_TURTLE}10_turtle.png"),(50,50)),
        "02t": pygame.transform.scale(pygame.image.load(f"{D_TURTLE}11_turtle.png"),(50,50)),
        "03t": pygame.transform.scale(pygame.image.load(f"{D_TURTLE}12_turtle.png"),(50,50)),
        "04t": pygame.transform.scale(pygame.image.load(f"{D_TURTLE}13_turtle.png"),(50,50)),
        "00t": pygame.transform.scale(pygame.image.load(f"{D_TURTLE}dead_turtle.png"),(50,50))
    }
}

SPRITES_PODERES = {
    "hongo rojo": {
        "1hr": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/hr/10_hr.png"), (50,50)),
        "2hr": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/hr/11_hr.png"), (50,50)),
        "3hr": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/hr/12_hr.png"), (50,50)),
        "4hr": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/hr/13_hr.png"), (50,50))
    },
    "hongo verde": {
        "1hv": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/hv/10_hv.png"), (50,50)),
        "2hv": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/hv/11_hv.png"), (50,50)),
        "3hv": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/hv/12_hv.png"), (50,50)),
        "4hv": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Hongos/hv/13_hv.png"), (50,50))    
    },
    "estrella": {
        "1s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrella/10_starman.png"), (40,40)),
        "2s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrella/11_starman.png"), (40,40)),
        "3s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrella/12_starman.png"), (40,40)),
        "4s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrella/13_starman.png"), (40,40)),
        "5s": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Estrella/14_starman.png"), (40,40))
    },
    "coin": {
        "1c": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Moneda/10_coin.png"), (40, 40)),
        "2c": pygame.transform.scale(pygame.image.load(f"{D_PODERES}Moneda/11_coin.png"), (40, 40)),
        "3c": pygame.transform.scale(pygame.image.load(f"{D_PODERES}/Moneda/12_coin.png"), (40, 40)),
        "4c": pygame.transform.scale(pygame.image.load(f"{D_PODERES}/Moneda/13_coin.png"), (40, 40))
    }
}

SOUNDEFFECTS = {
    "salto": pygame.mixer.Sound("assets/soundeffects/soundjump/jump.wav"),
    "star": pygame.mixer.Sound("assets/soundeffects/soundpower/star/22-star-power-restored-101soundboards (mp3cut.net).wav"),
    "daño": pygame.mixer.Sound("assets/soundeffects/soundamage/385046__mortisblack__damage.ogg"),
    "daño1": pygame.mixer.Sound("assets/soundeffects/soundamage/753607__etheraudio__retro-hit-eight-bit.wav"),
    "daño2": pygame.mixer.Sound("assets/soundeffects/soundamage/406113_daleonfire_dead-8bit (mp3cut.net).wav"),
    "coin": pygame.mixer.Sound("assets/soundeffects/soundcoins/242857__plasterbrain__coin-get - copia.wav"),
    "vida": pygame.mixer.Sound("assets/soundeffects/soundpower/hv/518306__mrthenoronha__extra-life-8-bit.wav"),
    "gigante": pygame.mixer.Sound("assets/soundeffects/soundpower/hr/647977__cloud-10__8-bit-coin-or-power-up-fx-for-retro-video-games.mp3"),
    "GAMEOVER": pygame.mixer.Sound("assets/soundeffects/soundtrack/game-over-deep-male-voice-clip-352695.mp3")
}