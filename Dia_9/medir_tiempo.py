#import time
import timeit

# inicio = time.time()
# prueba_for(1000000)
# final = time.time()
# print(final-inicio)
#
# inicio = time.time()
# prueba_while(1000000)
# final = time.time()
# print(final-inicio)

declaracion = '''
prueba_for(10)
'''

mi_setup = '''
def prueba_for(numero):
    list = []
    for num in range(1, numero + 1):
        list.append(num)
    return list
'''
duracion = timeit.timeit(declaracion, mi_setup, number=10000000)


declaracion2 = '''
prueba_while(10)
'''

mi_setup2 = '''
def prueba_while(numero):
    list = []
    contador = 1
    while contador <= numero:
        list.append(contador)
        contador += 1
    return list
'''
duracion2 = timeit.timeit(declaracion2, mi_setup2, number=10000000)

print(duracion)
print(duracion2)
