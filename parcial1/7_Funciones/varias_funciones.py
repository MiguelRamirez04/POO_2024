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
    else:
        print("opcion invalida")

def esperatecla():
    print("Presiona cualquier tecla para continuar")
    input()