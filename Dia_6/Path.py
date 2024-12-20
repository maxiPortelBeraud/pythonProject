from pathlib import Path

# base = Path.home()
# guia = Path(base, "Europa", "España", Path("Barcelona", "Sagrada_Familia.txt"))
#
# print(guia.parent)


guia = Path("Desktop", "Otra", "prueba.txt")
en_carpeta_otra = guia.relative_to(Path("Desktop", "Otra"))
print(en_carpeta_otra)


for txt in Path(guia).glob("**/*.txt"):
    print(txt)
