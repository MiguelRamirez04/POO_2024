def solicitar_datos():
    print("\n")
    global n1,n2,ope
    n1 = int(input("Numero #1: "))
    n2 = int(input("Numero #2: "))
    ope = input("Operacion: ").upper()


def getCalculadora(num1, num2, operacion):
    if operacion == "1" or operacion == "+" or operacion == "SUMA":
        resultado = (f"{num1} + {num2} = {int(num1)+int(num2)}")
    elif operacion == "2" or operacion == "-" or operacion == "RESTA":
        resultado = (f"{num1} - {num2} = {int(num1)+int(num2)}")
    elif operacion == "3" or operacion == "*" or operacion == "MULTIPLICACION":
        resultado = (f"{num1} * {num2} = {int(num1)+int(num2)}")
    elif operacion == "4" or operacion == "/" or operacion == "DIVISION":
        resultado = (f"{num1} / {num2} = {int(num1)+int(num2)}")
    return resultado

print("\n...::: CALCULADORA BASICA :::...\n1.- Suma\n2.- Resta\n3.- Multiplicacion \n4.- Division \n5.- Salir")


solicitar_datos()
print(getCalculadora(n1,n2,ope))