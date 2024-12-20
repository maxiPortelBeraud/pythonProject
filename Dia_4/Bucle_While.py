monedas = 5

while monedas >= 0:
    if monedas == 0:
        print("Perdiste te quedaste sin monedas")
        break
    else:
        print(f"Tengo {monedas} monedas")
        monedas -= 1
