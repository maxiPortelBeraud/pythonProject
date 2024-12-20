# from random import shuffle

# # Lista   inicial
# palitos = ["-", "--", "---", "----"]


# # Mezclar palitos
# def mezclar(lista):
#     shuffle(lista)
#     return lista


# # pedirle intento
# def probar_suerte():
#     intento = ''
#     while intento not in ["1", "2", "3", "4"]:
#         intento = input("Elige un N° del 1 al 4: ")
#     return int(intento)


# # Comprobar intento
# def chequear_intento(lista, intento):
#     if lista[intento - 1] == '-':
#         print("Toca lavar los platos")
#     else:
#         print("Hoy te salvaste")
#     print(f"Te ha tocado {lista[intento-1]}")


# palitos_mezclados = mezclar(palitos)
# seleccion = probar_suerte()
# chequear_intento(palitos_mezclados, seleccion)


from random import choice
# from random import randint


# def lanzar_dados():
#     dado1 = randint(1, 6)
#     dado2 = randint(1, 6)
#     resultado = [dado1, dado2]
#     return resultado


# def elevar_jugada(dados):
#     if dados[0] + dados[1] <= 6:
#         print(f"La suma de tus dados es {dados[0] + dados[1]}. Lamentable")
#     elif dados[0] + dados[1] in range(7, 11):
#         print(f"La suma de tus dados es {
#             dados[0] + dados[1]}. Tienes buenas chances")
#     else:
#         print(f"La suma de tus dados es {
#             dados[0] + dados[1]}. Parece una jugada ganadora")


# elevar_jugada(lanzar_dados())

# lista_numeros = [1, 2, 15, 7, 2, 8]


# def reducir_lista(lista):
#     lista = list(set(lista))
#     lista.sort()
#     lista.pop(-1)
#     return lista


# def promedio(lista):
#     return sum(lista)/len(lista)


lista_numeros = [1, 2, 3, 4, 5]


def lanzar_moneda():
    moneda = choice(["Cara", "Cruz"])
    print(moneda)
    return moneda


def probar_suerte(resultado, lista_numeros):
    if resultado == "Cara":
        lista_numeros.clear()
        return lista_numeros
    else:
        print("La lista fue salvada")
        return lista_numeros


probar_suerte(lanzar_moneda(), lista_numeros)
