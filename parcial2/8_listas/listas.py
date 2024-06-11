"""

List(Array)
son colecciones o conjunto de datos/valores bajo un mismo nombre para accedes a los valores se hace con un indice numerico

Nota: sus valores si son modificables

La lista es una coleccion ordenada y modificable. Permite miembros duplicados.


"""
# import os
# os.system("cls")
# #ejemplo 1 crear una lista con datos numericos e imprimir el contenido
# lista=[23, 34]
# print(lista)

# # recorre la lista con el for

# for i in lista:
#     print(i)

# # recorrer la lista con el while
# i = 0
# while i <= len(lista)-1:
#     print(i)
#     i += 1

# #Ejemplo 2 Crear una lista de 4 palabras, solicitar una palabra y buscar la
# # coincidencia en la lista e indicar si la encontró o no y en que posicion
# os.system("cls")

# palabras=["hola","2024","bye","UTD"]
# palabra_buscar = input("Ingresa la palabra a buscar: ")

# noencontre = True
# for i in palabras:
#     if palabra_buscar == i:
#         print(f"La palabra {i} se encuentra en la posicion: ", (palabras.index(i)))
#         noencontre = False
    

# if noencontre:
#     print(f"La palabra {palabra_buscar} no se encuentra en la lista")

#Ejemplo 3 Crear una lista de 4 palabras, solicitar una palabra y buscar la
# coincidencia en la lista e indicar si la encontró o no y en que posicion usando while

# palabras=["hola","2024","bye","UTD"]
# palabra_buscar = input("Ingresa la palabra a buscar: ")

# noencontre = True
# i = 0

# while i <= len(palabras):
#     if palabra_buscar == palabras[i]:
#         print(f"La palabra {palabra_buscar} se encuentra en la posicion: ", i)
#         noencontre = False
#     i += 1

# if noencontre:
#     print(f"La palabra {palabra_buscar} no se encuentra en la lista")

# # agregar y eliminar elementos de una lista.
# numeros = [23,24]
# print(numeros)

# # Agregar un elemento
# numeros.append(25)
# print(numeros)

# numeros.insert(3, 200)

# #Eliminar elementos

# numeros.remove(100)
# print(numeros) #Indicar el elemento a borrar

# numeros.pop(2)
# print(numeros)
# numeros.remove(23)
# print(numeros) #Indicar el elemento a borrar

# #Ejemplo 4  crear una lista multidimensional (matriz) para almacenar los contactos telefonicos

# agenda=[
#     ["Carlos", "6182334567"],
#     ["Karin", "6182334568"],
#     ["Leon","6182334569"],
#     ["Pedro", "6182334570"]
# ]

# print(agenda)

# for i in agenda:
#     print(f"{agenda.index(i)+1},- {i}")