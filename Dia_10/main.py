import math
import pygame
import random
from pygame import mixer

# Inicializar Pygame
pygame.init()

# Imagen fondo
fondo = pygame.image.load("Fondo.jpg")

# Crear pantalla
pantalla = pygame.display.set_mode((800, 600))

# Titulo e Icono
pygame.display.set_caption("Invasión")
icono = pygame.image.load("rocket.png")
pygame.display.set_icon(icono)

# Agregar música
mixer.music.load("musica_fondo.mp3")
mixer.music.set_volume(0.1)
mixer.music.play(-1)

# Variables del Jugador
jugador_img = pygame.image.load("spaceship.png")
jugador_x = 368  # tamaño de pantalla - tamaño de imagen
jugador_y = 500
jugador_x_cambio = 0

enemigo_img = []
enemigo_x = []
enemigo_y = []
enemigo_x_cambio = []
enemigo_y_cambio = []
cantidad_enemigos = 8

# Variables del Enemigo
for e in range(cantidad_enemigos):
    enemigo_img.append(pygame.image.load("ufo.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    enemigo_x_cambio.append(0.2)
    enemigo_y_cambio.append(30)

# Variables del disparo
disparo_img = pygame.image.load("minus.png")
disparo_x = 0
disparo_y = 500
disparo_x_cambio = 0
disparo_y_cambio = 0.5
disparo_visible = False

# Puntaje
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 20)
texto_x = 10
texto_y = 10

# Texto final del juego
fuente_texto_final = pygame.font.Font('freesansbold.ttf', 40)


def texto_final():
    mi_fuente_final = fuente_texto_final.render("GAME OVER", True, (250, 250, 250))
    pantalla.blit(mi_fuente_final, (300, 300))


# Función mostrar puntaje
def mostrar_puntaje(x, y):
    texto = fuente.render(f"Puntaje: {puntaje}", True, (250, 250, 250))
    pantalla.blit(texto, (x, y))


# Función jugador
def jugador(x, y):
    pantalla.blit(jugador_img, (x, y))


# Función enemígo
def enemigo(x, y, enemigo):
    pantalla.blit(enemigo_img[enemigo], (x, y))


# Función disparar
def disparar(x, y):
    global disparo_visible
    disparo_visible = True
    pantalla.blit(disparo_img, (x + 16, y + 10))


# Función detectar colisiones
def hay_colisiones(x1, y1, x2, y2):
    distancia = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distancia < 27:
        return True
    else:
        return False


# Loop del juego
se_ejecuta = True
while se_ejecuta:

    pantalla.blit(fondo, (0, 0))  # RGB

    # Iterar eventos
    for evento in pygame.event.get():
        # Evento cerrar
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        # Evento presionar teclas
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                jugador_x_cambio = -0.3
            if evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0.3
            if evento.key == pygame.K_SPACE:
                sonido_disparo = mixer.Sound("disparo.mp3")
                if not disparo_visible:
                    disparo_x = jugador_x
                    disparar(disparo_x, disparo_y)
                    sonido_disparo.play()

        # Evento soltar flechas
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugador_x_cambio = 0

    # Modificar ubicación del jugador
    jugador_x += jugador_x_cambio

    # Mantener dentro de bordes al jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # Modificar ubicación del enemigo
    for e in range(cantidad_enemigos):
        # Fin del juego
        if enemigo_y[e] > 450:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[e] += enemigo_x_cambio[e]

        # Mantener dentro de bordes al enemigo
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e] = 0.2
            enemigo_y[e] += enemigo_y_cambio[e]
        elif enemigo_x[e] >= 736:
            enemigo_x_cambio[e] = -0.2
            enemigo_y[e] += enemigo_y_cambio[e]

        # colisión
        colision = hay_colisiones(enemigo_x[e], enemigo_y[e], disparo_x, disparo_y)
        if colision:
            sonido_colision = mixer.Sound("impacto-.mp3")
            sonido_colision.play()
            disparo_y = 500
            disparo_visible = False
            puntaje += 1
            enemigo_x[e] = random.randint(0, 736)
            enemigo_y[e] = random.randint(50, 200)

        enemigo(enemigo_x[e], enemigo_y[e], e)

    # Movimiento disparo
    if disparo_y <= -64:
        disparo_y = 500
        disparo_visible = False

    if disparo_visible:
        disparar(disparo_x, disparo_y)
        disparo_y -= disparo_y_cambio

    jugador(jugador_x, jugador_y)

    mostrar_puntaje(texto_x, texto_y)
    # Actualizar
    pygame.display.update()
