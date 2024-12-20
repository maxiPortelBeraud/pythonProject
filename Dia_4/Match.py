serie = "N-02"

match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("No existe este producto ")


cliente = {"nombre": "Federico", "edad": 45, "ocupacion": "Instructor"}
pelicula = {"titulo": "Matrix", "ficha_tecnica": {
    "protagonista": "Keanu Reeves", "director": "Lana y Lilly Wachowski"}}
elementos = [cliente, pelicula, "libro"]


for e in elementos:
    match e:
        case {"nombre": nombre, "edad": edad, "ocupacion": ocupacion}:
            print(f"Es un cliente. {nombre, edad, ocupacion}")
        case {"titulo": titulo, "ficha_tecnica": {
                "protagonista": protagonista, "director": director}}:
            print(f"Es una pelicula. {titulo, protagonista, director}")
        case _:
            print("Es un elemento desconocido")
