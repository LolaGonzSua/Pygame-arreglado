import pygame
from constantes import *
from funciones import mostrar_texto

pygame.init()
fuente_boton = pygame.font.SysFont("Arial Narrow", 23)
boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_HEX)


def generar_imagen(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]):
    retorno = "reglas"

    fondo = pygame.image.load("Pygame profe\Assets\lasreglas.png")
    fondo = pygame.transform.scale(fondo, (pantalla.get_width(), pantalla.get_height()))  
    pantalla.blit(fondo, (0, 0)) 

    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
            
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                print("VOLVER AL MENU")
                CLICK_SONIDO.play()
                retorno = "menu"

    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"], (10, 10))
    mostrar_texto(boton_volver["superficie"], "VOLVER", (10, 10), fuente_boton, COLOR_BLANCO)


    pygame.display.update()

    return retorno