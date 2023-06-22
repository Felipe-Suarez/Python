"""
Importar modulos
Ejemplos de importacion de modulos
"""

# Las funciones no se exportan
# El nombre de los archivos debe seguir las reglas de nombrado de variables

# import functions  # importacion de modulo
import functions as f  # importacion de modulo con alias

from vars import NAME  # importacion de variable especifica

# HELLO = functions.HELLO2(NAME)
HELLO = f.Hello2(NAME)

print(HELLO)
