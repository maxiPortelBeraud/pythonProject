# def suma():
#     n1 = int(input("Ingrese numero: "))
#     n2 = int(input("Ingrese numero: "))
#     print(n1 + n2)
#     print("Gracias por sumar")
#
#
# try:
#     suma()
# except TypeError:
#     print("Algo no ha salido bien")
# else:
#     print("Funciono correctamente")
# finally:
#     print("Eso fue todo.")


def pedir_numero():
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un número")
        else:
            print(f"Ingresaste el numero: {numero}")
            break

pedir_numero()

