class Bird:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie


my_bird = Bird("Negro", 'Cuervo')

palabra = 'hola'
print(f'El pájaro {my_bird.color} es un {my_bird.especie}')


class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color


cubo_rojo = Cubo("rojo")
