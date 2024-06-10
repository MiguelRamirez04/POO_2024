# los errores de excepciones en un lenguaje de programacion no es otra cosa que los errores en tiempo de ejecucion...
# Cuando se manejan los errores mediante las excepciones en realidad se dice que se evita que se presenten esos errores en
# el programa en el tiempo de ejecucion

# Ejemplo: Se presenta un error cuando no es generada una variable.
nombre = input("Dame el nombre completo de una persona: ")
if len(nombre) > 0:
    nombre_usuario = "El nombre del usuario del sistema es: " +nombre

print(nombre_usuario)