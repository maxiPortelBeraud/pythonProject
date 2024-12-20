from random import choice

palabras = ["Palabra", "Onomatopeya", "Hormiga", "Rinoceronte"]


def ahorcado(posibles_palabras):
    vidas = 8
    palabra_seleccionada = choice(posibles_palabras)
    palabra_a_adivinar = preparar_ahorcado(palabra_seleccionada)

    while vidas > 0:
        print(palabra_a_adivinar)
        palabra_a_adivinar, vidas = procesar_letra(
            palabra_seleccionada, palabra_a_adivinar, vidas)
        if "_" not in palabra_a_adivinar:
            return "Ganaste!"

    return f"Perdiste. La palabra era: '{palabra_seleccionada}'"


def preparar_ahorcado(palabra_seleccionada):
    palabra_a_adivinar = []
    for indice, letra in enumerate(palabra_seleccionada):
        if indice == 0:
            palabra_a_adivinar.append(letra)
        else:
            palabra_a_adivinar.append("_")
    return palabra_a_adivinar


def procesar_letra(palabra_seleccionada, palabra_a_adivinar, vidas):
    input_letra = input(f"Tenes {vidas} vidas. Ingresa la letra: ").lower()
    for indice, letra in enumerate(palabra_seleccionada):
        if input_letra == letra and letra not in palabra_a_adivinar:
            palabra_a_adivinar[indice] = input_letra
    if input_letra not in palabra_seleccionada:
        vidas -= 1

    return palabra_a_adivinar, vidas


print(ahorcado(palabras))
