from conexionBD import get_connection, get_cursor, mysql

class Material:
    def __init__(self, id, nombre, autor, anio, tipo, disponible=True):
        self.id = id
        self.nombre = nombre
        self.autor = autor
        self.anio = anio
        self.tipo = tipo
        self.disponible = disponible
    
    def agregar_material(self):
        try:
            conexion = get_connection()
            cursor = get_cursor(conexion)
            cursor.execute("INSERT INTO material (titulo, autor, anio, tipo, disponible) VALUES (%s, %s, %s, %s, %s)",
                           (self.nombre, self.autor, self.anio, self.tipo, self.disponible))
            conexion.commit()
            cursor.execute("SELECT LAST_INSERT_ID()")
            material_id = cursor.fetchone()[0]
            self.id = material_id
            return material_id is not None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            cursor.close()
            conexion.close()
