nombres = ["Ana", "Hugo", "Valeria"]
edades = [24, 30, 42, 50]
ciudades = ["Lima", "Madrid", "Buenos Aires"]

combinados = list(zip(nombres, edades, ciudades))
print(combinados)

for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")
