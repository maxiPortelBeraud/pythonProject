def devolver_distintos(num1, num2, num3):
    suma = num1 + num2 + num3
    lista = [num1, num2, num3]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        return sorted(lista)[1]
