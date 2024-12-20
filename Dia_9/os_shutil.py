import os
import shutil
import send2trash

# archivo = open('curso.txt', 'w')
# archivo.write('texto de prueba')
# archivo.close()
#
# print(os.listdir())
#
# #shutil.move('curso.txt', "C:\\Users\\maximiliano.portel\\Desktop")
#
# send2trash.send2trash('curso.txt')
ruta_carpeta = "C:\\Users\\maximiliano.portel\\Desktop\\Otra"
for carpeta, subcarpeta, archivos in os.walk(ruta_carpeta):
    print(f"En la carpeta {carpeta}")
    print(f"Las subcarpetas son {subcarpeta}")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print('Los archivos son: ')
    for archivo in archivos:
        print(f"\t{archivo}")
    print('\n')

