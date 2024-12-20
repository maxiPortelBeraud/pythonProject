def perfumeria():
    for turno_perfumeria in range(1, 10000):
        yield f"P-0{turno_perfumeria}"


def farmacia():
    for turno_farmacia in range(1, 10000):
        yield f"F-0{turno_farmacia}"


def cosmetica():
    for turno_cosmetica in range(1, 10000):
        yield f"C-0{turno_cosmetica}"


turno_perfumeria = perfumeria()
turno_farmacia = farmacia()
turno_cosmetica = cosmetica()


def sacar_turno(area):
    if area.upper() == 'P':
        turno = next(turno_perfumeria)
    elif area.upper() == 'F':
        turno = next(turno_farmacia)
    elif area.upper() == 'C':
        turno = next(turno_cosmetica)
    elif area.upper() == 'OFF':
        print("Apagando...")
        pass
    else:
        print('Eso no es un elemento válido')
        pass
    mensaje((turno))


def mensaje(turno):
    print(f"Su turno es: {turno}")
    print("Aguarde a ser atendido")
