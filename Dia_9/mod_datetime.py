# import datetime
# hora = datetime.time(17,35)
# print(hora.minute)
#
# dia = datetime.date(2016, 12, 29)
# print(dia)

# from datetime import datetime, date
#
# fecha = datetime(2016, 12, 29, 22, 10, 15, 25340)
# fecha = fecha.replace(month=11)
# print(fecha)
#
#
# nacimiento = date(1995, 3, 5)
# muerte = date(2095, 6, 19)
#
# vida = muerte - nacimiento
# print(f"Vivió {vida} días")
#
# despierta = datetime(2022, 10 ,5, 7,30)
# duerme = datetime(2022, 10, 5, 23, 45)
# vigilia = duerme - despierta
#
# print(vigilia.seconds)
#
# print(type(despierta.today()))


import datetime

hoy = datetime.datetime(2000, 1, 1).today()

minutos = hoy.minute
