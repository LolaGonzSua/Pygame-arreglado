import pygame
from constantes import *
from funciones import mostrar_texto
from archivos import *


pygame.init()
fuente = pygame.font.SysFont("Arial Narrow", 32)
fuente_boton = pygame.font.SysFont("Arial Narrow", 23)
fuente_titulo = pygame.font.SysFont("Castellar", 40)


boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_HEX)



def ordenar_lista_ranking(lista_alementos: list) -> list:
    lista_alementos.sort(key=lambda jugador: jugador["puntaje"], reverse=True)
    return lista_alementos[:10]  # Solo los mejores 10

def mostrar_rankings(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event]):
    retorno = "rankings"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                print("VOLVER AL MENU")
                CLICK_SONIDO.play()
                retorno = "menu"
    

    fondo = pygame.image.load("Pygame profe\Assets\901095.jpeg")
    fondo = pygame.transform.scale(fondo, (pantalla.get_width(), pantalla.get_height()))  
    pantalla.blit(fondo, (0, 0))  

    texto_titulo = "Top 10"
    ancho_titulo = fuente.size(texto_titulo)[0]  
    x_titulo = (pantalla.get_width() - ancho_titulo) // 2  
    mostrar_texto(pantalla, texto_titulo, (x_titulo, 20), fuente_titulo, COLOR_BLANCO)  

    boton_volver["rectangulo"] = pantalla.blit(boton_volver["superficie"], (10, 10))
    mostrar_texto(boton_volver["superficie"], "VOLVER", (10, 10), fuente_boton, COLOR_BLANCO)

    lista_elementos = cargar_datos_jugadores_json("Datos jugadores.json")
    ordenar_lista_ranking(lista_elementos)

    y = 160

    if lista_elementos == []:
        mostrar_texto(pantalla, "NO SE REGISTRARON \nPARTIDAS", (100, 230), fuente, COLOR_NEGRO)
    else:
        for i in range(len(lista_elementos)):

            texto = f"{i + 1}. {lista_elementos[i]['nombre']}: {lista_elementos[i]['puntaje']}"
            

            ancho_texto = fuente.size(texto)[0]
            alto_texto = fuente.size(texto)[1]
            

            pygame.draw.rect(pantalla, COLOR_BLANCO, (170, y - 5, ancho_texto + 10, alto_texto + 10))  # El +10 es para darle algo de margen
            

            mostrar_texto(pantalla, texto, (175, y), fuente, COLOR_NEGRO)
            y += 45

    return retorno
