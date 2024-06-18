"""
Existe una estructura de condicion llamada "if"
La cual evalua una condicion pata encontrar el valor "true" o se cumple
la condicion se ejecuta la linea o lineas de codigo
Tienes 4 variantes del if

1.- if simple
2.- if compuesto
3.- if anidado
4.- if y elif

"""

# ejemplo 1. if simple

color = "rojo"
if color == "rojo":
    print("soy el color rojo")

# ejemplo 2. if compuesto

color = "rojo"
if color == "rojo":
    print("soy el color rojo")
else:
    print("no soy del color rojo")

#Ejemplo 3 if anidado

color="rojo"
if color=="rojo":
    print("Soy el color rojo")  
    if color!="rojo":
       print("Soy otro color")   
else:      
    print("No soy el color rojo")
    if color!="rojo":
       print("Soy otro color") 

#Ejemplo 4 if con elif

color="rojo"
if color=="rojo":
    print("Soy el color rojo")  
elif color=="negro":    
    print(" soy el color negro")
elif color=="verde":    
    print(" soy el color verde")   
else:
    print("No soy rojo, verde o negro")
    