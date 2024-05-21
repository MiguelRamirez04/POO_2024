# 7.- Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))

if num1 > num2:
    num1, num2 = num2, num1

print(f"Números impares entre {num1} y {num2}:")
for i in range(num1 + 1, num2):
    if i % 2 != 0:
        print(i)
