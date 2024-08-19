from modelos import *
from revision import *
from funciones import *

def menu_principal():
    while True:
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Gestionar Clientes
          2.- Gestionar Autos
          3.- Gestionar Revisiones
          4.- Salir 
          """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            menu_clientes()
        elif opcion == '2':
            menu_autos()
        elif opcion == '3':
            menu_revisiones()
        elif opcion == '4':
            print("\n\t.. ¡Gracias Bye! ...")
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_clientes():
    while True:
        borrarPantalla()
        print("""
        .::  Menu Clientes ::. 
        1.- Crear Cliente
        2.- Ver Clientes
        3.- Actualizar Cliente
        4.- Eliminar Cliente
        5.- Regresar al Menú Principal
        """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            registrar_cliente()
        elif opcion == '2':
            ver_clientes()
        elif opcion == '3':
            actualizar_cliente()
        elif opcion == '4':
            eliminar_cliente()
        elif opcion == '5':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_autos():
    while True:
        borrarPantalla()
        print("""
        .::  Menu Autos ::. 
        1.- Crear Auto
        2.- Ver Autos
        3.- Actualizar Auto
        4.- Eliminar Auto
        5.- Regresar al Menú Principal
        """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            registrar_auto()
        elif opcion == '2':
            ver_autos()
        elif opcion == '3':
            actualizar_auto()
        elif opcion == '4':
            eliminar_auto()
        elif opcion == '5':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def menu_revisiones():
    while True:
        borrarPantalla()
        print("""
        .::  Menu Revisiones ::. 
        1.- Crear Revisión
        2.- Ver Revisiones
        3.- Actualizar Revisión
        4.- Eliminar Revisión
        5.- Regresar al Menú Principal
        """)
        opcion = input("\t Elige una opción: ")

        if opcion == '1':
            registrar_revision()
        elif opcion == '2':
            ver_revisiones()
        elif opcion == '3':
            actualizar_revision()
        elif opcion == '4':
            eliminar_revision()
        elif opcion == '5':
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

def registrar_cliente():
    borrarPantalla()
    print("\n \t ..:: Registro de Cliente ::..")
    nif = input("\t Ingresa el NIF: ")
    nombre = input("\t ¿Cual es su nombre?: ")
    direccion = input("\t ¿Cuál es su dirección?: ")
    ciudad = input("\t ¿Cuál es su ciudad?: ")
    tel = input("\t Ingresa su teléfono: ")

    cliente = Cliente(nif, nombre, direccion, ciudad, tel)
    resultado = cliente.registrar()
    if resultado:
        print(f"\n\t {nombre} se registró correctamente.")
    else:
        print(f"\n\t ** Por favor intentalo de nuevo, no fue posible insertar el registro ** ...")
    esperarTecla()

def ver_clientes():
    borrarPantalla()
    clientes = Cliente.mostrar()
    if clientes:
        print(f"\n \t \t Aquí están los clientes registrados:  ")
        for cliente in clientes:
            print(f"\t NIF: {cliente[0]}, Nombre: {cliente[1]}, Dirección: {cliente[2]}, Ciudad: {cliente[3]}, Teléfono: {cliente[4]}")
    else:
        print(f"...** No hay clientes registrados **...")
    esperarTecla()

def actualizar_cliente():
    borrarPantalla()
    print("\n \t ..:: Actualizar Cliente ::..")
    nif = input("\t Ingresa el NIF del cliente a actualizar: ")
    nombre = input("\t Nuevo nombre: ")
    direccion = input("\t Nueva dirección: ")
    ciudad = input("\t Nueva ciudad: ")
    tel = input("\t Nuevo teléfono: ")

    resultado = Cliente.actualizar(nif, nombre, direccion, ciudad, tel)
    if resultado:
        print(f"\n\t Cliente actualizado correctamente.")
    else:
        print(f"\n\t ** Por favor intentalo de nuevo, no fue posible actualizar el cliente ** ...")
    esperarTecla()

def eliminar_cliente():
    borrarPantalla()
    print("\n \t ..:: Eliminar Cliente ::..")
    nif = input("\t Ingresa el NIF del cliente a eliminar: ")

    resultado = Cliente.eliminar(nif)
    if resultado:
        print(f"\n\t Cliente eliminado correctamente.")
    else:
        print(f"\n\t ** Por favor intentalo de nuevo, no fue posible eliminar el cliente ** ...")
    esperarTecla()

if __name__ == "__main__":
    menu_principal()
