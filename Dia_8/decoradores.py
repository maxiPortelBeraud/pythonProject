# def lower_or_upper(type_process):
#     def upper(texto):
#         print(texto.upper())
#
#     def lower(texto):
#         print("Hola")
#         print(texto.lower())
#
#     if type_process == "upper":
#         return upper
#     if type_process == "lower":
#         return lower
#
#
# operation = lower_or_upper("upper")
#
# operation("maxi")


def decorar_saludo(fn):
    def another_function(word):
        print("Hola")
        fn(word)
        print("Adios")

    return another_function


def to_upper(text):
    print(text.upper())


def to_lower(text):
    print(text.lower())


upper_decorate = decorar_saludo(to_upper)

upper_decorate("maxi")
to_upper("maxi")
