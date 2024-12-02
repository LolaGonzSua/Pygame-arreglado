import pygame
from constantes import *
from funciones import mostrar_texto

pygame.init()

fuente_botones = pygame.font.SysFont("Arial Narrow",23)
fuente_volumen = pygame.font.SysFont("Arial Narrow",33)

fondo = pygame.image.load("Pygame profe\Assets\IMG_4425 (1).jpeg")
fondo = pygame.transform.scale(fondo,VENTANA)

boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_HEX)
boton_mute = {}
boton_mute["superficie"] = pygame.Surface(TAMAÑO_BOTON_MUTE)
boton_mute["rectangulo"] = boton_mute["superficie"].get_rect()
boton_mute["superficie"].fill(COLOR_SAN_JUAN)
boton_max = {}
boton_max["superficie"] = pygame.Surface(TAMAÑO_BOTON_MAX)
boton_max["rectangulo"] = boton_max["superficie"].get_rect()
boton_max["superficie"].fill(COLOR_SAN_JUAN)  

#Barra de volumen
barra_musica = pygame.Rect(250, 235, 500, 10) 
control_musica = pygame.Rect(250 + int(490 * (100 / 100)), 235 - 5, 10, 20)  
barra_sonidos = pygame.Rect(250, 360, 500, 10) 
control_sonidos = pygame.Rect(250 + int(490 * (100 / 100)), 360 - 5, 10, 20)  

arrastrando_musica = False
arrastrando_sonidos = False

def mostrar_configuracion(pantalla:pygame.Surface,cola_eventos:list[pygame.event.Event],datos_juego:dict) -> str:
    global arrastrando_musica,arrastrando_sonidos
    retorno = "configuraciones"
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        if evento.type == pygame.MOUSEBUTTONDOWN:
            if boton_volver["rectangulo"].collidepoint(evento.pos):
                print("VOLVER AL MENU")
                CLICK_SONIDO.play()
                retorno = "menu"
            elif barra_musica.collidepoint(evento.pos): 
                arrastrando_musica = True
                control_musica.x = evento.pos[0] - control_musica.width // 2
                # Limitar la posición dentro de la barra de volumen
                if control_musica.x < barra_musica.left:
                    control_musica.x = barra_musica.left
                elif control_musica.x > barra_musica.right - control_musica.width:
                    control_musica.x = barra_musica.right - control_musica.width
                
                datos_juego["volumen_musica"] = (control_musica.x - barra_musica.x) * 100 // (barra_musica.width - control_musica.width)
                pygame.mixer.music.set_volume(datos_juego["volumen_musica"] / 100)

            elif barra_sonidos.collidepoint(evento.pos):  
                arrastrando_sonidos = True
                control_sonidos.x = evento.pos[0] - control_sonidos.width // 2
                if control_sonidos.x < barra_sonidos.left:
                    control_sonidos.x = barra_sonidos.left
                elif control_sonidos.x > barra_sonidos.right - control_sonidos.width:
                    control_sonidos.x = barra_sonidos.right - control_sonidos.width
                
                datos_juego["volumen_sonidos"] = (control_sonidos.x - barra_sonidos.x) * 100 // (barra_sonidos.width - control_sonidos.width)
                CLICK_SONIDO.set_volume(datos_juego["volumen_sonidos"] / 100)

            elif boton_mute["rectangulo"].collidepoint(evento.pos): 
                if datos_juego["volumen_musica"] != 0:
                    datos_juego["volumen_musica"] = 0
                    datos_juego["volumen_sonidos"] = 0  
                    pygame.mixer.music.set_volume(0)  
                    CLICK_SONIDO.set_volume(0) 
            elif boton_max["rectangulo"].collidepoint(evento.pos): 
                datos_juego["volumen_musica"] = 100
                datos_juego["volumen_sonidos"] = 100
                pygame.mixer.music.set_volume(1) 
                CLICK_SONIDO.set_volume(1)  

        elif evento.type == pygame.MOUSEBUTTONUP: #El mousebuttonup es para cuando el mouse se deja de apretar, se suelta
            arrastrando_musica = False  
            arrastrando_sonidos = False

        elif evento.type == pygame.MOUSEMOTION: #El mousemotion es para que el mouse se mueva por la pantalla (el control)
            if arrastrando_musica:  
                control_musica.x = evento.pos[0] - control_musica.width // 2
                if control_musica.x < barra_musica.left:
                    control_musica.x = barra_musica.left
                elif control_musica.x > barra_musica.right - control_musica.width:
                    control_musica.x = barra_musica.right - control_musica.width
                datos_juego["volumen_musica"] = (control_musica.x - barra_musica.x) * 100 // (barra_musica.width - control_musica.width)
                pygame.mixer.music.set_volume(datos_juego["volumen_musica"] / 100)

            elif arrastrando_sonidos: 
                control_sonidos.x = evento.pos[0] - control_sonidos.width // 2
                if control_sonidos.x < barra_sonidos.left:
                    control_sonidos.x = barra_sonidos.left
                elif control_sonidos.x > barra_sonidos.right - control_sonidos.width:
                    control_sonidos.x = barra_sonidos.right - control_sonidos.width
                datos_juego["volumen_sonidos"] = (control_sonidos.x - barra_sonidos.x) * 100 // (barra_sonidos.width - control_sonidos.width)
                CLICK_SONIDO.set_volume(datos_juego["volumen_sonidos"] / 100)
                
    pantalla.blit(fondo,(0,0))
    
    boton_volver["rectangulo"] = pantalla.blit(boton_volver['superficie'],(10,10))
    boton_mute["rectangulo"] = pantalla.blit(boton_mute['superficie'],(350,430))
    boton_max["rectangulo"] = pantalla.blit(boton_max['superficie'],(550,430))

    # Barra 
    pygame.draw.rect(pantalla, COLOR_BLANCO, barra_musica, 2)
    pygame.draw.rect(pantalla, COLOR_VERDE, control_musica)
    pygame.draw.rect(pantalla, COLOR_BLANCO, barra_sonidos, 2)
    pygame.draw.rect(pantalla, COLOR_AZUL, control_sonidos)
    
    mostrar_texto(boton_volver["superficie"],"VOLVER",(10,10),fuente_botones,COLOR_BLANCO)
    mostrar_texto(boton_mute["superficie"],"MUTE",(10,10),fuente_botones, COLOR_BLANCO)
    mostrar_texto(boton_max["superficie"],"MAX",(10,10),fuente_botones, COLOR_BLANCO)

    mostrar_texto(pantalla, f"{datos_juego['volumen_musica']} %", (180, 230), fuente_volumen, COLOR_BLANCO)
    mostrar_texto(pantalla, f"{datos_juego['volumen_sonidos']} %", (180, 355), fuente_volumen, COLOR_BLANCO)

    return retorno
                