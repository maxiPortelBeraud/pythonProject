def letras_de_palabras(palabra):
    palabra_lista = set(palabra)
    return sorted(palabra_lista)


print(letras_de_palabras("entretenido"))
