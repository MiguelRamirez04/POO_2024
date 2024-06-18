
# los errores de excepciones en un lenguaje de programacion no es otra cosa que los errores en tiempo de ejecucion...
# Cuando se manejan los errores mediante las excepciones en realidad se dice que se evita que se presenten esos errores en
# el programa en el tiempo de ejecucion

# Ejemplo: Se presenta un error cuando no es generada una variable.

# try:
#     nombre = input("Dame el nombre completo de una persona: ")
#     if len(nombre) > 0:
#         nombre_usuario = "El nombre del usuario del sistema es: " +nombre

#     print(nombre_usuario)
#     print(len(nombre))
# except:
#     print("Es necesario introducir un nombre de persona")

# Ejemplo 2: Cuando se solicita un nimero y se ingresa otra cosa

# try:
#     numero = int(input("Ingresa un numero entero:"))

#     if numero > 0:
#         print("Soy un numero positivo")
#     else:
#         print("Soy un numero negativo")
# except ValueError:
#     print("No es posible convertir una letra en un numero, verifica por favor...")

# Ejemplo 3: Cuando se generan multimpes excepciones
try:
    numero = int(input("Ingresa un numero: "))

    print("El cuadrado del numero es:" +str(numero*numero))
except TypeError:
    print("Es necesario convertir el numero a entero")
except ValueError:
    print("No es posible convertir una letra a un numero, verifica por favor")

else:
    print("Todo se ejecutó sin errores")
finally:
    print("Ya terminó")