def hay_doble_cero(*args):
    ceros = 0
    for arg in args:
        if arg == 0:
            ceros += 1
    if ceros >= 2:
        return True
    else:
        return False


print(hay_doble_cero(5, 0, 1))
