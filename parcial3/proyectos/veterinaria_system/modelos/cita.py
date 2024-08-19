from datetime import datetime

class Cita:
    def __init__(self, fecha, id_cliente, id_animal, id_emp, id_servicio):
        self.fecha = fecha
        self.id_cliente = id_cliente
        self.id_animal = id_animal
        self.id_emp = id_emp
        self.id_servicio = id_servicio

    def guardar(self, cursor):
        cursor.execute('''
        INSERT INTO citas (fecha, id_cliente, id_animal, id_emp, id_servicio)
        VALUES (%s, %s, %s, %s, %s)
        ''', (self.fecha, self.id_cliente, self.id_animal, self.id_emp, self.id_servicio))

    @staticmethod
    def buscar(cursor, nombre_cliente, nombre_animal):
        cursor.execute('''
        SELECT c.fecha, cl.nombre AS nombre_cliente, cl.direccion, cl.telefono, a.nombre AS nombre_animal, 
               a.raza, a.edad, e.nombre AS nombre_empleado, s.nombre AS nombre_servicio, s.descripcion, s.costo
        FROM citas c
        JOIN clientes cl ON c.id_cliente = cl.id
        JOIN animales a ON c.id_animal = a.id
        JOIN empleados e ON c.id_emp = e.id
        JOIN servicios s ON c.id_servicio = s.id
        WHERE cl.nombre = %s AND a.nombre = %s
        ''', (nombre_cliente, nombre_animal))
        result = cursor.fetchone()
        if result:
            print(f"Fecha de la cita: {result[0]}")
            print(f"Nombre del cliente: {result[1]}")
            print(f"Dirección del cliente: {result[2]}")
            print(f"Teléfono del cliente: {result[3]}")
            print(f"Nombre del animal: {result[4]}")
            print(f"Raza del animal: {result[5]}")
            print(f"Edad del animal: {result[6]}")
            print(f"Nombre del empleado: {result[7]}")
            print(f"Servicio: {result[8]}")
            print(f"Descripción del servicio: {result[9]}")
            print(f"Costo del servicio: {result[10]}")
        else:
            print("No se encontró ninguna cita con los datos proporcionados.")
