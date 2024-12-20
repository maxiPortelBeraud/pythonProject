class Bird:
    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f'pio, mi color es {self.color}')

    def volar(self, metros):
        print(f'El pájaro ha volado {metros} metros.')
        self.piar()

    def black_paint(self):
        self.color = "Negro"
        print(f"Ahora el pájaro es {self.color}")

    @classmethod
    def poner_huevos(cls, cantidad):
        print(f"Puso {cantidad} huevos")

    @staticmethod
    def mirar():
        print('Observa')


pajaro_piolin = Bird('Amarillo', 'Canario')
pajaro_loco = Bird('Azul', 'Carpintero')

pajaro_piolin.alas = False
print(pajaro_loco.alas)
print(pajaro_piolin.alas)

