# lista = ["a", "b", "c"]

# for indice, item in enumerate(lista):
#     print(indice, item)


string = "Python"
lista_indices = []
for indice, letra in enumerate(string):
    lista_indices.append((indice, letra))
print(lista_indices)
