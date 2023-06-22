"""
Regexp
ejemplos basicos en Python con el modulo (re)
"""

import re

TEXT = """
Hola Mundo! 
Esto es un texto para probar
las expresiones regulares
en Python.
Chau Mundo
"""

# re . metodo ( patron, texto, banderas )

result1 = re.search("Hola", TEXT)  # Devuelve el primer match

result2 = re.findall("mundo", TEXT, flags=re.IGNORECASE)  # Devuelve todos los matches
result3 = re.findall(r"\w+", TEXT)

# subtituye los matches por el segundo parametro
result4 = re.sub(r"\w+", "Mundo", TEXT)
# count es la cantidad de veces que se reemplaza
result5 = re.sub(r"\w+", "Mundo", TEXT, count=2)

# Devuelve una lista con el texto separado por el patron
result6 = re.split(r"\n", TEXT)

print(result6)
