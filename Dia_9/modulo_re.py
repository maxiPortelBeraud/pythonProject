import re

text = "Si necesitas ayuda llama al (658)-598.9977 las 24 horas al servicio de ayuda online"
patron = 'ayuda'
busqueda = re.findall(patron, text)
print(busqueda)

for hallazgo in re.finditer(patron, text):
    print(hallazgo)

otro_texto = "Llamá al 124-854-4259"
patron = r'(\d{3})-(\d{3})-(\d{4})'  # r'\d{3}-\d{3}-\d{4}'  # r'\d\d\d-\d\d\d-\d\d\d'

resultado = re.search(patron, otro_texto)
print(resultado.group(2))

# /d    digito numérico              v\d.\d\d       ej: v1.05
# /w    carácter alfanumérico        \w\w\w-\w\w    ej: abc-ab
# /s    espacio en blanco            números\s\d\d  ej: "número 25"
# /D    NO es numérico               \D\D\D\D
# /W    NO es alfanumérico           \W\W\W\W
# /S    NO espacio blanco            \S\S\S\S

# +     1 o mas veces                código_\d-\d+  ej: código_5-5 / código_9-956556
# {n}   se repite n veces           \d-\d{4}        ej: 1-0000 / 1-2687
# {n,m} se repite de n a m veces    \w{3,5}         ej: hola / toz526
# {n,}  desde n hacia arriba        -\d{4,}-        ej: -111111- / -5235-
# *     0 o mas veces               \w\s*\w         ej: " a 2 " / "a   b"
# ?     1 o 0                       casas?          ej: casa / casas
