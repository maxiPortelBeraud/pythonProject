from pathlib import Path, PureWindowsPath

carpeta = Path("C:/Users/maximiliano.portel/Desktop/Otra/prueba.txt")
ruta_windows = PureWindowsPath(carpeta)
print(carpeta.read_text())
print(ruta_windows)
