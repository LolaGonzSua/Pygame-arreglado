import csv
import json
import os 
from preguntas import *
from datetime import datetime

def guardar_preguntas_csv(path: str, lista: list):
    archivo = open(path, "w", newline= "", encoding= "utf-8")
    archivo.write("Pregunta,Respuesta 1,Respuesta 2,Respuesta 3,Respuesta 4,Respuesta Correcta\n")
    
    for pregunta in lista:
        linea = f'"{pregunta["pregunta"]}",' \
                f'"{pregunta["respuesta_1"]}",' \
                f'"{pregunta["respuesta_2"]}",' \
                f'"{pregunta["respuesta_3"]}",' \
                f'"{pregunta["respuesta_4"]}",' \
                f'{pregunta["respuesta_correcta"]}\n'
        archivo.write(linea)
    archivo.close()
       
guardar_preguntas_csv("preguntas.csv", lista_preguntas)

# Guardar los datos del jugador en un archivo JSON
def guardar_datos_jugador_json(nombre_archivo: str, nombre: str, puntaje: int):
    # Crear o leer el archivo JSON existente
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo_json:
            lista_jugadores = json.load(archivo_json)
    else:
        lista_jugadores = []

    # Obtener la fecha actual
    fecha_actual = datetime.now().strftime("%d/%m/%Y")

    # Crear el nuevo registro del jugador
    nuevo_jugador = {
        "nombre": nombre,
        "puntaje": puntaje,
        "fecha": fecha_actual
    }

    # Añadir el nuevo jugador
    lista_jugadores.append(nuevo_jugador)

    # Guardar el archivo actualizado
    with open(nombre_archivo, "w") as archivo_json:
        json.dump(lista_jugadores, archivo_json, indent=4, ensure_ascii=False)

    print(f"Datos guardados: {nombre} con {puntaje} puntos.")

# Función para cargar los datos de los jugadores desde el archivo JSON
def cargar_datos_jugadores_json(nombre_archivo: str) -> list:
    if os.path.exists(nombre_archivo):
        with open(nombre_archivo, "r") as archivo_json:
            lista_jugadores = json.load(archivo_json)
        return lista_jugadores
    else:
        return []  # Si el archivo no existe, retornar lista vacía
