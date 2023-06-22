"""
Archivos .txt
Operaciones de archivos de texto
"""

## READ

## - Abre el archivo de texto y lo codifica en utf-8 -
## por defecto contiene el argumento 'r' = read
# text = open("19-data.txt", encoding="utf-8")

# readedText = text.read()  ## Lee todo el texto (devuelve un string)
# lines = text.readlines()  ## Lee linea por linea (devuelve una lista)
# characters = text.readline(7)  ## Lee los primeros 7 caracteres

# text.close() ## Cierra el archivo

# print(readedText)

## *Forma optima de leer archivos de texto:

## - Abre y Cierra el archivo automaticamente -
# with open("19-data.txt", encoding="utf-8") as text:
#     print(text.read())

## WRITE

with open("19-data.txt", "w", encoding="utf-8") as text:  ## w = write
    # text.write("Hola Mundo\n") ## Sobre escribe el archivo

    text.writelines(["Hola Mundo\n", "Este es un texto escrito con python\n"])
    text.writelines([":) Nueva linea"])  ## Sobre escribe pero no se borran entre si

## APPEND

# with open("19-data.txt", "a", encoding="utf-8") as text:  ## a = append
# text.write("Hola Mundo\n")  ## Agrega
