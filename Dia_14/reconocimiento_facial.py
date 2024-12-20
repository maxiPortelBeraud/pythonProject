import cv2
import face_recognition as fr

# cargar imágenes
foto_control = fr.load_image_file('MaxiA.png')
foto_prueba = fr.load_image_file('Empleados/Maxi Portel.jpg')

# pasar imágenes a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# localizar cara-control
lugar_cara_a = fr.face_locations(foto_control)[0]
cara_codificada_a = fr.face_encodings(foto_control)[0]

# mostrar rectángulo
cv2.rectangle(foto_control,
              (lugar_cara_a[3], lugar_cara_a[0]),
              (lugar_cara_a[1], lugar_cara_a[2]),
              (0, 255, 0),
              2)

# localizar cara-prueba
lugar_cara_b = fr.face_locations(foto_prueba)[0]
cara_codificada_b = fr.face_encodings(foto_prueba)[0]

# mostrar rectángulo
cv2.rectangle(foto_prueba,
              (lugar_cara_b[3], lugar_cara_b[0]),
              (lugar_cara_b[1], lugar_cara_b[2]),
              (0, 255, 0),
              2)

# realizamos comparación
resultado = fr.compare_faces([cara_codificada_a], cara_codificada_b)
# medida de la distancia
distancia = fr.face_distance([cara_codificada_a], cara_codificada_b)

# mostrar resultado
cv2.putText(foto_prueba,
            f'{resultado} {distancia.round(2)}',
            (50, 50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0, 255, 0),
            2)

# mostrar imágenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

# mantener el programa abierto
cv2.waitKey(0)
