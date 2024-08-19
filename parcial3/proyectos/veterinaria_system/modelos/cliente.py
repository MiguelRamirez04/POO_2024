class Cliente:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def guardar(self, cursor):
        cursor.execute('''
        INSERT INTO clientes (nombre, direccion, telefono)
        VALUES (%s, %s, %s)
        ''', (self.nombre, self.direccion, self.telefono))
        self.id = cursor.lastrowid
