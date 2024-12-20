# archivo = open("prueba1.txt", "a")
# lista = ['hola', 'mundo', 'aquí', 'estoy']
# archivo.write('bienvenido')
# archivo.close()


mi_archivo = open('mi_archivo.txt', "w")
mi_archivo.write("Nuevo texto")
mi_archivo.close()
mi_archivo = open('mi_archivo.txt', "r")
todas = mi_archivo.read()
print(todas)
