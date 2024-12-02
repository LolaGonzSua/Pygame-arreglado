import pygame
pygame.init()

COLOR_BLANCO = (255,255,255)
COLOR_NEGRO = (0,0,0)
COLOR_VERDE = (0,255,0)
COLOR_ROJO = (255,0,0)
COLOR_AZUL = (0,0,255)
COLOR_VIOLETA = (134,23,219)
COLOR_HEX = (152,175,190)
COLOR_SAN_JUAN = (71,97,100)
COLOR_KOBE = (136,40,27)
COLOR_CIE = (184,168,152)
COLOR_CIAN = (95,115,121)


ANCHO = 1000
ALTO = 600
VENTANA = (ANCHO,ALTO)
FPS = 60

BOTON_JUGAR = 0
BOTON_CONFIG = 1
BOTON_PUNTUACIONES = 2
BOTON_REGLAS = 3
BOTON_SALIR = 4

TAMAÑO_PREGUNTA = (350,150)
TAMAÑO_RESPUESTA = (250,60)
TAMAÑO_BOTON = (290,50)
CUADRO_TEXTO = (250,50)
TAMAÑO_BOTON_VOLVER = (100,40)
TAMAÑO_BOTON_MUTE = (80,45)
TAMAÑO_BOTON_MAX = (80,45)
TAMAÑO_BOTON_PASAR = (90,40)
TAMAÑO_BOTON_X2 = (90,40)
GAME_OVER = (200,40)
CLICK_SONIDO = pygame.mixer.Sound("Pygame profe\Assets\casual-click-pop-ui-2-262119.mp3")
ERROR_SONIDO = pygame.mixer.Sound("Pygame profe\Assets\casual-click-pop-ui-2-262119.mp3")
LATIDOS_SONIDO = pygame.mixer.Sound("Pygame profe\Assets\heartbeat-sound-effects-for-you-122458.mp3")
DRACARYS_SONIDO = pygame.mixer.Sound("Pygame profe\Assets\Project-Dracarys.mp3")

CANTIDAD_VIDAS = 3
PUNTUACION_ACIERTO = 100
PUNTUACION_ERROR = 25