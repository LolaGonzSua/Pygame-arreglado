import pygame
from constantes import *
from archivos import *
from funciones import *

pygame.init()

# Carga y escala de la imagen de las vidas
vida_imagen = pygame.image.load("Pygame profe\Assets\lasvidas.png") 
vida_imagen = pygame.transform.scale(vida_imagen, (30, 30))

cuadro_pregunta = {}
cuadro_pregunta["superficie"] = pygame.Surface(TAMAÑO_PREGUNTA)
cuadro_pregunta["rectangulo"] = cuadro_pregunta["superficie"].get_rect()

cartas_respuestas = []
for i in range(4):
    cuadro_respuesta = {}
    cuadro_respuesta["superficie"] = pygame.Surface(TAMAÑO_RESPUESTA)
    cuadro_respuesta["rectangulo"] = cuadro_respuesta["superficie"].get_rect()
    cartas_respuestas.append(cuadro_respuesta)

fuente_pregunta = pygame.font.SysFont("Arial Narrow", 30)
fuente_respuesta = pygame.font.SysFont("Arial Narrow", 23)
fuente_texto = pygame.font.SysFont("Arial Narrow", 25)
fuentes = pygame.font.SysFont("Arial Narrow", 23)

fondo = pygame.image.load("Pygame profe\Assets\IMG_4557.jpeg")
fondo = pygame.transform.scale(fondo,VENTANA)

boton_pasar = {}
boton_pasar["superficie"] = pygame.Surface(TAMAÑO_BOTON_PASAR)
boton_pasar["rectangulo"] = boton_pasar["superficie"].get_rect()
boton_pasar["superficie"].fill(COLOR_CIAN)
boton_x2 = {}
boton_x2["superficie"] = pygame.Surface(TAMAÑO_BOTON_X2)
boton_x2["rectangulo"] = boton_x2["superficie"].get_rect()
boton_x2["superficie"].fill(COLOR_CIAN)
boton_volver = {}
boton_volver["superficie"] = pygame.Surface(TAMAÑO_BOTON_VOLVER)
boton_volver["rectangulo"] = boton_volver["superficie"].get_rect()
boton_volver["superficie"].fill(COLOR_HEX)

mezclar_lista(lista_preguntas)
indice = 0
bandera_respuesta = False
correctas_consecutivas = 0
tiempo_restante_segundos = 30  # 30 segundos
TIEMPO_EXTRA = 15  # 15 segundos extra

# Temporizador
ultimo_tiempo = pygame.time.get_ticks()
comodin_pasar = 1


def mostrar_juego(pantalla: pygame.Surface, cola_eventos: list[pygame.event.Event], datos_juego: dict) -> str:
    global indice, bandera_respuesta, correctas_consecutivas, tiempo_restante_segundos, ultimo_tiempo, comodin_pasar
    
    retorno = "juego"
    
    # Actualiza el cronómetro cada segundo
    tiempo_actual = pygame.time.get_ticks()
    if tiempo_actual - ultimo_tiempo >= 1000:  # Si pasó 1 segundo
        ultimo_tiempo = tiempo_actual
        if tiempo_restante_segundos > 0:
            tiempo_restante_segundos -= 1

        # Si no hay vidas, el juego termina
        if datos_juego["vidas"] == 0:
            bandera_respuesta = False
            retorno = "terminado"

    cuadro_pregunta["superficie"].fill(COLOR_CIAN)
    for carta in cartas_respuestas:
        carta["superficie"].fill(COLOR_HEX)
    
    if bandera_respuesta:
        pygame.time.delay(500)
        bandera_respuesta = False
    
    pregunta_actual = lista_preguntas[indice]
    
    for evento in cola_eventos:
        if evento.type == pygame.QUIT:
            retorno = "salir"
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(cartas_respuestas)):
                if cartas_respuestas[i]['rectangulo'].collidepoint(evento.pos):
                    respuesta_usuario = (i + 1)
                    
                    if verificar_respuesta(datos_juego, pregunta_actual, respuesta_usuario):
                        CLICK_SONIDO.play()
                        cartas_respuestas[i]['superficie'].fill(COLOR_VERDE)
                        print("RESPUESTA CORRECTA")
                        
                        correctas_consecutivas += 1
                        if correctas_consecutivas == 5:
                            tiempo_restante_segundos += TIEMPO_EXTRA  # En caso de que las respuestas consecutivas correctas sean 5, se añaden 15 segundos extras.
                            print("¡15 SEGUNDOS EXTRA!")
                            correctas_consecutivas = 0  # Resetea el contador de respuestas correctas consecutivas
                    else:
                        ERROR_SONIDO.play()
                        cartas_respuestas[i]['superficie'].fill(COLOR_ROJO)
                        print("RESPUESTA INCORRECTA")
                        
                        # Resta una vida y sigue jugando si hay vidas restantes
                        datos_juego["vidas"] - 1
                        if datos_juego["vidas"] > 0:
                            # No termina el juego, se vuelve a la siguiente pregunta
                            indice += 1
                        else:
                            retorno = "terminado"
                            bandera_respuesta = False
                        
                        correctas_consecutivas = 0
                    
                    print(f"SE HIZO CLICK EN UNA RESPUESTA {respuesta_usuario}")
                    bandera_respuesta = True

                    if indice == len(lista_preguntas):
                        indice = 0
                        mezclar_lista(lista_preguntas)
                    indice += 1
                if boton_pasar["rectangulo"].collidepoint(evento.pos) and comodin_pasar < 3:
                    CLICK_SONIDO.play()
                    comodin_pasar += 1  
                    indice += 1  
                    if indice == len(lista_preguntas):
                        indice = 0
                        mezclar_lista(lista_preguntas)
                    print(f"Comodines restantes: {comodin_pasar}")
                # Comodín X2: 
                if boton_x2["rectangulo"].collidepoint(evento.pos):
                    if not datos_juego["comodin_x2"]:  
                        CLICK_SONIDO.play()
                        datos_juego["comodin_x2"] = True  
                        print("COMODÍN X2 ACTIVADO")
    
    # En caso de que haya terminado la partida, que se reinicie el temporizador -> Bug arreglado.
    if retorno == "terminado":
        tiempo_restante_segundos = 30  # Reiniciar el tiempo a 30 segundos
        ultimo_tiempo = pygame.time.get_ticks()  # Reiniciar el tiempo de referencia del cronómetro

    pantalla.blit(fondo,(0,0))

    mostrar_texto(cuadro_pregunta["superficie"], f"{pregunta_actual['pregunta']}", (20, 20), fuente_pregunta, COLOR_BLANCO)
    mostrar_texto(cartas_respuestas[0]["superficie"], f"{pregunta_actual['respuesta_1']}", (20, 20), fuentes, COLOR_BLANCO)
    mostrar_texto(cartas_respuestas[1]["superficie"], f"{pregunta_actual['respuesta_2']}", (20, 20), fuentes, COLOR_BLANCO)
    mostrar_texto(cartas_respuestas[2]["superficie"], f"{pregunta_actual['respuesta_3']}", (20, 20), fuentes, COLOR_BLANCO)
    mostrar_texto(cartas_respuestas[3]["superficie"], f"{pregunta_actual['respuesta_4']}", (20, 20), fuentes, COLOR_BLANCO)
    mostrar_texto(boton_volver["superficie"],"VOLVER",(10,10),fuentes,COLOR_BLANCO)
    mostrar_texto(boton_pasar["superficie"],"PASAR",(10,10),fuentes, COLOR_BLANCO)
    mostrar_texto(boton_x2["superficie"],"X2",(10,10),fuentes, COLOR_BLANCO)

    pantalla.blit(cuadro_pregunta["superficie"], (320, 80))
    cartas_respuestas[0]['rectangulo'] = pantalla.blit(cartas_respuestas[0]['superficie'], (365, 300))
    cartas_respuestas[1]['rectangulo'] = pantalla.blit(cartas_respuestas[1]['superficie'], (365, 370))
    cartas_respuestas[2]['rectangulo'] = pantalla.blit(cartas_respuestas[2]['superficie'], (365, 440))
    cartas_respuestas[3]['rectangulo'] = pantalla.blit(cartas_respuestas[3]['superficie'], (365, 510))
    boton_volver["rectangulo"] = pantalla.blit(boton_volver['superficie'],(10,10))
    boton_pasar["rectangulo"] = pantalla.blit(boton_pasar['superficie'],(350,230))
    boton_x2["rectangulo"] = pantalla.blit(boton_x2['superficie'],(545,230))  
    
    mostrar_texto(pantalla, f"PUNTUACION: {datos_juego['puntuacion']}", (350, 10), fuentes, COLOR_BLANCO)

    # Para mostrar las vidas como imágenes
    for i in range(datos_juego["vidas"]):
        pantalla.blit(vida_imagen, (550 + i * 35, 10))

    # Muestra el tiempo como minutos.
    minutos = tiempo_restante_segundos // 60
    segundos = tiempo_restante_segundos % 60
    mostrar_texto(pantalla, f"TIEMPO: {minutos:02}:{segundos:02}", (435, 60), fuentes, COLOR_BLANCO)

    return retorno



