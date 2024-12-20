class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = 0

    def imprimir(self):
        print(f"{self.nombre}, {self.apellido}, Cuenta: {self.numero_cuenta}, Saldo: ${self.balance}")

    def depositar(self, cantidad):
        self.balance += cantidad

    def retirar(self, cantidad):
        self.balance -= cantidad


def create_client():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    cliente = Cliente(nombre, apellido, 1, 0)
    return cliente


def inicio():
    cliente = create_client()
    print(f"Bienvenido {cliente.nombre}. Su balance actual es: ${cliente.balance}")
    print("¿Que desea hacer?")
    choices(cliente)


def choices(cliente):
    decision = 0
    while decision != 3:
        cliente.imprimir()
        decision = int(input(""""
                [1] - Depositar
                [2] - Retirar
                [3] - Salir
                """))
        if decision == 1:
            cantidad = int(input("indice cuanto desea ingresar o pulse 0 para regresar: "))
            if cantidad == 0:
                continue
            else:
                cliente.depositar(cantidad)
                print("Dinero ingresado correctamente")
        elif decision == 2:
            cantidad = int(input("indice cuanto desea retirar o pulse 0 para regresar: "))
            if cantidad == 0:
                continue
            elif cliente.balance - cantidad < 0:
                print("Su saldo es insuficiente")
            else:
                cliente.retirar(cantidad)
                print("Dinero retirado correctamente")
        elif decision == 3:
            print(f"Adios {cliente.nombre}")
        else:
            print("Ha ingresado un dato inválido")


inicio()
