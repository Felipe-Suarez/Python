"""
Set
Ejemplos de Set
"""

setOne = {1, 1, 2, 2, 3}  # set

setOne.add(4)  # agrega un elemento
setOne.remove(1)  # elimina un elemento

setTwo = [3, 4, 5]
setTwo = set(setTwo)  # convierte a set (recibe iterable)

# union (concatena/une ambos sets)
setThree = setOne | setTwo

# interseccion (devuelve coincidencias entre ambos)
print(setOne & setTwo)

# diferencia (quita elementos del set 1 que se encuentren en el set 2)
print(setOne - setTwo)

# diferencia simetrica (devuelve elementos que no coinciden entre ambos)
print(setOne ^ setTwo)
