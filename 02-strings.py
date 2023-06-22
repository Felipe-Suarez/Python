"""
Strings
Ejemplos de strings
"""

TEXT = "Hola Mundo"

MULTIPLIED_TEXT = "hola " * 4

DESCRIPTION = """
Este es un TEXTo
con saltos
de linea
"""  # string

print(TEXT[0], TEXT[0:3], TEXT[3:], TEXT[-1])  # obtener caracteres

INDEX_M = TEXT.find("M")  # posicion de la letra
REPLACED_TEXT = TEXT.replace("M", "Chanchito feliz")  # reemplazar

EXIST = "Mundo" in TEXT  # existe
NOT_EXIST = "Hola" not in TEXT  # no existe

LENGTH = len(TEXT)  # longitud

CONCATENATION = TEXT + " 1"  # concatenar
CONCATENATION_2 = f"{TEXT} 2"  # concatenar

UPPERCASE = TEXT.upper()  # mayuscula
LOWERCASE = TEXT.lower()  # minuscula

TEXT1 = "HOLA".capitalize()  # capitalizar
TEXT2 = "hola mundo".title()  # capitalizar palabras

TEXT3 = "hola mundo".center(50, "-")
TEXT4 = "    hola mundo    ".strip()  # quitar espacios
TEXT5 = "   hola mundo".lstrip()  # quitar espacios izquierda
TEXT6 = "hola mundo   ".rstrip()  # quitar espacios derecha

TEXT7 = "hola mundo".split(" ")  # separar
TEXT8 = " ".join(["hola", "mundo"])  # unir

TEXT9 = "TEXTo con \"comillas\" ' ', backslash \\ y \n salto de linea"  # caracteres especiales

print(TEXT)
