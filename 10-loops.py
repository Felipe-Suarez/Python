"""
Loops
Ejemplos de loops
"""

languages = [
    "Python",
    "C",
    "C++",
]

# while loop
i = 1
while i < len(languages):
    print(i)
    print(languages[i])
    i += 1
    if i == 2:
        break

# for in loop
for language in languages:
    print(language)

print([language + " 2" for language in languages])  # for en linea

# for in else loop with break and range
SEARCH = "Javascript"
for numero in range(3):
    print("analizando", languages[numero])
    if languages[numero] == SEARCH:
        print("encontrado", SEARCH)
        break
else:
    print("no encontrado", SEARCH)

# for in loop with string
for i in "Ultimate python":
    print(i)

# for in loop with enumerate
for language in enumerate(languages):  # (indice, valor) / tupla
    print(language)
    print(language[0])
    print(language[1])

# recorre 2 listas al mismo tiempo del mismo tamaño
list1 = list(range(1, 11))
list2 = list(range(11, 21))

for list1, list2 in zip(list1, list2):
    print(list1, list2)
