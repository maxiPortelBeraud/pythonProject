# def chequear_3_cifras(numero):
#     return numero in range(100, 1000)

# resultado = chequear_3_cifras(658)
# print(resultado)


# def chequear_3_cifras(lista):
#     for n in lista:
#         if n in range(100, 1000):
#             return True
#         else:
#             pass
#     return False


# resultado = chequear_3_cifras([55, 99, 6000])

# print(resultado)

def suma_menores(lista):
    resultado = 0
    for e in lista:
        if e in range(0, 1001):
            resultado += e
    return resultado


lista_numerous = [1, 2, 31000, 100]

print(suma_menores(lista_numerous))
