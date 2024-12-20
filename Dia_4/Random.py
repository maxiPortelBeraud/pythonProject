"""Importando random"""
from random import randint, uniform, random, choice, shuffle

integer_aleatorio = randint(1, 50)

uniform_aleatorio = round(uniform(1, 5), 1)

aleatorio = round(random(), 2)

colores = ["azul", "amarillo", "verde"]
color_aleatorio = choice(colores)

numeros_aleatorios = list(range(5, 50, 5))
shuffle(numeros_aleatorios)

print(numeros_aleatorios)
