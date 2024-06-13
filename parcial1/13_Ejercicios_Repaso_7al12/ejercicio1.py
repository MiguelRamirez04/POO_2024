lista = [23, 12, 3, 44, 58, 99, 1200, 1467]


for i in lista:

    print(i)

def funcion(lista):
    return str(lista)

print("Lista ordenada: ")
lista.sort()
print(lista)

print("Longitud: ")
print(len(lista))

def buscar(lista):
    busqueda = int(input("Ingrese el numero a buscar: "))
    if busqueda in lista:
        print("El numero se encuentra en la lista\n")
    else:
        print("El numero no se encuentra en la lista\n")

opcion = True

while opcion:
    buscar(lista)
    opcion = input("Desea buscar otro numero? S/N: ")
    if opcion == "s" or "S":
        opcion = True
    else:
        opcion = False
        print("\nGracias por usar el programa")