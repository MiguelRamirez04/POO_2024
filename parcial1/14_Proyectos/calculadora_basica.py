import os
from varias_funciones import * #* importa todas las funciones - poner nombre para especificar funcion
# def solicitarDatos():
#    print("\n")
#    global n1,n2
#    n1=int(input("Numero #1: "))
#    n2=int(input("Numero #2: "))

# def getCalculadora(num1,num2,operacion):
#     if operacion=="1" or operacion=="+" or operacion=="SUMA":
#         resultado=f"{num1} + {num2} = {int(num1)+int(num2)}"
#     elif operacion=="2" or operacion=="-" or operacion=="RESTA":
#         resultado=f"{num1} - {num2} = {int(num1)-int(num2)}"  
#     elif operacion=="3" or operacion=="*" or operacion=="MULTIPLICACION":
#         resultado=f"{num1} * {num2} = {int(num1)*int(num2)}"        
#     elif operacion=="4" or operacion=="/" or operacion=="DIVISION":
#         resultado=f"{num1} / {num2} = {int(num1)/int(num2)}"      
#     return resultado

# def esperatecla():
#     print("Presiona cualquier tecla para continuar")
#     input()

opcion = True
while opcion:
    os.system("cls")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- Potencia \n 6.- Raíz \n 7.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()
    
    if opcion != "7":
        n1,n2=solicitarDatos()
        print(getCalculadora(n1,n2,opcion))
        esperatecla()
    else:
        opcion = False
        print("Gracias por utilizar el sistema...")