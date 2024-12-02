import pygame
from constantes import *
from funciones import mostrar_texto
from archivos import * 
from datetime import datetime



fuente = pygame.font.SysFont("qatar-2022-book",40)
cuadro = {}
cuadro["superficie"] = pygame.Surface(CUADRO_TEXTO)
cuadro["rectangulo"] = cuadro["superficie"].get_rect()
cuadro['superficie'].fill(COLOR_AZUL)
nombre = ""

pygame.init()

fuente = pygame.font.SysFont("Arial Narrow",30)

fondo = pygame.image.load("Pygame profe\Assets\IMG_4567.webp")
fondo = pygame.transform.scale(fondo,VENTANA)

cuadro = {}
cuadro["superficie"] = pygame.Surface(CUADRO_TEXTO)
cuadro["rectangulo"] = cuadro["superficie"].get_rect()
cuadro['superficie'].fill(COLOR_SAN_JUAN)
boton_game_over = {}
boton_game_over["superficie"] = pygame.Surface(GAME_OVER)
boton_game_over["rectangulo"] = boton_game_over["superficie"].get_rect()
boton_game_over["superficie"].fill(COLOR_SAN_JUAN)
nombre = ""

def mostrar_fin_juego(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global nombre
    retorno = "terminado"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            #Estaria bueno forzarle al usuario que no pueda salir del juego hasta que guarde la puntuacion -> A gusto de ustedes
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_game_over["rectangulo"].collidepoint(evento.pos):
                retorno = "menu"  
                CLICK_SONIDO.play()            
        elif evento.type == pygame.KEYDOWN:
            bloc_mayus = pygame.key.get_mods() and pygame.KMOD_CAPS
            letra_presionada = pygame.key.name(evento.key)
            
            if letra_presionada == "backspace" and len(nombre) > 0:
                nombre = nombre[0:-1]#Elimino el ultimo
                cuadro["superficie"].fill(COLOR_KOBE)
            
            if letra_presionada == "space":
                nombre += " "
            
            if len(letra_presionada) == 1:  
                if bloc_mayus != 0:
                    nombre += letra_presionada.upper()
                else:
                    nombre += letra_presionada

            if (letra_presionada == "return") and (len(nombre) > 0):
                    guardar_datos_jugador_json("Datos jugadores.json",nombre,datos_juego["puntuacion"])
                    cuadro['superficie'].fill(COLOR_BLANCO)
                    nombre = ""
                    retorno = "menu"

        
        
    pantalla.blit(fondo,(0,0))

    cuadro["rectangulo"] = pantalla.blit(cuadro["superficie"],(363,290))
    boton_game_over["rectangulo"] = pantalla.blit(boton_game_over['superficie'],(390,490))

    mostrar_texto(cuadro["superficie"],nombre,(10,0),fuente,COLOR_BLANCO)
    mostrar_texto(boton_game_over["superficie"],"GAME OVER",(10,10),fuente, COLOR_BLANCO)
    mostrar_texto(pantalla,f"Obtuvo: {datos_juego['puntuacion']} puntos",(398,235),fuente,COLOR_BLANCO)
    
    return retorno