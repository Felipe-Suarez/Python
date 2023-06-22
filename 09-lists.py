"""
Listas
Ejemplos de listas
"""

languages = [
    "Python",
    "C",
    "C++",
    "Java",
    "JavaScript",
]

INDEX_1 = languages[1]
languages[1] = "Go"  # modificar elemento en el indice 1

LAST = languages[-1]  # ultimo
BEFORE_LAST = languages[-2]  # penultimo

lenguajeA = languages[1:3]  # desde el 1 hasta el 3
lenguajeB = languages[1:]  # desde el 1
lenguajeC = languages[:3]  # hasta el 3
lenguajeD = languages[::2]  # de 2 en 2
lenguajeE = languages[1:5:2]  # de 2 en 2 desde el 1 hasta el 5
lenguajeF = languages[::-1]  # reversa

LENGTH = len(languages)  # longitud

IS_IN_LANGUAGES = "PHP" in languages  # existe PHP en languages

languages.insert(3, "PHP")  # insertar en la posicion 3
languages.remove("PHP")  # remover por valor (solo el primero)

languages.clear()  # vaciar

languages.extend(["C++", "Java", "JavaScript"])  # extender

languages.append("Python")  # agregar al final
languages.pop()  # eliminar el ultimo
languages.pop(1)  # eliminar el indice 1

multipleList = [["Javascript", 1], ["Python", 2], ["PHP", 3], ["Java", 4]]

# en caso que sea un array de arrays como 'multipleList' ordena por el elemento de indice 0
languages.sort()  # ordenar
multipleList.sort(key=lambda item: item[1])  # ordenar por el elemento de indice 1
languages.sort(reverse=True)  # ordenar reversa

languages.reverse()  # reversa

languages2 = sorted(languages)  # ordenar y guardar en otra variable

languages3 = languages.copy()  # copiar

repeatedList = [0, 1] * 10  # repetir

languages4 = ["array1"] + ["array2"]  # concatenar

range1 = list(range(10))  # rango de 0 a 9
range2 = list(range(1, 11))  # rango de 1 a 10
splitedString = list("Hola mundo")  # convertir string a lista

numbers = [1, 2, 3]
first, second, third = numbers  # desempaquetar

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, second, *rest, befereLast, last = numbers  # desempaquetar

if "C++" in languages:
    print(languages.index("C++"))  # indice del elemento
# si no lo encuentra tira un error, por eso se verifica antes

# cuantas veces aparece un elemento en la lista
countOfLanguage = languages.count("C++")

every = all([True, "10", 2])  # todos los elementos son verdaderos
some = any([False, "10", 0])  # algun elemento es verdadero

# extraer un elemento de cada array
namesOfLists = [name[0] for name in multipleList]

filterList = [item for item in multipleList if item[1] > 2]  # filtrar
# por cada item de la lista, devolveme el item si el item en la posicion 0 es mayor a 2
# podria devolver item + 1 por ejemplo (modificado)

# alternativas

namesOfLists = list(map(lambda name: name[0], multipleList))

filterList = list(filter(lambda item: item[1] > 2, multipleList))  # filtrar
