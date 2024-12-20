import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta = 'D:\\Cursos\\Python2\\pythonProject\\Dia_9\\Mi_Gran_Directorio'

patron = r'N\D{3}-\d{5}'

hoy = datetime.date.today()
numeros = []

archivos = []

def buscar_numero(archivo, patron):
    archivo = open(archivo, 'r')
    text = archivo.read()
    if re.search(patron, text):
        return re.search(patron, text)
    else:
        return ''

def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta):
        for a in archivo:
            resultado = buscar_numero(Path(carpeta,a), patron)
            if resultado != '':
                numeros.append((resultado.group()))
                archivos.append(a.title())

def mostrar_todo():
    indice = 0
    print(f'Fecha de Búsqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('ARCHIVO\t\t\tNRO. SERIE')
    for a in archivos:
        print(f'{a}\t{numeros[indice]}')
        indice += 1
    print('\n')
    print(f'Números encotrados: {len(numeros)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duración de la búsqueda: {math.ceil(duracion)} segundos')

crear_listas()
mostrar_todo()


