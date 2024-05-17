# El ciclo while es una estructura de control que itera o repite la ejecucion de una serie de instrucciones tantas veces como la condición se cumpla 'true'

# Sintaxis:

#  while condicion:
#      bloque instrucciones


# Ejemplo 1 Crear un programa que imprima 5 veces el caracter @

contador = 1
while contador <= 5:
    print("@")
    contador += 1

# Ejemplo 2 crear un programa que imprima los numeros del 1 al 5, los sume y al final imprima la suma

i = 1
suma = 0
while i <= 5:
    print(i)
    suma += i
    i +=1
print(f"La suma es: {suma}")

# Ejemplo 3 crear un programa que solicite un numero entero y a continuacion imprima la tabla de multiplicar correspondiente

numero = int(input("Ingrese un numero entero: "))
i = 1
while i <= 10:
    print(f"{numero} x {i} = {numero*i}")
    i += 1