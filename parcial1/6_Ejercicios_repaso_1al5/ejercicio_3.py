# 3.- Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for

contador = 1
while contador <= 60:
    cuadrado = contador*contador
    print(f"{contador} x {contador} = {cuadrado}")
    contador += 1

for cont in range(1,61):
    cuadrado = cont*cont
    print(f"{cont} x {cont} = {cuadrado}")
    