import Proyecto_8


def gestion_turnos():
    turno = ''

    while turno.lower() != "off":
        try:
            turno = input("Desea sacar otro turno?")
            if turno.lower() == "off":
                print("Apagando...")
                continue
            else:
                turno = input("""
                [P] - Para area de perfumería
                [F] - Para area de farmacia
                [C] - Para area de cosmética
                """)
                Proyecto_8.sacar_turno(turno)
        except:
            print("Algo salió mal")


gestion_turnos()
