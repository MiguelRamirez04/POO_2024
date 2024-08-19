class Animal:
    def __init__(self, nombre, raza, edad, id_cliente):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
        self.id_cliente = id_cliente

    def guardar(self, cursor):
        cursor.execute('''
        INSERT INTO animales (nombre, raza, edad, id_cliente)
        VALUES (%s, %s, %s, %s)
        ''', (self.nombre, self.raza, self.edad, self.id_cliente))
        self.id = cursor.lastrowid
