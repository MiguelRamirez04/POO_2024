import os  
os.system("cls")
from db import conectar_db
import modelos
from datetime import datetime

def main():
    db = conectar_db()
    cursor = db.cursor()

    while True:
        print("\nOpciones:")
        print("1. Agregar Cliente")
        print("2. Agregar Empleado")
        print("3. Eliminar Empleado")
        print("4. Buscar Cita")
        print("5. Salir")
        
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            nombre = input("Ingresa el nombre del cliente: ")
            direccion = input("Ingresa la dirección del cliente: ")
            telefono = input("Ingresa el teléfono del cliente: ")
            cliente = modelos.Cliente(nombre, direccion, telefono)
            cliente.guardar(cursor)
            
            nombre_animal = input("Ingresa el nombre del animal: ")
            raza = input("Ingresa la raza del animal: ")
            edad = int(input("Ingresa la edad del animal: "))
            animal = modelos.Animal(nombre_animal, raza, edad, cliente.id)
            animal.guardar(cursor)
            
            empleado_id = input("Ingresa el ID del empleado: ")
            servicio_id = input("Ingresa el ID del servicio: ")
            
            cita = modelos.Cita(datetime.now(), cliente.id, animal.id, empleado_id, servicio_id)
            cita.guardar(cursor)
            db.commit()
            print("Cliente, animal y cita agregados exitosamente.")
        elif opcion == "2":
            nombre = input("Ingresa el nombre del empleado: ")
            direccion = input("Ingresa la dirección del empleado: ")
            telefono = input("Ingresa el teléfono del empleado: ")
            puesto = input("Ingresa el puesto del empleado: ")
            salario = float(input("Ingresa el salario del empleado: "))
            empleado = modelos.Empleado(nombre, direccion, telefono, puesto, salario)
            empleado.guardar(cursor)
            db.commit()
            print("Empleado agregado exitosamente.")
        elif opcion == "3":
            empleado_id = int(input("Ingresa el ID del empleado a eliminar: "))
            modelos.Empleado.eliminar(cursor, empleado_id)
            db.commit()
            print("Empleado eliminado exitosamente.")
        elif opcion == "4":
            nombre_cliente = input("Ingresa el nombre del cliente: ")
            nombre_animal = input("Ingresa el nombre del animal: ")
            modelos.Cita.buscar(cursor, nombre_cliente, nombre_animal)
        elif opcion == "5":
            break
        else:
            print("Opción no válida, intenta nuevamente.")

    db.close()

if __name__ == '__main__':
    main()
