import pygame
from constantes import *
from funciones import mostrar_texto

pygame.init()
fuente_menu = pygame.font.SysFont("Pygame profe\Assets\Game of Thrones.ttf", 30)

# Tamaño de los botones modificado
TAMAÑO_BOTON = (300, 60)

lista_botones = []

for i in range(5):
    boton = {}
    boton["superficie"] = pygame.Surface(TAMAÑO_BOTON)
    boton["superficie"].fill(COLOR_HEX)
    boton["rectangulo"] = boton["superficie"].get_rect()
    lista_botones.append(boton)

fondo = pygame.image.load("Pygame profe\Assets\IMG_4484.jpeg")
fondo = pygame.transform.scale(fondo, VENTANA)

def mostrar_menu(pantalla:pygame.Surface, cola_eventos:list[pygame.event.Event]) -> str:
    # Gestionar eventos:
    retorno = "menu"
    for evento in cola_eventos:
        if evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(lista_botones)): 
                if lista_botones[i]["rectangulo"].collidepoint(evento.pos):
                    CLICK_SONIDO.play()
                    if i == BOTON_SALIR:
                        retorno = "salir"  
                    elif i == BOTON_JUGAR:
                        retorno = "juego"  
                    elif i == BOTON_PUNTUACIONES:
                        retorno = "rankings"
                    elif i == BOTON_CONFIG:
                        retorno = "configuraciones"
                    elif i == BOTON_REGLAS:
                        retorno = "reglas"
                        
        elif evento.type == pygame.QUIT:
            retorno = "salir"
                
    
    pantalla.blit(fondo, (0, 0))


    lista_botones[0]["rectangulo"] = pantalla.blit(lista_botones[0]["superficie"], (365, 190))
    lista_botones[1]["rectangulo"] = pantalla.blit(lista_botones[1]["superficie"], (365, 270))  
    lista_botones[2]["rectangulo"] = pantalla.blit(lista_botones[2]["superficie"], (365, 350))  
    lista_botones[3]["rectangulo"] = pantalla.blit(lista_botones[3]["superficie"], (365, 430)) 
    lista_botones[4]["rectangulo"] = pantalla.blit(lista_botones[4]["superficie"], (365, 510))  
    

    mostrar_texto(lista_botones[0]["superficie"], "JUGAR", (100, 15), fuente_menu, COLOR_BLANCO)
    mostrar_texto(lista_botones[1]["superficie"], "CONFIGURACION", (50, 15), fuente_menu, COLOR_BLANCO)
    mostrar_texto(lista_botones[2]["superficie"], "PUNTUACIONES", (57, 15), fuente_menu, COLOR_BLANCO)
    mostrar_texto(lista_botones[3]["superficie"], "REGLAS", (100, 15), fuente_menu, COLOR_BLANCO)
    mostrar_texto(lista_botones[4]["superficie"], "SALIR", (100, 15), fuente_menu, COLOR_BLANCO)
    
    return retorno
