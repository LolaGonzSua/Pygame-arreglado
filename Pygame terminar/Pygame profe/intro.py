import pygame
from pyvidplayer import Video
from constantes import *
import time
vid = Video("Pygame profe\Assets\copy_A9845392-64B4-4288-BAD0-3509B3B62BE3 (1).mp4")
vid.set_size((1000, 600))

def mostrar_video(pantalla,cola_eventos):
    """
    Reproduce el video de introducción y luego pasa al menú.
    """
    #vid = Video("Pygame profe\Assets\copy_A9845392-64B4-4288-BAD0-3509B3B62BE3 (1).mp4")
    #vid.set_size((1000, 600))
    retorno = "video"

    # Reproducir el video de introducción
    pantalla.fill((0, 0, 0))
    vid.draw(pantalla, (0, 0))  # Dibuja el video en la ventana
    pygame.display.update()
        
    for event in cola_eventos:
        if event.type == pygame.QUIT:
            pygame.quit()
            return
        if event.type == pygame.MOUSEBUTTONDOWN:
            vid.restart()  # Si el usuario hace clic, reiniciar el video
            return  # Ir directamente al juego

        # Verificar si el video ha terminado
    if not vid.active:
        vid.close()
        retorno = "menu"  

    return retorno





def intro(pantalla):
    """
    Reproduce el video de introducción y luego pasa al menú.
    """
    vid = Video("Pygame profe\Assets\copy_A9845392-64B4-4288-BAD0-3509B3B62BE3 (1).mp4")
    vid.set_size((1000, 600))

    # Reproducir el video de introducción
    while vid.active:
        pantalla.fill((0, 0, 0))
        vid.draw(pantalla, (0, 0))  # Dibuja el video en la ventana
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.MOUSEBUTTONDOWN:
                vid.restart()  # Si el usuario hace clic, reiniciar el video
                return  # Ir directamente al juego

        # Verificar si el video ha terminado
        if not vid.active:
            break  # Video terminado, pasar al juego

    vid.close()
    # time.sleep(0.1)
    # pygame.mixer.quit()  # Cerrar el sistema de audio
    # pygame.mixer.init()  # Volver a inicializarlo para asegurarse de que esté listo

    # pygame.mixer.music.load("Pygame profe\Assets\The Rains of Castamere (Instrumental - Long Version)_L9SIS6wBxpI.mp3")
    # pygame.mixer.music.play(-1)
    return "menu"  # Después de terminar el video, regresamos al menú