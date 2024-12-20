from collections import Counter, defaultdict, namedtuple, deque

#Counter
nums = [8, 2, 7, 4, 7, 7, 44, 7, 14, 8, 2, 5]

print(Counter(nums))
print(Counter('mississippi'))

counter_nums = Counter(nums)

print(counter_nums.most_common())

#defaultdict
my_dictionary = defaultdict(lambda: 'nada')
my_dictionary['uno'] = 'azul'

print(my_dictionary['dos'])
print(my_dictionary)

#namedtuple
my_tuple = (500, 18, 65)
Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.83, 79)
print(ariel[2])

#deque
lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])

print(lista_ciudades)
