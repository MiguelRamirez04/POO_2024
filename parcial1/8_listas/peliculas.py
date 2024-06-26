# Ejemplo 5 Crear un programa que permita gestionar (administrar) peliculas, clocar un menu de opcione para agregar, remover, consultar peliculas.
# Notas:
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar listas para almacenar los nombres de peliculas

import os

peliculas = []

def agregar(pelicula):
    peliculas.append(pelicula)
    print(f"\nLa pelicula {pelicula} se agrego correctamente\n")
    print(peliculas)
    return peliculas

def eliminar(pelicula):
    peliculas.remove(pelicula)
    print(f"\nLa pelicula {pelicula} se elimino correctamente\n")
    print(peliculas)
    return peliculas

def consultar(pelicula):
    if pelicula in peliculas:
        print(f"\nLa pelicula {pelicula} se encuentra en la lista\n")
    else:
        print(f"\nLa pelicula {pelicula} no se encuentra en la lista\n")
    return peliculas

def menu():
    print("\n1.- Agregar pelicula\n2.- Eliminar pelicula\n3.- Consultar pelicula\n4.- Salir\n")
    opcion = int(input("\tIngresa una opcion: "))
    return opcion

opcion = menu()

while opcion != 4:
    if opcion == 1 or opcion == 2 or opcion == 3:
        pelicula = input("\nIngresa el nombre de la pelicula: \n")
        agregar(pelicula)
    else:
        print("\nOpcion no valida")
    opcion = menu()

print("\nGracias por usar el programa")