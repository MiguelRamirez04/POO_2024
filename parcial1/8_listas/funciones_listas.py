paises=["Mexico", "USA", "Brasil", "Japon"]
numeros=[23,34,12.56,0.100]
texto=["Hola", True, 23, 3.141516]

# Ordenar una lista
print(paises)
paises.sort()
print(paises)

print(numeros)
numeros.sort()
print(numeros)


#Añadir elementos
print(texto)
texto.insert(len(texto), "True")
print(texto)
texto.insert(len(texto),True)
print(texto)
texto.append(False)
print(texto)

# Dar la vuelta a una lista

print(numeros)
numeros.reverse()
print(numeros)

# buscar datos dentro de una lista
respuesta= "Brasil" in paises
print(respuesta)

# cuantas veces aparece un valor dentro de una lista 
print(numeros)
numeros.append(23)
cuantos=numeros.count(23)
print(f"El numero 23 se encontró: {cuantos}")

# unir listas
print(paises)
paises.extend(numeros)
print(paises)

print(numeros)
numeros.sort()
print(numeros)