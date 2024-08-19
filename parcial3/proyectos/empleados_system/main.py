from empleados import *
from funciones import *
import getpass

def menu_principal():
    while True:
        borrarPantalla()
        print("""
      .::  Menú Principal ::. 
          1.- Registro de Empleado
          2.- Login
          3.- Salir
          """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            registrar_empleado()
        elif opcion == '2':
            email = input("\t Ingresa tu E-mail: ")
            password = getpass.getpass("\t Ingresa tu Contraseña: ")
            registro = Empleado.iniciar_sesion(email, password)
            if registro:
                if registro[6]:  # Verificacion
                    menu_admin()
                else:
                    menu_empleado(registro)
            else:
                print(f"\n\t ** Nombre de empleado y/o contraseña incorrectos, inténtalo de nuevo ** ...")
                esperarTecla()
        elif opcion == '3':
            print("\n\t.. ¡Gracias Bye! ...")
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def registrar_empleado():
    borrarPantalla()
    print("\n \t ..:: Registro en el Sistema ::..")
    nombre = input("\t ¿Cuál es tu nombre?: ")
    apellidos = input("\t ¿Cuáles son tus apellidos?: ")
    email = input("\t Ingresa tu email: ")
    password = getpass.getpass("\t Ingresa tu contraseña: ")
    is_admin = input("\t ¿Es administrador? (s/n): ").lower() == 's'

    obj_empleado = Empleado(nombre, apellidos, email, password, is_admin)
    resultado = obj_empleado.registrar()
    if resultado:
        print(f"\n\t {nombre} {apellidos} se registró correctamente, con el email: {email}")
    else:
        print(f"\n\t ** Por favor inténtalo de nuevo, no fue posible insertar el registro ** ...")    
    esperarTecla()

def menu_empleado(registro):
    while True:
        borrarPantalla()
        print(f"\n \t Bienvenido {registro[1]} {registro[2]}")
        print("""
          \n \t 
              .::  Menú Empleado ::. 
          1.- Registrar Entrada
          2.- Registrar Salida
          3.- Salir
          """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            resultado = Empleado.registrar_entrada(registro[0])
            if resultado:
                print("\n \t Entrada registrada correctamente.")
            else:
                print("\n \t ** No fue posible registrar la entrada. **")
            esperarTecla()

        elif opcion == '2':
            resultado = Empleado.registrar_salida(registro[0])
            if resultado:
                print("\n \t Salida registrada correctamente.")
            else:
                print("\n \t ** No fue posible registrar la salida. **")
            esperarTecla()

        elif opcion == '3':
            break

        else:
            print("\n \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_admin(registro):
    while True:
        borrarPantalla()
        print(f"\n \t \t \t Bienvenido Admin {registro[1]}")
        print("""
              \n \t 
                  .::  Menú Admin ::. 
              1.- Mostrar todos los empleados
              2.- Mostrar registros de entradas/salidas
              3.- Agregar empleado
              4.- Eliminar empleado
              5.- Salir 
              """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            mostrar_empleados()
        elif opcion == '2':
            mostrar_registros()
        elif opcion == '3':
            registrar_empleado()
        elif opcion == '4':
            eliminar_empleado()
        elif opcion == '5':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def mostrar_empleados():
    borrarPantalla()
    print("\n \t .:: Lista de Empleados ::. ")

    try:
        cursor.execute("select * from empleados")
        empleados = cursor.fetchall()
        if empleados:
            for emp in empleados:
                print(f"\t ID: {emp[0]}, Nombre: {emp[1]}, Apellidos: {emp[2]}, Email: {emp[3]}, Admin: {'Sí' if emp[6] else 'No'}")
        else:
            print("\n \t \t...** No hay empleados registrados **...")
    except:
        print("\n \t \t...** No fue posible recuperar los empleados **...")
    esperarTecla()

def mostrar_registros():
    borrarPantalla()
    print("\n \t .:: Lista de Registros ::. ")

    try:
        cursor.execute("select r.id, e.nombre, e.apellidos, r.tipo, r.fecha_hora from registros r join empleados e on r.empleado_id = e.id")
        registros = cursor.fetchall()
        if registros:
            for reg in registros:
                print(f"\t ID: {reg[0]}, Empleado: {reg[1]} {reg[2]}, Tipo: {reg[3]}, Fecha y Hora: {reg[4]}")
        else:
            print("\n \t \t...** No hay registros **...")
    except:
        print("\n \t \t...** No fue posible recuperar los registros **...")
    esperarTecla()

def eliminar_empleado():
    borrarPantalla()
    print(f"\n \t .:: Vamos a borrar un empleado ::. \n")
    emp_id = input("\t \t ID del empleado a eliminar: ")

    try:
        cursor.execute("delete from empleados where id=%s", (emp_id,))
        conexion.commit()
        print("\n \t .:: El empleado se ha eliminado correctamente ::.")
    except:
        print("\n \t \t...** No fue posible eliminar el empleado, por favor verifique **...")
    esperarTecla()

if __name__ == "__main__":
    menu_principal()