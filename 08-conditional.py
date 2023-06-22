"""
Condicional
Ejemplo de condicional
"""

RESULT = 90

if RESULT >= 90:
    print("Excelente")
elif RESULT >= 80:
    print("Muy bien")
else:
    print("Regular")


if RESULT >= 80 and RESULT <= 100:
    print("Muy bien")

if 80 <= RESULT <= 100:  # sintaxis alternativa
    print("Muy bien")
