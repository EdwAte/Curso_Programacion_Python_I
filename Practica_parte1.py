#Generador contraseñas

import random
import string

def generar_contrasena(longitud=9, incluir_numeros=True, incluir_mayusculas=True, incluir_minusculas=True, incluir_especiales=True):
    def obtener_caracteres():
        caracteres = []
        if incluir_numeros:
            caracteres.extend(string.digits)
        if incluir_mayusculas:
            caracteres.extend(string.ascii_uppercase)
        if incluir_minusculas:
            caracteres.extend(string.ascii_lowercase)
        if incluir_especiales:
            caracteres.extend(string.punctuation)
        return caracteres

    caracteres = obtener_caracteres()

    if not caracteres:
        print("Debes incluir al menos un tipo de caracter.")
        return None

    contrasena = ''.join(random.sample(caracteres, longitud))
    return contrasena

# Ejemplo de uso con una contraseña de longitud 12 que incluye números, mayúsculas, minúsculas y caracteres especiales
nueva_contrasena = generar_contrasena(longitud=12, incluir_numeros=True, incluir_mayusculas=True, incluir_minusculas=True, incluir_especiales=True)
print(nueva_contrasena)

