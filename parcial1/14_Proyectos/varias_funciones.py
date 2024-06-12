import math
def solicitarDatos():
   print("\n")
#    global n1,n2
   n1=int(input("Numero #1: "))
   n2=int(input("Numero #2: "))
   return n1,n2

def getCalculadora(num1,num2,operacion):
    if operacion=="1" or operacion=="+" or operacion=="SUMA":
        return f"{num1} + {num2} = {int(num1)+int(num2)}"
    elif operacion=="2" or operacion=="-" or operacion=="RESTA":
        return f"{num1} - {num2} = {int(num1)-int(num2)}"  
    elif operacion=="3" or operacion=="*" or operacion=="MULTIPLICACION":
        return f"{num1} * {num2} = {int(num1)*int(num2)}"        
    elif operacion=="4" or operacion=="/" or operacion=="DIVISION":
        return f"{num1} / {num2} = {int(num1)/int(num2)}" 
    elif operacion=="5" or operacion=="**" or operacion=="POTENCIA":
        return f"{num1} ** {num2} = {int(num1)**int(num2)}"
    elif operacion=="6" or operacion=="%" or operacion=="Raiz":
        return f"{num1} % {num2} = {math.sqrt(num1**2 + num2**2)}"    
    else:
        print("opcion invalida")

def esperatecla():
    print("Presiona cualquier tecla para continuar")
    input()

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

def consultar(peliculas):
    print(f"\nCartelera Completa:\n")
    return peliculas

def buscar(pelicula):
    if pelicula in peliculas:
        print(f"\nLa pelicula {pelicula} se encuentra en la lista\n")
    else:
        print(f"\nLa pelicula {pelicula} no se encuentra en la lista\n")
    return peliculas

def vaciar():
    peliculas.clear()
    print(f"\nLa lista se vacio correctamente\n")
    return peliculas

def menu():
    print("\n\t..::: CINEPOLIS CLON :::... \n\t..::: SISTEMA GESTOR DE PELICULAS :::... \n\n1.- Agregar\n2.- Eliminar\n3.- Actualizar\n4.- Consultar\n5.- Buscar\n6.- Vaciar\n7.- Salir\n")
    opcion = int(input("\tElige una opcion: "))
    return opcion
