# 5.- Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    num1, num2 = num2, num1

print(f"Números entre {num1} y {num2}: ")
for i in range(num1 , num2 + 1):
    print(i)