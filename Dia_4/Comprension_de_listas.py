palabra = "python"

lista = [letra for letra in palabra]
lista_numeros = [n for n in range(0, 21, 2) if n > 10]
lista_numeros2 = [n if n > 10 else 'no' for n in range(0, 21, 2)]

print(lista_numeros2)
