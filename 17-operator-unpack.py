"""
Unpack Operator
Ejemplos de Unpacking
"""

# list

list1 = [1, 2, 3, 4]
print(*list1)  # unpacking

list2 = [5, 6, 7, 8]

list3 = [*list, *list2]

# dict

dict1 = {"x": 1}
dict2 = {"y": 2}

dict3 = {**dict1, **dict2}

print(dict3)
