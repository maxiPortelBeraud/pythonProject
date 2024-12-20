def my_function():
    a_list = []
    for x in range(1, 5):
        a_list.append(x * 10)
    return a_list


def my_generator():
    for x in range(1, 5):
        yield x * 10


print(my_function())
generator = my_generator()

print(next(generator))
print(next(generator))


