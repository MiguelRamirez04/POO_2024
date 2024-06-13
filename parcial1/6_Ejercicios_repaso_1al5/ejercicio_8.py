# 8.- Hacer un programa que resuelva lo siguiente. ¿Cuanto es el X por ciento de X numero?

porcent = int(input("Introduce el porcentaje: "))
num = int(input("Introduce el número: "))

result = (porcent / 100) * num
print(f"El {porcent}% de {num} es: {result}")