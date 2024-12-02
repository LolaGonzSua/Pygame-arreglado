import pygame
from constantes import *
from menu import *
from jugar import *
from configuracion import *
from rankings import *
from terminado import *
from intro import *
from reglas import *


#Configuraciones Basicas
pygame.init()
pygame.mixer.init()
pygame.display.set_caption("Preguntados")
icono = pygame.image.load("Pygame profe\Assets\IMG_4425 (1).jpeg")
pygame.display.set_icon(icono)
pantalla = pygame.display.set_mode(VENTANA)
corriendo = True
reloj = pygame.time.Clock()
datos_juego = {"puntuacion":0,"vidas":CANTIDAD_VIDAS,"nombre":"","volumen_musica":100,"volumen_sonidos":100,"comodin_x2": False}
ventana_actual = "video"
bandera_musica = False

#intro(pantalla)
pygame.mixer.quit()  # Reiniciamos el mixer al finalizar la intro
pygame.mixer.init()

while corriendo:
    reloj.tick(FPS)
    cola_eventos = pygame.event.get()
    if ventana_actual == "video":
        ventana_actual = mostrar_video(pantalla,cola_eventos)



    if ventana_actual == "menu":
        if bandera_musica == False:
            pygame.mixer.quit()
            pygame.mixer.init()
            porcentaje_volumen = datos_juego["volumen_musica"] / 100
            pygame.mixer.music.load("Pygame profe\Assets\The Rains of Castamere (Instrumental - Long Version)_L9SIS6wBxpI.mp3")
            pygame.mixer.music.play(-1)
            bandera_musica = True
        ventana_actual = mostrar_menu(pantalla,cola_eventos)
    elif ventana_actual == "juego":
        pygame.mixer.music.stop()
        #LATIDOS_SONIDO.play()
        if bandera_musica == False:
            porcentaje_volumen = datos_juego["volumen_musica"] / 100
            pygame.mixer.music.load("musica.mp3")
            pygame.mixer.music.set_volume(porcentaje_volumen)
            pygame.mixer.music.play(-1)
            bandera_musica = True
        ventana_actual = mostrar_juego(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "configuraciones":
        ventana_actual = mostrar_configuracion(pantalla,cola_eventos,datos_juego)
    elif ventana_actual == "rankings":
        ventana_actual = mostrar_rankings(pantalla,cola_eventos)
    elif ventana_actual == "terminado":
        #LATIDOS_SONIDO.stop()
        #DRACARYS_SONIDO.play()
        if bandera_musica == True:
            pygame.mixer.music.stop()
            bandera_musica = False
        ventana_actual = mostrar_fin_juego(pantalla,cola_eventos,datos_juego)

    elif ventana_actual == "reglas":
        ventana_actual = generar_imagen(pantalla,cola_eventos)
    
    elif ventana_actual == "salir":
        corriendo = False
    
    #Actualizar cambios
    pygame.display.flip()

pygame.quit()