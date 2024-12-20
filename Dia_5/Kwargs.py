def prueba(num1, num2, *args, **kwargs):

    print(f"El primer valor es {num1}")
    print(f"El segundo valor es {num2}")
    for arg in args:
        print(f"arg={arg}")
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total


prueba(1, 2, 3, 4, 5, x=3, y=5, z=2)


def lista_atributos(**keywords):
    lista_valores = []
    for clave, valor in keywords.items():
        lista_valores.append(valor)
    print(list(lista_valores))


def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


describir_persona("María", color_ojos="azules", color_pelo="rubio")
