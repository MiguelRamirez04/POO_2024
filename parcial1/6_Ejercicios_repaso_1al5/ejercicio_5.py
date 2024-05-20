# 5.- Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))

if numero1 > numero2:
    numero1, numero2 = numero2, numero1

print(f"Números entre {numero1} y {numero2}: ")
for i in range(numero1 + 1, numero2):
    print(i)