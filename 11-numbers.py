"""
Numeros
Ejemplos de operaciones con numeros
"""

import math

numbers = [1, 2, 3, 4, 5, 6]

highest = max(numbers)
lowest = min(numbers)

rounded = round(5.5)
roundedFloat = round(5.5355, 2)  # 5.54 (redondea a partir del segundo decimal)

absolute = abs(-5.5)

total = sum(numbers)

# todos los metodos de Math
roundedFloor = math.floor(5.5)
roundedCeil = math.ceil(5.5)
isNaN = math.isnan(5.5)
# etc ...

a, b = 0, 1  # asignacion multiple (a = 0, b = 1)
