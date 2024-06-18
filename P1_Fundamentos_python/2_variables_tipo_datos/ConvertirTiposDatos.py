"""
comentario de varias lineas
Nota: Cuando se imprime en pantalla una cadena de caracteres
se trabaja por default con "cadenas", es decir python no
puede concatenar otra cosa que no sea un string (str)

"""

texto = "Soy una cadena de caracteres"
numero = 23

# concatenar str con str

print("Soy otra cadena y "+texto)

# concatenar str con int

numero_str = str(numero)
print("El numero: "+"\""+numero_str+"\"")
print("El numero:"+str(numero))

# concatenar int con str
n1 = int('23')
n2 = 33

suma = n1 + n2

print("La suma es: "+str(suma))
print(f"La suma es: {suma}")

# concatenar float y int con str
n3 = 23.99
n2 = 99

sum = int(n3 + n2)
print(f"La suma es: {sum}")