texto = input("Ingrese texto: ").lower()
letra1 = input("1° letra para analizar: ").lower()
letra2 = input("2° letra: ").lower()
letra3 = input("3° letra: ").lower()
lista = [letra1, letra2, letra3]

print(f'La letra ingresada, "{letra1}" , aparece {
      texto.count(lista[0])} veces en el texto')
print(f'La letra ingresada, "{letra2}" , aparece {
      texto.count(lista[1])} veces en el texto')
print(f'La letra ingresada, "{letra3}" , aparece {
      texto.count(lista[2])} veces en el texto')

print(f'La cantidad de palabras del texto es de {len(texto.split())}')
print(f'Empieza con {texto[0]} y termina con {texto[-1]}')
