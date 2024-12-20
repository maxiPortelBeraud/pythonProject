class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice muuu")


class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f'{self.nombre} dice beee')


vaca = Vaca('Lala')
oveja = Oveja('Lele')

animales = [vaca, oveja]


def animal_habla(animal):
    animal.hablar()


animal_habla(oveja)
animal_habla(vaca)

palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)


def cantidad(elemento):
    print(len(elemento))


cantidad(palabra)
cantidad(lista)
cantidad(tupla)


class Mago():
    def atacar(self):
        print("Ataque mágico")


class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")


class Samurai():
    def atacar(self):
        print("Ataque con katana")


arquero = Arquero()
mago = Mago()
samurai = Samurai()

personajes = [arquero, mago, samurai]
for personaje in personajes:
    personaje.atacar()
