"""Ejemplo_Funcion"""
precios_cafe = [("capuchino", 1.5), ("expresso", 1.2), ("moka", 1.91234)]


def cafe_mas_caro(lista_precios):
    """Function printing python version."""
    precio_mayor = 0
    cafe_mayor_precio = ''
    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mayor_precio = cafe
        else:
            pass

    return (cafe_mayor_precio, precio_mayor)


tipo_cafe, precio_cafe = cafe_mas_caro(precios_cafe)
print(f"El mas caro es {tipo_cafe} cuyo precio es ${round(precio_cafe, 2)}")
