"""
Funciones
Ejemplos de funciones
"""

# funcion con parametros requeridos y opcionales


def hello(name, lastname, second_name=""):
    print(f"Hola {name} {lastname} {second_name}")


hello("Felipe", "Suarez")
hello(lastname="Suarez", name="Felipe")  # asignar argumentos


def add(*nums):  # recibe muchos parametros en forma de lista
    total = 0
    for num in nums:
        total += num
    return total


print(add(2, 3, 5, 6, 7, 4, 3))


def get_product(**data):  # recibe muchos parametros en forma de diccionario
    print(data)
    print(data["id"])


get_product(id=1, name="Iphone", price=1000)

# las variables globales son una mala practica
NAME = "Felipe"


def change_name():
    # no se puede llamar a la variabla global ya que tambien se define en local
    # y se esta llamando antes que se defina
    # print(NAME)
    global NAME  # cambia variable global, no es buena practica
    NAME = "Juan"


change_name()
print(NAME)

hello2 = lambda name: print(f"Hola {name}")  # funcion anonima
# en este caso seria mejor usar una funcion normal
hello2("Felipe")
