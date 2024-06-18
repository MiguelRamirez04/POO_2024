# 9.- Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa

num = 0
while num != 111:
    num = int(input("Introduce un número (111 para finalizar): "))
    if num == 111:
        print("Programa cerrado.")
        