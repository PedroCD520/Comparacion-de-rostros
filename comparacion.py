import face_recognition
import cv2

def load_and_encode_image(image_path):
    # Cargar la imagen desde el archivo
    image = face_recognition.load_image_file(image_path)

    # Intentar obtener los encodings de los rostros en la imagen
    face_encodings = face_recognition.face_encodings(image)

    if len(face_encodings) == 0:
        print(f"No se encontró ningún rostro en {image_path}")
        return None
    else:
        # Devolver solo el primer encoding encontrado
        return face_encodings[0]

def compare_faces(image1_path, image2_path):
    # Cargar y codificar las dos imágenes
    encoding1 = load_and_encode_image(image1_path)
    encoding2 = load_and_encode_image(image2_path)

    # Si ambos encodings se obtuvieron correctamente, comparar
    if encoding1 is not None and encoding2 is not None:
        # Comparar los rostros
        results = face_recognition.compare_faces([encoding1], encoding2)

        # Mostrar si son la misma persona o no
        if results[0]:
            print("Las fotos son de la misma persona.")
        else:
            print("Las fotos son de personas diferentes.")
    else:
        print("No se pudo realizar la comparación porque falta uno de los rostros.")

# Rutas de las dos imágenes a comparar
image1_path = "ruta/a/la/primera_foto.jpg"
image2_path = "ruta/a/la/segunda_foto.jpg"

# Comparar las dos imágenes
compare_faces(image1_path, image2_path)
