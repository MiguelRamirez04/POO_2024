class Empleado:

    def __init__(self, nombre, direccion, telefono, puesto, salario):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.puesto = puesto
        self.salario = salario

    def guardar(self, cursor):
        cursor.execute('''
        INSERT INTO empleados (nombre, direccion, telefono, puesto, salario)
        VALUES (%s, %s, %s, %s, %s)
        ''', (self.nombre, self.direccion, self.telefono, self.puesto, self.salario))

    @staticmethod
    def eliminar(cursor, empleado_id):
        cursor.execute('''
        DELETE FROM empleados WHERE id = %s
        ''', (empleado_id,))
