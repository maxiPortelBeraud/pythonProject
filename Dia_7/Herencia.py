# class Animal:
#     def __init__(self, age, color):
#         self.age = age
#         self.color = color
#
#     def nacer(self):
#         print("Este animal ha nacido")
#
#     def hablar(self):
#         print("Este animal emite un sonido")
#
#
# class Pajaro(Animal):
#     def __init__(self, edad, color, altura_vuelo):
#         # self.edad = edad
#         # self.color = color
#         super().__init__(edad, color)
#         self.altura_vuelo = altura_vuelo
#
#     def hablar(self):
#         print('he he he hee heeee')
#
#     def volar(self, metros):
#         print(f'El pájaro vuelva {metros} metros')
#
#
# pajaro_loco = Pajaro(4, 'Blue', 60)
#
# pajaro_loco.volar(100)


# ---------------------------------------------------------------------------------------

# class Padre:
#     def hablar(self):
#         print('Hola')
#
#
# class Madre:
#     def reir(self):
#         print('jaja')
#
#     def hablar(self):
#         print('Buenas tardes')
#
#
# class Hijo(Padre, Madre):
#     pass
#
#
# class Nieto(Hijo):
#     pass
#
#
# mi_nieto = Nieto()
#
# mi_nieto.hablar()


class Vertebrado:
    vertebrado = True


class Ave(Vertebrado):
    tiene_pico = True

    def poner_huevos(self):
        print("Poniendo huevos")


class Reptil(Vertebrado):
    venenoso = True


class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")

    def poner_huevos(self):
        print("Poniendo huevos")


class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")

    def amamantar(self):
        print("Amamantando crías")


class Ornitorrinco(Vertebrado, Pez, Reptil, Ave, Mamifero):
    def __init__(self, tiene_pico, vertebrado, venenoso):
        super().__init__(tiene_pico, vertebrado, venenoso)


pedro = Ornitorrinco()

print(pedro.vertebrado)
