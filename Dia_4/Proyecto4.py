from random import randint

name = input("Bienvenido, cual es tu nombre?: ")
intento: int = 0
eleccion: int = 0
numero_aleatorio: int = randint(1, 100)

while intento < 8:
    if intento == 0:
        eleccion = int(input(f"{name} elegí entre 1 y 100. Hay 8 intentos: "))
    else:
        if eleccion not in range(1, 101):
            print(f"{name}... ese numero no está permitido.")
            eleccion = int(input("Una nueva oportunidad: "))
        elif eleccion > numero_aleatorio:
            print(f"Lo siento {name}, pero es un numero menor")
            eleccion = int(input("Dame otro numero: "))
        elif eleccion < numero_aleatorio:
            print(f"Lo siento {name}, pero es un numero mayor")
            eleccion = int(input("Dame otro numero: "))
        elif eleccion == numero_aleatorio:
            print(f"Descubriste el numero, solo te llevó {intento} intentos")
            break
    intento += 1
    if intento == 8:
        print(f"{name} Has perdido. El numero era {numero_aleatorio}")
