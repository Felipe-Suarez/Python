"""
CSV: Comma Separated Values
Operaciones con archivos CSV
"""

# import csv
import pandas as pd

## CSV

# with open("data\\data.csv", encoding="utf-8") as data:
#     reader = csv.reader(data) ## lee y devuelve un array
#     for row in reader:
#         print(row)


## PANDAS

# dataFrame = pd.read_csv("data\\data.csv", names=["name", "age"])
## names crea los nombres de las columnas

dataFrame = pd.read_csv("data\\data.csv")

names = dataFrame["name"]  ## imprime la columna nombre

dataFrameSort1 = dataFrame.sort_values("age")  ## default ascending=True
dataFrameSort2 = dataFrame.sort_values("age", ascending=False)

dataFrameSort3 = dataFrame.sort_index(ascending=False)  ## default ascending=True

dataFrame2 = pd.concat([dataFrame, dataFrameSort1])  ## concatena los dataframes
# dataFrame2 = pd.concat([dataFrame, dataFrameSort1], axis=1)
## axis concatena los dataframes en columnas

firstsRows = dataFrame2.head(2)  ## imprime las primeras N filas
lastsRows = dataFrame2.tail(2)  ## imprime las ultimas N filas

## imprime el total de filas y columnas (tuple (rows, columns))
totalColumsAndRows = dataFrame2.shape
totalRows, totalColumns = totalColumsAndRows  ## unpacking

describe = dataFrame2.describe()  ## imprime estadisticas de las columnas numericas
# info = dataFrame2.info() ## imprime el tipo de dato de cada columna

# [x,y]
element = dataFrame.loc[2, "age"]  ## imprime el elemento de la fila 2 y columna age
allNames = dataFrame.loc[:, "name"]  ## imprime todos los nombres
elementIndex = dataFrame.iloc[2, 2]  ## imprime el elemento de la fila 2 y columna 2

highAge = dataFrame[dataFrame["age"] > 30]  ## imprime las filas con edad mayor a 30

dataFrame2["age"] = dataFrame2["age"].astype(float)  ## convierte la columna age a float

## reemplaza valparaiso por Buenos aires
dataFrame2["city"].replace("valparaiso", "Buenos aires", inplace=True)

# dataFrame2 = dataFrame2.drop(columns=["age"])  ## elimina la columna age
# dataFrame2 = dataFrame2.drop(index=[0])  ## elimina la fila 0

dataFrame2 = dataFrame2.dropna()  ## elimina los valores nulos
dataFrame2 = dataFrame2.drop_duplicates()  ## elimina los duplicados

## elimina los duplicados de la columna name
# dataFrame2 = dataFrame2.drop_duplicates(subset=["name"])

print(dataFrameSort2)  ## imprime todo el archivo

## guarda el archivo en csv sin los indices
dataFrameSort2.to_csv("data\\dataSort.csv", index=False)

# Archivos mas grandes se leen con chunks
