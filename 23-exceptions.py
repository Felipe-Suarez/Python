"""
Exceptions
Ejemplo de manejo de excepciones basico
"""

N1 = 10
N2 = 0

try:
    print(N1 / N2)
except ZeroDivisionError:
    print("No se puede dividir por cero")
finally:
    print("Fin del programa")
