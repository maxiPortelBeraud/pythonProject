import zipfile

# mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')
#
# mi_zip.write('mi_texto_A.txt')
# mi_zip.write('mi_texto_B.txt')
#
# mi_zip.close()


# zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
#
# zip_abierto.extractall()


import shutil

# carpeta_origen = 'C:\\Users\\maximiliano.portel\\Desktop\\Carpeta_superior'
#
# archivo_destino = 'Todo_comprimido'
#
# shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

shutil.unpack_archive('Todo_comprimido.zip', "Extraccion realizada", "zip")
