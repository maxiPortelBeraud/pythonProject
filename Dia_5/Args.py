def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total


print(suma(1, 23, 123, 12, 123, 324, 1))


def numeros_persona(nombre, *num):
    total = 0
    for numero in num:
        total += numero
    return f"{nombre}, la suma de tus números es {total}"
