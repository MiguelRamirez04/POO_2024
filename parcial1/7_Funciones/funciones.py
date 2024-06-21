"""
  Una función es un conjunto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumple una funcion especifica. La funcion se puede reutulizar con el simple hecho de invocarla es decir mandarla llamar 

  Sintaxis:

   def nombredeMifuncion(parametros):
      bloque o conjunto de instrucciones

   nombredeMifuncion(parametros)

   Las funciones pueden ser de 4 tipos
   1.- Funcion que no recibe parametros y no regresa valor
   2.- Funcion que no recibe parametros y regresa valor
   3.- Funcion que recibe parametros y no regresa valor
   4.- Funcion que recibe parametros y regresa valor

"""

#Ejemplo 1 Crear una funcion para imprimir nombres de personas
#    1.- Funcion que no recibe parametros y no regresa valor 
def solicitarNombres():
   nombre=input("Ingresa el nombre completo: ")

solicitarNombres()  

#Ejemplo 2 sumar dos numeros
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

suma()    

#Ejemplo 3 sumar dos numeros 
#2.- Funcion que no recibe parametros y regresa valor
def suma():
    n1=int(input("Numero #1: "))
    n2=int(input("Numero #2: "))
    suma=n1+n2
    return suma

resultado_suma=suma()
print(f"La suma es: {resultado_suma}")

#Ejemplo 4 sumar dos numeros 
# 3.- Funcion que recibe parametros y no regresa valor
def suma(num1,num2):
    suma=num1+num2
    print(f"La suma es: {suma}")

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
suma(n1,n2)

#Ejemplo 5 sumar dos numeros 
# 4.- Funcion que recibe parametros y regresa valor
def suma(num1,num2):
    suma=num1+num2
    return suma

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))
resultado_suma=suma(n1,n2)
print(f"La suma es: {resultado_suma}")

#Ejemplo 6 Crear un programa que solicite a traves de una funcion la siguiente informacion: Nombre del Paciente, Edad, Estatura, Tipo de Sangre. Utilizar los 4 tipos de funciones


# Función 1: Sin parámetros y sin regreso de valor
def func1():
    global nombre1, edad1, estatura1, tipo_sangre1
    nombre1 = input("Ingrese el nombre del paciente: ")
    edad1 = input("Ingrese la edad del paciente: ")
    estatura1 = input("Ingrese la estatura del paciente (ej. 1.70): ")
    tipo_sangre1 = input("Ingrese el tipo de sangre del paciente: ")
    print(f"Nombre: {nombre1}")
    print(f"Edad: {edad1}")
    print(f"Estatura: {estatura1} metros")
    print(f"Tipo de Sangre: {tipo_sangre1}")

func1()

# Función 2: Sin parámetros y con regreso de valor
def func2():
    nombre = input("Ingrese el nombre del paciente: ")
    edad = input("Ingrese la edad del paciente: ")
    estatura = input("Ingrese la estatura del paciente (en metros): ")
    tipo_sangre = input("Ingrese el tipo de sangre del paciente: ")
    return nombre, edad, estatura, tipo_sangre


nombre2, edad2, estatura2, tipo_sangre2 = func2()

# Función 3: Sin parámetros y con retorno de valor
def func3(nombre, edad, estatura, tipo_sangre):
    global nombre2, edad2, estatura2, tipo_sangre2
    nombre2 = nombre
    edad2 = edad
    estatura2 = estatura
    tipo_sangre2 = tipo_sangre
    print("\nInformación del Paciente (función 2):")
    print(f"Nombre: {nombre2}")
    print(f"Edad: {edad2}")
    print(f"Estatura: {estatura2} metros")
    print(f"Tipo de Sangre: {tipo_sangre2}")

func3(nombre1, edad1, estatura1, tipo_sangre1)

# Función 4: Con parámetros y sin regreso de valor
def func4(nombre, edad, estatura, tipo_sangre):
    return nombre, edad, estatura, tipo_sangre
