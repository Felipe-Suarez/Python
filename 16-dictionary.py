"""
Diccionarios
Ejemplos de Diccionarios
"""

point = {"x": 10, "y": 20}

POINT_X = point["x"]
POINT_X = point.get("x")

pointZ = point.get("z", 0)  # si no existe z devuelve 0

del point["x"]  # eliminar

# loops

for value in point:
    print(value, point[value])

for key, value in point.items():
    print(key, value)

for key in point.keys():
    print(key)

for value in point.values():
    print(value)
